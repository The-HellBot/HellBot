#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from random import choice
import requests
import re
import time

from cowpy import cow
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName

from hellbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp

#$$$$$$$$$$$$$$$$$¢$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$¢$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$¢

GENDER = [
    "u is mard",
    "u is man",
    "u is aurat",
    "u is woman",
    "u is gey",
    "u is chakka",
]
    
EMOTICONS = [
    "(҂⌣̀_⌣́)",
    "（；¬＿¬)",
    "(-｡-;",
    "┌[ O ʖ̯ O ]┐",
    "〳 ͡° Ĺ̯ ͡° 〵",
]

WAVING = [
    "(ノ^∇^)",
    "(;-_-)/",
    "@(o・ェ・)@ノ",
    "ヾ(＾-＾)ノ",
    "ヾ(◍’౪◍)ﾉﾞ♡",
    "(ό‿ὸ)ﾉ",
    "(ヾ(´・ω・｀)",
]

WTF = [
    "༎ຶ‿༎ຶ",
    "(‿ˠ‿)",
    "╰U╯☜(◉ɷ◉ )",
    "(;´༎ຶ益༎ຶ)♡",
    "╭∩╮(︶ε︶*)chu",
    "( ＾◡＾)っ (‿|‿)",
]
    
LOB = [
    "乂❤‿❤乂",
    "(｡♥‿♥｡)",
    "( ͡~ ͜ʖ ͡°)",
    "໒( ♥ ◡ ♥ )७",
    "༼♥ل͜♥༽",
]
    
CONFUSED = [
    "(・_・ヾ",
    "｢(ﾟﾍﾟ)",
    "﴾͡๏̯͡๏﴿",
    "(￣■￣;)!?",
    "▐ ˵ ͠° (oo) °͠ ˵ ▐",
    "(-_-)ゞ゛",
]
    
DEAD = [
    "(✖╭╮✖)",
    "✖‿✖",
    "(+_+)",
    "(✖﹏✖)",
    "∑(✘Д✘๑)",
]
  
SED = [
    "(＠´＿｀＠)",
    "⊙︿⊙",
    "(▰˘︹˘▰)",
    "●︿●",
    "(　´_ﾉ` )",
    "彡(-_-;)彡",
]
    
DOG = [
    "-ᄒᴥᄒ-",
    "◖⚆ᴥ⚆◗",
]

SHRUG = [
    "( ͡° ͜ʖ ͡°)",
    "¯\_(ツ)_/¯",
    "( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)",
    "ʕ•ᴥ•ʔ",
    "(▀ Ĺ̯▀   )",
    "(ง ͠° ͟ل͜ ͡°)ง",
    "༼ つ ◕_◕ ༽つ",
    "ಠ_ಠ",
    "(☞ ͡° ͜ʖ ͡°)☞",
    "¯\_༼ ି ~ ି ༽_/¯",
    "c༼ ͡° ͜ʖ ͡° ༽⊃",
]

#✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓

@bot.on(admin_cmd(pattern=f"gendar$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"gendar$", allow_sudo=True))
async def metoo(e):
    if e.fwd_from:
        return
    txt = random.choice(GENDER)
    await edit_or_reply(e, txt)
    
@bot.on(admin_cmd(pattern=f"shrug$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"shrug$", allow_sudo=True))
async def metoo(e):
    if e.fwd_from:
        return
    txt = random.choice(SHRUG)
    await edit_or_reply(e, txt)
    
@bot.on(admin_cmd(pattern=f"doge", outgoing=True))
@bot.on(sudo_cmd(pattern=f"doge", allow_sudo=True))
async def metoo(e):
    if e.fwd_from:
        return
    txt = random.choice(DOG)
    await edit_or_reply(e, txt)
    
@bot.on(admin_cmd(pattern=f"mesed$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"mesed$", allow_sudo=True))
async def metoo(e):
    if e.fwd_from:
        return
    txt = random.choice(SED)
    await edit_or_reply(e, txt)
    
@bot.on(admin_cmd(pattern=f"medead$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"medead$", allow_sudo=True))
async def metoo(e):
    if e.fwd_from:
        return
    txt = random.choice(DEAD)
    await edit_or_reply(e, txt)
    
@bot.on(admin_cmd(pattern=f"confused$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"confused$", allow_sudo=True))
async def metoo(e):
    if e.fwd_from:
        return
    txt = random.choice(CONFUSED)
    await edit_or_reply(e, txt)
    
@bot.on(admin_cmd(pattern=f"lobb$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"lobb$", allow_sudo=True))
async def metoo(e):
    if e.fwd_from:
        return
    txt = random.choice(LOB)
    await edit_or_reply(e, txt)
    
@bot.on(admin_cmd(pattern=f"wut$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"wut$", allow_sudo=True))
async def metoo(e):
    if e.fwd_from:
        return
    txt = random.choice(WTF)
    await edit_or_reply(e, txt)
    
@bot.on(admin_cmd(pattern=f"wavee$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"wavee$", allow_sudo=True))
async def metoo(e):
    if e.fwd_from:
        return
    txt = random.choice(WAVING)
    await edit_or_reply(e, txt)
    
@bot.on(admin_cmd(pattern=f"hehe$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"hehe$", allow_sudo=True))
async def metoo(e):
    if e.fwd_from:
        return
    txt = random.choice(EMOTICONS)
    await edit_or_reply(e, txt)
    
CmdHelp("edits").add_command(
  "hehe", None, "Use and see"
).add_command(
  "wavee", None, "Use and see"
).add_command(
  "wut", None, "Use and see"
).add_command(
  "lobb", None, "Use and see"
).add_command(
  "confused", None, "Use and see"
).add_command(
  "medead", None, "Use and see"
).add_command(
  "mesed", None, "Use and see"
).add_command(
  "doge", None, "Use and see"
).add_command(
  "shrug", None, "Use and see"
).add_command(
  "gendar", None, "Use and see"
).add()
