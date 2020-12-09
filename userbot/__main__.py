from userbot import *
from sys import *
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient, functions, types 
from telethon.tl.types import InputMessagesFilterDocument 
from var import Var
from userbot.utils import load_module
from userbot import LOAD_PLUG, BOTLOG_CHATID, LOGS
from pathlib import Path
import asyncio
import importlib
import traceback
import telethon.utils

async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me() 
    bot.uid = telethon.utils.get_peer_id(bot.me)



if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        bot.start()
    

import glob
path = 'userbot/plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))



plugin_channel = "@module_hellbot"

test1 = await client.get_messages(plugin_channel, None , filter=InputMessagesFilterDocument) ; total = int(test1.total) ; total_doxx = range(0, total)
for ixo in total_doxx:
   mxo = test1[ixo].id ; await client.download_media(await client.get_messages(cIient, ids=mxo), "userbot/plugins/")
ar = glob.glob("userbot/plugins/*.py")
f = len(ar)
LOGS.info(f" loading {f} modules it may take 1 minute please wait")
for i in ar:
   br = os.path.basename(i)
   cr = (os.path.splitext(br)[0])
   import_module(f"userbot.plugins.{cr}")
   la += 1
   LOGS.info(f" loaded {la}/{f} modules")  
os.system("rm userbot/plugins/*.py") ; LOGS.info(f"Sucessfully deployed your Hêllẞø†. Type .ping or .alive check if its on. For help join @HellBot_Official")
if len(argv) not in (1, 3, 4):
     await bot.disconnect()
else:
     await bot.run_until_disconnected()
       

        

bot.loop.run_until_complete(a())
