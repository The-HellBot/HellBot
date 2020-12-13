import importlib
from importlib import import_module
from sqlite3 import connect
import os
import requests
from telethon.tl.types import InputMessagesFilterDocument
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
from telethon.tl.functions.channels import GetMessagesRequest
from userbot import BRAIN_CHECKER, LOGS, bot, PLUGIN_CHANNEL, CMD_HELP, hellverison, PATTERNS
from userbot.plugins import ALL_MODULES
import userbot.plugins.sql_helper.message_sql as MSJ_SQL
import userbot.plugins.sql_helper.gallery_sql as GALLERY_SQL
from pySmartDL import SmartDL
from telethon.tl import functions

from random import choice
import chromedriver_autoinstaller
from json import loads, JSONDecodeError
import re
import userbot.cmdhelp

KANGING_STR = [
    "Using Witchery to kang this sticker...",
    "Plagiarising hehe...",
    "Inviting this sticker over to my pack...",
    "Kanging this sticker...",
    "Hey that's a nice sticker!\nMind if I kang?!..",
    "hehe me stel ur stikér\nhehe.",
    "Ay look over there (☉｡☉)!→\nWhile I kang this...",
    "Roses are red violets are blue, kanging this sticker so my pacc looks cool",
    "Imprisoning this sticker...",
    "Mr.Steal Your Sticker is stealing this sticker",
]

AFKSTR = [
  "Maa chuda, maa chuda, maa chuda",
]

UNAPPROVED_MSG = ["`Hello, This is **Hêllẞø† Úl†rã Pr¡va†e Security Protocol⚠️**.\n"
                    "This is my master Inbox\n"
                    "\n**Trespassing this area may lead to destruction**\n\n"
                    "To start a valid conversation\n🔱Register Your Request!🔱\nSend `/start` To Register Your Request\nHopefully u will get a reply🔥",
]

DB = connect("learning-data-root.check")
CURSOR = DB.cursor()
CURSOR.execute("""SELECT * FROM BRAIN1""")
ALL_ROWS = CURSOR.fetchall()
INVALID_PH = '\nERROR: The given phone number is invalid' \
             '\n  TIP: Enter your phone number using your country code' \
             '\n       Check your phone number again'

for i in ALL_ROWS:
    BRAIN_CHECKER.append(i[0])
connect("learning-data-root.check").close()

def extractCommands(file):
    FileRead = open(file, 'r').read()
    
    if '/' in file:
        file = file.split('/')[-1]

    Pattern = re.findall(r"@register\(.*pattern=(r|)\"(.*)\".*\)", FileRead)
    Commands = []

    if re.search(r'CmdHelp\(.*\)', FileRead):
        pass
    else:
      dosyaAdi = file.replace('.py', '')
      CmdHelp = userbot.cmdhelp.CmdHelp(dosyaAdi, False)

        for Command in Pattern:
            Command = Command[1]
            if Command == '' or len(Command) <= 1:
                continue
            Command = re.findall("(^.*[a-zA-Z0-9şğüöçı]\w)", Command)
            if (len(Command) >= 1) and (not Command[0] == ''):
                Command = Command[0]
                if Command[0] == '^':
                    CommandStr = Command[1:]
                    if CommandStr[0] == '.':
                        CommandStr = CommandStr[1:]
                    Commands.append(CommandStr)
                else:
                    if Command[0] == '^':
                        CommandStr = Command[1:]
                        if CommandStr[0] == '.':
                            CommandStr = CommandStr[1:]
                        else:
                            CommandStr = Command
                        Commands.append(CommandStr)

            Hellbot = re.search('\"\"\"HELLBOT(.*)\"\"\"', FileRead, re.DOTALL)
            if not Hellbot == None:
                Hellbot = Hellbot.group(0)
                for Satir in Hellbot.splitlines():
                    if (not '"""' in Satir) and (':' in Satir):
                        Satir = Satir.split(':')
                        Isim = Satir[0]
                        Deger = Satir[1][1:]
                                
                        if Isim == 'INFO':
                            CmdHelp.add_info(Deger)
                        elif Isim == 'WARN':
                            CmdHelp.add_warning(Deger)
                        else:
                            CmdHelp.set_file_info(Isim, Deger)
            for Command in Commands:
                CmdHelp.add_command(Command, None, 'This plugin has been installed externally. No explanation is defined.')
            CmdHelp.add()

  
    try:
        chromedriver_autoinstaller.install()
    except:
        pass
    
    
    GALLERY = {}

    
    PLUGIN_MESSAGES = {}
    ORJ_PLUGIN_MESSAGES = {"alive": "`Legendary AF Hêllẞø†.`", "afk": f"`{str(choice(AFKSTR))}`", "kickme": "`I iz lev this kensur grp🚶`🤠", "pm": UNAPPROVED_MSG, "kanger": str(choice(KANGING_STR)), "ban": "{mention}`, prohibited!`", "mute": "{mention}`, muted!`", "approve": "{mention}`, approved to pm!`", "disapprove": "{mention}`, disapprove to pm!`", "block": "{mention}`, you have been blocked!`"}

    PLUGIN_MESSAGES_TURLER = ["alive", "afk", "kickme", "pm", "kanger", "ban", "mute", "approve", "disapprove", "block"]
    for message in PLUGIN_MESSAGES_TURLER:
        dmsj = MSJ_SQL.getir_message(message)
        if dmsj == False:
            PLUGIN_MESSAGES[message] = ORJ_PLUGIN_MESSAGES[message]
        else:
            if dmsj.startswith("MEDIA_"):
                media = int(dmsj.split("MEDIA_")[1])
                media = bot.get_messages(PLUGIN_CHANNEL, ids=media)

                PLUGIN_MESSAGES[message] = media
            else:
                PLUGIN_MESSAGES[message] = dmsj
    if not PLUGIN_CHANNEL == None:
        LOGS.info("Loading plugins")
        try:
            KanalId = bot.get_entity(PLUGIN_CHANNEL)
        except: 
            KanalId = "me"

        for plugin in bot.iter_messages(KanalId, filter=InputMessagesFilterDocument):
            if plugin.file.name and (len(plugin.file.name.split('.')) > 1) \
                and plugin.file.name.split('.')[-1] == 'py':
                Split = plugin.file.name.split('.')

                if not os.path.exists("./userbot/plugins/" + plugin.file.name):
                    dosya = bot.download_media(plugin, "./userbot/plugins/")
                else:
                    LOGS.info("Bu Plugin Zaten Yüklü " + plugin.file.name)
                    extractCommands('./userbot/plugins/' + plugin.file.name)
                    dosya = plugin.file.name
                    continue 
                
                try:
                    spec = importlib.util.spec_from_file_location("userbot.plugins." + Split[0], dosya)
                    mod = importlib.util.module_from_spec(spec)

                    spec.loader.exec_module(mod)
                except Exception as e:
                    LOGS.info(f"`Upload failed. Plugin is in wrong format.\n\nERROR: {e}`")

                    try:
                        plugin.delete()
                    except:
                        pass

                    if os.path.exists("./userbot/plugins/" + plugin.file.name):
                        os.remove("./userbot/plugins/" + plugin.file.name)
                    continue
                extractCommands('./userbot/plugins/' + plugin.file.name)
    else:
        bot.send_message("me", f"`Please set var PLUGIN_CHANNEL to help bot work smoothly`")
except PhoneNumberInvalidError:
    print(INVALID_PH)
    exit(1)

async def FotoDegistir (foto):
    FOTOURL = GALLERY_SQL.TUM_GALLERY[foto].foto
    r = requests.get(FOTOURL)

    with open(str(foto) + ".jpg", 'wb') as f:
        f.write(r.content)    
    file = await bot.upload_file(str(foto) + ".jpg")
    try:
        await bot(functions.photos.UploadProfilePhotoRequest(
            file
        ))
        return True
    except:
        return False

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.plugins." + module_name)

LOGS.info("Aree On Ho Gaya Bhenchod!! Abb jake .alive likh ke dekho!! Abb Jaao aur sabki maroo.... Join @HellBot_Official for any help..
")
LOGS.info(f"Bot version : HellBot • {hellverison}")

"""
if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
"""
bot.run_until_disconnected()
