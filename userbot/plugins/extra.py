import asyncio
from collections import deque

from userbot import CMD_HELP
from userbot.utils import admin_cmd


@borg.on(admin_cmd(";__;$"))
# @register(outgoing=True, pattern="^;__;$")
async def fun(e):
    t = ";__;"
    for j in range(10):
        t = t[:-1] + "_;"
        await e.edit(t)


@borg.on(admin_cmd("yo$"))
# @register(outgoing=True, pattern="^yo$")
async def Ooo(e):
    t = "yo"
    for j in range(15):
        t = t[:-1] + "oo"
        await e.edit(t)


@borg.on(admin_cmd("Oof$"))
# @register(outgoing=True, pattern="^Oof$")
async def Oof(e):
    t = "Oof"
    for j in range(15):
        t = t[:-1] + "of"
        await e.edit(t)


@borg.on(admin_cmd("ccry$"))
# @register(outgoing=True, pattern="^.cry$")
async def cry(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("(;´༎ຶД༎ຶ)")


@borg.on(admin_cmd("fp$"))
# @register(outgoing=True, pattern="^.fp$")
async def facepalm(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("🤦‍♂")


@borg.on(admin_cmd("moon$"))
# @register(outgoing=True, pattern="^.mmoon$")
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    for _ in range(32):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@borg.on(admin_cmd("source$"))
# @register(outgoing=True, pattern="^.source$")
async def source(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("/HellBoy-OP/HellBot")


@borg.on(admin_cmd("readme$"))
# @register(outgoing=True, pattern="^.readme$")
async def reedme(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("/HellBoy-OP/HellBot/blob/master/README.md")


@borg.on(admin_cmd(pattern="evil ?(.*)"))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("😒You Know I'm a good **PERSON**😏")
        await asyncio.sleep(1.9)
        await event.edit("BUT😡")
        await asyncio.sleep(1.2)
        await event.edit("😑Don't give me a reason😠")
        await asyncio.sleep(1.9)
        await event.edit("🤨To show my😎")
        await asyncio.sleep(1.4)
        await event.edit("**😈EVIL SIDE**😈")
        await asyncio.sleep(1.3)
        await event.edit(
            "**😈YOU KNOW THAT I'M A GOOD PERSON. BUT DON'T GIVE ME REASON TO SHOW MY EVIL SIDE😈**"
        )


@borg.on(admin_cmd("heart$"))
# @register(outgoing=True, pattern="^.heart$")
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("❤️🧡💛💚💙💜🖤"))
    for _ in range(32):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@borg.on(admin_cmd("fap$"))
# @register(outgoing=True, pattern="^.fap$")
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🍆✊🏻💦"))
    for _ in range(32):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


CMD_HELP.update({";__;": "You try it!"})
CMD_HELP.update({"evil": "Evil Guy"})
CMD_HELP.update({"cry": "Cry"})
CMD_HELP.update({"fp": "Send face palm emoji."})
CMD_HELP.update({"moon": "Bot will send a cool moon animation."})
CMD_HELP.update({"clock": "Bot will send a cool clock animation."})
CMD_HELP.update({"readme": "Reedme."})
CMD_HELP.update({"source": "Gives the source of your userbot"})
CMD_HELP.update({"myusernames": "List of Usernames owned by you."})
CMD_HELP.update({"oof": "Same as ;__; but ooof"})
CMD_HELP.update({"earth": "Sends Kensar Earth animation"})
CMD_HELP.update({"heart": "Try and you'll get your emotions back"})
CMD_HELP.update({"fap": "Faking orgasm"})
