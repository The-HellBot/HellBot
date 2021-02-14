
import asyncio

from hellbot.utils import admin_cmd, sudo_cmd, edit_or_reply


@bot.on(admin_cmd(pattern="unoob$", outgoing=True))
@bot.on(sudo_cmd(pattern="unoob$", allow_sudo=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 9)

    await edit_or_reply(event, "You Noob")

    animation_chars = [
        "EvErYbOdY",
        "iZ",
        "BiGGeSt",
        "NoOoB",
        "uNtiL",
        "YoU",
        "aRriVe",
        "😈",
        "EvErYbOdY iZ BiGGeSt NoOoB uNtiL YoU aRriVe 😈",
    ]

    for i in animation_ttl:

        await event.edit(animation_chars[i % 9])
        await asyncio.sleep(animation_interval)

@bot.on(admin_cmd(pattern="menoob$", outgoing=True))
@bot.on(sudo_cmd(pattern="menoob$", allow_sudo=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 9)

    await edit_or_reply(event, "Me Noob")

    animation_chars = [
        "EvErYbOdY",
        "iZ",
        "BiGGeSt",
        "NoOoB",
        "uNtiL",
        "i",
        "aRriVe",
        "😈",
        "EvErYbOdY iZ BiGGeSt NoOoB uNtiL i aRriVe 😈",
    ]

    for i in animation_ttl:

        await event.edit(animation_chars[i % 9])
        await asyncio.sleep(animation_interval)


@bot.on(admin_cmd(pattern="uproo$", outgoing=True))
@bot.on(sudo_cmd(pattern="uproo$", allow_sudo=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 8)

    await edit_or_reply(event, "You Pro")

    animation_chars = [
        "EvErYbOdY",
        "iZ",
        "PeRu",
        "uNtiL",
        "YoU",
        "aRriVe",
        "😈",
        "EvErYbOdY iZ PeRu uNtiL YoU aRriVe 😈",
    ]

    for i in animation_ttl:

        await event.edit(animation_chars[i % 8])
        await asyncio.sleep(animation_interval)


@bot.on(admin_cmd(pattern="mepro$", outgoing=True))
@bot.on(sudo_cmd(pattern="mepro$", allow_sudo=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 8)

    await edit_or_reply(event, "Me Pro")

    animation_chars = [
        "EvErYbOdY",
        "iZ",
        "PeRu",
        "uNtiL",
        "i",
        "aRriVe",
        "😈",
        "EvErYbOdY iZ PeRu uNtiL i aRriVe 😈",
    ]

    for i in animation_ttl:

        await event.edit(animation_chars[i % 8])
        await asyncio.sleep(animation_interval)
