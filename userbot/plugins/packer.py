
import os
import asyncio

from userbot import CmdHelp
from hellbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot import bot as hellbot


@hellbot.on(admin_cmd(pattern=r"unpack", outgoing=True))
@hellbot.on(sudo_cmd(pattern=r"unpack"))
async def _(event):
    b = await event.client.download_media(await event.get_reply_message())
    a = open(b, "r")
    c = a.read()
    a.close()
    a = await edit_or_reply(event, "```unpacking...```")
    if len(c) > 4095:
        await a.edit("`word limit of telegram is exceded!!! aborting...`")
    else:
        await event.client.send_message(event.chat_id, f"```{c}```")
        await a.delete()
    os.remove(b)


@hellbot.on(admin_cmd(pattern="repack ?(.*)", outgoing=True))
@hellbot.on(sudo_cmd(pattern="repack ?(.*)", allow_sudo=True))
async def _(event):
    a = await event.get_reply_message()
    input_str = event.pattern_match.group(1)
    b = open(input_str, "w")
    b.write(str(a.message))
    b.close()
    a = await edit_or_reply(event, f"Packing into `{input_str}`")
    await asyncio.sleep(2)
    await a.edit(f"Uploading `{input_str}`")
    await asyncio.sleep(2)
    await event.client.send_file(event.chat_id, input_str)
    await a.delete()
    os.remove(input_str)


CmdHelp("packer").add_command(
  "unpack", "<reply to a file>", "Read contents of file and send as a telegram message."
).add_command(
  "repack", "<reply to text> <filename . extension>", "Packs the text and sends as a file of given extension", "<reply to text> example.py"
).add()
