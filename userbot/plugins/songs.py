
# Port to UserBot
# modified by @hellboi_atul
# extra mod by @kraken_the_badass
# Copyright (C) 2020.

from telethon import events
import asyncio
#from userbot.utils import admin_cmd
from userbot.events import register 
from userbot import bot, CMD_HELP
from telethon.errors.rpcerrorlist import YouBlockedUserError
import os
try:
 import subprocess
except:
 os.system("pip install instantmusic")
 


os.system("rm -rf *.mp3")


def bruh(name):
    
    os.system("instantmusic -q -s "+name)
    


@register(outgoing=True, pattern="^.song(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@SpotifyMusicDownloaderBot"
    await event.edit("```🎶Getting Your Music🎶```")
    async with bot.conversation(chat) as conv:
          await asyncio.sleep(2)
          await event.edit("`🎵Downloading music taking some times,  Stay Tuned.....🔥😉`")
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=752979930))
              await bot.send_message(chat, link)
              respond = await response
          except YouBlockedUserError:
              await event.reply("```😐Please unblock @SpotifyMusicDownloaderBot and try again```")
              return
          await event.delete()
          await bot.forward_messages(event.chat_id, respond.message)

@register(outgoing=True, pattern="^.getsong(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@MissAlexaRobot"
    await event.edit("```🎶Getting Your Music🎶```")
    async with bot.conversation(chat) as conv:
          await asyncio.sleep(2)
          await event.edit("`🎵Downloading music taking some times,  Stay Tuned.....🔥😉`")
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1361631434))
              await bot.send_message(chat, link)
              respond = await response
          except YouBlockedUserError:
              await event.reply("```😐Please unblock @MissAlexaRobot and try again```")
              return
          await event.delete()
          await bot.forward_messages(event.chat_id, respond.message)



@register(outgoing=True, pattern="^.dwlsong(?: |$)(.*)")
async def DeezLoader(Deezlod):
    if Deezlod.fwd_from:
        return
    d_link = Deezlod.pattern_match.group(1)
    if ".com" not in d_link:
        await Deezlod.edit("` I need a link to download something pro.`**(._.)**")
    else:
        await Deezlod.edit("**Initiating Download!**")
    chat = "@DeezLoadBot"
    async with bot.conversation(chat) as conv:
          try:
              msg_start = await conv.send_message("/start")
              response = await conv.get_response()
              r = await conv.get_response()
              msg = await conv.send_message(d_link)
              details = await conv.get_response()
              song = await conv.get_response()
              """ - don't spam notif - """
              await bot.send_read_acknowledge(conv.chat_id)
          except YouBlockedUserError:
              await Deezlod.edit("**Error:** `unblock` @DeezLoadBot `and retry!`")
              return
          await bot.send_file(Deezlod.chat_id, song, caption=details.text)
          await Deezlod.client.delete_messages(conv.chat_id,
                                             [msg_start.id, response.id, r.id, msg.id, details.id, song.id])
          await Deezlod.delete()          
    
CMD_HELP.update({
        "music":
        ".song`<Artist - Song Title>\
            \nUsage:For searching songs from Spotify.\
            \n\n`.getsong` <Artist - Song Title>\
            \nUsage:Download music with @MissAlexaRobot\
            \n\n`.dwlsong` <Spotify/Deezer Link>\
            \nUsage:Download music from Spotify or Deezer.\
            \n\n`.deezload` <spotify/deezer link> <Format>\
            \nUsage: Download music from deezer.\
            \n\n Well deezer is not available in India so create an deezer account using vpn. Set DEEZER_ARL_TOKEN in vars to make this work.\
            \n\n *Format= `FLAC`, `MP3_320`, `MP3_256`, `MP3_128`.\
            \n\n\n Guide:Video guide of arl token: [here](https://www.youtube.com/watch?v=O6PRT47_yds&feature=youtu.be) or Read [This](https://notabug.org/RemixDevs/DeezloaderRemix/wiki/Login+via+userToken)."
})


