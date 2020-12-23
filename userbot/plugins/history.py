import logging

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp


@bot.on(admin_cmd(pattern="history ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="history ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await edit_or_reply(event, "```Reply to any user message.```")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await edit_or_reply(event, "```reply to text message```")
        return
    chat = "@SangMataInfo_bot"
    reply_message.sender
    if reply_message.sender.bot:
        await edit_or_reply(event, "```Reply to actual users message.```")
        return
    await edit_or_reply(event, "```Processing```")
    async with borg.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=461843263)
            )
            await borg.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await edit_or_reply(event, "`Please unblock` @sangmatainfo_bot `and try again`")
            return
        if response.text.startswith("Forward"):
            await event.edit(
                "```This user had disabled their forward privacy... Ask 'em to enable🥺```"
            )
        else:
            await edit_or_reply(event, f"{response.message.message}")

CmdHelp("history").add_command(
  "history", "<reply to a user>", "Fetches the Name history of the tagged user"
).add()