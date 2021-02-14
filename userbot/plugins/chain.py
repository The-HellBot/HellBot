# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from telethon.tl.functions.messages import SaveDraftRequest

from userbot import CMD_HELP
from hellbot.utils import admin_cmd, sudo_cmd
from userbot.cmdhelp import CmdHelp


@bot.on(admin_cmd(pattern="chain$"))
@bot.on(sudo_cmd(pattern="chain$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Counting...")
    count = -1
    message = event.message
    while message:
        reply = await message.get_reply_message()
        if reply is None:
            await event.client(
                SaveDraftRequest(
                    await event.get_input_chat(), "", reply_to_msg_id=message.id
                )
            )
        message = reply
        count += 1
    await event.edit(f"Chain length: {count}")


CmdHelp("chain").add_command(
  'chain', 'Reply to a message', 'Reply this command to any msg so that it finds chain length of that msg'
).add()