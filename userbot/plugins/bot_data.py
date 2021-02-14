"""Available Commands:
.mf"""

import asyncio

from telethon import functions

from hellbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp


@bot.on(admin_cmd(pattern=r"dc"))  # pylint:disable=E0602
@bot.on(sudo_cmd(pattern=r"dc", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    result = await borg(functions.help.GetNearestDcRequest())  # pylint:disable=E0602
    await edit_or_reply(event, result.stringify())


@bot.on(admin_cmd(pattern=r"config"))  # pylint:disable=E0602
@bot.on(sudo_cmd(pattern=r"config", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    result = await borg(functions.help.GetConfigRequest())  # pylint:disable=E0602
    result = result.stringify()
    logger.info(result)  # pylint:disable=E0602
    await event.edit("""Telethon UserBot powered by @HellBot_Official""")

CmdHelp("bot").add_command(
  "dc", None, "Gets the DataCenter Number"
).add_command(
  "config", None, "😒"
).add()