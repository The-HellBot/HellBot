
from telethon import events

import asyncio

from uniborg.util import admin_cmd



@borg.on(admin_cmd(pattern="phub"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 101)

    await event.edit("phub")

    animation_chars = [

            "P_",

            "PO_",

            "POR_",

            "PORN_",
            
            "PORNH_",
            
            "PORNHU_",
            
           "PORNHUB_", 
           
           "PORNHUB",

        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 10])


@borg.on(admin_cmd(pattern=r"amore"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 101)

    await event.edit("amore")

    animation_chars = [

            "A_",

            "AM_",

            "AMO_",

            "AMOR_",
            
            "AMORE_",
            
            "AMORE❤_",
            
            ".-.",

        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 10])




from telethon import events

import asyncio





@borg.on(admin_cmd(pattern=r"sexy"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 101)

    await event.edit("Sexy")

    animation_chars = [

            "S_",

            "SE_",

            "SEX_",

            "SEXY_",
            
            "SEXY👄_",
            
            "SEXY👄",
            
        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 10])
