import asyncio
import os
from datetime import datetime

import requests
from bs4 import BeautifulSoup
from google_images_download import google_images_download

from hellbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp


def progress(current, total):
    logger.info(
        "Downloaded {} of {}\nCompleted {}".format(
            current, total, (current / total) * 100
        )
    )


@bot.on(admin_cmd(pattern="google (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="google (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    await edit_or_reply(event, "Processing ...")
    # SHOW_DESCRIPTION = False
    input_str = event.pattern_match.group(
        1
    )  # + " -inurl:(htm|html|php|pls|txt) intitle:index.of \"last modified\" (mkv|mp4|avi|epub|pdf|mp3)"
    input_url = "https://bots.shrimadhavuk.me/search/?q={}".format(input_str)
    headers = {"USER-AGENT": "UniBorg"}
    response = requests.get(input_url, headers=headers).json()
    output_str = " "
    for result in response["results"]:
        text = result.get("title")
        url = result.get("url")
        result.get("description")
        result.get("image")
        output_str += " 👉🏻  [{}]({}) \n\n".format(text, url)
    end = datetime.now()
    ms = (end - start).seconds
    await edit_or_reply(event, 
        "searched Google for {} in {} seconds. \n{}".format(input_str, ms, output_str),
        link_preview=False,
    )
    await asyncio.sleep(5)
    await edit_or_reply(event, "Google: {}\n{}".format(input_str, output_str), link_preview=False)


@bot.on(admin_cmd(pattern="image (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="image (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    await edit_or_reply(event, "Processing ...")
    input_str = event.pattern_match.group(1)
    response = google_images_download.googleimagesdownload()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    arguments = {
        "keywords": input_str,
        "limit": Config.TG_GLOBAL_ALBUM_LIMIT,
        "format": "jpg",
        "delay": 1,
        "safe_search": True,
        "output_directory": Config.TMP_DOWNLOAD_DIRECTORY,
    }
    paths = response.download(arguments)
    logger.info(paths)
    lst = paths[0].get(input_str)
    if len(lst) == 0:
        await event.delete()
        return
    await borg.send_file(
        event.chat_id,
        lst,
        caption=input_str,
        reply_to=event.message.id,
        progress_callback=progress,
    )
    logger.info(lst)
    for each_file in lst:
        os.remove(each_file)
    end = datetime.now()
    ms = (end - start).seconds
    await edit_or_reply(event, 
        "Searched Google for {} in {} seconds.".format(input_str, ms),
        link_preview=False,
    )
    await asyncio.sleep(5)
    await event.delete()


@bot.on(admin_cmd(pattern="reverse"))
@bot.on(sudo_cmd(pattern="reverse", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    BASE_URL = "http://www.google.com"
    OUTPUT_STR = "Reply to an image to do Google Reverse Search"
    if event.reply_to_msg_id:
        await edit_or_reply(event, "Pre Processing Media")
        previous_message = await event.get_reply_message()
        previous_message_text = previous_message.message
        if previous_message.media:
            downloaded_file_name = await borg.download_media(
                previous_message, Config.TMP_DOWNLOAD_DIRECTORY
            )
            SEARCH_URL = "{}/searchbyimage/upload".format(BASE_URL)
            multipart = {
                "encoded_image": (
                    downloaded_file_name,
                    open(downloaded_file_name, "rb"),
                ),
                "image_content": "",
            }
            # https://stackoverflow.com/a/28792943/4723940
            google_rs_response = requests.post(
                SEARCH_URL, files=multipart, allow_redirects=False
            )
            the_location = google_rs_response.headers.get("Location")
            os.remove(downloaded_file_name)
        else:
            previous_message_text = previous_message.message
            SEARCH_URL = "{}/searchbyimage?image_url={}"
            request_url = SEARCH_URL.format(BASE_URL, previous_message_text)
            google_rs_response = requests.get(request_url, allow_redirects=False)
            the_location = google_rs_response.headers.get("Location")
        await edit_or_reply(event, "Found Google Result. Pouring some soup on it!")
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0"
        }
        response = requests.get(the_location, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        # document.getElementsByClassName("r5a77d"): PRS
        prs_div = soup.find_all("div", {"class": "r5a77d"})[0]
        prs_anchor_element = prs_div.find("a")
        prs_url = BASE_URL + prs_anchor_element.get("href")
        prs_text = prs_anchor_element.text
        # document.getElementById("jHnbRc")
        img_size_div = soup.find(id="jHnbRc")
        img_size = img_size_div.find_all("div")
        end = datetime.now()
        ms = (end - start).seconds
        OUTPUT_STR = """{img_size}
**Possible Related Search**: <a href="{prs_url}">{prs_text}</a>

More Info: Open this <a href="{the_location}">Link</a> in {ms} seconds""".format(
            **locals()
        )
    await edit_or_reply(event, OUTPUT_STR, parse_mode="HTML", link_preview=False)

CmdHelp("google").add_command(
  "google", "<query>", "Does a google search for the query provided"
).add_command(
  "img", "<query>", "Does a image search for the query provided"
).add_command(
  "reverse", "<reply to a sticker/pic>", "Does a reverse image search on google and provides the similar images"
).add_command(
  "gps", "<place>", "Gives the location of the given place/city/state."
).add()
