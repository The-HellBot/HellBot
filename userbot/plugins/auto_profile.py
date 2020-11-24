import asyncio
import base64
import os
import random
import shutil
import time
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.errors import FloodWaitError
from telethon.tl import functions
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME, CMD_HELP, BIO_MSG

DEFAULTUSERBIO = str(BIO_MSG) if BIO_MSG else "ʟɛɢɛռɖaʀʏ ᴀғ ɦɛʟʟɮօt"
CHANGE_TIME = int(os.environ.get("CHANGE_TIME", 60))
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Hell User"

FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"

global AUTOPICSTART
global DIGITALPICSTART
global BLOOMSTART
global AUTONAMESTART
global AUTOBIOSTART

BLOOMSTART = False
AUTOPICSTART = False
AUTOBIOSTART = False
AUTONAMESTART = False
DIGITALPICSTART = False

@bot.on(admin_cmd(pattern="bloom$"))
async def autopic(event):
    if event.fwd_from:
        return
    global BLOOMSTART
    downloaded_file_name = "userbot/original_pic.png"
    downloader = SmartDL(
        Config.DOWNLOAD_PFP_URL_CLOCK, downloaded_file_name, progress_bar=True
    )
    downloader.start(blocking=False)
    photo = "userbot/photo_pfp.png"
    while not downloader.isFinished():
        pass
    if BLOOMSTART:
        return await edit_delete(event, f"`Bloom is already enabled`")
    else:
        BLOOMSTART = True
    await edit_delete(
        event, "`Bloom colour profile pic have been enabled by my master`"
    )
    while BLOOMSTART:
        # RIP Danger zone Here no editing here plox
        R = random.randint(0, 256)
        B = random.randint(0, 256)
        G = random.randint(0, 256)
        FR = 256 - R
        FB = 256 - B
        FG = 256 - G
        shutil.copy(downloaded_file_name, photo)
        image = Image.open(photo)
        image.paste((R, G, B), [0, 0, image.size[0], image.size[1]])
        image.save(photo)
        current_time = datetime.now().strftime("\n Time: %H:%M:%S \n \n Date: %d/%m/%y")
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 60)
        ofnt = ImageFont.truetype(FONT_FILE_TO_USE, 250)
        drawn_text.text((95, 250), current_time, font=fnt, fill=(FR, FG, FB))
        drawn_text.text((95, 250), "      😈", font=ofnt, fill=(FR, FG, FB))
        img.save(photo)
        file = await event.client.upload_file(photo)
        try:
            await event.client(functions.photos.UploadProfilePhotoRequest(file))
            os.remove(photo)
            await asyncio.sleep(CHANGE_TIME)
        except BaseException:
            return

@bot.on(admin_cmd(pattern="autoname$"))
async def _(event):
    if event.fwd_from:
        return
    global AUTONAMESTART
    if AUTONAMESTART:
        return await edit_delete(event, f"`Autoname is already enabled`")
    else:
        AUTONAMESTART = True
    await edit_delete(event, "`Auto Name has been started by my Master `")
    while AUTONAMESTART:
        DM = time.strftime("%d-%m-%y")
        HM = time.strftime("%H:%M")
        name = f"⌚️ {HM}||›  {DEFAULTUSER} ‹||📅 {DM}"
        logger.info(name)
        try:
            await event.client(functions.account.UpdateProfileRequest(first_name=name))
        except FloodWaitError as ex:
            logger.warning(str(e))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(CHANGE_TIME)


@bot.on(admin_cmd(pattern="autobio$"))
async def _(event):
    global AUTOBIOSTART
    if event.fwd_from:
        return
    if AUTOBIOSTART:
        return await edit_delete(event, f"`Autobio is already enabled`")
    else:
        AUTOBIOSTART = True
    await edit_delete(event, "`Autobio has been started by my Master`")
    while AUTOBIOSTART:
        DMY = time.strftime("%d.%m.%Y")
        HM = time.strftime("%H:%M:%S")
        bio = f"📅 {DMY} | {DEFAULTUSERBIO} | ⌚️ {HM}"
        logger.info(bio)
        try:
            await event.client(functions.account.UpdateProfileRequest(about=bio))
        except FloodWaitError as ex:
            logger.warning(str(e))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(CHANGE_TIME)

CMD_HELP.update(
    {
        "auto_profile": """**Plugin : **`auto_profile`
  •**Syntax : **`.autoname`
  •**Function : **__for time along with name, you must set __`ALIVE_NAME`__ in the heroku vars first for this to work__
  •**Syntax : **`.bloom`
  •**Function : **__autodp... May result in account ban... Use on your own risk__
  •**Syntax : **`.autobio`
  •**Function : **__for time along with your bio, Set __`BIO_MSG`__ in the heroku vars first__
"""
    }
)
