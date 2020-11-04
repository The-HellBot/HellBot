from userbot import bot
from telethon import events
from userbot.utils import command, remove_plugin, load_module
from var import Var
import importlib
from pathlib import Path
from userbot import LOAD_PLUG, ALIVE_NAME
import sys
import asyncio
import traceback
import os
import userbot.utils
from datetime import datetime

DELETE_TIMEOUT = 5

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Hell User"

@command(pattern="^.install", outgoing=True)
async def install(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        try:
            downloaded_file_name = await event.client.download_media(  # pylint:disable=E0602
                await event.get_reply_message(),
                "userbot/plugins/"  # pylint:disable=E0602
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                await event.edit("Installed Plugin `{}` By @HellBot_Official".format(os.path.basename(downloaded_file_name)))
            else:
                os.remove(downloaded_file_name)
                await event.edit("Errors! This plugin is already installed/pre-installed.")
        except Exception as e:  # pylint:disable=C0103,W0703
            await event.edit(str(e))
            os.remove(downloaded_file_name)
    await asyncio.sleep(DELETE_TIMEOUT)
    await event.delete()

@command(pattern="^.send (?P<shortname>\w+)$", outgoing=True)
async def send(event):
    if event.fwd_from:
        return
    kraken = bot.uid
    message_id = event.message.id
    input_str = event.pattern_match(1)
    the_plugin_file = "./userbot/plugins/{}.py".format(input_str)
    if os.path.exists(the_plugin_file):
    start = datetime.now()
    hell = await event.client.send_file(
        event.chat_id,
        the_plugin_file,
        force_document=True,
        allow_cache=False,
        reply_to=message_id
    )
    end = datetime.now()
    time_taken_in_ms = (end - start).seconds
    await hell.edit(f"**『Module Name』:** `{input_str}`\n**『Uploaded in』**: `{time_taken_in_ms} secs`\n**『Uploaded by』:** [{DEFAULTUSER}](tg://user?id={kraken})\n"
        )
    await asyncio.sleep(DELETE_TIMEOUT)
    await event.delete()
    else:
        await edit_or_reply(event, "**File Not found... Kek**")

@command(pattern="^.unload (?P<shortname>\w+)$", outgoing=True)
async def unload(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        remove_plugin(shortname)
        await event.edit(f"Unloaded {shortname} successfully")
    except Exception as e:
        await event.edit("Successfully unload {shortname}\n{}".format(shortname, str(e)))

@command(pattern="^.load (?P<shortname>\w+)$", outgoing=True)
async def load(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        try:
            remove_plugin(shortname)
        except:
            pass
        load_module(shortname)
        await event.edit(f"Successfully loaded {shortname}")
    except Exception as e:
        await event.edit(f"Could not load {shortname} because of the following error.\n{str(e)}")
