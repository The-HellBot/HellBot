"""command:.sr"""

import asyncio

from telethon import events


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "star":

        await event.edit(input_str)

        animation_chars = [
            "I Party like a rockstar",
            "I Look like a movie star",
            "I Play like an all star",
            "I Fuck like a pornstar",
            "Baby I'm a superstar",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])
