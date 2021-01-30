from userbot import *
from userbot.utils import *
from userbot.cmdhelp import CmdHelp
from telethon import events
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User
#-------------------------------------------------------------------------------
async def make_mention(user):
          if user.username:
            return f"@{user.username}"
          return inline_mention(user)

async def inline_mention(user):
          full_name = user_full_name(user) or "No Name"
          return f"[{full_name}](tg://user?id={user.id})"

async def user_full_name(user):
          names = [user.first_name, user.last_name]
          names = [i for i in list(names) if i]
          return " ".join(names)


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Hell User"

full_name = inline_mention(borg.get_me())

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

kraken = bot.uid

PM_IMG = "https://telegra.ph/file/80e5200c615cf0cb57aa9.mp4"
pm_caption = "__**🔥🔥ɦɛʟʟɮօt ɨs օռʟɨռɛ🔥🔥**__\n\n"

pm_caption += (
    f"               __↼🄼🄰🅂🅃🄴🅁⇀__\n**『 {full_name} 』**\n\n"
)

pm_caption += "🛡️TELETHON🛡️ : `1.15.0` \n"

pm_caption += f"😈Hêllẞø†😈       : __**{hellversion}**__\n"

pm_caption += f"⚜️Sudo⚜️            : `{sudou}`\n"

pm_caption += "⚠️CHANNEL⚠️   : [ᴊᴏɪɴ](https://t.me/HellBot_Official)\n"

pm_caption += "🔥CREATOR🔥    : [Nub Here](https://t.me/kraken_the_badass)\n\n"

pm_caption += "    [✨REPO✨](https://github.com/hellboy-op/hellbot) 🔹 [📜License📜](https://github.com/HellBoy-OP/HellBot/blob/master/LICENSE)"


@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()


CmdHelp("alive").add_command(
  'alive', None, 'Check weather the bot is alive or not'
).add_command(
  'hell', None, 'Check weather the bot is alive or not. In your custom Alive Pic and Alive Msg'
).add()
