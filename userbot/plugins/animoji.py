import asyncio
from collections import deque

from userbot import CMD_HELP
from hellbot.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp


@bot.on(admin_cmd(pattern="think$", outgoing=True))
@bot.on(sudo_cmd(pattern="think$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "think")
    deq = deque(list("🤔🧐🤔🧐🤔🧐"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)

@bot.on(admin_cmd(pattern="ccry$", outgoing=True))
@bot.on(sudo_cmd(pattern="ccry$", allow_sudo=True))
async def cry(e):
    if e.fwd_from:
        return
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("(;´༎ຶД༎ຶ)")

@bot.on(admin_cmd(pattern="fap$", outgoing=True))
@bot.on(sudo_cmd(pattern="fap$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "fapping(°_°)")
    deq = deque(list("🍆✊🏻💦"))
    for _ in range(32):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)

@bot.on(admin_cmd(pattern=r"lmao$"))
@bot.on(sudo_cmd(pattern="lmao$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "lmao")
    deq = deque(list("😂🤣😂🤣😂🤣"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern=r"nothappy$"))
@bot.on(sudo_cmd(pattern="nothappy$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "nathappy")
    deq = deque(list("😁☹️😁☹️😁☹️😁"))
    for _ in range(48):
        await asyncio.sleep(0.4)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(outgoing=True, pattern="clock$"))
@bot.on(sudo_cmd(pattern="clock$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "clock")
    deq = deque(list("🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern=r"muah$"))
@bot.on(sudo_cmd(pattern="muah$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "muah")
    deq = deque(list("😗😙😚😚😘"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern="heart$"))
@bot.on(sudo_cmd(pattern="heart$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "heart")
    deq = deque(list("❤️🧡💛💚💙💜🖤"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern="gym$", outgoing=True))
@bot.on(sudo_cmd(pattern="gym$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "gym")
    deq = deque(list("🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern=f"earth$", outgoing=True))
@bot.on(sudo_cmd(pattern="earth$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "earth")
    deq = deque(list("🌏🌍🌎🌎🌍🌏🌍🌎"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(outgoing=True, pattern="moon$"))
@bot.on(sudo_cmd(pattern="moon$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "moon")
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


import asyncio

from hellbot.utils import admin_cmd


@bot.on(admin_cmd(pattern=f"lovestory", outgoing=True))
@bot.on(sudo_cmd(pattern=f"lovestory", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 3
    animation_ttl = range(0, 103)
    await edit_or_reply(event, "Let me tel you")
    animation_chars = [
        "1 ❤️ love story",
        "  😐             😕 \n/👕\         <👗\ \n 👖               /|",
        "  😉          😳 \n/👕\       /👗\ \n  👖            /|",
        "  😚            😒 \n/👕\         <👗> \n  👖             /|",
        "  😍         ☺️ \n/👕\      /👗\ \n  👖          /|",
        "  😍          😍 \n/👕\       /👗\ \n  👖           /|",
        "  😘   😊 \n /👕\/👗\ \n   👖   /|",
        " 😳  😁 \n /|\ /👙\ \n /     / |",
        "😈    /😰\ \n<|\      👙 \n /🍆    / |",
        "😅 \n/(),✊😮 \n /\         _/\\/|",
        "😎 \n/\\_,__😫 \n  //    //       \\",
        "😖 \n/\\_,💦_😋  \n  //         //        \\",
        "  😭      ☺️ \n  /|\   /(👶)\ \n  /!\   / \ ",
        "Abee aur kitna dekhoge be besharmi ki bhi hadd hoti hai..,The End 😂...",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 103])

@bot.on(admin_cmd(pattern=f"smoon$", outgoing=True))
@bot.on(sudo_cmd(pattern="smoon$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "smoon")
    animation_interval = 0.1
    animation_ttl = range(101)
    await event.edit("smoon..")
    animation_chars = [
        "🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗",
        "🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘",
        "🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑",
        "🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒",
        "🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓",
        "🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔",
        "🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕",
        "🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8])


@bot.on(admin_cmd(pattern=f"tmoon$", outgoing=True))
@bot.on(sudo_cmd(pattern="tmoon$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "tmoon")
    animation_interval = 0.1
    animation_ttl = range(117)
    await event.edit("tmoon")
    animation_chars = [
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 32])


@bot.on(admin_cmd(pattern=f"hart$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"hart$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(20)
    event = await edit_or_reply(event, "❤️")
    animation_chars = ["🖤", "❤️", "🖤", "❤️", "‎"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 4])


@bot.on(admin_cmd(pattern=f"anim$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"anim$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(20)
    event = await edit_or_reply(event, "😢")
    animation_chars = [
        "😁",
        "😧",
        "😡",
        "😢",
        "😁",
        "😧",
        "😡",
        "😢",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 10])

@bot.on(admin_cmd(pattern=f"fuck$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"fuck$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 101)
    await edit_or_reply(event, "fuk")
    animation_chars = ["👉       ✊️", "👉     ✊️", "👉  ✊️", "👉✊️💦"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 4])


@bot.on(admin_cmd(pattern=f"sux", outgoing=True))
@bot.on(sudo_cmd(pattern=f"sux", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 101)
    await edit_or_reply(event, "sux")
    animation_chars = ["🤵       👰", "🤵     👰", "🤵  👰", "🤵👼👰"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 4])

@bot.on(admin_cmd(pattern=f"kiss", outgoing=True))
@bot.on(sudo_cmd(pattern=f"kiss", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 101)
    await edit_or_reply(event, "kiss")
    animation_chars = ["🤵       👰", "🤵     👰", "🤵  👰", "🤵💋👰"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 4])

@bot.on(admin_cmd(pattern=f"fnl$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"fnl$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(6)
    event = await edit_or_reply(event, "Hey There....")
    animation_chars = ["😁🏿", "😁🏾", "😁🏽", "😁🏼", "‎😁"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 6])


@bot.on(admin_cmd(pattern=f"monkey$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"monkey$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(12)
    event = await edit_or_reply(event, "Hey There....")
    animation_chars = ["🐵", "🙉", "🙈", "🙊", "🖕‎🐵🖕"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 6])


@bot.on(admin_cmd(pattern=f"hand$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"hand$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(13)
    event = await edit_or_reply(event, "🖐️")
    animation_chars = [
        "👈",
        "👉",
        "☝️",
        "👆",
        "🖕",
        "👇",
        "✌️",
        "🤞",
        "🖖",
        "🤘",
        "🤙",
        "🖐️",
        "👌",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 13])


@bot.on(admin_cmd(pattern=f"gsg$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"gsg$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(12)
    event = await edit_or_reply(event, "ContDown....")
    animation_chars = [
        "🔟",
        "9️⃣",
        "8️⃣",
        "7️⃣",
        "6️⃣",
        "5️⃣",
        "4️⃣",
        "3️⃣",
        "2️⃣",
        "1️⃣",
        "0️⃣",
        "🆘",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 12])


@bot.on(admin_cmd(pattern=r"theart$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"theart$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(54)
    event = await edit_or_reply(event, "🖤")
    animation_chars = [
        "❤️",
        "🧡",
        "💛",
        "💚",
        "💙",
        "💜",
        "🖤",
        "💘",
        "💝",
        "❤️",
        "🧡",
        "💛",
        "💚",
        "💙",
        "💜",
        "🖤",
        "💘",
        "💝",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])


CmdHelp("animoji").add_command(
  'think', None, 'Use and see'
).add_command(
  'lmao', None, 'Use and see'
).add_command(
  'nothappy', None, 'Use and see'
).add_command(
  'clock', None, 'Use and see'
).add_command(
  'muah', None, 'Use and see'
).add_command(
  'heart', None, 'Use and see'
).add_command(
  'gym', None, 'Use and see'
).add_command(
  'earth', None, 'Use and see'
).add_command(
  'moon', None, 'Use and see'
).add_command(
  'smoon', None, 'Use and see'
).add_command(
  'tmoon', None, 'Use and see'
).add_command(
  'hart', None, 'Use and see'
).add_command(
  'anim', None, 'Use and see'
).add_command(
  'fnl', None, 'Use and see'
).add_command(
  'monkey', None, 'Use and see'
).add_command(
  'hand', None, 'Use and see'
).add_command(
  'gsg', None, 'Use and see'
).add_command(
  'theart', None, 'Use and see'
).add_command(
  'ccry', None, 'Crying animation🥱'
).add_command(
  'fap', None, 'Cool fapping animation'
).add_command(
  'kiss', None, 'Lets kiss😘'
).add_command(
  'sux', None, 'Wanna do sex wid me?'
).add_command(
  'fuck', None, 'Tapa tap tapa tap'
).add_command(
  'lovestory', None, 'A true love story😃'
).add()
