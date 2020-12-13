import re
from importlib import import_module
from sqlite3 import connect

import chromedriver_autoinstaller

import userbot.cmdhelp
from userbot import BRAIN_CHECKER, LOGS, bot
from userbot.plugins import ALL_MODULES

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

UNAPPROVED_MSG = [
    "`Hello, This is **Hêllẞø† Úl†rã Pr¡va†e Security Protocol⚠️**.\n"
    "This is my master Inbox\n"
    "\n**Trespassing this area may lead to destruction**\n\n"
    "To start a valid conversation\n🔱Register Your Request!🔱\nSend `/start` To Register Your Request\nHopefully u will get a reply🔥",
]

DB = connect("learning-data-root.check")
CURSOR = DB.cursor()
CURSOR.execute("""SELECT * FROM BRAIN1""")
ALL_ROWS = CURSOR.fetchall()
INVALID_PH = (
    "\nERROR: The given phone number is invalid"
    "\n  TIP: Enter your phone number using your country code"
    "\n       Check your phone number again"
)

for i in ALL_ROWS:
    BRAIN_CHECKER.append(i[0])
connect("learning-data-root.check").close()


def extractCommands(file):
    FileRead = open(file, "r").read()

    if "/" in file:
        file = file.split("/")[-1]

    Pattern = re.findall(r"@register\(.*pattern=(r|)\"(.*)\".*\)", FileRead)
    Komutlar = []

    if re.search(r"CmdHelp\(.*\)", FileRead):
        pass
    else:
        dosyaAdi = file.replace(".py", "")
        CmdHelp = userbot.cmdhelp.CmdHelp(dosyaAdi, False)

        for Command in Pattern:
            Command = Command[1]
            if Command == "" or len(Command) <= 1:
                continue
            Komut = re.findall("(^.*[a-zA-Z0-9şğüöçı]\w)", Command)
            if (len(Komut) >= 1) and (not Komut[0] == ""):
                Komut = Komut[0]
                if Komut[0] == "^":
                    KomutStr = Komut[1:]
                    if KomutStr[0] == ".":
                        KomutStr = KomutStr[1:]
                    Komutlar.append(KomutStr)
                else:
                    if Command[0] == "^":
                        KomutStr = Command[1:]
                        if KomutStr[0] == ".":
                            KomutStr = KomutStr[1:]
                        else:
                            KomutStr = Command
                        Komutlar.append(KomutStr)

            Hellbot = re.search('"""HELLBOT(.*)"""', FileRead, re.DOTALL)
            if not Hellbot == None:
                Hellbot = Hellbot.group(0)
                for Satir in Hellbot.splitlines():
                    if (not '"""' in Satir) and (":" in Satir):
                        Satir = Satir.split(":")
                        Isim = Satir[0]
                        Deger = Satir[1][1:]

                        if Isim == "INFO":
                            CmdHelp.add_info(Deger)
                        elif Isim == "WARN":
                            CmdHelp.add_warning(Deger)
                        else:
                            CmdHelp.set_file_info(Isim, Deger)
            for Command in Commands:
                CmdHelp.add_command(
                    Command,
                    None,
                    "This plugin has been installed externally. No explanation is defined.",
                )
            CmdHelp.add()

    try:
        chromedriver_autoinstaller.install()
    except:
        pass


for module_name in ALL_MODULES:
    imported_module = import_module("userbot.plugins." + module_name)

LOGS.info(
    "Aree On Ho Gaya Bhenchod!! Abb jake .alive likh ke dekho!! Abb Jaao aur sabki maroo.... Join @HellBot_Official for any help.."
)
LOGS.info(f"Bot version : HellBot • 2.0")

"""
if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
"""
bot.run_until_disconnected()
