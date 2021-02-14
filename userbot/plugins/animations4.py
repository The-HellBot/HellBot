import asyncio

from hellbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp


@bot.on(admin_cmd(pattern="phub$", outgoing=True))
@bot.on(sudo_cmd(pattern="phub$", allow_sudo=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 101)

    await edit_or_reply(event, "phub")

    animation_chars = [
        "P_",
        "PO_",
        "POR_",
        "PORN_",
        "PORNH_",
        "PORNHU_",
        "PORNHUB_",
        "PORNHUB",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 10])


@bot.on(admin_cmd(pattern=r"amore$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"amore$", allow_sudo=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 101)

    await edit_or_reply(event, "amore")

    animation_chars = [
        "A_",
        "AM_",
        "AMO_",
        "AMOR_",
        "AMORE_",
        "AMORE❤_",
        ".-.",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 10])


import asyncio


@bot.on(admin_cmd(pattern=r"sexy$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"sexy$", allow_sudo=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 101)

    await edit_or_reply(event, "Sexy")

    animation_chars = [
        "S_",
        "SE_",
        "SEX_",
        "SEXY_",
        "SEXY👄_",
        "SEXY👄",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 10])
        
@bot.on(admin_cmd(pattern="istar$", outgoing=True))
@bot.on(sudo_cmd(pattern="istar$", allow_sudo=True))
async def ammastar(hellstar):
  
    if hellstar.fwd_from:
      
        return
      
    animation_interval = 2
    
    animation_ttl = range(0, 11)
    
    await edit_or_reply(hellstar, "I am A Star")
    
    animation_chars = [
        "I Party like a rockstar",
        "I Look like a movie star",
        "I Play like an all star",
        "I Fuck like a pornstar",
        "Baby I'm a superstar",
    ]
    
    for i in animation_ttl:
      
        await asyncio.sleep(animation_interval)
        
        await hellstar.edit(animation_chars[i % 11])
    
        
@bot.on(admin_cmd(pattern=r"lmoon", outgoing=True))
@bot.on(sudo_cmd(pattern=r"lmoon", allow_sudo=True))
async def test(event):
    if event.fwd_from:
        return
    await edit_or_reply(event, 
        "🌕🌕🌕🌕🌕🌕🌕🌕\n🌕🌕🌖🌔🌖🌔🌕🌕\n🌕🌕🌗🌔🌖🌓🌕🌕\n🌕🌕🌗🌔🌖🌓🌕🌕\n🌕🌕🌖🌓🌗🌔🌕🌕\n🌕🌕🌗🌑🌑🌓🌕🌕\n🌕🌕🌗👀🌑🌓🌕🌕\n🌕🌕🌘👄🌑🌓🌕🌕\n🌕🌕🌗🌑🌑🌒🌕🌕\n🌕🌖🌑🌑🌑🌑🌔🌕\n🌕🌘🌑🌑🌑🌑🌒🌕\n🌖🌑🌑🌑🌑🌑🌑🌔\n🌕🤜🏻🌑🌑🌑🌑🤛🏻🌕\n🌕🌖🌑🌑🌑🌑🌔🌕\n🌘🌑🌑🌑🌑🌑🌑🌒\n🌕🌕🌕🌕🌕🌕🌕🌕"
    )


@bot.on(admin_cmd(pattern=r"city", outgoing=True))
@bot.on(sudo_cmd(pattern=r"city", allow_sudo=True))
async def test(event):
    if event.fwd_from:
        return
    await edit_or_reply(event, 
        """☁☁🌞      ☁           ☁
       ☁  ✈         ☁    🚁    ☁    ☁        ☁          ☁     ☁   ☁

🏬🏨🏫🏢🏤🏥🏦🏪🏫
              🌲/     l🚍\🌳👭
           🌳/  🚘 l  🏃 \🌴 👬                       👬  🌴/            l  🚔    \🌲
      🌲/   🚖     l               \
   🌳/🚶           |   🚍         \ 🌴🚴🚴
🌴/                    |                     \🌲"""
    )


@bot.on(admin_cmd(pattern=r"hii", outgoing=True))
@bot.on(sudo_cmd(pattern=r"hii", allow_sudo=True))
async def hi(event):
    if event.fwd_from:
        return
    await edit_or_reply(event, "🌺✨✨🌺✨🌺🌺🌺\n🌺✨✨🌺✨✨🌺✨\n🌺🌺🌺🌺✨✨🌺✨\n🌺✨✨🌺✨✨🌺✨\n🌺✨✨🌺✨🌺🌺🌺\n☁☁☁☁☁☁☁☁")


@bot.on(admin_cmd(pattern=r"cheer", outgoing=True))
@bot.on(sudo_cmd(pattern=r"cheer", allow_sudo=True))
async def cheer(event):
    if event.fwd_from:
        return
    await edit_or_reply(event, 
        "💐💐😉😊💐💐\n☕ Cheer Up  🍵\n🍂 ✨ )) ✨  🍂\n🍂┃ (( * ┣┓ 🍂\n🍂┃*💗 ┣┛ 🍂 \n🍂┗━━┛  🍂🎂 For YOU  🍰\n💐💐😌😚💐💐"
    )


@bot.on(admin_cmd(pattern=r"getwell", outgoing=True))
@bot.on(sudo_cmd(pattern=r"getwell", allow_sudo=True))
async def getwell(event):
    if event.fwd_from:
        return
    await edit_or_reply(event, "🌹🌹🌹🌹🌹🌹🌹🌹 \n🌹😷😢😓😷😢💨🌹\n🌹💝💉🍵💊💐💝🌹\n🌹 GetBetter Soon! 🌹\n🌹🌹🌹🌹🌹🌹🌹🌹")

@bot.on(admin_cmd(pattern="switch$", outgoing=True))
@bot.on(sudo_cmd(pattern="switch$", allow_sudo=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 11)

  #  input_str = event.pattern_match.group(1)

  #  if input_str == "switch":

    await edit_or_reply(event, "Switch")

    animation_chars = [
         "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜[🔲](https://github.com/HellBoy-OP/HellBot)\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜",
         "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜[🔲](https://github.com/HellBoy-OP/HellBot)\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n[👉](https://t.me/kraken_the_badass)⬜⬜⬜⬜⬜⬜",
         "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜[🔲](https://github.com/HellBoy-OP/HellBot)\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬛[👉](https://t.me/kraken_the_badass)⬜⬜⬜⬜⬜",
         "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜[🔲](https://github.com/HellBoy-OP/HellBot)\n⬜⬜⬜⬜⬜⬜⬜\n⬜[👆](https://t.me/kraken_the_badass)⬜⬜⬜⬜⬜\n⬛⬛⬜⬜⬜⬜⬜",
         "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜[🔲](https://github.com/HellBoy-OP/HellBot)\n⬜[👆](https://t.me/kraken_the_badass)⬜⬜⬜⬜⬜\n⬜⬛⬜⬜⬜⬜⬜\n⬛⬛⬜⬜⬜⬜⬜",
         "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜[🔲](https://github.com/HellBoy-OP/HellBot)\n⬜⬛[👉](https://t.me/kraken_the_badass)⬜⬜⬜⬜\n⬜⬛⬜⬜⬜⬜⬜\n⬛⬛⬜⬜⬜⬜⬜",
         "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜[🔲](https://github.com/HellBoy-OP/HellBot)\n⬜⬛⬛[👉](https://t.me/kraken_the_badass)⬜⬜⬜\n⬜⬛⬜⬜⬜⬜⬜\n⬛⬛⬜⬜⬜⬜⬜",
         "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜🔲\n⬜⬛⬛⬛[👉](https://t.me/kraken_the_badass)⬜⬜\n⬜⬛⬜⬜⬜⬜⬜\n⬛⬛⬜⬜⬜⬜⬜",
         "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜[👆](https://t.me/kraken_the_badass)⬜🔲\n⬜⬛⬛⬛⬛⬜⬜\n⬜⬛⬜⬜⬜⬜⬜\n⬛⬛⬜⬜⬜⬜⬜",
         "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬛[👉](https://t.me/kraken_the_badass)🔲\n⬜⬛⬛⬛⬛⬜⬜\n⬜⬛⬜⬜⬜⬜⬜\n⬛⬛⬜⬜⬜⬜⬜",
         "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛🔳\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 11])


@bot.on(admin_cmd(pattern=r"sprinkle", outgoing=True))
@bot.on(sudo_cmd(pattern=r"sprinkle", allow_sudo=True))
async def sprinkle(event):
    if event.fwd_from:
        return
    await edit_or_reply(event, 
        "✨.•*¨*.¸.•*¨*.¸¸.•*¨*• ƸӜƷ\n🌸🌺🌸🌺🌸🌺🌸🌺\n Sprinkled with love❤\n🌷🌻🌷🌻🌷🌻🌷🌻\n ¨*.¸.•*¨*. ¸.•*¨*.¸¸.•*¨`*•.✨\n🌹🍀🌹🍀🌹🍀🌹🍀"
    )
    

@bot.on(admin_cmd(pattern=r"f", outgoing=True))
@bot.on(sudo_cmd(pattern=r"f", allow_sudo=True))
async def payf(event):
    if event.fwd_from:
        return
    paytext = event.pattern_match.group(1)
    pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(
        paytext * 8,
        paytext * 8,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 6,
        paytext * 6,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 2,
    )
    await edit_or_reply(event, pay)



CmdHelp("animations4").add_command(
  "phub", None, "Animated PORNHUB Typing"
).add_command(
  "amore", None, "Animated AMORE Typing"
).add_command(
  "sexy", None, "Animated SEXY Typing"
).add_command(
  "unoob", None, "Animated text calling them noob🚶"
).add_command(
  "menoob", None, "Animated text claiming you noob"
).add_command(
  "uproo", None, "Animated text claiming you to be proooo"
).add_command(
  "mepro", None, "Animated text calling them proo Af!!"
).add_command(
  "sprinkle", None, "Use and see"
).add_command(
  "getwell", None, "Use and see"
).add_command(
  "cheer", None, "Use and see"
).add_command(
  "hii", None, "Use and see"
).add_command(
  "city", None, "Use and see"
).add_command(
  "lmoon", None, "Use and see"
).add_command(
  "istar", None, "I am a Superstar⚡✨"
).add_command(
  "switch", None, "Click on the switch to reveal the price✨"
).add_command(
  "thanos", None, "A poem on Thanos... Maybe🤐"
).add_command(
  "tp", None, "Use and see"
).add_command(
  "f", "<text>", "Prints the given text in 'F' format"
).add_command(
  "wahack", None, "Whatsapp Hack animation"
).add()
