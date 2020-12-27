# Added by @Sur_vivor

import asyncio

import requests
from userbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp

# ================= CONSTANT =================


GAMBAR_TITIT = """
🍆🍆
🍆🍆🍆
  🍆🍆🍆
    🍆🍆🍆
     🍆🍆🍆
       🍆🍆🍆
        🍆🍆🍆
         🍆🍆🍆
          🍆🍆🍆
          🍆🍆🍆
      🍆🍆🍆🍆
 🍆🍆🍆🍆🍆🍆
 🍆🍆🍆  🍆🍆🍆
    🍆🍆       🍆🍆
"""

CUSTOM_HII = """
{hell}{hell}{hell}{hell}{hell}{hell}{hell}{hell}{hell}
{hell}🔷🔷🔷🔷🔷🔷🔷{hell}
{hell}{hell}{hell}{hell}🔷{hell}{hell}{hell}{hell}
{hell}{hell}{hell}{hell}🔷{hell}{hell}{hell}{hell}
{hell}{hell}{hell}{hell}🔷{hell}{hell}{hell}{hell}
{hell}🔷🔷🔷🔷️🔷🔷🔷{hell}
{hell}{hell}{hell}{hell}{hell}{hell}{hell}{hell}{hell}
{hell}{hell}{hell}{hell}{hell}{hell}{hell}{hell}{hell}
{hell}🔷{hell}{hell}️{hell}{hell}{hell}🔷{hell}
{hell}🔷🔷🔷🔷🔷🔷🔷{hell}          
{hell}🔷🔷🔷🔷🔷🔷️🔷{hell}
{hell}🔷{hell}{hell}{hell}{hell}️{hell}🔷{hell}
{hell}{hell}{hell}{hell}{hell}{hell}{hell}{hell}{hell}
"""
        
# ===========================================


@bot.on(admin_cmd(pattern=r"hf$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"hf$", allow_sudo=True))
async def facepalm(e):
    """ Facepalm  🤦‍♂ """
    await edit_or_reply(e, "🤦‍♂")

@bot.on(admin_cmd(pattern=r"corona$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"corona$", allow_sudo=True))
async def iqless(e):
    await edit_or_reply(e, "Antivirus scan was completed \n⚠️ Warning! This  donkey has Corona Virus"
    )

@bot.on(admin_cmd(pattern=r"fail$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"fail$", allow_sudo=True))
async def fail(e):
    await edit_or_reply(e, "`\n▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ `"
      "`\n████▌▄▌▄▐▐▌█████ `"
      "`\n████▌▄▌▄▐▐▌▀████ `"
      "`\n▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ `"
      )

@bot.on(admin_cmd(pattern=r"lol$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"lol$", allow_sudo=True))
async def lol(e):
    await edit_or_reply(e, "`\n╱┏┓╱╱╱╭━━━╮┏┓╱╱╱╱ `"
      "`\n╱┃┃╱╱╱┃╭━╮┃┃┃╱╱╱╱ `"
      "`\n╱┃┗━━┓┃╰━╯┃┃┗━━┓╱ `"
      "`\n╱┗━━━┛╰━━━╯┗━━━┛╱ `"
      )


@bot.on(admin_cmd(pattern=r"rock$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"rock$", allow_sudo=True))
async def lol(e):
    await edit_or_reply(e, 
        "`\n┈╭╮┈┈┈┈┈┈┈┈┈┈┈┈ `"
        "`\n┈┃┃┈╭╮┈┏╮╭╮╭╮┃╭ `"
        "`\n┈┃┃┈┃┃┈┣┫┃┃┃┈┣┫ `"
        "`\n┈┃┣┳┫┃┈┃╰╰╯╰╯┃╰ `"
        "`\n╭┻┻┻┫┃┈┈╭╮┃┃━┳━ `"
        "`\n┃╱╭━╯┃┈┈┃┃┃┃┈┃┈ `"
        "`\n╰╮╱╱╱┃┈┈╰╯╰╯┈┃┈ `"
    )


@bot.on(admin_cmd(pattern=r"lool$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"lool$", allow_sudo=True))
async def lool(e):
    await edit_or_reply(e, 
        "`\n╭╭━━━╮╮┈┈┈┈┈┈┈┈┈┈\n┈┃╭━━╯┈┈┈┈▕╲▂▂╱▏┈\n┈┃┃╱▔▔▔▔▔▔▔▏╱▋▋╮┈`"
        "`\n┈┃╰▏┃╱╭╮┃╱╱▏╱╱▆┃┈\n┈╰━▏┗━╰╯┗━╱╱╱╰┻┫┈\n┈┈┈▏┏┳━━━━▏┏┳━━╯┈`"
        "`\n┈┈┈▏┃┃┈┈┈┈▏┃┃┈┈┈┈ `"
    )


@bot.on(admin_cmd(pattern=r"nih$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"nih$", allow_sudo=True))
async def nih(e):
    await edit_or_reply(e, 
        "`\n(\_/)`"
        "`\n(•_•)`"
        "`\n >🌹 *`"
        "`\n                    `"
        "`\n(\_/)`"
        "`\n(•_•)`"
        "`\n🌹<\ *`"
    )


@bot.on(admin_cmd(pattern=r"hoi$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"hoi$", allow_sudo=True))
async def gtfo(e):
    await edit_or_reply(e, 
        "`\n█████████`"
        "`\n█▄█████▄█`"
        "`\n█▼▼▼▼▼`"
        "`\n█  Hello Man`"
        "`\n█▲▲▲▲▲`"
        "`\n█████████`"
        "`\n ██   ██`"
    )


@bot.on(admin_cmd(pattern=r"ml(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern=r"ml(?: |$)(.*)", allow_sudo=True))
async def gtfo(e):
    message = e.pattern_match.group(1)
    await edit_or_reply(e, 
        "`\n█████████`"
        "`\n█▄█████▄█`"
        "`\n█▼▼▼▼▼`"
        f"`\n█  {message}`"
        "`\n█▲▲▲▲▲`"
        "`\n█████████`"
        "`\n ██   ██`"
    )


@bot.on(admin_cmd(pattern=r"taco$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"taco$", allow_sudo=True))
async def taco(e):
    await edit_or_reply(e, "\n{\__/}" "\n(●_●)" "\n( >🌮 Want a taco?")


@bot.on(admin_cmd(pattern=r"paw$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"paw$", allow_sudo=True))
async def paw(e):
    await edit_or_reply(e, "`(=ↀωↀ=)")


@bot.on(admin_cmd(pattern=r"tf$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"tf$", allow_sudo=True))
async def tf(e):
    await edit_or_reply(e, "(̿▀̿ ̿Ĺ̯̿̿▀̿ ̿)̄  ")


@bot.on(admin_cmd(pattern=r"gay$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"gay$", allow_sudo=True))
async def gey(e):
    await edit_or_reply(e, 
        "`\n┈┈┈╭━━━━━╮┈┈┈┈┈\n┈┈┈┃┊┊┊┊┊┃┈┈┈┈┈`"
        "`\n┈┈┈┃┊┊╭━╮┻╮┈┈┈┈\n┈┈┈╱╲┊┃▋┃▋┃┈┈┈┈\n┈┈╭┻┊┊╰━┻━╮┈┈┈┈`"
        "`\n┈┈╰┳┊╭━━━┳╯┈┈┈┈\n┈┈┈┃┊┃╰━━┫┈U GAY`"
        "\n┈┈┈┈┈┈┏━┓┈┈┈┈┈┈"
    )


@bot.on(admin_cmd(pattern=r"bot$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"bot$", allow_sudo=True))
async def bot(e):
    await edit_or_reply(e, 
        "` \n   ╲╲╭━━━━╮ \n╭╮┃▆┈┈▆┃╭╮ \n┃╰┫▽▽▽┣╯┃ \n╰━┫△△△┣━╯`"
        "`\n╲╲┃┈┈┈┈┃  \n╲╲┃┈┏┓┈┃ `"
    )


@bot.on(admin_cmd(pattern=r"nou$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"nou$", allow_sudo=True))
async def nou(e):
    await edit_or_reply(e, 
        "`\n┈╭╮╭╮\n┈┃┃┃┃\n╭┻┗┻┗╮`"
        "`\n┃┈▋┈▋┃\n┃┈╭▋━╮━╮\n┃┈┈╭╰╯╰╯╮`"
        "`\n┫┈┈  NoU\n┃┈╰╰━━━━╯`"
        "`\n┗━━┻━┛`"
    )


@bot.on(admin_cmd(pattern=r"mf$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"mf$", allow_sudo=True))
async def gtfo(e):
    await edit_or_reply(e, 
        "\n......................................../´¯/) "
        "\n......................................,/¯../ "
        "\n...................................../..../ "
        "\n..................................../´.¯/"
        "\n..................................../´¯/"
        "\n..................................,/¯../ "
        "\n................................../..../ "
        "\n................................./´¯./"
        "\n................................/´¯./"
        "\n..............................,/¯../ "
        "\n............................./..../ "
        "\n............................/´¯/"
        "\n........................../´¯./"
        "\n........................,/¯../ "
        "\n......................./..../ "
        "\n....................../´¯/"
        "\n....................,/¯../ "
        "\n.................../..../ "
        "\n............./´¯/'...'/´¯¯`·¸ "
        "\n........../'/.../..../......./¨¯\ "
        "\n........('(...´...´.... ¯~/'...') "
        "\n.........\.................'...../ "
        "\n..........''...\.......... _.·´ "
        "\n............\..............( "
        "\n..............\.............\..."
    )


@bot.on(admin_cmd(pattern=r"chi(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern=r"chi(?: |$)(.*)", allow_sudo=True))
async def cstm(e):
    hell = e.pattern_match.group(1)
    chii = CUSTOM_HII
    if hell:
        chii = chii.replace("💛", hell)
    await edit_or_reply(e, chii)


@bot.on(admin_cmd(pattern=r"(?:penis|dick)\s?(.)?", outgoing=True))
@bot.on(sudo_cmd(pattern=r"(?:penis|dick)\s?(.)?", allow_sudo=True))
async def emoji_penis(e):
    emoji = e.pattern_match.group(1)
    titid = GAMBAR_TITIT
    if emoji:
        titid = titid.replace("🍆", emoji)
    await edit_or_reply(e, titid)


@bot.on(admin_cmd(pattern=f"muth", outgoing=True))
@bot.on(sudo_cmd(pattern=f"muth", allow_sudo=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 100)

    animation_chars = [
        "8✊️===D",
        "8=✊️==D",
        "8==✊️=D",
        "8===✊️D",
        "8==✊️=D",
        "8=✊️==D",
        "8✊️===D",
        "8===✊️D💦",
        "8==✊️=D💦💦",
        "8=✊️==D💦💦💦",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 8])


emojis = {
    "yee": "ツ",
    "happy": "(ʘ‿ʘ)",
    "veryhappy": "=͟͟͞͞٩(๑☉ᴗ☉)੭ु⁾⁾",
    "amazed": "ヾ(o✪‿✪o)ｼ",
    "crying": "༎ຶ︵༎ຶ",
    "dicc": "╰U╯☜(◉ɷ◉ )",
    "fek": "╰U╯\n(‿ˠ‿)",
    "ded": "✖‿✖",
    "sad": "⊙︿⊙",
    "lenny": "( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)",
    "idc": "¯\_(ツ)_/¯",
    "f": "😂😂😂😂😂😂😂😂\n😂😂😂😂😂😂😂😂😂\n😂😂\n😂😂\n😂😂😂😂😂😂\n😂😂😂😂😂😂\n😂😂\n😂😂\n😂😂\n😂😂\n😂😂",
}

unpacked_emojis = ""

for emoji in emojis:
    unpacked_emojis += f"`{emoji}`\n"


@bot.on(admin_cmd(pattern="emoji ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    try:
        req_emoji = emojis[str(input_str)]
        await edit_or_reply(event, req_emoji)
    except KeyError:
        await edit_or_reply(event, "Emoji not found!")


CmdHelp("memes2").add_command(
  "dick", "<emoji>", "A dick art in given emoji"
).add_command(
  "chi", "<emoji>", "Custom Hii message. Based on your emoji along with cmd"
).add_command(
  "mf", None, "Use and see"
).add_command(
  "nou", None, "Use and see"
).add_command(
  "hai", None, "Use and see"
).add_command(
  "bot", None, "Use and see"
).add_command(
  "gay", None, "Use and see"
).add_command(
  "tf", None, "Use and see"
).add_command(
  "paw", None, "Use and see"
).add_command(
  "taco", None, "Use and see"
).add_command(
  "ml", "<msg>", "Use and see"
).add_command(
  "hoi", None, "Use and see"
).add_command(
  "hf", None, "Use and see"
).add_command(
  "corona", None, "Use and see"
).add_command(
  "fail", None, "Use and see"
).add_command(
  "lol", None, "Use and see"
).add_command(
  "lool", None, "Use and see"
).add_command(
  "rock", None, "Use and see"
).add_command(
  "nih", None, "Use and see"
).add()
