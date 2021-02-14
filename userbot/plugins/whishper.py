# Made by @Kraken_The_BadASS for @HellBot_Official

from hellbot.utils import *
from userbot.cmdhelp import CmdHelp


@bot.on(admin_cmd(pattern="wspr ?(.*)"))
@bot.on(sudo_cmd(pattern="wspr ?(.*)", allow_sudo=True))
async def wspr(event):
    if event.fwd_from:
        return
    wwwspr = event.pattern_match.group(1)
    botusername = "@whisperBot"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, wwwspr)
    await tap[0].click(event.chat_id)
    await event.delete()

CmdHelp("whisper").add_command(
  "wspr", "<your message> <reciver username>", "Sends a whisper message to a particular person"
).add()
