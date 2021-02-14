from userbot import ALIVE_NAME, bot, hellversion
from userbot.Config import Config
from telethon import version
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Hêllẞø† Mødê"

botversion = 1.0

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

kraken = bot.uid

PM_IMG = Config.ALIVE_PIC or "https://telegra.ph/file/80e5200c615cf0cb57aa9.mp4"
pm_caption = "__**🔥🔥ɦɛʟʟɮօt ɨs օռʟɨռɛ🔥🔥**__\n\n"

pm_caption += "      ✨ BOT MODE IS ON ✨\n"

pm_caption += (
    f"               __↼🄼🄰🅂🅃🄴🅁⇀__\n**『[{DEFAULTUSER}](tg://user?id={kraken})』**\n\n"
)

pm_caption += "      🏅 **BOT STATS** 🏅\n"

pm_caption += f"🛡️TELETHON🛡️ : `{version.__version__}` \n"

pm_caption += f"😈Hêllẞø†😈       : __**{hellversion}**__\n"

pm_caption += f"⚡ ẞø† ⚡              :- __**{botversion}**__\n"

pm_caption += f"⚜️Sudo⚜️            : `{sudou}`\n"

pm_caption += "⚠️CHANNEL⚠️   : [ᴊᴏɪɴ](https://t.me/HellBot_Official)\n"

pm_caption += "🔥CREATOR🔥    : [Nub Here](https://t.me/kraken_the_badass)\n\n"

pm_caption += "    [✨REPO✨](https://github.com/hellboy-op/hellbot) 🔹 [📜License📜](https://github.com/HellBoy-OP/HellBot/blob/master/LICENSE)"


@hellbot_cmd("alive", is_args=False)
@pitaji
async def hellboy(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
