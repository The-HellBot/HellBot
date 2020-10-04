"""Emoji

Available Commands:

.load
.square
.up
.round
.heart
.anim
.fnl"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 100)

    input_str = event.pattern_match.group(1)

    if input_str == "load":

        await event.edit(input_str)

        animation_chars = [

            "▮",

            "▯",

            "▬",

            "▭"
            "‎"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 4])


"""Emoji

Available Commands:

.emoji shrug

.emoji apple

.emoji :/

.emoji -_-"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 100)

    input_str = event.pattern_match.group(1)

    if input_str == "square":

        await event.edit(input_str)

        animation_chars = [

            "◧",

            "◨",

            "◧",

            "◨"
            "‎"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 4])



@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 100)

    input_str = event.pattern_match.group(1)

    if input_str == "up":

        await event.edit(input_str)

        animation_chars = [

            "╹",

            "╻",

            "╹",

            "╻"
            "‎"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 4])

@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 100)

    input_str = event.pattern_match.group(1)

    if input_str == "round":

        await event.edit(input_str)

        animation_chars = [

            "⚫",

            "⬤",

            "●",

            "∘"
            "‎"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 4])



@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 100)

    input_str = event.pattern_match.group(1)

    if input_str == "heart":

        await event.edit(input_str)

        animation_chars = [

            "🖤",

            "❤️",

            "🖤",

            "❤️"
            "‎"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 4])



@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "anim":

        await event.edit(input_str)

        animation_chars = [

            "😁",

            "😧",

            "😡",

            "😢",

            "‎**Repo by @Kraken_The_BadASS**",
 
            "😁",

            "😧",

            "😡",

            "😢",

            "‎github.com/hellboy-op/hellbot",

            "__**R.D.X GeNg Is BeHiNd You....**__"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0, 6)

    input_str = event.pattern_match.group(1)

    if input_str == "fnl":

        await event.edit(input_str)

        animation_chars = [

            "😁🏿",

            "😁🏾",

            "😁🏽",

            "😁🏼",

            "‎😁",

            "**Fair & Lovely GeNg Is BeHiNd You....**"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 6])
