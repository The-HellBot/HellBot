#Challenge Accepted @Hellboi_Atul now STFO!!!
#Hellbot ported glitch from userge.. le* dc :- mai chadarmod hu jo isko challenge dia
"""
designed By @Krishna_Singhal in userge
ported to hellbot by @kraken_the_badass
"""

import os

from glitch_this import ImageGlitcher
from PIL import Image
from telethon import functions, types

from userbot import CMD_HELP, LOGS
from userbot.utils import admin_cmd, edit_or_reply

@borg.on(admin_cmd(outgoing=True, pattern="(glitch)(?: |$)(.*)"))
async def glitch(hell):
    cmd = hell.pattern_match.group(1)
    hellinput = hell.pattern_match.group(2)
    reply = await hell.get_reply_message()
    hellid = hell.reply_to_msg_id
    hell = await edit_or_reply(hell, "Hahaha.... Glitching🤪")
    if not (reply and (reply.media)):
        await hell.edit("`Media not found...`")
        return
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    hellsticker = await reply.download_media(file="./temp/")
    if not hellsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg")):
        os.remove(hellsticker)
        await hell.edit("`Media not found...`")
        return
    os.path.join("./temp/", "glitch.png")
    if hellinput:
        if not hellinput.isdigit():
            await hell.edit("`You input is invalid, check help`")
            return
        hellinput = int(hellinput)
        if not 0 < hellinput < 9:
            await hell.edit("`Invalid Range...`")
            return
    else:
        hellinput = 2
    if hellsticker.endswith(".tgs"):
        hellfile = os.path.join("./temp/", "glitch.png")
        hellcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {hellsticker} {hellfile}"
        )
        stdout, stderr = (await runcmd(hellcmd))[:2]
        if not os.path.lexists(hellfile):
            await hell.edit("`hellsticker not found...`")
            LOGS.info(stdout + stderr)
        glitch_file = hellfile
    elif hellsticker.endswith(".webp"):
        hellfile = os.path.join("./temp/", "glitch.png")
        os.rename(hellsticker, hellfile)
        if not os.path.lexists(hellfile):
            await hell.edit("`hellsticker not found... `")
            return
        glitch_file = hellfile
    elif hellsticker.endswith(".mp4"):
        hellfile = os.path.join("./temp/", "glitch.png")
        await take_screen_shot(hellsticker, 0, hellfile)
        if not os.path.lexists(hellfile):
            await hell.edit("```hellsticker not found...```")
            return
        glitch_file = hellfile
    else:
        glitch_file = hellsticker
    glitcher = ImageGlitcher()
    img = Image.open(glitch_file)
    if cmd == "glitchs":
        glitched = "./temp/" + "glitched.webp"
        glitch_img = glitcher.glitch_image(img, hellinput, color_offset=True)
        glitch_img.save(glitched)
        await borg.send_file(hell.chat_id, glitched, reply_to=hellid)
        os.remove(glitched)
        await hell.delete()
    elif cmd == "glitch":
        Glitched = "./temp/" + "glitch.gif"
        glitch_img = glitcher.glitch_image(img, hellinput, color_offset=True, gif=True)
        DURATION = 200
        LOOP = 0
        glitch_img[0].save(
            Glitched,
            format="GIF",
            append_images=glitch_img[1:],
            save_all=True,
            duration=DURATION,
            loop=LOOP,
        )
        sandy = await borg.send_file(hell.chat_id, Glitched, reply_to=hellid)
        await borg(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=sandy.media.document.access_hash,
                    file_reference=sandy.media.document.file_reference,
                ),
                unsave=True,
            )
        )
        os.remove(Glitched)
        await hell.delete()
    for files in (hellsticker, glitch_file):
        if files and os.path.exists(files):
            os.remove(files)


CMD_HELP.update(
    {
        "glitch": "**Plugin : **`glitch`\
    \n\n**Syntax : **`.glitch` reply to media file\
    \n**Usage :** glitches the given mediafile(gif , stickers , image, videos) to a gif and glitch range is from 1 to 8.\
    If nothing is mentioned then by default it is 2\
    \n\n**Syntax : **`.glitchs` reply to media file\
    \n**Usage :** glitches the given mediafile(gif , stickers , image, videos) to a sticker and glitch range is from 1 to 8.\
    If nothing is mentioned then by default it is 2\
    "
    }
)
