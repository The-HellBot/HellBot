import asyncio
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import bot
from hellbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp


@bot.on(admin_cmd(pattern=r"ss(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern=r"ss(?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await edit_or_reply(event, "```Reply to any user message.```")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await edit_or_reply(event, "```Reply to text message```")
        return
    chat = "@QuotLyBot"
    reply_message.sender
    if reply_message.sender.bot:
        await edit_or_reply(event, "```Reply to actual users message.```")
        return
    await edit_or_reply(event, "```Making a Quote```")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1031952739)
            )
            await conv.send_message(f"/qcolor")
            await asyncio.sleep(3)
            await bot.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("```Please unblock @QuotLyBot and try again```")
            return
        if response.text.startswith("Hi!"):
            await edit_or_reply(event, "```Can you kindly disable your forward privacy settings for good?```"
            )
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)

@bot.on(admin_cmd(pattern=r"css ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern=r"css ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await edit_or_reply(event, "```Reply to any user message.```")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await edit_or_reply(event, "```Reply to text message```")
        return
    hell = event.pattern_match.group(1)
    chat = "@QuotLyBot"
    reply_message.sender
    if reply_message.sender.bot:
        await edit_or_reply(event, "```Reply to actual users message.```")
        return
    await edit_or_reply(event, "```Making a Quote```")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1031952739)
            )
            await conv.send_message(f"/qcolor {hell}")
            await asyncio.sleep(4)
            await bot.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("```Please unblock @QuotLyBot and try again```")
            return
        if response.text.startswith("Hi!"):
            await edit_or_reply(event, "```Can you kindly disable your forward privacy settings for good?```"
            )
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


CmdHelp("qbot").add_command(
  "ss", "<reply to a text msg>", "Makes the sticker of the replied text message."
).add_command(
  "css", "<reply to a text msg> <colour name>", "Makes the sticker of the replied text message in desired color"
).add()
