# Added more fonts by @Kraken_The_BadASS
# Ported from saitama i guess

from hellbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp

normiefont = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
weebyfont = [
    "卂",
    "乃",
    "匚",
    "刀",
    "乇",
    "下",
    "厶",
    "卄",
    "工",
    "丁",
    "长",
    "乚",
    "从",
    "𠘨",
    "口",
    "尸",
    "㔿",
    "尺",
    "丂",
    "丅",
    "凵",
    "リ",
    "山",
    "乂",
    "丫",
    "乙",
]
tantextfont = [
    "Ꭿ",
    "Ᏸ",
    "Ꮳ",
    "Ꮄ",
    "Ꮛ",
    "Ꮄ",
    "Ꮆ",
    "Ꮒ",
    "i",
    "Ꮰ",
    "Ꮶ",
    "l",
    "m",
    "Ꮑ",
    "Ꮻ",
    "Ꮅ",
    "Ꮔ",
    "ᖇ",
    "Ꭶ",
    "Ꮏ",
    "Ꮜ",
    "Ꮙ",
    "Ꮿ",
    "ﾒ",
    "Ꭹ",
    "Ꮓ",
]
linetextfont = [
    "𝔸",
    "𝔹",
    "ℂ",
    "𝔻",
    "𝔼",
    "𝔽",
    "𝔾",
    "ℍ",
    "𝕀",
    "𝕁",
    "𝕂",
    "𝕃",
    "𝕄",
    "ℕ",
    "𝕆",
    "ℙ",
    "ℚ",
    "ℝ",
    "𝕊",
    "𝕋",
    "𝕌",
    "𝕍",
    "𝕎",
    "𝕏",
    "𝕐",
    "ℤ",
]
boxtextfont = [
    "🄰",
    "🄱",
    "🄲",
    "🄳",
    "🄴",
    "🄵",
    "🄶",
    "🄷",
    "🄸",
    "🄹",
    "🄺",
    "🄻",
    "🄼",
    "🄽",
    "🄾",
    "🄿",
    "🅀",
    "🅁",
    "🅂",
    "🅃",
    "🅄",
    "🅅",
    "🅆",
    "🅇",
    "🅈",
    "🅉",
]
bubbletextfont = [
    "Ⓐ",
    "Ⓑ",
    "Ⓒ",
    "Ⓓ",
    "Ⓔ",
    "Ⓕ",
    "Ⓖ",
    "Ⓗ",
    "Ⓘ",
    "Ⓙ",
    "Ⓚ",
    "Ⓛ",
    "Ⓜ",
    "Ⓝ",
    "Ⓞ",
    "Ⓟ",
    "Ⓠ",
    "Ⓡ",
    "Ⓢ",
    "Ⓣ",
    "Ⓤ",
    "Ⓥ",
    "Ⓦ",
    "Ⓧ",
    "Ⓨ",
    "Ⓩ",
]

@bot.on(admin_cmd(pattern="weeb(?: |$)(.*)", command="weeb"))
@bot.on(sudo_cmd(pattern="weeb(?: |$)(.*)", command="weeb", allow_sudo=True))
async def weebify(event):
    if event.fwd_from:
        return
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "`What I am Supposed to Weebify U Dumb`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = weebyfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)
    await edit_or_reply(event, string)


@bot.on(admin_cmd(pattern="tanify(?: |$)(.*)", command="tanify"))
@bot.on(sudo_cmd(pattern="tanify(?: |$)(.*)", command="tanify", allow_sudo=True))
async def tantxt(event):
    if event.fwd_from:
        return
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "`What I am Supposed to tanify U Dumb`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            tanycharacter = tantextfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, tanycharacter)
    await edit_or_reply(event, string)


@bot.on(admin_cmd(pattern="lintxt(?: |$)(.*)", command="lintxt"))
@bot.on(sudo_cmd(pattern="lintxt(?: |$)(.*)", command="lintxt", allow_sudo=True))
async def linetxt(event):
    if event.fwd_from:
        return
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "`What I am Supposed to linefy U Dumb`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            linecharacter = linetextfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, linecharacter)
    await edit_or_reply(event, string)


@bot.on(admin_cmd(pattern="boxify(?: |$)(.*)", command="boxify"))
@bot.on(sudo_cmd(pattern="boxify(?: |$)(.*)", command="boxify", allow_sudo=True))
async def boxtxt(event):
    if event.fwd_from:
        return
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "`What I am Supposed to boxify U Dumb`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            boxcharacter = boxtextfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, boxcharacter)
    await edit_or_reply(event, string)


@bot.on(admin_cmd(pattern="bubble(?: |$)(.*)", command="bubble"))
@bot.on(sudo_cmd(pattern="bubble(?: |$)(.*)", command="bubble", allow_sudo=True))
async def bubbletxt(event):
    if event.fwd_from:
        return
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "`What I am Supposed to bubblify U Dumb`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            bubblecharacter = bubbletextfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, bubblecharacter)
    await edit_or_reply(event, string)

CmdHelp("fonts").add_command(
  'weeb', '<text>', 'Modifies your text in weeby font'
).add_command(
  'tanify', '<text>', 'Mofifies your text in tany font'
).add_command(
  'lintxt', '<text>', 'Modifies your text in liny font'
).add_command(
  'boxify', '<text>', 'Modifies your text in box font'
).add_command(
  'bubble', '<text>', 'Modifies your text in bubble font'
).add_command(
  'cp', '<text>', 'Gives the text a funny look'
).add_command(
  'vapor', '<text>', 'Vaporizes Your text'
).add_command(
  'str', '<text>', 'Streches the text'
).add_command(
  'zal', '<text>', 'Zagolifies your text'
).add()
#Hellbot_Op
