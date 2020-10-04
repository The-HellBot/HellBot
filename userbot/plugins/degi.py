"""Fun pligon...for DC
\nCode by DC , ©[Hellboi_atul](https://t.me/hellboi_atul)
type `.degi` and `.nehi` to see the fun.
"""
import random, re
from uniborg.util import admin_cmd
import asyncio
from telethon import events

@borg.on(admin_cmd(pattern="degi ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("Wo")
        await asyncio.sleep(0.7)
        await event.edit("Degi")
        await asyncio.sleep(1)
        await event.edit("Tum")
        await asyncio.sleep(0.8)
        await event.edit("Ekbar")
        await asyncio.sleep(0.9)
        await event.edit("Mang")
        await asyncio.sleep(1)
        await event.edit("Kar")
        await asyncio.sleep(0.8)
        await event.edit("Toh")
        await asyncio.sleep(0.7)
        await event.edit("Dekho")
        await asyncio.sleep(1)
        await event.edit("`Wo Degi Tum Ekbar Mang Kar toh Dekho`")

@borg.on(events.NewMessage(pattern=r"\.nehi", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("`Wo PaKkA DeGi Tu ManG KaR ToH DekH`")
    await asyncio.sleep(999)
