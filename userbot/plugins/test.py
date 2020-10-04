from telethon import events
import asyncio
import os
import sys
from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern=r"test"))
async def test(event):
    if event.fwd_from:
        return 
    await event.edit("Test Successfull.\n\nBot working Perfectly\n\n [HellBot](https://t.me/hellbot_official) !!")      
