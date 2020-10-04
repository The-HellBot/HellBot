"""Upload local Files to Mirrorace
Syntax:
.ma"""

import aiohttp
import asyncio
import os
import requests
import time
from datetime import datetime
from uniborg.util import admin_cmd, progress


@borg.on(admin_cmd(pattern="ma ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    mone = await event.reply("Processing ...")
    if Config.MIRROR_ACE_API_KEY is None or Config.MIRROR_ACE_API_TOKEN is None:
        await mone.edit("This module requires API key from https://ouo.io/My1jdU. Aborting!")
        return False
    input_str = event.pattern_match.group(1)
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    required_file_name = None
    start = datetime.now()
    if event.reply_to_msg_id and not input_str:
        reply_message = await event.get_reply_message()
        try:
            c_time = time.time()
            downloaded_file_name = await borg.download_media(
                reply_message,
                Config.TMP_DOWNLOAD_DIRECTORY,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, mone, c_time, "trying to download")
                )
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            await mone.edit(str(e))
            return False
        else:
            end = datetime.now()
            ms = (end - start).seconds
            required_file_name = downloaded_file_name
            await mone.edit("Downloaded to `{}` in {} seconds.".format(downloaded_file_name, ms))
    elif input_str:
        input_str = input_str.strip()
        if os.path.exists(input_str):
            end = datetime.now()
            ms = (end - start).seconds
            required_file_name = input_str
            await mone.edit("Found `{}` in {} seconds.".format(input_str, ms))
        else:
            await mone.edit("File Not found in local server. Give me a file path :((")
            return False
    # logger.info(required_file_name)
    if required_file_name:
        # required_file_name will have the full path
        file_name = os.path.basename(required_file_name)
        file_size = os.stat(required_file_name).st_size
        # /* STEP 1: get upload_key */
        step_one_url = "https://mirrorace.com/api/v1/file/upload"
        step_one_auth_params = {
            "api_key": Config.MIRROR_ACE_API_KEY,
            "api_token": Config.MIRROR_ACE_API_TOKEN
        }
        async with aiohttp.ClientSession() as session:
            resp = await session.post(step_one_url, data=step_one_auth_params)
            # logger.info(resp.status)
            if resp.status == 200:
                step_one_response_json = await resp.json()
                logger.info(step_one_response_json)
                if step_one_response_json["status"] == "success":
                    await mone.edit("Received Upload URL from MirrorAce. ...")
                    start = datetime.now()
                    # /* STEP 2: Upload file */
                    # step one: response vars
                    step_two_upload_url = step_one_response_json["result"]["server_file"]
                    cTracker = step_one_response_json["result"]["cTracker"]
                    upload_key = step_one_response_json["result"]["upload_key"]
                    default_mirrors = step_one_response_json["result"]["default_mirrors"]
                    max_chunk_size = step_one_response_json["result"]["max_chunk_size"]
                    max_file_size = step_one_response_json["result"]["max_file_size"]
                    max_mirrors = step_one_response_json["result"]["max_mirrors"]

                    # check file size limit
                    if int(file_size) >= int(max_file_size):
                        await mone.edit(f"File exceeds maximum file size allowed: {max_file_size}")
                        return False

                    # step two: setup
                    mirrors = default_mirrors
                    chunk_size = int(max_chunk_size)
                    step_two_params = {
                        "api_key": Config.MIRROR_ACE_API_KEY,
                        "api_token": Config.MIRROR_ACE_API_TOKEN,
                        "cTracker": cTracker,
                        "upload_key": upload_key,
                        "mirrors[]": mirrors,
                        # //these required vars will be added by buildMultiPartRequest function
                        # //'files' => $file,
                        # //'mirrors[1]' => 1,
                        # //'mirrors[2]' => 2,
                    }

                    # //range vars //for multi chunk upload
                    response = False

                    with open(required_file_name, "rb") as f_handle:
                        # start chunk upload
                        for chunk in iter((lambda: f_handle.read(chunk_size)), ""):
                            # for chunk in f_handle.read(chunk_size):
                            # print(chunk)
                            # while (i < chunks) and not while_error:
                            # chunk = f_handle.read(chunk_size)
                            if not chunk:
                                break
                            headers = {
                                "Content-Range": str(len(chunk)),
                                "Content-Length": str(len(step_two_params) + len(chunk)),
                                # "Content-Type": "multipart/form-data"
                            }

                            # https://github.com/aio-libs/aiohttp/issues/3571#issuecomment-456528924
                            response = requests.post(
                                step_two_upload_url,
                                files=[("files", (file_name, chunk))],
                                data=step_two_params,
                                # headers=headers
                            )
                            logger.info(response.content)

                    logger.info(response)
                    final_response = response.json()
                    if final_response["status"] == "success":
                        end = datetime.now()
                        ms = (end - start).seconds
                        final_url = final_response["result"]["url"]
                        await mone.edit(f"Added to {final_url} in {ms} seconds")
                    else:
                        await mone.edit(f"MirrorAce returned {final_response['status']} => {final_response['result']}")
                else:
                    await mone.edit(f"MirrorAce returned {step_one_response_json['status']} => {step_one_response_json['result']}, after STEP TWO")
            else:
                await mone.edit(f"MirrorAce returned {resp['status']} => {resp['result']}, after STEP ONE")
    else:
        await mone.edit("File Not found in local server. Give me a file path :((")
