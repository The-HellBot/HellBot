"""
Telegram Channel Media Downloader Plugin for userbot.
usage: .geta channel_username [will  get all media from channel, tho there is limit of 3000 there to prevent API limits.]
       .getc number_of_messsages channel_username  
By: @Zero_cool7870
"""
import os
import subprocess

from userbot import CMD_HELP
from hellbot.utils import admin_cmd
from userbot.cmdhelp import CmdHelp

@borg.on(admin_cmd(pattern=r"getc"))
async def get_media(event):
    if event.fwd_from:
        return
    dir = "./temp/"
    try:
        os.makedirs("./temp/")
    except:
        pass
    channel_username = event.text
    limit = channel_username[6:9]
    print(limit)
    channel_username = channel_username[11:]
    print(channel_username)
    await event.edit("Downloading Media From this Channel.")
    msgs = await borg.get_messages(channel_username, limit=int(limit))
    with open("log.txt", "w") as f:
        f.write(str(msgs))
    for msg in msgs:
        if msg.media is not None:
            await borg.download_media(msg, dir)
    ps = subprocess.Popen(("ls", "temp"), stdout=subprocess.PIPE)
    output = subprocess.check_output(("wc", "-l"), stdin=ps.stdout)
    ps.wait()
    output = str(output)
    output = output.replace("b'", "")
    output = output.replace("\n'", "")
    await event.edit("Downloaded " + output + " files.")


@borg.on(admin_cmd(pattern=r"geta"))
async def get_media(event):
    if event.fwd_from:
        return
    dir = "./temp/"
    try:
        os.makedirs("./temp/")
    except:
        pass
    channel_username = event.text
    channel_username = channel_username[7:]

    print(channel_username)
    await event.edit("Downloading All Media From this Channel.")
    msgs = await borg.get_messages(channel_username, limit=3000)
    with open("log.txt", "w") as f:
        f.write(str(msgs))
    for msg in msgs:
        if msg.media is not None:
            await borg.download_media(msg, dir)
    ps = subprocess.Popen(("ls", "temp"), stdout=subprocess.PIPE)
    output = subprocess.check_output(("wc", "-l"), stdin=ps.stdout)
    ps.wait()
    output = str(output)
    output = output.replace("b'", "")
    output = output.replace("\n'", "")
    await event.edit("Downloaded " + output + " files.")


CmdHelp("channel_download").add_command(
  'geta', 'channel username', 'will download all media from channel into your bot server but there is limit of 3000 to prevent API limits.'
).add_command(
  'getc', 'channel username', 'will download latest given number of media from channel into your bot server'
).add()