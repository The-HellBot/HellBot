# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import asyncio

import telethon.utils
from telethon import events
from userbot.utils import admin_cmd, sudo_cmd, edit_or_reply, errors_handler
from userbot.cmdhelp import CmdHelp


async def get_target_message(event):
    if event.is_reply and (await event.get_reply_message()).from_id == borg.uid:
        return await event.get_reply_message()
    async for message in borg.iter_messages(await event.get_input_chat(), limit=20):
        if message.out:
            return message


async def await_read(chat, message):
    chat = telethon.utils.get_peer_id(chat)

    async def read_filter(read_event):
        return read_event.chat_id == chat and read_event.is_read(message)

    fut = borg.await_event(events.MessageRead(inbox=False), read_filter)

    if await is_read(borg, chat, message):
        fut.cancel()
        return

    await fut

)

@bot.on(admin_cmd(outgoing=True, pattern="del$"))
@bot.on(sudo_cmd(allow_sudo=True, pattern="del$"))
@errors_handler
async def delete_it(delme):
    """ For .del command, delete the replied message. """
    msg_src = await delme.get_reply_message()
    if delme.reply_to_msg_id:
        try:
            await msg_src.delete()
            await delme.delete()


CmdHelp("ninja").add_command(
  "del", "<reply to a msg>", "Deletes the replied msg."
).add_command(
  "edit", "<reply to a msg>", "Edits the replied msg"
).add_command(
  "purge", "<reply>", "Purges all messages starting from the reply."
).add_command(
  "purgeme", "<count>", "Deletes 'x' amount of your latest messages."
).add_command(
  "sd", "<time> <message>", "Creates a message that selfdestructs in 'x' seconds. Keep the seconds under 100 since it puts your bot to sleep"
).add()