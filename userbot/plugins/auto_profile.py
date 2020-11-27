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
global AUTONAMESTART
global AUTOBIOSTART

BLOOMSTART = False
AUTOPICSTART = False
AUTOBIOSTART = False
AUTONAMESTART = False
DIGITALPICSTART = False


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
  •**Syntax : **`.autobio`
  •**Function : **__for time along with your bio, Set __`BIO_MSG`__ in the heroku vars first__
"""
    }
)
