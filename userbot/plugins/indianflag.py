# Coded by @CyberBoyAyush
# For HellBot : https://github.com/HellBoy-OP/HellBot


from telethon import events
import asyncio
from userbot.utils import admin_cmd

@borg.on(admin_cmd("inflag"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0,36)
    await event.edit("Hello")
    animation_chars = [
    "Indian Flag",
    "**🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧\n⬜️⬜️⬜️⬜️⬜️🟦🟦🟦⬜️⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️🟦🟦🟦⬜️⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️🟦🟦🟦⬜️⬜️⬜️⬜️⬜️\n🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩\n\n                🧡🤍💚\n\nProud To Be An Indian❣️!!**"
    ]
            

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
