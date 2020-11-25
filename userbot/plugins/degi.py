
import random, re
from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd
import asyncio
from telethon import events
from userbot import CMD_HELP

@bot.on(admin_cmd(pattern=f"degi$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"degi$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
        event = await edit_or_reply(event, "degi")
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

@bot.on(admin_cmd(pattern=f"nehi$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"nehi$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "nehi")
    await event.edit("`Wo PaKkA DeGi Tu ManG KaR ToH DekH`")
    await asyncio.sleep(999)
