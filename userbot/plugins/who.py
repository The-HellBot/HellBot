import html

from telethon import events, utils
from telethon.tl import types
from userbot.cmdhelp import CmdHelp
from hellbot.utils import admin_cmd, sudo_cmd, edit_or_reply

def get_who_string(who):
    who_string = html.escape(utils.get_display_name(who))
    if isinstance(who, (types.User, types.Channel)) and who.username:
        who_string += f" <i>(@{who.username})</i>"
    who_string += f", <a href='tg://user?id={who.id}'>#{who.id}</a>"
    return who_string


@bot.on(admin_cmd(pattern="urid", outgoing=True))
@bot.on(sudo_cmd(pattern="urid", allow_sudo=True))
async def _(event):
    if not event.message.is_reply:
        who = await event.get_chat()
    else:
        msg = await event.message.get_reply_message()
        if msg.forward:
            # FIXME forward privacy memes
            who = await borg.get_entity(msg.forward.sender_id or msg.forward.channel_id)
        else:
            who = await msg.get_sender()

    await edit_or_reply(event, get_who_string(who), parse_mode="html")


@bot.on(admin_cmd(pattern=r"members", outgoing=True))
@bot.on(sudo_cmd(pattern=r"members", allow_sudo=True))
async def _(event):
    members = [get_who_string(m) async for m in borg.iter_participants(event.chat_id)]

    await edit_or_reply(event, "\n".join(members), parse_mode="html")