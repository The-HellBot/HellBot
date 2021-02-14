
import os
import textwrap

from PIL import Image, ImageDraw, ImageFont

from hellbot.utils import admin_cmd, sudo_cmd, edit_or_reply


@bot.on(admin_cmd(pattern=r"mmf ?(.*)"))
@bot.on(sudo_cmd(pattern=r"mmf ?(.*)", allow_sudo=True))
async def handler(event):

    if event.fwd_from:

        return

    if not event.reply_to_msg_id:

        await edit_or_reply(event, "Usage:- `memify upper text ; lower text`")

        return

    reply_message = await event.get_reply_message()

    if not reply_message.media:

        await edit_or_reply(event, "Reply to a image/sticker")

        return

    file = await borg.download_media(reply_message, Var.TEMP_DOWNLOAD_DIRECTORY)

    a = await edit_or_reply(event, "Hahaha...Memifying this image....")

    text = str(event.pattern_match.group(1)).strip()

    if len(text) < 1:

        return await edit_or_reply(a, "Usage:- `memify upper text ; lower text`")

    meme = await drawText(file, text)

    await event.client.send_file(event.chat_id, file=meme, force_document=False)

    os.remove(meme)

    await event.delete()

    await a.delete()


async def drawText(image_path, text):

    img = Image.open(image_path)

    os.remove(image_path)

    i_width, i_height = img.size

    if os.name == "nt":

        fnt = "arial.ttf"

    else:

        fnt = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

    m_font = ImageFont.truetype(fnt, int((70 / 640) * i_width))

    if ";" in text:

        upper_text, lower_text = text.split(";")

    else:

        upper_text = text

        lower_text = ""

    draw = ImageDraw.Draw(img)

    current_h, pad = 10, 5

    if upper_text:

        for u_text in textwrap.wrap(upper_text, width=15):

            u_width, u_height = draw.textsize(u_text, font=m_font)

            draw.text(
                xy=(((i_width - u_width) / 2) - 2, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )

            draw.text(
                xy=(((i_width - u_width) / 2) + 2, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )

            draw.text(
                xy=((i_width - u_width) / 2, int(((current_h / 640) * i_width)) - 2),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )

            draw.text(
                xy=(((i_width - u_width) / 2), int(((current_h / 640) * i_width)) + 2),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )

            draw.text(
                xy=((i_width - u_width) / 2, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(255, 255, 255),
            )

            current_h += u_height + pad

    if lower_text:

        for l_text in textwrap.wrap(lower_text, width=15):

            u_width, u_height = draw.textsize(l_text, font=m_font)

            draw.text(
                xy=(
                    ((i_width - u_width) / 2) - 2,
                    i_height - u_height - int((20 / 640) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )

            draw.text(
                xy=(
                    ((i_width - u_width) / 2) + 2,
                    i_height - u_height - int((20 / 640) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )

            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    (i_height - u_height - int((20 / 640) * i_width)) - 2,
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )

            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    (i_height - u_height - int((20 / 640) * i_width)) + 2,
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )

            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    i_height - u_height - int((20 / 640) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(255, 255, 255),
            )

            current_h += u_height + pad

    image_name = "memify.webp"

    webp_file = os.path.join(Var.TEMP_DOWNLOAD_DIRECTORY, image_name)

    img.save(webp_file, "webp")

    return webp_file
