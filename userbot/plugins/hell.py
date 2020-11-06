#Hello guys... Nub here @Kraken_the_badass
#Pro is @Hellboi_atul. Who never kanged a single plugin...
"""Check if userbot working or not . 

"""
import os
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import ALIVE_NAME, CMD_HELP
from userbot.utils import admin_cmd
from telethon import version
from math import ceil
import json
import random
import re
from telethon import events, errors, custom
import io
from platform import python_version, uname

ALIVE_PIC = Config.ALIVE_PHOTTO
if ALIVE_PIC is None:
   ALIVE_PIC = "https://telegra.ph/file/f34675b4e94d4290c0b6b.mp4"


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

ALIVE_MESSAGE = Config.ALIVE_MSG
if ALIVE_MESSAGE is None:
   ALIVE_MESSAGE = "**🔱HellBot Zinda Tha....Zinda Hai....Aur Zinda Rahega🔱 \n\n\n**"
   ALIVE_MESSAGE += "🤙__My Bot Status__🤙 \n\n\n"
   ALIVE_MESSAGE += f"Telethon: TELETHON-1.15.0 \n\n"
   ALIVE_MESSAGE += f"Python: PYTHON-3.8.5 \n\n"
   ALIVE_MESSAGE += "**I'll Be With You Master Till My Dyno Ends!!**☠ \n\n"
   ALIVE_MESSAGE += f"Support Channel : @HellBot_Official \n\n"
   ALIVE_MESSAGE += f"MY BOSS : {DEFAULTUSER} \n\n "
                
            
#@command(outgoing=True, pattern="^.hell$")
@command(outgoing=True, pattern="^.hell$")
async def amireallyalive(awake):
    """ For .hell command, check if the bot is running.  """
    await awake.delete() 
    await borg.send_file(awake.chat_id, ALIVE_PIC,caption=ALIVE_MESSAGE)
