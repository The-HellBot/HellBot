# (c) Shrimadhav U K
#
# This file is part of @UniBorg
#
# @UniBorg is free software; you cannot redistribute it and/or modify
# it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# @UniBorg is not distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
"""Remove.BG Plugin for @UniBorg
Syntax: .rmbg https://link.to/image.extension
Syntax: .rmbg as reply to a media"""
import io
import os
from datetime import datetime

import requests

from userbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp


@borg.on(admin_cmd(pattern="rmbg ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="rmbg ?(.*)", allow_sudo=True))
async def _(event):
    HELP_STR = (
        "`.rmbg` as reply to a media, or give a link as an argument to this command"
    )
    if event.fwd_from:
        return
    if Config.REM_BG_API_KEY is None:
        await edit_or_reply(event, "You need API token from remove.bg to use this plugin.")
        return False
    input_str = event.pattern_match.group(1)
    start = datetime.now()
    message_id = event.message.id
    if event.reply_to_msg_id:
        message_id = event.reply_to_msg_id
        reply_message = await event.get_reply_message()
        # check if media message
        await edit_or_reply(event, "Ooh Analysing this pic...")
        try:
            downloaded_file_name = await borg.download_media(
                reply_message, Config.TMP_DOWNLOAD_DIRECTORY
            )
        except Exception as e:
            await edit_or_reply(event, str(e))
            return
        else:
            await edit_or_reply(event, "sending to ReMove.BG")
            output_file_name = ReTrieveFile(downloaded_file_name)
            os.remove(downloaded_file_name)
    elif input_str:
        await edit_or_reply(event, "sending to ReMove.BG")
        output_file_name = ReTrieveURL(input_str)
    else:
        await edit_or_reply(event, HELP_STR)
        return
    contentType = output_file_name.headers.get("content-type")
    if "image" in contentType:
        with io.BytesIO(output_file_name.content) as remove_bg_image:
            remove_bg_image.name = "HELLBOT_RM_BG.png"
            await borg.send_file(
                event.chat_id,
                remove_bg_image,
                force_document=True,
                supports_streaming=False,
                allow_cache=False,
                reply_to=message_id,
            )
        end = datetime.now()
        ms = (end - start).seconds
        await edit_or_reply(event, 
            "Removed dat annoying Backgroup in {} seconds, powered by @HellBot_Official ©™".format(
                ms
            )
        )
    else:
        await edit_or_reply(event, 
            "ReMove.BG API returned Errors. Please report to @Hellbot_Official\n`{}".format(
                output_file_name.content.decode("UTF-8")
            )
        )


# this method will call the API, and return in the appropriate format
# with the name provided.
def ReTrieveFile(input_file_name):
    headers = {
        "X-API-Key": Config.REM_BG_API_KEY,
    }
    files = {
        "image_file": (input_file_name, open(input_file_name, "rb")),
    }
    r = requests.post(
        "https://api.remove.bg/v1.0/removebg",
        headers=headers,
        files=files,
        allow_redirects=True,
        stream=True,
    )
    return r


def ReTrieveURL(input_url):
    headers = {
        "X-API-Key": Config.REM_BG_API_KEY,
    }
    data = {"image_url": input_url}
    r = requests.post(
        "https://api.remove.bg/v1.0/removebg",
        headers=headers,
        data=data,
        allow_redirects=True,
        stream=True,
    )
    return r

CmdHelp("removebg").add_command(
  "rmbg", "<reply to img>", "Removes that annoying background from the replied image. NEED TO GET A API KEY"
).add()