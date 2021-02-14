"""COMMAND : .join , .pay , .work , .push , .aag , .climb, .ohh, .suckit, .lovestory, .bf"""
import asyncio
import random

from telethon.tl.types import ChannelParticipantsAdmins

from userbot import LOGS
from hellbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp

@bot.on(admin_cmd(pattern="join$", outgoing=True))
@bot.on(sudo_cmd(pattern="join$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`━━━━━┓ \n┓┓┓┓┓┃\n┓┓┓┓┓┃　ヽ○ノ ⇦ Me When You Joined \n┓┓┓┓┓┃.     /　 \n┓┓┓┓┓┃ ノ) \n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃`"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await edit_or_reply(event, mentions)


@bot.on(admin_cmd(pattern="pay$", outgoing=True))
@bot.on(sudo_cmd(pattern="pay$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`█▀▀▀▀▀█░▀▀░░░█░░░░█▀▀▀▀▀█\n█░███░█░█▄░█▀▀░▄▄░█░███░█\n█░▀▀▀░█░▀█▀▀▄▀█▀▀░█░▀▀▀░█\n▀▀▀▀▀▀▀░▀▄▀▄▀▄█▄▀░▀▀▀▀▀▀▀\n█▀█▀▄▄▀░█▄░░░▀▀░▄█░▄▀█▀░▀\n░█▄▀░▄▀▀░░░▄▄▄█░▀▄▄▄▀▄▄▀▄\n░░▀█░▀▀▀▀▀▄█░▄░████ ██▀█▄\n▄▀█░░▄▀█▀█▀░█▄▀░▀█▄██▀░█▄\n░░▀▀▀░▀░█▄▀▀▄▄░▄█▀▀▀█░█▀▀\n█▀▀▀▀▀█░░██▀█░░▄█░▀░█▄░██\n█░███░█░▄▀█▀██▄▄▀▀█▀█▄░▄▄\n█░▀▀▀░█░█░░▀▀▀░█░▀▀▀▀▄█▀░\n▀▀▀▀▀▀▀░▀▀░░▀░▀░░░▀▀░▀▀▀▀`"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await edit_or_reply(event, mentions)
  

@bot.on(admin_cmd(pattern="climb$", outgoing=True))
@bot.on(sudo_cmd(pattern="climb$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`😏/\n/▌ \n/ \\n████\n╬╬\n╬╬\n╬╬\n╬╬\n╬╬\n╬╬\n╬╬\😦\n╬╬/▌\n╬╬/\`"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await edit_or_reply(event, mentions)
  

@bot.on(admin_cmd(pattern="aag$", outgoing=True))
@bot.on(sudo_cmd(pattern="aag$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`😲💨  🔥\n/|\     🔥🔥\n/ \   🔥🔥🔥`"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await edit_or_reply(event, mentions)
    

@bot.on(admin_cmd(pattern="push$", outgoing=True))
@bot.on(sudo_cmd(pattern="push$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`.      😎\n          |\👐\n         / \\\n━━━━━┓ ＼＼ \n┓┓┓┓┓┃\n┓┓┓┓┓┃ ヽ😩ノ\n┓┓┓┓┓┃ 　 /　\n┓┓┓┓┓┃  ノ)　 \n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃`"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await edit_or_reply(event, mentions)
    

@bot.on(admin_cmd(pattern="work$", outgoing=True))
@bot.on(sudo_cmd(pattern="work$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`📔📚           📚\n📓📚📖  😫  📚📚📓\n📕📚📚  📝  📗💻📘\n📖⁣📖📖📖📖📖📖📖📖`"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await edit_or_reply(event, mentions)
    

@bot.on(admin_cmd(pattern="suckit$", outgoing=True))
@bot.on(sudo_cmd(pattern="suckit$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`......................................... \n \n𝕔𝕠𝕞𝕖 𝕥𝕠 𝕞𝕖, 𝕞𝕪 𝕔𝕙𝕚𝕝𝕕𝕣𝕖𝕟 \n`` \n. . /. ))) . . . . . . . . . (((ヽ \n/. .ノ￣. . . ___. . .￣ Y .\ \n| . (.\, . . . ( ͡° ͜ʖ ͡°). . . ./.) . ) \nヽ.ヽ..ᯢ._.|﹀|._._ノ₄₂₀ // \n. . .\|. 𓀐𓂸Ｙ. . ࿕. . . / \n. . . .|. \. . ᯪ. . .|. . ᯪ. . ﾉ \n. . . . . \ .トー仝ーイ \n. . . . . . . |. ミ土彡 / \n. . . . . . . )\. . .° . ./( \n. . . . . . /. . .\͎̦ ̷̫ ̴́ ̴̢/̴͖. . \ \n. . . . . /. ⁶⁹ . /̴͝Ѽ̔̕☰̴̈́☰☰☰☰D,̰̱ \n. . . . /. / . . / . . .\. \. . \ \n. . . .((. . . .(. . . . .). . . .)) \n. . . .| . . . .). . . . .(|. . . / \n. . . . |. . . /. . . . /. . . ./ \n. . . . |. . ..| . . . ./. . ./. . ... . . 𓁉𓀏𓀃𓁏`"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await edit_or_reply(event, mentions)
   

@bot.on(admin_cmd(pattern="ohh$", outgoing=True))
@bot.on(sudo_cmd(pattern="ohh$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`´´´´´████████´´\n´´`´███▒▒▒▒███´´´´´\n´´´███▒●▒▒●▒██´´´\n´´´███▒▒👄▒▒██´´\n´´█████▒▒████´´´´´\n´█████▒▒▒▒███´´\n█████▒▒▒▒▒▒███´´´´\n´´▓▓▓▓▓▓▓▓▓▓▓▓▓▒´´\n´´▒▒▒▒▓▓▓▓▓▓▓▓▓▒´´´´´\n´.▒▒▒´´▓▓▓▓▓▓▓▓▒´´´´´\n´.▒▒´´´´▓▓▓▓▓▓▓▒\n..▒▒.´´´´▓▓▓▓▓▓▓▒\n´▒▒▒▒▒▒▒▒▒▒▒▒\n´´´´´´´´´███████´´´´\n´´´´´´´´████████´´´´´´\n´´´´´´´█████████´´´´´\n´´´´´´██████████´´´\n´´´´´´██████████´´\n´´´´´´´█████████´\n´´´´´´´█████████´\n´´´´´´´´████████´´´\n´´´´´´´´´´´▒▒▒▒▒´´´\n´´´´´´´´´´▒▒▒▒▒´´´\n´´´´´´´´´´▒▒▒▒▒´´´\n´´´´´´´´´´▒▒´▒▒´´´\n´´´´´´´´´▒▒´´▒▒´´´\n´´´´´´´´´´▒▒´´´▒▒´´´\n´´´´´´´´´▒▒´´´▒▒´´´\n´´´´´´´´▒▒´´´´´▒▒´´´\n´´´´´´´´▒▒´´´´´´▒▒´´´\n´´´´´´´´███´´´´███´´´\n´´´´´´´´████´´███´´´\n´´´´´´´´█´´███´´████´´´`"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await edit_or_reply(event, mentions)
  

@bot.on(admin_cmd(pattern="lovestory$", outgoing=True))
@bot.on(sudo_cmd(pattern="lovestory$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 3
    animation_ttl = range(0, 103)
    await edit_or_reply(event, "Starting asf")
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
        "The End 😂...",
    ]

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 103])


@bot.on(admin_cmd(pattern="bf$", outgoing=True))
@bot.on(sudo_cmd(pattern="bf$", allow_sudo=True))
async def pressf(f):
    if f.fwd_from:
        return
    """Pays respects"""
    args = f.text.split()
    arg = (f.text.split(" ", 1))[1] if len(args) > 1 else None
    if len(args) == 1:
        r = random.randint(0, 3)
        LOGS.info(r)
        if r == 0:
            await edit_or_reply(f, "┏━━━┓\n┃┏━━┛\n┃┗━━┓\n┃┏━━┛\n┃┃\n┗┛")
        elif r == 1:
            await edit_or_reply(f, "╭━━━╮\n┃╭━━╯\n┃╰━━╮\n┃╭━━╯\n┃┃\n╰╯")
        else:
            arg = "F"
    if arg is not None:
        out = ""
        F_LENGTHS = [5, 1, 1, 4, 1, 1, 1]
        for line in F_LENGTHS:
            c = max(round(line / len(arg)), 1)
            out += (arg * c) + "\n"
        await edit_or_reply(f"`" + out + "`")


@bot.on(admin_cmd(pattern="session$", outgoing=True))
@bot.on(sudo_cmd(pattern="session$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    mentions = "**telethon.errors.rpcerrorlist.AuthKeyDuplicatedError: The authorization key (session file) was used under two different IP addresses simultaneously, and can no longer be used. Use the same session exclusively, or use different sessions (caused by GetMessagesRequest)**"
    await edit_or_reply(event, mentions)


CmdHelp("fun2").add_command(
  "join", None, "Use and see"
).add_command(
  "bf", None, "Use and see"
).add_command(
  "push", None, "Use and see"
).add_command(
  "lovestory", None, "Use and see"
).add_command(
  "session", None, "Use and see"
).add_command(
  "ohh", None, "Use and see"
).add_command(
  "suckit", None, "Use and see"
).add_command(
  "work", None, "Use and see"
).add_command(
  "aag", None, "Use and see"
).add_command(
  "climb", None, "Use and see"
).add_command(
  "pay", None, "Use and see"
).add()
