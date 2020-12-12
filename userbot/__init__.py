
import os
import sys
import time
from telethon.sessions import StringSession
from telethon import TelegramClient
from userbot.helpers import functions as simpdef

from var import Var

StartTime = time.time()
hellversion = "1.9" 

os.system("pip install --upgrade pip")
if Var.STRING_SESSION:
    session_name = str(Var.STRING_SESSION)
    bot = TelegramClient(StringSession(session_name), Var.APP_ID, Var.API_HASH)
else:
    session_name = "startup"
    bot = TelegramClient(session_name, Var.APP_ID, Var.API_HASH)


CMD_LIST = {}
# for later purposes
CMD_HELP = {}
CMD_HELP_BOT = {}
INT_PLUG = ""
LOAD_PLUG = {}

# PaperPlaneExtended Support Vars
ENV = os.environ.get("ENV", False)

CAT_ID = ["1289422521"]

""" PPE initialization. """

from logging import basicConfig, getLogger, INFO, DEBUG
from distutils.util import strtobool as sb
import asyncio

import pylast
from pySmartDL import SmartDL
from requests import get
# Bot Logs setup:
if bool(ENV):
    CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

    if CONSOLE_LOGGER_VERBOSE:
        basicConfig(
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            level=DEBUG,
        )
    else:
        basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    level=INFO)
    LOGS = getLogger(__name__)

    # Check if the config was edited by using the already used variable.
    # Basically, its the 'virginity check' for the config file ;)
    CONFIG_CHECK = os.environ.get(
        "___________PLOX_______REMOVE_____THIS_____LINE__________", None)

    if CONFIG_CHECK:
        LOGS.info(
            "Please remove the line mentioned in the first hashtag from the config.env file"
        )
        quit(1)

    # Logging channel/group configuration.
    BOTLOG_CHATID = os.environ.get("BOTLOG_CHATID", None)
    try:
        BOTLOG_CHATID = int(BOTLOG_CHATID)
    except:
        pass

    # Userbot logging feature switch.
    BOTLOG = sb(os.environ.get("BOTLOG", "False"))
    LOGSPAMMER = sb(os.environ.get("LOGSPAMMER", "False"))
    
    # Bleep Blop, this is a bot ;)
    PM_AUTO_BAN = sb(os.environ.get("PM_AUTO_BAN", "False"))

    # Console verbose logging
    CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

    # SQL Database URI
    DB_URI = os.environ.get("DATABASE_URL", None)

    # OCR API key
    OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)

    # remove.bg API key
    REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)

    # Chrome Driver and Headless Google Chrome Binaries
    CHROME_DRIVER = os.environ.get("CHROME_DRIVER", None)
    GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", None)

    # OpenWeatherMap API Key
    OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)

    # Anti Spambot Config
    ANTI_SPAMBOT = sb(os.environ.get("ANTI_SPAMBOT", "False"))

    ANTI_SPAMBOT_SHOUT = sb(os.environ.get("ANTI_SPAMBOT_SHOUT", "False"))
  
    # FedBan Premium Module
    F_BAN_LOGGER_GROUP = os.environ.get("F_BAN_LOGGER_GROUP", None)

# Heroku Credentials for updater.
    HEROKU_MEMEZ = sb(os.environ.get("HEROKU_MEMEZ", "False"))
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)

    OTOMATIK_KATILMA = sb(os.environ.get("OTOMATIK_KATILMA", "True"))
   
    # Youtube API key
    YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)

    # Default .alive name
    ALIVE_NAME = os.environ.get("ALIVE_NAME", None)
    AUTONAME = os.environ.get("AUTONAME", None)
    REDIRECTCHANNEL = os.environ.get("REDIRECTCHANNEL", None)

    # Time & Date - Country and Time Zone
    COUNTRY = str(os.environ.get("COUNTRY", "India"))

    TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))

    # Clean Welcome
    CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME", "True"))
    
    # Custom Module
    CUSTOM_PMPERMIT = os.environ.get("CUSTOM_PMPERMIT", None)
    CUSTOM_AFK = os.environ.get("CUSTOM_AFK", None)

    # Upstream Repo
    UPSTREAM_REPO_URL = os.environ.get(
    "UPSTREAM_REPO_URL",
    "https://github.com/HellBoy-OP/HellBot.git")

    # Last.fm Module
    BIO_PREFIX = os.environ.get("BIO_PREFIX", None)
    BIO_MSG = os.environ.get("BIO_MSG", None)
    PATTERNS = os.environ.get("PATTERNS", ".;!,")
    LASTFM_API = os.environ.get("LASTFM_API", None)
    LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
    LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME", None)
    LASTFM_PASSWORD_PLAIN = os.environ.get("LASTFM_PASSWORD", None)
    LASTFM_PASS = pylast.md5(LASTFM_PASSWORD_PLAIN)
    if not LASTFM_USERNAME == "None":
        lastfm = pylast.LastFMNetwork(api_key=LASTFM_API,
                                      api_secret=LASTFM_SECRET,
                                      username=LASTFM_USERNAME,
                                      password_hash=LASTFM_PASS)
    else:
        lastfm = None

    # Google Drive Module
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    G_DRIVE_AUTH_TOKEN_DATA = os.environ.get("G_DRIVE_AUTH_TOKEN_DATA", None)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY",
                                         "./downloads")
else:
    # Put your ppe vars here if you are using local hosting
    PLACEHOLDER = None

# Setting Up CloudMail.ru and MEGA.nz extractor binaries,
# and giving them correct perms to work properly.
if not os.path.exists('bin'):
    os.mkdir('bin')

binaries = {
    "https://raw.githubusercontent.com/yshalsager/megadown/master/megadown":
    "bin/megadown",
    "https://raw.githubusercontent.com/yshalsager/cmrudl.py/master/cmrudl.py":
    "bin/cmrudl"
}

for binary, path in binaries.items():
    downloader = SmartDL(binary, path, progress_bar=False)
    downloader.start()
    os.chmod(path, 0o755)

def button(page, modules):
    Row = 5
    Column = 2
    
    modules = sorted([modul for modul in modules if not modul.startswith("_")])
    pairs = list(map(list, zip(modules[::2], modules[1::2])))
    if len(modules) % 2 == 1:
        pairs.append([modules[-1]])
    max_pages = ceil(len(pairs) / Row)
    pairs = [pairs[i:i + Row] for i in range(0, len(pairs), Row)]
    buttons = []
    for pairs in pairs[page]:
        buttons.append([
            custom.Button.inline("🔸 " + pair, data=f"Information[{page}]({pair})") for pair in pairs
        ])

    buttons.append([custom.Button.inline("◀️ ᏰᎯᏣᏦ", data=f"page({(max_pages - 1) if page == 0 else (page - 1)})"), custom.Button.inline("ᏁᏋﾒᎿ ▶️", data=f"page({0 if page == (max_pages - 1) else page + 1})")])
    return [max_pages, buttons]

with bot:
    if OTOMATIK_KATILMA:
        try:
            bot(JoinChannelRequest("@HellBot_Official"))
            bot(JoinChannelRequest("@HellBot_Official"))
        except:
            pass
#Changing this line may give error in bot as i added some special cmds in hellbot channel to get this module work...

    modules = CMD_HELP
    me = bot.get_me()
    uid = me.id

    try:
        @tgbot.on(NewMessage(pattern='/start'))
        async def start_bot_handler(event):
            if not event.message.from_id == uid:
                await event.reply(f'Hoo gya aapka. Kabse tapar tapar dabae jaa rhe h. Khudka bna lo na agr chaiye to. © Hêllẞø† ™')
            else:
                await event.reply(f'`Aa gae aap🚶`')

        @tgbot.on(InlineQuery)  # pylint:disable=E0602
        async def inline_handler(event):
            builder = event.builder
            result = None
            query = event.text
            if event.query.user_id == uid and query == "@HellBot_Official":
                rev_text = query[::-1]
                veriler = (button(0, sorted(CMD_HELP)))
                result = await builder.article(
                    f"Hey! Only use .help please",
                    text=f"**Running HellBot**\n\n__Number of plugins installed__ :`{len(CMD_HELP)}`\n**page:** 1/{veriler[0]}",
                    buttons=veriler[1],
                    link_preview=False
                )
            elif query.startswith("http"):
                part = query.split(" ")
                result = builder.article(
                    "File uploaded",
                    text=f"**File uploaded successfully to {part[2]} site.\n\nUpload Time : {part[1][:3]} second\n[‏‏‎ ‎]({part[0]})",
                    buttons=[
                        [custom.Button.url('URL', part[0])]
                    ],
                    link_preview=True
                )
            else:
                result = builder.article(
                    "@HellBot_Official",
                    text="""Hey! This is [Hêllẞø†.](https://t.me/HellBot_Official) You can know more about this from the link given below""",
                    buttons=[
                        [custom.Button.url("Channel", "https://t.me/HellBot_Official"), custom.Button.url(
                            "Group", "https://t.me/HellBot_Official_Chat")],
                        [custom.Button.url(
                            "GitHub", "https://github.com/HellBoy-OP/HellBot")]
                    ],
                    link_preview=False
                )
            await event.answer([result] if result else None)

        @tgbot.on(callbackquery.CallbackQuery(data=compile(b"page\((.+?)\)")))
        async def page(event):
            if not event.query.user_id == uid: 
                return await event.answer("Hoo gya aapka. Kabse tapar tapar dabae jaa rhe h. Khudka bna lo na agr chaiye to. © Hêllẞø† ™", cache_time=0, alert=True)
            page = int(event.data_match.group(1).decode("UTF-8"))
            veriler = button(page, CMD_HELP)
            await event.edit(
                f"**Legenday AF** [Hêllẞøt](https://t.me/HellBot_Official) __Working...__\n\n**Number of modules installed :** `{len(CMD_HELP)}`\n**page:** {page + 1}/{veriler[0]}",
                buttons=veriler[1],
                link_preview=False
            )
        
        @tgbot.on(callbackquery.CallbackQuery(data=compile(b"Information\[(\d*)\]\((.*)\)")))
        async def Information(event):
            if not event.query.user_id == uid: 
                return await event.answer("Hoo gya aapka. Kabse tapar tapar dabae jaa rhe h. Khudka bna lo na agr chaiye to. © Hêllẞø† ™", cache_time=0, alert=True)

            page = int(event.data_match.group(1).decode("UTF-8"))
            commands = event.data_match.group(2).decode("UTF-8")
            try:
                buttons = [custom.Button.inline("🔹 " + cmd[0], data=f"commands[{commands}[{page}]]({cmd[0]})") for cmd in CMD_HELP_BOT[commands]['commands'].items()]
            except KeyError:
                return await event.answer("No Description is written for this plugin", cache_time=0, alert=True)

            buttons = [buttons[i:i + 2] for i in range(0, len(buttons), 2)]
            buttons.append([custom.Button.inline("◀️ ᏰᎯᏣᏦ", data=f"page({page})")])
            await event.edit(
                f"**📗 File:** `{commands}`\n**🔢 Number of commands :** `{len(CMD_HELP_BOT[commands]['commands'])}`",
                buttons=buttons,
                link_preview=False
            )
        
        @tgbot.on(callbackquery.CallbackQuery(data=compile(b"commands\[(.*)\[(\d*)\]\]\((.*)\)")))
        async def commands(event):
            if not event.query.user_id == uid: 
                return await event.answer("Hoo gya aapka. Kabse tapar tapar dabae jaa rhe h. Khudka bna lo na agr chaiye to. © Hêllẞø† ™", cache_time=0, alert=True)

            cmd = event.data_match.group(1).decode("UTF-8")
            page = int(event.data_match.group(2).decode("UTF-8"))
            commands = event.data_match.group(3).decode("UTF-8")

            result = f"**📗 File:** `{cmd}`\n"
            if CMD_HELP_BOT[cmd]['info']['info'] == '':
                if not CMD_HELP_BOT[cmd]['info']['warning'] == '':
                    result += f"**⬇️ Official:** {'✅' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n"
                    result += f"**⚠️ Warning :** {CMD_HELP_BOT[cmd]['info']['warning']}\n\n"
                else:
                    result += f"**⬇️ Official:** {'✅' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n\n"
            else:
                result += f"**⬇️ Official:** {'✅' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n"
                if not CMD_HELP_BOT[cmd]['info']['warning'] == '':
                    result += f"**⚠️ Warning:** {CMD_HELP_BOT[cmd]['info']['warning']}\n"
                result += f"**ℹ️ Info:** {CMD_HELP_BOT[cmd]['info']['info']}\n\n"

            command = CMD_HELP_BOT[cmd]['commands'][commands]
            if command['params'] is None:
                result += f"**🛠 commands:** `{PATTERNS[:1]}{command['command']}`\n"
            else:
                result += f"**🛠 commands:** `{PATTERNS[:1]}{command['command']} {command['params']}`\n"
                
            if command['example'] is None:
                result += f"**💬 Explanation:** `{command['usage']}`\n\n"
            else:
                result += f"**💬 Explanation:** `{command['usage']}`\n"
                result += f"**⌨️ For Example:** `{PATTERNS[:1]}{command['example']}`\n\n"

            await event.edit(
                result,
                buttons=[custom.Button.inline("◀️ ᏰᎯᏣᏦ", data=f"Information[{page}]({cmd})")],
                link_preview=False
            )
    except Exception as e:
        print(e)
        LOGS.info(
            "Inline Mode is being disabled. Please turn it on."
            "Get a Bot token and turn on inline mode to work"
            "If you think there is problem other than these then contact us."
        )

    try:
        bot.loop.run_until_complete(check_botlog_chatid())
    except:
        LOGS.info(
            "BOTLOG_CHATID is not a valid entity"
            "Check your config vars"
        )
        quit(1)

# Global Variables
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
CMD_HELP = {}
ISAFK = False
AFKREASON = None
SUDO_LIST = {}


from userbot.helpers import *
from userbot.helpers import functions as helldef
