import asyncio
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Hell User"
PM_IMG = "https://telegra.ph/file/f34675b4e94d4290c0b6b.mp4"
pm_caption = "🔱 **Hêllẞø† Is Online** 🔱\n\n"

pm_caption += f"🔸🔹 **ɱყ ცơʂʂ**           :   {DEFAULTUSER}\n"

pm_caption += "🔹🔸 тєℓєтнσи νєяѕισи   :   1.15.0 \n"

pm_caption += "🔸🔹 σffι¢ιαℓ ¢нαииєℓ   :   [ᴊᴏɪɴ](https://t.me/HellBot_Official)\n"

pm_caption += "🔹🔸 σffι¢ιαℓ gяσυρ     :   [ᴊᴏɪɴ](https://t.me/HellBot_Official_Chat)\n"

pm_caption += "🔸🔹 ℓι¢єиѕє            :   [ӀíϲҽղՏҽ](https://github.com/HellBoy-OP/HellBot/blob/master/LICENSE)\n"

pm_caption += "🔹🔸 ¢σρуяιgнт          :   [HellBot-Owner](https://github.com/HellBoy-OP)\n"

pm_caption += " [...▄███▄███▄\n....█████████\n.......▀█████▀\n............▀█▀\n](https://t.me/hellbot_official)\n"
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 
