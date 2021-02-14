import os
from datetime import datetime

from PIL import Image
from telegraph import Telegraph, exceptions, upload_file

from userbot import ALIVE_NAME
from hellbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp

HELL_NAME = str(ALIVE_NAME) if ALIVE_NAME else "Hêllẞø†"

kraken = bot.uid

telegraph = Telegraph()
r = telegraph.create_account(short_name=Config.TELEGRAPH_SHORT_NAME)
auth_url = r["auth_url"]


@bot.on(admin_cmd(pattern="t(m|t) ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="t(m|t) ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if Config.PLUGIN_CHANNEL is None:
        await edit_or_reply(event, "Please set the required environment variable `PLUGIN_CHANNEL` for this plugin to work\n\nGo to [HellBot Chat Group](t.me/hellbot_official_chat) for assistance"
        )
        return
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    await borg.send_message(
        Config.PLUGIN_CHANNEL,
        "Created New Telegraph account {} for the current session. \n**Do not give this url to anyone, even if they say they are from Telegram!**".format(
            auth_url
        ),
    )
    optional_title = event.pattern_match.group(2)
    if event.reply_to_msg_id:
        start = datetime.now()
        r_message = await event.get_reply_message()
        input_str = event.pattern_match.group(1)
        if input_str == "m":
            downloaded_file_name = await borg.download_media(
                r_message, Config.TMP_DOWNLOAD_DIRECTORY
            )
            end = datetime.now()
            ms = (end - start).seconds
            await edit_or_reply(event, 
                "Downloaded to {} in {} seconds. \nMaking Telegraph Link.....".format(downloaded_file_name, ms)
            )
            if downloaded_file_name.endswith((".webp")):
                resize_image(downloaded_file_name)
            try:
                start = datetime.now()
                media_urls = upload_file(downloaded_file_name)
            except exceptions.TelegraphException as exc:
                await edit_or_reply(event, "ERROR: " + str(exc))
                os.remove(downloaded_file_name)
            else:
                end = datetime.now()
                ms_two = (end - start).seconds
                os.remove(downloaded_file_name)
                await edit_or_reply(event, 
                   "✓ **File uploaded to [telegraph](https://telegra.ph{})** \n✓ **Time Taken :-** `{}` secs \n✓ **By :- [{}](tg://user?id={})**".format(
                        media_urls[0], (ms + ms_two), HELL_NAME, kraken
                    ),
                    link_preview=True,
                )
        elif input_str == "t":
            user_object = await borg.get_entity(r_message.sender_id)
            title_of_page = user_object.first_name  # + " " + user_object.last_name
            # apparently, all Users do not have last_name field
            if optional_title:
                title_of_page = optional_title
            page_content = r_message.message
            if r_message.media:
                if page_content != "":
                    title_of_page = page_content
                downloaded_file_name = await borg.download_media(
                    r_message, Config.TMP_DOWNLOAD_DIRECTORY
                )
                m_list = None
                with open(downloaded_file_name, "rb") as fd:
                    m_list = fd.readlines()
                for m in m_list:
                    page_content += m.decode("UTF-8") + "\n"
                os.remove(downloaded_file_name)
            page_content = page_content.replace("\n", "<br>")
            response = telegraph.create_page(title_of_page, html_content=page_content)
            end = datetime.now()
            ms = (end - start).seconds
            hellboy = f"https://telegra.ph/{response['path']}"
            await edit_or_reply(event, 
                  f"✓ **Pasted to** [telegraph]({hellboy}) \n✓ **Time Taken :-** `{ms}` secs\n✓** By :- **[{HELL_NAME}](tg://user?id={kraken})", link_preview=True)
    else:
        await edit_or_reply(event, 
            "Reply to a message to get a permanent telegra.ph link."
        )


def resize_image(image):
    im = Image.open(image)
    im.save(image, "PNG")


CmdHelp("telegraph").add_command(
  "tt", "<reply to text message>", "Uploads the replied text message to telegraph making a short telegraph link"
).add_command(
  "tm", "<reply to media>", "Uploads the replied media (sticker/ gif/ video/ image) to telegraph and gives a short telegraph link"
).add()