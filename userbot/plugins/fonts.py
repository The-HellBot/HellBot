""" Weebify a text,
Ported from Saitama Bot. 
By :- @PhycoNinja13b
Modified by :- @Kraken_The_BadAsS
.weeb <text> """

from telethon import events
from uniborg.util import admin_cmd

normiefont = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']
weebyfont = ['卂', '乃', '匚', '刀', '乇', '下', '厶', '卄', '工', '丁', '长', '乚', '从', '𠘨', '口', '尸', '㔿', '尺', '丂', '丅', '凵',
             'リ', '山', '乂', '丫', '乙']
tantextfont = ['Ꭿ', 'Ᏸ', 'Ꮳ', 'Ꮄ', 'Ꮛ', 'Ꮄ', 'Ꮆ', 'Ꮒ', 'i', 'Ꮰ', 'Ꮶ', 'l', 'm', 'Ꮑ', 'Ꮻ', 'Ꮅ', 'Ꮔ', 'ᖇ', 'Ꭶ', 'Ꮏ', 'Ꮜ', 
              'Ꮙ', 'Ꮿ', 'ﾒ', 'Ꭹ', 'Ꮓ']
linetextfont = [' 𝔸',' 𝔹',' ℂ',' 𝔻',' 𝔼',' 𝔽',' 𝔾',' ℍ',' 𝕀',' 𝕁',' 𝕂',' 𝕃',' 𝕄',' ℕ',' 𝕆',' ℙ',' ℚ',' ℝ',' 𝕊',' 𝕋',' 𝕌',
             ' 𝕍',' 𝕎',' 𝕏',' 𝕐',' ℤ']


@borg.on(admin_cmd(pattern="weeb ?(.*)"))
async def weebify(event):

    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text   
    if not args:
        await event.edit("`What I am Supposed to Weebify U Dumb`")
        return
    string = '  '.join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = weebyfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)
    await event.edit(string)
    

@borg.on(admin_cmd(pattern="tantext ?(.*)"))
async def tantxt(event):

    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text   
    if not args:
        await event.edit("`What I am Supposed to tanify U Dumb`")
        return
    string = '  '.join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            tanycharacter = tantextfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, tanycharacter)
    await event.edit(string)


@borg.on(admin_cmd(pattern="linetext ?(.*)"))
async def linetxt(event):

    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text   
    if not args:
        await event.edit("`What I am Supposed to linefy U Dumb`")
        return
    string = '  '.join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            linecharacter = linetextfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, linecharacter)
    await event.edit(string)

