# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.b (the "License");
# you may not use this file except in compliance with the License.
#
#

""" Userbot module for having some fun with people. """

import random
import re
import time

import requests
from cowpy import cow
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName

from userbot.cmdhelp import CmdHelp
from hellbot.utils import admin_cmd, sudo_cmd, edit_or_reply

# ================= CONSTANT =================

ZALG_LIST = [
    [
        "̖",
        " ̗",
        " ̘",
        " ̙",
        " ̜",
        " ̝",
        " ̞",
        " ̟",
        " ̠",
        " ̤",
        " ̥",
        " ̦",
        " ̩",
        " ̪",
        " ̫",
        " ̬",
        " ̭",
        " ̮",
        " ̯",
        " ̰",
        " ̱",
        " ̲",
        " ̳",
        " ̹",
        " ̺",
        " ̻",
        " ̼",
        " ͅ",
        " ͇",
        " ͈",
        " ͉",
        " ͍",
        " ͎",
        " ͓",
        " ͔",
        " ͕",
        " ͖",
        " ͙",
        " ͚",
        " ",
    ],
    [
        " ̍",
        " ̎",
        " ̄",
        " ̅",
        " ̿",
        " ̑",
        " ̆",
        " ̐",
        " ͒",
        " ͗",
        " ͑",
        " ̇",
        " ̈",
        " ̊",
        " ͂",
        " ̓",
        " ̈́",
        " ͊",
        " ͋",
        " ͌",
        " ̃",
        " ̂",
        " ̌",
        " ͐",
        " ́",
        " ̋",
        " ̏",
        " ̽",
        " ̉",
        " ͣ",
        " ͤ",
        " ͥ",
        " ͦ",
        " ͧ",
        " ͨ",
        " ͩ",
        " ͪ",
        " ͫ",
        " ͬ",
        " ͭ",
        " ͮ",
        " ͯ",
        " ̾",
        " ͛",
        " ͆",
        " ̚",
    ],
    [
        " ̕",
        " ̛",
        " ̀",
        " ́",
        " ͘",
        " ̡",
        " ̢",
        " ̧",
        " ̨",
        " ̴",
        " ̵",
        " ̶",
        " ͜",
        " ͝",
        " ͞",
        " ͟",
        " ͠",
        " ͢",
        " ̸",
        " ̷",
        " ͡",
    ],
]


EMOJIS = [
    "😂",
    "😂",
    "👌",
    "✌",
    "💞",
    "👍",
    "👌",
    "💯",
    "🎶",
    "👀",
    "😂",
    "👓",
    "👏",
    "👐",
    "🍕",
    "💥",
    "🍴",
    "💦",
    "💦",
    "🍑",
    "🍆",
    "😩",
    "😏",
    "👉👌",
    "👀",
    "👅",
    "😩",
    "🚰",
]

UWUS = [
    "(・`ω´・)",
    ";;w;;",
    "owo",
    "UwU",
    ">w<",
    "^w^",
    r"\(^o\) (/o^)/",
    "( ^ _ ^)∠☆",
    "(ô_ô)",
    "~:o",
    ";-;",
    "(*^*)",
    "(>_",
    "(♥_♥)",
    "*(^O^)*",
    "((+_+))",
]

FACEREACTS = [
    "ʘ‿ʘ",
    "ヾ(-_- )ゞ",
    "(っ˘ڡ˘ς)",
    "(´ж｀ς)",
    "( ಠ ʖ̯ ಠ)",
    "(° ͜ʖ͡°)╭∩╮",
    "(ᵟຶ︵ ᵟຶ)",
    "(งツ)ว",
    "ʚ(•｀",
    "(っ▀¯▀)つ",
    "(◠﹏◠)",
    "( ͡ಠ ʖ̯ ͡ಠ)",
    "( ఠ ͟ʖ ఠ)",
    "(∩｀-´)⊃━☆ﾟ.*･｡ﾟ",
    "(⊃｡•́‿•̀｡)⊃",
    "(._.)",
    "{•̃_•̃}",
    "(ᵔᴥᵔ)",
    "♨_♨",
    "⥀.⥀",
    "ح˚௰˚づ ",
    "(҂◡_◡)",
    "ƪ(ړײ)‎ƪ​​",
    "(っ•́｡•́)♪♬",
    "◖ᵔᴥᵔ◗ ♪ ♫ ",
    "(☞ﾟヮﾟ)☞",
    "[¬º-°]¬",
    "(Ծ‸ Ծ)",
    "(•̀ᴗ•́)و ̑̑",
    "ヾ(´〇`)ﾉ♪♪♪",
    "(ง'̀-'́)ง",
    "ლ(•́•́ლ)",
    "ʕ •́؈•̀ ₎",
    "♪♪ ヽ(ˇ∀ˇ )ゞ",
    "щ（ﾟДﾟщ）",
    "( ˇ෴ˇ )",
    "눈_눈",
    "(๑•́ ₃ •̀๑) ",
    "( ˘ ³˘)♥ ",
    "ԅ(≖‿≖ԅ)",
    "♥‿♥",
    "◔_◔",
    "⁽⁽ଘ( ˊᵕˋ )ଓ⁾⁾",
    "乁( ◔ ౪◔)「      ┑(￣Д ￣)┍",
    "( ఠൠఠ )ﾉ",
    "٩(๏_๏)۶",
    "┌(ㆆ㉨ㆆ)ʃ",
    "ఠ_ఠ",
    "(づ｡◕‿‿◕｡)づ",
    "(ノಠ ∩ಠ)ノ彡( \\o°o)\\",
    "“ヽ(´▽｀)ノ”",
    "༼ ༎ຶ ෴ ༎ຶ༽",
    "｡ﾟ( ﾟஇ‸இﾟ)ﾟ｡",
    "(づ￣ ³￣)づ",
    "(⊙.☉)7",
    "ᕕ( ᐛ )ᕗ",
    "t(-_-t)",
    "(ಥ⌣ಥ)",
    "ヽ༼ ಠ益ಠ ༽ﾉ",
    "༼∵༽ ༼⍨༽ ༼⍢༽ ༼⍤༽",
    "ミ●﹏☉ミ",
    "(⊙_◎)",
    "¿ⓧ_ⓧﮌ",
    "ಠ_ಠ",
    "(´･_･`)",
    "ᕦ(ò_óˇ)ᕤ",
    "⊙﹏⊙",
    "(╯°□°）╯︵ ┻━┻",
    r"¯\_(⊙︿⊙)_/¯",
    "٩◔̯◔۶",
    "°‿‿°",
    "ᕙ(⇀‸↼‶)ᕗ",
    "⊂(◉‿◉)つ",
    "V•ᴥ•V",
    "q(❂‿❂)p",
    "ಥ_ಥ",
    "ฅ^•ﻌ•^ฅ",
    "ಥ﹏ಥ",
    "（ ^_^）o自自o（^_^ ）",
    "ಠ‿ಠ",
    "ヽ(´▽`)/",
    "ᵒᴥᵒ#",
    "( ͡° ͜ʖ ͡°)",
    "┬─┬﻿ ノ( ゜-゜ノ)",
    "ヽ(´ー｀)ノ",
    "☜(⌒▽⌒)☞",
    "ε=ε=ε=┌(;*´Д`)ﾉ",
    "(╬ ಠ益ಠ)",
    "┬─┬⃰͡ (ᵔᵕᵔ͜ )",
    "┻━┻ ︵ヽ(`Д´)ﾉ︵﻿ ┻━┻",
    r"¯\_(ツ)_/¯",
    "ʕᵔᴥᵔʔ",
    "(`･ω･´)",
    "ʕ•ᴥ•ʔ",
    "ლ(｀ー´ლ)",
    "ʕʘ̅͜ʘ̅ʔ",
    "（　ﾟДﾟ）",
    r"¯\(°_o)/¯",
    "(｡◕‿◕｡)",
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

SLAP_TEMPLATES = [
    "{hits} {victim} with a {item}.",
    "{hits} {victim} in the face with a {item}.",
    "{hits} {victim} around a bit with a {item}.",
    "{throws} a {item} at {victim}.",
    "grabs a {item} and {throws} it at {victim}'s face.",
    "launches a {item} in {victim}'s general direction.",
    "starts slapping {victim} silly with a {item}.",
    "pins {victim} down and repeatedly {hits} them with a {item}.",
    "grabs up a {item} and {hits} {victim} with it.",
    "ties {victim} to a chair and {throws} a {item} at them.",
    "gave a friendly push to help {victim} learn to swim in lava.",
]

ITEMS = [
    "cast iron skillet",
    "large trout",
    "baseball bat",
    "cricket bat",
    "wooden cane",
    "nail",
    "printer",
    "shovel",
    "CRT monitor",
    "physics textbook",
    "toaster",
    "portrait of Richard Stallman",
    "television",
    "five ton truck",
    "roll of duct tape",
    "book",
    "laptop",
    "old television",
    "sack of rocks",
    "rainbow trout",
    "rubber chicken",
    "spiked bat",
    "fire extinguisher",
    "heavy rock",
    "chunk of dirt",
    "beehive",
    "piece of rotten meat",
    "bear",
    "ton of bricks",
]

THROW = [
    "throws",
    "flings",
    "chucks",
    "hurls",
]

HIT = [
    "hits",
    "whacks",
    "fek ke maari",
    "slaps",
    "smacks",
    "bashes",
]

# ===========================================

@bot.on(admin_cmd(pattern=r"(\w+)say (.*)"))
@bot.on(sudo_cmd(pattern=r"(\w+)say (.*)", allow_sudo=True))
async def univsaye(cowmsg):
    """ For .cowsay module, userbot wrapper for cow which says things. """
    if not cowmsg.text[0].isalpha() and cowmsg.text[0] not in ("/", "#", "@", "!"):
        arg = cowmsg.pattern_match.group(1).lower()
        text = cowmsg.pattern_match.group(2)

        if arg == "cow":
            arg = "default"
        if arg not in cow.COWACTERS:
            return
        cheese = cow.get_cow(arg)
        cheese = cheese()

        await edit_or_reply(cowmsg, f"`{cheese.milk(text).replace('`', '´')}`")


@bot.on(admin_cmd(pattern=":/$", outgoing=True))
@bot.on(sudo_cmd(pattern=":/$", allow_sudo=True))
async def kek(keks):
    if not keks.text[0].isalpha() and keks.text[0] not in ("/", "#", "@", "!"):
        """ Check yourself ;)"""
        uio = ["/", "\\"]
        for i in range(1, 15):
            time.sleep(0.3)
            await keks.edit(":" + uio[i % 2])


@bot.on(admin_cmd(pattern="slap(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="slap(?: |$)(.*)", allow_sudo=True))
async def who(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        """ slaps a user, or get slapped if not a reply. """
        if event.fwd_from:
            return

        replied_user = await get_user(event)
        caption = await slap(replied_user, event)
        message_id_to_reply = event.message.reply_to_msg_id

        if not message_id_to_reply:
            message_id_to_reply = None

        try:
            await edit_or_reply(event, caption)

        except:
            await edit_or_reply(event, "`Can't slap this person, need to fetch some sticks and stones !!`"
            )


async def get_user(event):
    """ Get the user from argument or replied message. """
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(previous_message.sender_id))
    else:
        user = event.pattern_match.group(1)

        if user.isnumeric():
            user = int(user)

        if not user:
            self_user = await event.client.get_me()
            user = self_user.id

        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]

            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user
        try:
            user_object = await event.client.get_entity(user)
            replied_user = await event.client(GetFullUserRequest(user_object.id))

        except (TypeError, ValueError):
            await edit_or_reply(event, "`I don't slap aliens, they ugly AF !!`")
            return None

    return replied_user


async def slap(replied_user, event):
    """ Construct a funny slap sentence !! """
    user_id = replied_user.user.id
    first_name = replied_user.user.first_name
    username = replied_user.user.username

    if username:
        slapped = "@{}".format(username)
    else:
        slapped = f"[{first_name}](tg://user?id={user_id})"

    temp = random.choice(SLAP_TEMPLATES)
    item = random.choice(ITEMS)
    hit = random.choice(HIT)
    throw = random.choice(THROW)

    caption = "..." + temp.format(victim=slapped, item=item, hits=hit, throws=throw)

    return caption


@bot.on(admin_cmd(pattern="-_-$", outgoing=True))
@bot.on(sudo_cmd(pattern="-_-$", allow_sudo=True))
async def lol(lel):
    if not lel.text[0].isalpha() and lel.text[0] not in ("/", "#", "@", "!"):
        """ Ok... """
        okay = "-_-"
        for _ in range(10):
            okay = okay[:-1] + "_-"
            await edit_or_reply(lel, okay)


@bot.on(admin_cmd(pattern=";_;$", outgoing=True))
@bot.on(sudo_cmd(pattern=";_;$", allow_sudo=True))
async def fun(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        t = ";__;"
        for j in range(10):
            t = t[:-1] + "_;"
            await edit_or_reply(e, t)


@bot.on(admin_cmd(pattern="cry$", outgoing=True))
@bot.on(sudo_cmd(pattern="cry$", allow_sudo=True))
async def cry(e):
    """ y u du dis, i cry everytime !! """
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await edit_or_reply(e, random.choice(CRI))


@bot.on(admin_cmd(pattern="cp(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="cp(?:|$)(.*)", allow_sudo=True))
async def copypasta(cp_e):
    """ Copypasta the famous meme """
    if not cp_e.text[0].isalpha() and cp_e.text[0] not in ("/", "#", "@", "!"):
        textx = await cp_e.get_reply_message()
        message = cp_e.pattern_match.group(1)

        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await edit_or_reply(cp_e, "`😂🅱️IvE👐sOME👅text👅for✌️Me👌tO👐MAkE👀iT💞funNy!💦`")
            return

        reply_text = random.choice(EMOJIS)
        b_char = random.choice(
            message
        ).lower()  # choose a random character in the message to be substituted with 🅱️
        for owo in message:
            if owo == " ":
                reply_text += random.choice(EMOJIS)
            elif owo in EMOJIS:
                reply_text += owo
                reply_text += random.choice(EMOJIS)
            elif owo.lower() == b_char:
                reply_text += "🅱️"
            else:
                if bool(random.getrandbits(1)):
                    reply_text += owo.upper()
                else:
                    reply_text += owo.lower()
        reply_text += random.choice(EMOJIS)
        await edit_or_reply(cp_e, reply_text)


@bot.on(admin_cmd(pattern="vapor(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="vapor(?: |$)(.*)", allow_sudo=True))
async def vapor(vpr):
    """ Vaporize everything! """
    if not vpr.text[0].isalpha() and vpr.text[0] not in ("/", "#", "@", "!"):
        reply_text = list()
        textx = await vpr.get_reply_message()
        message = vpr.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await edit_or_reply(vpr, "`Ｇｉｖｅ ｓｏｍｅ ｔｅｘｔ ｆｏｒ ｖａｐｏｒ！`")
            return

        for charac in message:
            if 0x21 <= ord(charac) <= 0x7F:
                reply_text.append(chr(ord(charac) + 0xFEE0))
            elif ord(charac) == 0x20:
                reply_text.append(chr(0x3000))
            else:
                reply_text.append(charac)

        await edit_or_reply(vpr, "".join(reply_text))


@bot.on(admin_cmd(pattern=f"repo", outgoing=True))
@bot.on(sudo_cmd(pattern=f"repo", allow_sudo=True))
async def source(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await edit_or_reply(e, "Click [here](https://github.com/HellBoy-OP/HellBot) to open this 🔥**Lit AF!!**🔥 __Hêllẞø†__ Repo.. Join channel :- @HellBot_Official")


@bot.on(admin_cmd(pattern="str(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="str(?: |$)(.*)", allow_sudo=True))
async def stretch(stret):
    """ Stretch it."""
    if not stret.text[0].isalpha() and stret.text[0] not in ("/", "#", "@", "!"):
        textx = await stret.get_reply_message()
        message = stret.text
        message = stret.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await edit_or_reply(stret, "`GiiiiiiiB sooooooomeeeeeee teeeeeeext!`")
            return

        count = random.randint(3, 10)
        reply_text = re.sub(
            r"([aeiouAEIOUａｅｉｏｕＡＥＩＯＵаеиоуюяыэё])", (r"\1" * count), message
        )
        await edit_or_reply(stret, reply_text)


@bot.on(admin_cmd(pattern="zal(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="zal(?: |$)(.*)", allow_sudo=True))
async def zal(zgfy):
    """ Invoke the feeling of chaos. """
    if not zgfy.text[0].isalpha() and zgfy.text[0] not in ("/", "#", "@", "!"):
        reply_text = list()
        textx = await zgfy.get_reply_message()
        message = zgfy.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await edit_or_reply(zgfy, "`gͫ ̆ i̛ ̺ v͇̆ ȅͅ   a̢ͦ   s̴̪ c̸̢ ä̸ rͩͣ y͖͞   t̨͚ é̠ x̢͖  t͔͛`"
            )
            return

        for charac in message:
            if not charac.isalpha():
                reply_text.append(charac)
                continue

            for _ in range(0, 3):
                randint = random.randint(0, 2)

                if randint == 0:
                    charac = charac.strip() + random.choice(ZALG_LIST[0]).strip()
                elif randint == 1:
                    charac = charac.strip() + random.choice(ZALG_LIST[1]).strip()
                else:
                    charac = charac.strip() + random.choice(ZALG_LIST[2]).strip()

            reply_text.append(charac)

        await edit_or_reply(zgfy, "".join(reply_text))


@bot.on(admin_cmd(pattern="pkill$", outgoing=True))
@bot.on(sudo_cmd(pattern="pkill$", allow_sudo=True))
async def killing(killed):
    """ Dont Kill Too much -_-"""
    if not killed.text[0].isalpha() and killed.text[0] not in ("/", "#", "@", "!"):
        if await killed.get_reply_message():
            await edit_or_reply(killed, "`My Master killed targeted user by Headshot 😈......`\n"
                "#Sad_Reacts_Onli\n"
            )

@bot.on(admin_cmd(pattern="bt$", outgoing=True))
@bot.on(sudo_cmd(pattern="bt$", allow_sudo=True))
async def bluetext(bte):
    """ Believe me, you will find this useful. """
    if not bte.text[0].isalpha() and bte.text[0] not in ("/", "#", "@", "!"):
        if await bte.get_reply_message():
            await edit_or_reply(bte, "`BLUETEXT MUST CLICK.`\n"
                "`Are you a stupid animal which is attracted to colours?`"
            )

@bot.on(admin_cmd(pattern="owo(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="owo(?: |$)(.*)", allow_sudo=True))
async def faces(owo):
    """ UwU """
    if not owo.text[0].isalpha() and owo.text[0] not in ("/", "#", "@", "!"):
        textx = await owo.get_reply_message()
        message = owo.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await edit_or_reply(owo, "` UwU no text given! `")
            return

        reply_text = re.sub(r"(r|l)", "w", message)
        reply_text = re.sub(r"(R|L)", "W", reply_text)
        reply_text = re.sub(r"n([aeiou])", r"ny\1", reply_text)
        reply_text = re.sub(r"N([aeiouAEIOU])", r"Ny\1", reply_text)
        reply_text = re.sub(r"\!+", " " + random.choice(UWUS), reply_text)
        reply_text = reply_text.replace("ove", "uv")
        reply_text += " " + random.choice(UWUS)
        await edit_or_reply(owo, reply_text)

@bot.on(admin_cmd(pattern="react$", outgoing=True))
@bot.on(sudo_cmd(pattern="react$", allow_sudo=True))
async def react_meme(react):
    """ Make your userbot react to everything. """
    if not react.text[0].isalpha() and react.text[0] not in ("/", "#", "@", "!"):
        await edit(react, random.choice(FACEREACTS))

@bot.on(admin_cmd(pattern="shg$", outgoing=True))
@bot.on(sudo_cmd(pattern="shg$", allow_sudo=True))
async def shrugger(shg):
    r""" ¯\_(ツ)_/¯ """
    if not shg.text[0].isalpha() and shg.text[0] not in ("/", "#", "@", "!"):
        await edit_or_reply(shg, random.choice(SHGS))

@bot.on(admin_cmd(pattern="10iq$", outgoing=True))
@bot.on(sudo_cmd(pattern="10iq$", allow_sudo=True))
async def iqless(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await edit_or_reply(e, "♿")

@bot.on(admin_cmd(pattern="mock(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="mock(?: |$)(.*)", allow_sudo=True))
async def spongemocktext(mock):
    """ Do it and find the real fun. """
    if not mock.text[0].isalpha() and mock.text[0] not in ("/", "#", "@", "!"):
        reply_text = list()
        textx = await mock.get_reply_message()
        message = mock.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await edit_or_reply(mock, "`gIvE sOMEtHInG tO MoCk!`")
            return

        for charac in message:
            if charac.isalpha() and random.randint(0, 1):
                to_app = charac.upper() if charac.islower() else charac.lower()
                reply_text.append(to_app)
            else:
                reply_text.append(charac)

        await edit_or_reply(mock, "".join(reply_text))

@bot.on(admin_cmd(pattern="clap(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="clap(?: |$)(.*)", allow_sudo=True))
async def claptext(memereview):
    """ Praise people! """
    if not memereview.text[0].isalpha() and memereview.text[0] not in (
        "/",
        "#",
        "@",
        "!",
    ):
        textx = await memereview.get_reply_message()
        message = memereview.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await edit_or_reply(memereview, "`Hah, I don't clap pointlessly!`")
            return
        reply_text = "👏 "
        reply_text += message.replace(" ", " 👏 ")
        reply_text += " 👏"
        await edit_or_reply(memereview, reply_text)

@bot.on(admin_cmd(pattern="smk (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="smk (.*)", allow_sudo=True))
async def smrk(smk):
    if not smk.text[0].isalpha() and smk.text[0] not in ("/", "#", "@", "!"):
        textx = await smk.get_reply_message()
        message = smk.text
    if message[5:]:
        message = str(message[5:])
    elif textx:
        message = textx
        message = str(message.message)
    if message == "dele":
        await edit_or_reply(smk, message + "te the hell" + "ツ")
        await edit_or_reply(smk, "ツ")
    else:
        smirk = " ツ"
        reply_text = message + smirk
        await edit_or_reply(smk, reply_text)

@bot.on(admin_cmd(pattern="lfy (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="lfy (.*)", allow_sudo=True))
async def let_me_google_that_for_you(lmgtfy_q):
    if not lmgtfy_q.text[0].isalpha() and lmgtfy_q.text[0] not in ("/", "#", "@", "!"):
        textx = await lmgtfy_q.get_reply_message()
        query = lmgtfy_q.text
        if query[5:]:
            query = str(query[5:])
        elif textx:
            query = textx
            query = query.message
        query_encoded = query.replace(" ", "+")
        lfy_url = f"http://lmgtfy.com/?s=g&iie=1&q={query_encoded}"
        payload = {"format": "json", "url": lfy_url}
        r = requests.get("http://is.gd/create.php", params=payload)
        await edit_or_reply(lmgtfy_q, f"[{query}]({r.json()['shorturl']})")
        if BOTLOG:
            await bot.send_message(
                BOTLOG_CHATID,
                "LMGTFY query `" + query + "` was executed successfully",
            )


CmdHelp("memes").add_command(
  "lfy", "<text>", "Search result from LMGTFY site."
).add_command(
  "smk", "<word>", "Adds ツ in last of given word"
).add_command(
  "clap", "<reply>", "Gives the replied text a clapping look👏"
).add_command(
  "mock", "<text>", "MoCkS yOuR tExT iN cOoL sTyLe"
).add_command(
  "10iq", None, "Iq tester iz here guys"
).add_command(
  "shg", None, "Random Shrug Emoji"
).add_command(
  "react", None, "Reacts randomly"
).add_command(
  "owo", "<text>", "OwO your text. Use and see"
).add_command(
  "bt", None, "Do it yourself"
).add_command(
  "pkill", None, "Targeted User Iz Killed"
).add_command(
  "cry", None, "Lemme cry in corner ;_;"
).add_command(
  ";_;", None, "Shit animation."
).add_command(
  "-_-", None, "Shite animation"
).add_command(
  ":/", None, "Shit animation"
).add_command(
  "slap", "<Reply>", "Slapps the user virtually"
).add_command(
  "cowsay", "<text>", "Use and see....."
).add()
#HellBot_OP
