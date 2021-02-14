"""Schedule Plugin for @UniBorg
Syntax: .schd <time_in_seconds> ;=; <message to send>"""
import asyncio

from hellbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp


@bot.on(admin_cmd(pattern="schd ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="schd ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    ttl = 0
    message = "SYNTAX: `.schd <time_in_seconds> - <message to send>`"
    if input_str:
        await event.delete()
        if "-" in input_str:
            ttl, message = input_str.split("-")
        elif event.reply_to_msg_id:
            await event.delete()
            ttl = int(input_str)
            message = await event.get_reply_message()
        await asyncio.sleep(int(ttl))
        await event.respond(message)
    else:
        await event.edit(message)

CmdHelp("schedule").add_command(
  "schd", "<time in secs> - <msg to send>", "Sends the message in given time(seconds)", ".schd 60 - Hello"
).add()