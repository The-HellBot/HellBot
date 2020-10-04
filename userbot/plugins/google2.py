""" Powered by @Google
Available Commands:
.gs <query>

.grs"""



import requests
from bs4 import BeautifulSoup
from datetime import datetime
from google_images_download import google_images_download
from uniborg.util import admin_cmd


def progress(current, total):
    logger.info("Downloaded {} of {}\nCompleted {}".format(current, total, (current / total) * 100))


@borg.on(admin_cmd(pattern="gs (.*)"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    await event.edit("searching")
    # SHOW_DESCRIPTION = False
    input_str = event.pattern_match.group(1) # + " -inurl:(htm|html|php|pls|txt) intitle:index.of \"last modified\" (mkv|mp4|avi|epub|pdf|mp3)"
    input_url = "https://bots.shrimadhavuk.me/search/?q={}".format(input_str)
    headers = {"USER-AGENT": "UniBorg"}
    response = requests.get(input_url, headers=headers).json()
    output_str = " "
    for result in response["results"]:
        text = result.get("title")
        url = result.get("url")
        description = result.get("description")
        image = result.get("image")
        output_str += " 👉🏻  [{}]({}) \n\n".format(text, url)
    end = datetime.now()
    ms = (end - start).seconds
    await event.edit("searched Google for {} in {} seconds. \n{}".format(input_str, ms, output_str), link_preview=False)
    await asyncio.sleep(5)
    await event.edit("**Google: {}\n{}**".format(input_str, output_str), link_preview=False)





@borg.on(admin_cmd(pattern="grs"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    BASE_URL = "http://www.google.com"
    OUTPUT_STR = "Reply to an image to do Google Reverse Search"
    if event.reply_to_msg_id:
        await event.edit("Pre Processing Media")
        previous_message = await event.get_reply_message()
        previous_message_text = previous_message.message
        if previous_message.media:
            downloaded_file_name = await borg.download_media(
                previous_message,
                Config.TMP_DOWNLOAD_DIRECTORY
            )
            SEARCH_URL = "{}/searchbyimage/upload".format(BASE_URL)
            multipart = {
                "encoded_image": (downloaded_file_name, open(downloaded_file_name, "rb")),
                "image_content": ""
            }
            # https://stackoverflow.com/a/28792943/4723940
            google_rs_response = requests.post(SEARCH_URL, files=multipart, allow_redirects=False)
            the_location = google_rs_response.headers.get("Location")
            os.remove(downloaded_file_name)
        else:
            previous_message_text = previous_message.message
            SEARCH_URL = "{}/searchbyimage?image_url={}"
            request_url = SEARCH_URL.format(BASE_URL, previous_message_text)
            google_rs_response = requests.get(request_url, allow_redirects=False)
            the_location = google_rs_response.headers.get("Location")
        await event.edit("Found Google Result")
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
*Possible Related Search*: <a href="{prs_url}">{prs_text}</a>

More Info: Open this <a href="{the_location}">LINK</a> in {ms} seconds""".format(**locals())
    await event.edit(OUTPUT_STR, parse_mode="HTML", link_preview=False)


 
