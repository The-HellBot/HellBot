"""Execute GNU/Linux commands inside Telegram
Syntax: .lsroot , .lslocal"""
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import asyncio
import io
import os
import time

from telethon import events

from hellbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp

if not os.path.isdir("./SAVED"):
    os.makedirs("./SAVED")
if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
    os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)


@bot.on(admin_cmd(pattern="ls ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="ls ?(.*)", allow_sudo=True))
async def lst(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str:
        msg = "📂 **Files in {} :**\n".format(input_str)
        files = os.listdir(input_str)
    else:
        msg = "📂 **Files in Current Directory :**\n"
        files = os.listdir(os.getcwd())
    for file in files:
        msg += "📑 `{}`\n".format(file)
    if len(msg) <= Config.MAX_MESSAGE_SIZE_LIMIT:
        await edit_or_reply(event, msg)
    else:
        msg = msg.replace("`", "")
        out = "filesList.txt"
        with open(out, "w") as f:
            f.write(f)
        await borg.send_file(
            event.chat_id,
            out,
            force_document=True,
            allow_cache=False,
            caption="`Output is huge. Sending as a file...`",
        )
        await event.delete()
        

@bot.on(admin_cmd(pattern="ls_local$", outgoing=True))
@bot.on(sudo_cmd(pattern="ls_local$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    PROCESS_RUN_TIME = 100
    #    dirname = event.pattern_match.group(1)
    #    tempdir = "localdir"
    cmd = "ls -lh ./DOWNLOADS/"
    #    if dirname == tempdir:

    event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = f"**Files in [Hêllẞø†](t.me/hellbot_official) DOWNLOADS Folder:**\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id,
            )
            await event.delete()
    if stderr.decode():
        await edit_or_reply(event, f"**{stderr.decode()}**")
        return
    await edit_or_reply(event, f"{OUTPUT}`{stdout.decode()}`")


@bot.on(admin_cmd(pattern="ls_root$", outgoing=True))
@bot.on(sudo_cmd(pattern="ls_root$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    PROCESS_RUN_TIME = 100
    cmd = "ls -lh"

    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = f"**Files in root directory:**\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id,
            )
            await event.delete()
    if stderr.decode():
        await edit_or_reply(event, f"**{stderr.decode()}**")
        return
    await edit_or_reply(event, f"{OUTPUT}`{stdout.decode()}`")


@bot.on(admin_cmd(pattern="ls_saved$", outgoing=True))
@bot.on(sudo_cmd(pattern="ls_saved$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    PROCESS_RUN_TIME = 100
    cmd = "ls ./SAVED/"

    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = f"**Files in SAVED directory:**\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id,
            )
            await event.delete()
    if stderr.decode():
        await edit_or_reply(event, f"**{stderr.decode()}**")
        return
    await edit_or_reply(event, f"{OUTPUT}`{stdout.decode()}`")


@bot.on(admin_cmd(pattern="rnsaved ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="rnsaved ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    PROCESS_RUN_TIME = 100
    input_str = event.pattern_match.group(1)
    if "|" in input_str:
        src, dst = input_str.split("|")
        src = src.strip()
        dst = dst.strip()
    cmd = f"mv ./SAVED/{src} ./SAVED/{dst}"
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = f"**Files in root directory:**\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id,
            )
            await event.delete()
    if stderr.decode():
        await edit_or_reply(event, f"**{stderr.decode()}**")
        return
    await edit_or_reply(event, f"File renamed `{src}` to `{dst}`")


@bot.on(admin_cmd(pattern="rnlocal ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="rnlocal ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    PROCESS_RUN_TIME = 100
    input_str = event.pattern_match.group(1)
    if "|" in input_str:
        src, dst = input_str.split("|")
        src = src.strip()
        dst = dst.strip()
    cmd = f"mv ./DOWNLOADS/{src} ./DOWNLOADS/{dst}"
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = f"**Files in root directory:**\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id,
            )
            await event.delete()
    if stderr.decode():
        await edit_or_reply(event, f"**{stderr.decode()}**")
        return
    await edit_or_reply(event, f"File renamed `{src}` to `{dst}`")


@bot.on(admin_cmd(pattern="delsave (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="delsave (.*)", allow_sudo=True))
async def handler(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    pathtofile = f"./SAVED/{input_str}"

    if os.path.isfile(pathtofile):
        os.remove(pathtofile)
        await edit_or_reply(event, "✅ File Deleted 🗑")

    else:
        await edit_or_reply(event, "⛔️File Not Found😬")


@bot.on(admin_cmd(pattern="delocal (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="delocal (.*)", allow_sudo=True))
async def handler(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    pathtofile = f"./BotHub/{input_str}"

    if os.path.isfile(pathtofile):
        os.remove(pathtofile)
        await edit_or_reply(event, "✅ File Deleted 🗑")

    else:
        await edit_or_reply(event, "⛔️File Not Found😬")


CmdHelp("filemanager").add_command(
  'ls_local', None, 'Gives the list of downloaded medias in your hellbot server.'
).add_command(
  'ls_root', None, 'Gives the list of all files in root directory of Hellbot repo.'
).add_command(
  'ls_saved', None, 'Gives the list of all files in Saved directory of your hellbot server'
).add_command(
  'rnsaved', 'saved file name', 'Renames the file in saved directory'
).add_command(
  'rnlocal', 'downloaded file name', 'Renames the file in downloaded directory'
).add_command(
  'delsave', 'saved path', 'Deletes the file from given saved path'
).add_command(
  'delocal', 'downloaded path', 'Deletes the file from given downloaded path'
).add_command(
  'ls', '<path name>', 'Gives the list of all files in the given path'
).add()