import asyncio
from telethon import events
from userbot.utils import admin_cmd, sudo_cmd
from userbot import ALIVE_NAME, hellversion
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Hell User"

kraken = bot.uid

PM_IMG = "https://telegra.ph/file/f34675b4e94d4290c0b6b.mp4"
pm_caption = "🔥🔥**Hêllẞø† IS ONLINE**🔥🔥\n\n"

pm_caption += f"         ≈≈ 🄼   🄰   🅂   🅃   🄴   🅁 ≈≈      \n[{DEFAULTUSER}](tg://user?id={kraken})")\n\n"

pm_caption += "🛡️TELETHON🛡️ : 1.15.0 \n"

pm_caption += f"😈Hêllẞø†😈       : `{hellversion}`\n"

pm_caption += "⚠️CHANNEL⚠️   : [ᴊᴏɪɴ](https://t.me/HellBot_Official)\n"

pm_caption += "🔱GROUP🔱.       : [ᴊᴏɪɴ](https://t.me/HellBot_Official_Chat)\n"

pm_caption += "😎LICENSE😎     : [ӀíϲҽղՏҽ](https://github.com/HellBoy-OP/HellBot/blob/master/LICENSE)\n"

pm_caption += "🔥CREATOR🔥    : [Nub Here](https://t.me/kraken_the_badass)\n"
#@command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 
