import asyncio
import time

from telethon.errors import FloodWaitError
from telethon.tl import functions
from userbot.utils import edit_or_reply, admin_cmd

from userbot import ALIVE_NAME, CMD_HELP, BIO_MSG


DEFAULTUSERBIO = str(BIO_MSG) if BIO_MSG else "ʟɛɢɛռɖaʀʏ ᴀғ ɦɛʟʟɮօt"
DEL_TIME_OUT = 60
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Hell User"


@bot.on(admin_cmd(pattern="autoname"))  # pylint:disable=E0602
async def _(event):
    hell = await edit_or_reply(event, "`Starting AutoName Please Wait`")
    if event.fwd_from:
        return

    while True:

        HB = time.strftime("%d-%m-%y")

        HE = time.strftime("%H:%M")

        name = f"🕒{HE} ⚡{DEFAULTUSER}⚡ 📅{HB}"

        logger.info(name)

        try:

            await borg(
                functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                    first_name=name
                )
            )

        except FloodWaitError as ex:

            logger.warning(str(e))

            await asyncio.sleep(ex.seconds)

        # else:

        # logger.info(r.stringify())

        # await borg.send_message(  # pylint:disable=E0602

        #     Config.PRIVATE_GROUP_BOT_API_ID,  # pylint:disable=E0602

        #     "Successfully Changed Profile Name"

        # )

        await asyncio.sleep(DEL_TIME_OUT)

    await hell.edit(f"Auto Name has been started my Master")


@bot.on(admin_cmd(pattern="autobio"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    while True:
        DMY = time.strftime("%d.%m.%Y")
        HM = time.strftime("%H:%M:%S")
        bio = f"📅 {DMY} | {DEFAULTUSERBIO} | ⌚️ {HM}"
        logger.info(bio)
        try:
            await borg(
                functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                    about=bio
                )
            )
        except FloodWaitError as ex:
            logger.warning(str(e))
            await asyncio.sleep(ex.seconds)
        # else:
        # logger.info(r.stringify())
        # await borg.send_message(  # pylint:disable=E0602
        # Config.PRIVATE_GROUP_BOT_API_ID,  # pylint:disable=E0602
        # "Successfully Changed Profile Bio"
        # )
        await asyncio.sleep(DEL_TIME_OUT)




CMD_HELP.update(
    {
        "auto_profile": "**Auto_Profile**\
\n\n**Syntax : **`.autobio`\
\n**Usage :** Change your bio with time\
\n\n**Syntax : **`.autoname`\
\n**Usage :** Change your Name With Time"
    }
)
