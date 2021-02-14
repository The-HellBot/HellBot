# Enjoy

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import bot
from hellbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp


@bot.on(admin_cmd(pattern="nhentai(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="nhentai(?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group()
    chat = "@nHentaiBot"
    await edit_or_reply(event, "```Processing```")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=424466890)
            )
            await bot.send_message(chat, link)
            response = await response
        except YouBlockedUserError:
            await edit_or_reply(event, "```Please unblock @nHentaiBot and try again```")
            return
        if response.text.startswith("**Sorry I couldn't get manga from**"):
            await edit_or_reply(event, "```I think this is not the right link```")
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


CmdHelp("nhentai").add_command(
  "nhentai", "<link>", "Send one link like https://nhentai.net/g/234638 and this will turn it into a Telegra.ph Instant View articles!"
).add()