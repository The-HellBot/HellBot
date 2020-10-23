#Made by @Kraken_the_badass for @HellBot_Official

"""Emoji
Available Commands:
click gift as soon as fast as possible
.hgame
build by @Hack12R..
Second game is a xogame
Command:- .xogame .... By @Kraken_The_BadASS"""

from telethon import events
import asyncio
from userbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from var import Var


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1.2
    animation_ttl = range(0, 14)
    input_str = event.pattern_match.group(1)
    if input_str == "game":
        await event.edit(input_str)
        animation_chars = [
       
            "**Welcome To HellBot Repo Game**",
            "**Click The Gift As Fast As Possible**",
            "**Game Starts in 3**",
            "**Game Starts in 2**",
            "**Game Starts in 1**",    
            "🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇",
            "🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆[🎁](https://github.com/HellBoy-OP/HellBot)🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇",
            "🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆[🎁](https://github.com/HellBoy-OP/HellBot)🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇",
            "🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇[🎁](https://github.com/HellBoy-OP/HellBot)🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇",
            "🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆[🎁](https://github.com/HellBoy-OP/HellBot)🎆\n🎇🎆🎇🎆🎇🎆🎇",
            "🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n[🎁](https://github.com/HellBoy-OP/HellBot)🎆🎇🎆🎇🎆🎇",
            "🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇[🎁](https://HellBoy-OP/HellBot)\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆",
            "🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇\n🎇🎆🎇🎆🎇🎆🎇",
            "**Game Over**"
 ]
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 14])


from userbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from var import Var

@borg.on(admin_cmd(pattern="xogame$"))
async def gamez(event):
    if event.fwd_from:
        return
    botusername = "@xobot"
    noob = "play"
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    tap = await bot.inline_query(botusername, noob) 
    await tap[0].click(event.chat_id)
    await event.delete()
