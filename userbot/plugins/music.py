"""
Available Commands:
.music"""

from telethon import events

import asyncio

from uniborg.util import admin_cmd



@borg.on(admin_cmd(pattern=r"music"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1.5

    animation_ttl = range(0, 11)

   # input_str = event.pattern_match.group(1)

   # if input_str == "music":

    await event.edit("music")

    animation_chars = [
            "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[ceeHellBot Music Player](https://t.me/hellbot_official)\n\n⠀⠀⠀⠀**Now Playing:Kamasutra BGM**\n\n**00:00** ▱▱▱▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `▶️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: I Fone XXX**",
            "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[cee HellBot Music Player](https://t.me/hellbot_official)\n\n⠀⠀⠀⠀**Now Playing:Kamasutra BGM**\n\n**00:01** ▰▱▱▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: I Fone XXX**",
            "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[cee HellBot Music Player](https://t.me/hellbot_official)\n\n⠀⠀⠀⠀**Now Playing:Kamasutra BGM**\n\n**00:03** ▰▰▰▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: I Fone XXX**",
            "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[cee HellBot Music Player](https://t.me/hellbot_official)\n\n⠀⠀⠀⠀**Now Playing:Kamasutra BGM**\n\n**00:04** ▰▰▰▰▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: I Fone XXX**",
            "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[cee HellBot Music Player](https://t.me/hellbot_official)\n\n⠀⠀⠀⠀**Now Playing:Kamasutra BGM**\n\n**00:05** ▰▰▰▰▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: I Fone XXX**",    
            "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[cee HellBot Music Player](https://t.me/hellbot_official)\n\n⠀⠀⠀⠀**Now Playing:Kamasutra BGM**\n\n**00:06** ▰▰▰▰▰▰▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: I Fone XXX**",
            "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[cee HellBot Music Player](https://t.me/hellbot_official)\n\n⠀⠀⠀⠀**Now Playing:Kamasutra BGM**\n\n**00:07** ▰▰▰▰▰▰▰▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: I Fone XXX**",
            "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[cee HellBot Music Player](https://t.me/hellbot_official)\n\n⠀⠀⠀⠀**Now Playing:Kamasutra BGM**\n\n**00:08** ▰▰▰▰▰▰▰▰▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: I Fone XXX**",
            "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[cee HellBot Music Player](https://t.me/hellbot_official)\n\n⠀⠀⠀⠀**Now Playing:Kamasutra BGM**\n\n**00:09** ▰▰▰▰▰▰▰▰▰▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: I Fone XXX**",
            "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[cee HellBot Music Player](https://t.me/hellbot_official)\n\n⠀⠀⠀⠀**Now Playing:Kamasutra BGM**\n\n**00:10** ▰▰▰▰▰▰▰▰▰▰ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏺️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: I Fone XXX**"
        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 11])
