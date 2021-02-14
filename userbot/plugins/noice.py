import random
import re
import time
import asyncio
import requests
from telethon import events
from hellbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp

# ================= CONSTANT =================


HELLOSTR = [
    "`Hi !`",
    "`‘Ello, gov'nor!`",
    "`What’s crackin’?`",
    "`‘Sup, homeslice?`",
    "`Howdy, howdy ,howdy!`",
    "`Hello, who's there, I'm talking.`",
    "`You know who this is.`",
    "`Yo!`",
    "`Whaddup.`",
    "`Greetings and salutations!`",
    "`Hello, sunshine!`",
    "`Hey, howdy, hi!`",
    "`What’s kickin’, little chicken?`",
    "`Peek-a-boo!`",
    "`Howdy-doody!`",
    "`Hey there, freshman!`",
    "`I come in peace!`",
    "`Ahoy, matey!`",
    "`Hiya!`",
    "`Oh retarded gey! Well Hello`",
]

SHGS = [
    "┐(´д｀)┌",
    "┐(´～｀)┌",
    "┐(´ー｀)┌",
    "┐(￣ヘ￣)┌",
    "╮(╯∀╰)╭",
    "╮(╯_╰)╭",
    "┐(´д`)┌",
    "┐(´∀｀)┌",
    "ʅ(́◡◝)ʃ",
    "ლ(ﾟдﾟლ)",
    "┐(ﾟ～ﾟ)┌",
    "┐('д')┌",
    "ლ｜＾Д＾ლ｜",
    "ლ（╹ε╹ლ）",
    "ლ(ಠ益ಠ)ლ",
    "┐(‘～`;)┌",
    "ヘ(´－｀;)ヘ",
    "┐( -“-)┌",
    "乁༼☯‿☯✿༽ㄏ",
    "ʅ（´◔౪◔）ʃ",
    "ლ(•ω •ლ)",
    "ヽ(゜～゜o)ノ",
    "ヽ(~～~ )ノ",
    "┐(~ー~;)┌",
    "┐(-。ー;)┌",
    "¯\_(ツ)_/¯",
    "¯\_(⊙_ʖ⊙)_/¯",
    "乁ʕ •̀ ۝ •́ ʔㄏ",
    "¯\_༼ ಥ ‿ ಥ ༽_/¯",
    "乁( ⁰͡  Ĺ̯ ⁰͡ ) ㄏ",
]

CRI = [
    "أ‿أ",
    "╥﹏╥",
    "(;﹏;)",
    "(ToT)",
    "(┳Д┳)",
    "(ಥ﹏ಥ)",
    "（；へ：）",
    "(T＿T)",
    "（πーπ）",
    "(Ｔ▽Ｔ)",
    "(⋟﹏⋞)",
    "（ｉДｉ）",
    "(´Д⊂ヽ",
    "(;Д;)",
    "（>﹏<）",
    "(TдT)",
    "(つ﹏⊂)",
    "༼☯﹏☯༽",
    "(ノ﹏ヽ)",
    "(ノAヽ)",
    "(╥_╥)",
    "(T⌓T)",
    "(༎ຶ⌑༎ຶ)",
    "(☍﹏⁰)｡",
    "(ಥ_ʖಥ)",
    "(つд⊂)",
    "(≖͞_≖̥)",
    "(இ﹏இ`｡)",
    "༼ಢ_ಢ༽",
    "༼ ༎ຶ ෴ ༎ຶ༽",
]
# ===========================================

@bot.on(admin_cmd(pattern="cri$", outgoing=True))
@bot.on(sudo_cmd(pattern="cri$", allow_sudo=True))
async def cri(e):
    """ y u du dis, i cry everytime !! """
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await edit_or_reply(e, random.choice(CRI))
        

@bot.on(admin_cmd(pattern="hey$", outgoing=True))
@bot.on(sudo_cmd(pattern="hey$", allow_sudo=True))
async def hoi(hello):
    """ Greet everyone! """
    if not hello.text[0].isalpha() and hello.text[0] not in ("/", "#", "@", "!"):
        await edit_or_reply(hello, random.choice(HELLOSTR))


@bot.on(admin_cmd(pattern="shrug$", outgoing=True))
@bot.on(sudo_cmd(pattern="shrug$", allow_sudo=True))
async def shrugger(shg):
    r""" ¯\_(ツ)_/¯ """
    if not shg.text[0].isalpha() and shg.text[0] not in ("/", "#", "@", "!"):
        await edit_or_reply(shg, random.choice(SHGS))


@bot.on(admin_cmd(pattern="f (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="f (.*)", allow_sudo=True))
async def payf(e):
    paytext = e.pattern_match.group(1)[0]
    pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}".format(
        paytext * 5,
        paytext * 1,
        paytext * 1,
        paytext * 4,
        paytext * 1,
        paytext * 1,
        paytext * 1,
    )
    await edit_or_reply(e, pay)

@bot.on(admin_cmd(pattern="nopee$", outgoing=True))
@bot.on(sudo_cmd(pattern="nopee$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 36)
    await edit_or_reply(event, "nope")
    animation_chars = [
        "No",
        "Problem",
        "Boss",
        "Yeah ! No problem",
        "No Problem Boss.lol",
        "No Problem Boss😇.Lol",
        "No Problem Man😇.Lol",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])


@bot.on(admin_cmd(pattern="^Okk$", outgoing=True))
@bot.on(sudo_cmd(pattern="^Okk$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 36)
    # input_str = event.pattern_match.group(1)
    # if input_str == "ok":
    await event.edit("ok")
    animation_chars = [
        "OK",
        "BOSS",
        "OK MAN",
        "OK BITCH",
        "OK FUKCER",
        "OK SEXY BABE",
        "OK GAY",
        "OK SIR",
        "GO AND SAY OK",
        "OK LOL",
        "YAA OK",
        "FCUK",
        "OK",
        "Boss",
        "Yeahhhhhh",
        "O",
        "K",
        "Ok Boss! 😇",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
        

CmdHelp("noice").add_command(
  "f", "<text>", "Gives out the text in 'F' letter"
).add_command(
  "shrug", None, "¯\_(ツ)_/¯"
).add_command(
  "hey", None, "Random 'Hello' String."
).add_command(
  "cri", None, "Random Crying emojies..."
).add_command(
  "nopee", None, "Use and see"
).add_command(
  "Okk", None, "Ohh Ok"
).add()
