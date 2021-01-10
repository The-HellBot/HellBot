import asyncio
import os
from datetime import datetime
from pathlib import Path
from telethon import events
from telethon import functions, types
from telethon.tl.types import InputMessagesFilterDocument
from userbot.utils import admin_cmd, load_module, remove_plugin, edit_or_reply, sudo_cmd
from userbot import ALIVE_NAME, CmdHelp
from userbot import bot as hellbot

DELETE_TIMEOUT = 5
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Hell User"
hell_logo = "./KRAKEN/hellbot_logo.jpg"


@hellbot.on(admin_cmd(pattern=r"send (?P<shortname>\w+)", outgoing=True))
@hellbot.on(sudo_cmd(pattern=r"send (?P<shortname>\w+)", allow_sudo=True))
async def send(event):
    if event.fwd_from:
        return
    kraken = hellbot.uid
    message_id = event.message.id
    thumb = hell_logo
    input_str = event.pattern_match.group(1)
    the_plugin_file = "./userbot/plugins/{}.py".format(input_str)
    if os.path.exists(the_plugin_file):
        start = datetime.now()
        lauda = await event.client.send_file(
            event.chat_id,
            the_plugin_file,
            force_document=True,
            allow_cache=False,
            thumb=thumb,
            reply_to=message_id,
        )
        end = datetime.now()
        time_taken_in_ms = (end - start).seconds
        await edit_or_reply(lauda, f"**⍟ Plugin name ≈** `{input_str}`\n**⍟ Uploaded in ≈** `{time_taken_in_ms} secs`\n**⍟ Uploaded by ≈** [{DEFAULTUSER}](tg://user?id={kraken})\n"
        )
        await asyncio.sleep(DELETE_TIMEOUT)
        await event.delete()
    else:
        await edit_or_reply(event, "File not found..... Kek")

@hellbot.on(admin_cmd(pattern=r"install"))
@hellbot.on(sudo_cmd(pattern=r"install", allow_sudo=True))
async def install(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        try:
            downloaded_file_name = (
                await event.client.download_media(  # pylint:disable=E0602
                    await event.get_reply_message(),
                    "userbot/plugins/",  # pylint:disable=E0602
                )
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                await edit_or_reply(event, 
                    "Plugin `{}` is installed successfully".format(
                        os.path.basename(downloaded_file_name)
                    )
                )
            else:
                os.remove(downloaded_file_name)
                await edit_or_reply(event, 
                    "**Error!**\nPlugin cannot be installed!\n Or may have been pre-installed."
                )
        except Exception as e:  # pylint:disable=C0103,W0703
            await edit_or_reply(event, str(e))
            os.remove(downloaded_file_name)
    await asyncio.sleep(DELETE_TIMEOUT)
    await event.delete()
    
@hellbot.on(admin_cmd(pattern=r"uninstall (?P<shortname>\w+)", outgoing=True))
@hellbot.on(sudo_cmd(pattern=r"uninstall (?P<shortname>\w+)", allow_sudo=True))
async def unload(kraken):
    if kraken.fwd_from:
        return
    shortname = kraken.pattern_match["shortname"]
    dir_path =f"./userbot/plugins/{shortname}.py"
    try:
        remove_plugin(shortname)
        os.remove(dir_path)
        await kraken.edit(f"Uninstalled `{shortname}` successfully")
    except OSError as e:
        await kraken.edit("Error: %s : %s" % (dir_path, e.strerror))

@hellbot.on(admin_cmd(pattern=r"unload (?P<shortname>\w+)$"))
async def unload(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        remove_plugin(shortname)
        await event.edit(f"Successfully unloaded `{shortname}`")
    except Exception as e:
        await event.edit(
            "Successfully unloaded {shortname}\n{}".format(
                shortname, str(e)
            )
        )


@hellbot.on(admin_cmd(pattern=r"load (?P<shortname>\w+)$"))
async def load(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        try:
            remove_plugin(shortname)
        except BaseException:
            pass
        load_module(shortname)
        await event.edit(f"Successfully loaded `{shortname}`")
    except Exception as e:
        await event.edit(
            f"Sorry, could not load {shortname} because of the following error.\n{str(e)}"
        )

CmdHelp("core").add_command(
  "install", "<reply to a .py file>", "Installs the replied python file if suitable to userbot codes"
).add_command(
  "uninstall", "<plugin name>", "Uninstalls the given plugin from userbot. To get that again do .restart", "uninstall alive"
).add_command(
  "load", "<plugin name>", "Loades the unloaded plugin to your userbot", "load alive"
).add_command(
  "unload", "<plugin name>", "Unloads the plugin from your userbot", "unload alive"
).add_command(
  "send", "<file name>", "Sends the given file from your userbot server, if any.", "send alive"
).add()