
import random, re
from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd
import asyncio
from telethon import events
from userbot import CMD_HELP

@bot.on(admin_cmd(pattern="degi$"))
@bot.on(sudo_cmd(pattern="degi$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "degi")
    await event.edit("WO")
    await asyncio.sleep(1.5)
    await event.edit("DegI")
    await asyncio.sleep(1.5)
    await event.edit("TuM")
    await asyncio.sleep(1.5)
    await event.edit("EkbaR")
    await asyncio.sleep(1.5)
    await event.edit("ManG")
    await asyncio.sleep(1.5)
    await event.edit("KaR")
    await asyncio.sleep(1.5)
    await event.edit("ToH")
    await asyncio.sleep(1.5)
    await event.edit("DekhO")
    await asyncio.sleep(1.5)
    await event.edit("Wo DeGi TuM eKbAr MaNg KaR tOh DeKhO😄")


@bot.on(admin_cmd(pattern=f"nehi$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"nehi$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "nehi")
    await event.edit("`Wo PaKkA DeGi Tu ManG KaR ToH DekH\n AuR NaA De To UskI BheN Ko PakaD😚😚`")
    await asyncio.sleep(999)

CMD_HELP.update(
    {
        "degi": """**Plugin : **`degi`
        
**Commands in degi are **
  •  `.degi`
  •  `.nehi`
  
**Function : **__Leni deni hogi bc...__"""
    }
)
