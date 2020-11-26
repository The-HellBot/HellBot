import asyncio
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Hell User"
PM_IMG = "https://telegra.ph/file/8f9f8f9d884cf2d9cc72a.jpg"
pm_caption = "**Iᵐメʜɪɴᴀᴛᴀ✿ Online**\n"

pm_caption += f"**ᎷᎩ ᏰᎧᏕᏕ**               : {DEFAULTUSER}\n"

pm_caption += "тєℓєтнσи νєяѕισи    :  15.0.0 \n"

pm_caption += "σffι¢ιαℓ ¢нαииєℓ      : [ᴊᴏɪɴ](https://t.me/HellBot_Official)\n"

pm_caption += "σffι¢ιαℓ gяσυρ         : [ᴊᴏɪɴ](https://t.me/HellBot_Official_Chat)\n"

pm_caption += "ℓι¢єиѕє                     : [ӀíϲҽղՏҽ](https://github.com/HellBoy-OP/HellBot/blob/master/LICENSE)\n"

pm_caption += "¢σρуяιgнт                 : [HellBot-Owner](https://github.com/HellBoy-OP)\n"

pm_caption += " [...▄███▄███▄\n....█████████\n.......▀█████▀\n............▀█▀\n](https://t.me/hellbot_official)\n"
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 
