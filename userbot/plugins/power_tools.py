"""Restart or Terminate the bot from any chat
Available Commands:
.restartsys
.shutdown"""
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html
import os
import sys
import asyncio
from os import execl
from time import sleep

from hellbot.utils import admin_cmd
from userbot.cmdhelp import CmdHelp
from userbot import HEROKU_APP, bot

@bot.on(admin_cmd(pattern="restart"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Restarting **[ ░░░ ]** ...\nType `.ping` or `.help` to check if I am working 🙂")
    await event.edit("Restarting **[ █░░ ]** ...\nType `.ping` or `.help` to check if I am working 🙂")
    await event.edit("Restarting **[ ██░ ]** ...\nType `.ping` or `.help` to check if I am working 🙂")
    await event.edit("Restarting **[ ███ ]** ...\nType `.ping` or `.help` to check if I am working 🙂")
    await event.edit("Restarted **[ ✓ ]** ...\nType `.ping` or `.help` to check if I am working 🙂")
    await bot.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()

@bot.on(admin_cmd(pattern="shutdown$"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("**[ ! ]** `Turning off bot now ... Manually turn me on later` ಠ_ಠ")
    if HEROKU_APP is not None:
        HEROKU_APP.process_formation()["userbot"].scale(0)
    else:
        sys.exit(0)


CmdHelp("power_tools").add_command(
  "restart", None, "Restarts your userbot. Redtarting Bot may result in better functioning of bot when its laggy"
).add_command(
  "shutdown", None, "Turns off Dynos of Userbot. Userbot will stop working unless you manually turn it on from heroku"
).add()
