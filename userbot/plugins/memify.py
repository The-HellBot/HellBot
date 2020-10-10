# For The-TG-Bot-3.0
# By Priyam Kalra
# Parts of the code below is taken from other sources, the links to the
# sources is commented above the taken code

from PIL import Image, ImageFont, ImageDraw
import textwrap
import os
from userbot.events import register
from userbot import (
    CMD_HELP,
    LOGS,
    TEMP_DOWNLOAD_DIRECTORY,
    bot,
    BOTLOG_CHATID)


@register(outgoing=True, pattern=r"\.memify ?(.*)")
async def handler(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("You might want to try `.help memify`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("```Reply to a image/sticker.```")
        return
    file = await bot.download_media(reply_message)
    await event.edit("```Memifying this image! (」ﾟﾛﾟ)｣ ```")
    text = str(event.pattern_match.group(1)).strip()
    if len(text) < 1:
        return await event.edit("You might want to try `.help memify`")
    meme = await drawText(file, text)
    await bot.send_file(event.chat_id, file=meme, force_document=False)
    os.remove(meme)

# Taken from https://github.com/UsergeTeam/Userge-Plugins/blob/master/plugins/memify.py#L64
# Maybe edited to suit the needs of this module


async def drawText(image_path, text):
    img = Image.open(image_path)
    os.remove(image_path)
    shadowcolor = "black"
    i_width, i_height = img.size
    if os.name == "nt":
        fnt = "arial.ttf"
    else:
        fnt = "/usr/share/fonts/TTF/dejavu/OpenSans-Regular.ttf"
    m_font = ImageFont.truetype(fnt, int((70 / 640) * i_width))
    if ";" in text:
        upper_text, lower_text = text.split(";")
    else:
        upper_text = text
        lower_text = ''
    draw = ImageDraw.Draw(img)
    current_h, pad = 10, 5
    if upper_text:
        for u_text in textwrap.wrap(upper_text, width=15):
            u_width, u_height = draw.textsize(u_text, font=m_font)
            draw.text(xy=(((i_width - u_width) / 2) - 2, int((current_h / 640)
                                                             * i_width)), text=u_text, font=m_font, fill=(0, 0, 0))
            draw.text(xy=(((i_width - u_width) / 2) + 2, int((current_h / 640)
                                                             * i_width)), text=u_text, font=m_font, fill=(0, 0, 0))
            draw.text(xy=((i_width - u_width) / 2,
                          int(((current_h / 640) * i_width)) - 2),
                      text=u_text,
                      font=m_font,
                      fill=(0,
                            0,
                            0))
            draw.text(xy=(((i_width - u_width) / 2),
                          int(((current_h / 640) * i_width)) + 2),
                      text=u_text,
                      font=m_font,
                      fill=(0,
                            0,
                            0))

            draw.text(xy=((i_width - u_width) / 2, int((current_h / 640)
                                                       * i_width)), text=u_text, font=m_font, fill=(255, 255, 255))
            current_h += u_height + pad
    if lower_text:
        for l_text in textwrap.wrap(lower_text, width=15):
            u_width, u_height = draw.textsize(l_text, font=m_font)
            draw.text(
                xy=(((i_width - u_width) / 2) - 2, i_height -
                    u_height - int((20 / 640) * i_width)),
                text=l_text, font=m_font, fill=(0, 0, 0))
            draw.text(
                xy=(((i_width - u_width) / 2) + 2, i_height -
                    u_height - int((20 / 640) * i_width)),
                text=l_text, font=m_font, fill=(0, 0, 0))
            draw.text(
                xy=((i_width - u_width) / 2, (i_height -
                                              u_height - int((20 / 640) * i_width)) - 2),
                text=l_text, font=m_font, fill=(0, 0, 0))
            draw.text(
                xy=((i_width - u_width) / 2, (i_height -
                                              u_height - int((20 / 640) * i_width)) + 2),
                text=l_text, font=m_font, fill=(0, 0, 0))

            draw.text(
                xy=((i_width - u_width) / 2, i_height -
                    u_height - int((20 / 640) * i_width)),
                text=l_text, font=m_font, fill=(255, 255, 255))
            current_h += u_height + pad
    image_name = "memify.webp"
    webp_file = os.path.join(image_name)
    img.save(webp_file, "webp")
    return webp_file


CMD_HELP.update({
    "memify": "\
```.memify <text_to_be_pasted_on_top> ; <text_to_be_pasted_on_bottom>```\
\nUsage: Memifies the image/sticker/gif.\
"
})
