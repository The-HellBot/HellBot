""".admin Plugin for @UniBorg"""
from telethon.tl.types import ChannelParticipantsAdmins

from hellbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp


@bot.on(admin_cmd(pattern=r"warn1", outgoing=True))
@bot.on(sudo_cmd(pattern=r"warn1", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    mentions = (
        "⚠️ **You Have** `1/3` **Warnings** ⚠️\n\n__Watch out!__\n⚡ **Reason for warn:** Not given"
    )
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


""".admin Plugin for @UniBorg"""
from telethon.tl.types import ChannelParticipantsAdmins
from uniborg.util import admin_cmd


@bot.on(admin_cmd(pattern=r"warn2", outgoing=True))
@bot.on(sudo_cmd(pattern=r"warn2", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    mentions = (
        "⚠️ **You Have** `2/3` **Warnings** ⚠️\n\n__Watch out!__\n⚡ **Reason for warn:** Not given"
    )
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


""".admin Plugin for @UniBorg"""
from telethon.tl.types import ChannelParticipantsAdmins
from uniborg.util import admin_cmd


@bot.on(admin_cmd(pattern=r"warn3", outgoing=True))
@bot.on(sudo_cmd(pattern=r"warn3", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    mentions = (
        "⚠️ **You Have** `3/3` **Warnings** ⚠️\n\n__Banned!__\n⚡ **Reason for ban:** Not given"
    )
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


""".admin Plugin for @UniBorg"""
from telethon.tl.types import ChannelParticipantsAdmins
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern=r"warn0", outgoing=True))
@bot.on(sudo_cmd(pattern=r"warn0", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`Warning Resetted By Admin...\nYou Have  0/3  warnings`"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


""".admin Plugin for @UniBorg"""
from telethon.tl.types import ChannelParticipantsAdmins
from uniborg.util import admin_cmd


@bot.on(admin_cmd(pattern=r"ocb"))
@bot.on(sudo_cmd(pattern=r"ocb", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    mentions = "**Warning..\n\nBattery Low, Please Charge Your Phone**"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


@bot.on(admin_cmd(pattern=r"fw", outgoing=True))
@bot.on(sudo_cmd(pattern=r"fw", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`U Got A FloodWait:\nReason:telethon.errors.rpcerrorlist.FloodWaitError: A wait of 546578265716823 seconds is required (caused by EditMessageRequest)`"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()

CmdHelp("warn").add_command(
  "warn1", "<reply to someone>", "Fake warning"
).add_command(
  "warn2", "<reply>", "Fake warning 2"
).add_command(
  "warn3", "<reply>", "Fake warning 3"
).add_command(
  "ocb", None, "Try it out yourself"
).add_command(
  "fw", None, "Gets floodwait for a year"
).add()