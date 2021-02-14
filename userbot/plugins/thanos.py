import asyncio

from telethon import events
from hellbot.utils import admin_cmd, sudo_cmd, edit_or_reply

@bot.on(admin_cmd(pattern="thanos$", outgoing=True))
@bot.on(sudo_cmd(pattern="thanos$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 16)
  #  input_str = event.pattern_match.group(1)
 #   if input_str == "thanos":
    await edit_or_reply(event, "Thanos")
    animation_chars = [
        "JINGLE BELLS",
        "THANOS SMELL LOKI NECKED SNAPPED AWAY",
        "PETER DIED TONY CRIED NOBODY SAVED THE DAY HEY!!",
        "Jingle bells Thanos smells Loki's necked snapped away Peter died Tony cried And nobody saved the day",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 4])
