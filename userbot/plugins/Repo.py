#Made by @Kraken_The_BadASS. Keep credits cause it hurts...


import random, re
from uniborg.util import admin_cmd
import asyncio
from telethon import events

@borg.on(admin_cmd(pattern="repo ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
       await event.edit(" Click [here](https://github.com/hellboy-op/hellbot) to open this Lit AF🔥 Hêllẞø† Repo...🔥")