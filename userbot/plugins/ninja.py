# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import asyncio

import telethon.utils
from telethon import events
from userbot.utils import admin_cmd, sudo_cmd, edit_or_reply, errors_handler
from userbot.cmdhelp import CmdHelp


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