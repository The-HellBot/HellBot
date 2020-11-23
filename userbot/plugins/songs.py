#Originally made by @rkpavi for @javes05
#porting to hellbot by @kraken_the_badass...
#first userbot to port javes song module...
#keep credit if u wanna kang...
#else u are a gay...no doubt in that....


from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.utils import admin_cmd
import asyncio

 

@borg.on(admin_cmd(pattern="gaana ?(.*)"))
async def FindMusicPleaseBot(gaana):

    song = gaana.pattern_match.group(1)

    chat = "@FindMusicPleaseBot"

    if not song:

        return await gaana.edit("```what should i search```")

    await gaana.edit("```Getting Your Music```")

    await asyncio.sleep(2)

    async with bot.conversation(chat) as conv:

        await gaana.edit("`Downloading...Please wait`")

        try:

            msg = await conv.send_message(song)

            response = await conv.get_response()

            if response.text.startswith("Sorry"):

                await bot.send_read_acknowledge(conv.chat_id)

                return await gaana.edit(f"Sorry, can't find {song}")

            respond = await conv.get_response()

            cobra = await conv.get_response()

        except YouBlockedUserError:

            await gaana.edit("```Please unblock``` @FindmusicpleaseBot``` and try again```")

            return

        await gaana.edit("`Sending Your Music...wait!!! 😉😎`")

        await bot.send_file(gaana.chat_id, cobra)

        await bot.send_read_acknowledge(conv.chat_id)

    await gaana.delete()
    
    
#-------------------------------------------------------------------------------

    
from pathlib import Path
import asyncio, time, io, math, os, logging, asyncio, shutil, re, subprocess, json
from re import findall
from asyncio import sleep
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from datetime import datetime as dt
from pytz import country_names as c_n, country_timezones as c_tz, timezone as tz
from hachoir.parser import createParser
import pybase64
from base64 import b64decode
from pySmartDL import SmartDL
from telethon.tl.types import DocumentAttributeVideo, DocumentAttributeAudio
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from validators.url import url
from html import unescape
from urllib.error import HTTPError
from userbot.utils import admin_cmd, edit_or_reply, progress, humanbytes, time_formatter
from userbot import CMD_HELP
import bs4
from bs4 import BeautifulSoup
from youtube_dl import YoutubeDL

from youtube_dl.utils import (DownloadError, ContentTooShortError,

                              ExtractorError, GeoRestrictedError,
                              MaxDownloadsReached, PostProcessingError,
                              UnavailableVideoError, XAttrMetadataError)

try:

   from youtubesearchpython import SearchVideos 

except:
	os.system("pip install pip install youtube-search-python")
	from youtubesearchpython import SearchVideos 
	pass


@borg.on(admin_cmd(pattern="song(?: |$)(.*)"))
async def download_video(v_url):  

    lazy = v_url ; sender = await lazy.get_sender() ; me = await lazy.client.get_me()

    if not sender.id == me.id:
        rkp = await lazy.reply("`processing...`")
    else:
    	rkp = await lazy.edit("`processing...`")   
    url = v_url.pattern_match.group(1)
    if not url:
         return await rkp.edit("`Error \nusage song <song name>`")
    search = SearchVideos(url, offset = 1, mode = "json", max_results = 1)
    test = search.result()
    p = json.loads(test)
    q = p.get('search_result')
    try:
       url = q[0]['link']
    except:
    	return await rkp.edit("`failed to find`")
    type = "audio"
    await rkp.edit("`Preparing to download...`")
    if type == "audio":
        opts = {
            'format':
            'bestaudio',
            'addmetadata':
            True,
            'key':
            'FFmpegMetadata',
            'writethumbnail':
            True,
            'prefer_ffmpeg':
            True,
            'geo_bypass':
            True,
            'nocheckcertificate':
            True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
            'outtmpl':
            '%(id)s.mp3',
            'quiet':
            True,
            'logtostderr':
            False
        }
        video = False
        song = True    
    try:
        await rkp.edit("`Fetching data, please wait..`")
        with YoutubeDL(opts) as rip:
            rip_data = rip.extract_info(url)
    except DownloadError as DE:
        await rkp.edit(f"`{str(DE)}`")
        return
    except ContentTooShortError:
        await rkp.edit("`The download content was too short.`")
        return
    except GeoRestrictedError:
        await rkp.edit(
            "`Video is not available from your geographic location due to geographic restrictions imposed by a website.`"
        )
        return
    except MaxDownloadsReached:
        await rkp.edit("`Max-downloads limit has been reached.`")
        return
    except PostProcessingError:
        await rkp.edit("`There was an error during post processing.`")
        return
    except UnavailableVideoError:
        await rkp.edit("`Media is not available in the requested format.`")
        return
    except XAttrMetadataError as XAME:
        await rkp.edit(f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
        return
    except ExtractorError:
        await rkp.edit("`There was an error during info extraction.`")
        return
    except Exception as e:
        await rkp.edit(f"{str(type(e)): {str(e)}}")
        return
    c_time = time.time()
    if song:
        await rkp.edit(f"`Preparing to upload song:`\
        \n**{rip_data['title']}**\
        \nby *{rip_data['uploader']}*")
        await v_url.client.send_file(
            v_url.chat_id,
            f"{rip_data['id']}.mp3",
            supports_streaming=True,
            attributes=[
                DocumentAttributeAudio(duration=int(rip_data['duration']),
                                       title=str(rip_data['title']),
                                       performer=str(rip_data['uploader']))
            ],
            progress_callback=lambda d, t: asyncio.get_event_loop(
            ).create_task(
                progress(d, t, v_url, c_time, "Uploading..",
                         f"{rip_data['title']}.mp3")))
        os.remove(f"{rip_data['id']}.mp3")
        await v_url.delete()
    elif video:
        await rkp.edit(f"`Preparing to upload song :`\
        \n**{rip_data['title']}**\
        \nby *{rip_data['uploader']}*")
        await v_url.client.send_file(
            v_url.chat_id,
            f"{rip_data['id']}.mp4",
            supports_streaming=True,
            caption=url,
            progress_callback=lambda d, t: asyncio.get_event_loop(
            ).create_task(
                progress(d, t, v_url, c_time, "Uploading..",
                         f"{rip_data['title']}.mp4")))
        os.remove(f"{rip_data['id']}.mp4")
        await rkp.delete()
        
        
        
@borg.on(admin_cmd(pattern="vsong(?: |$)(.*)"))
async def download_video(v_url):  
    lazy = v_url ; sender = await lazy.get_sender() ; me = await lazy.client.get_me()
    if not sender.id == me.id:
        rkp = await lazy.reply("`processing...`")
    else:
    	rkp = await lazy.edit("`processing...`")   
    url = v_url.pattern_match.group(1)
    if not url:
         return await rkp.edit("`Error \nusage song <song name>`")
    search = SearchVideos(url, offset = 1, mode = "json", max_results = 1)
    test = search.result()
    p = json.loads(test)
    q = p.get('search_result')
    try:
       url = q[0]['link']
    except:
    	return await rkp.edit("`failed to find`")
    type = "audio"
    await rkp.edit("`Preparing to download...`")
    if type == "audio":
        opts = {
            'format':
            'best',
            'addmetadata':
            True,
            'key':
            'FFmpegMetadata',
            'prefer_ffmpeg':
            True,
            'geo_bypass':
            True,
            'nocheckcertificate':
            True,
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4'
            }],
            'outtmpl':
            '%(id)s.mp4',
            'logtostderr':
            False,
            'quiet':
            True
        }
        song = False
        video = True
    try:
        await rkp.edit("`Fetching data, please wait..`")
        with YoutubeDL(opts) as rip:
            rip_data = rip.extract_info(url)
    except DownloadError as DE:
        await rkp.edit(f"`{str(DE)}`")
        return
    except ContentTooShortError:
        await rkp.edit("`The download content was too short.`")
        return
    except GeoRestrictedError:
        await rkp.edit(
            "`Video is not available from your geographic location due to geographic restrictions imposed by a website.`"
        )
        return
    except MaxDownloadsReached:
        await rkp.edit("`Max-downloads limit has been reached.`")
        return
    except PostProcessingError:
        await rkp.edit("`There was an error during post processing.`")
        return
    except UnavailableVideoError:
        await rkp.edit("`Media is not available in the requested format.`")
        return
    except XAttrMetadataError as XAME:
        await rkp.edit(f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
        return
    except ExtractorError:
        await rkp.edit("`There was an error during info extraction.`")
        return
    except Exception as e:
        await rkp.edit(f"{str(type(e)): {str(e)}}")
        return
    c_time = time.time()
    if song:
        await rkp.edit(f"`Preparing to upload song `\
        \n**{rip_data['title']}**\
        \nby *{rip_data['uploader']}*")
        await v_url.client.send_file(
            v_url.chat_id,
            f"{rip_data['id']}.mp3",
            supports_streaming=True,
            attributes=[
                DocumentAttributeAudio(duration=int(rip_data['duration']),
                                       title=str(rip_data['title']),
                                       performer=str(rip_data['uploader']))
            ],
            progress_callback=lambda d, t: asyncio.get_event_loop(
            ).create_task(
                progress(d, t, v_url, c_time, "Uploading..",
                         f"{rip_data['title']}.mp3")))
        os.remove(f"{rip_data['id']}.mp3")
        await v_url.delete()
    elif video:
        await rkp.edit(f"`Preparing to upload video song :`\
        \n**{rip_data['title']}**\
        \nby *{rip_data['uploader']}*")
        await v_url.client.send_file(
            v_url.chat_id,
            f"{rip_data['id']}.mp4",
            supports_streaming=True,
            caption=rip_data['title'],
            progress_callback=lambda d, t: asyncio.get_event_loop(
            ).create_task(
                progress(d, t, v_url, c_time, "Uploading..",
                         f"{rip_data['title']}.mp4")))
        os.remove(f"{rip_data['id']}.mp4")
        await rkp.delete()

#-------------------------------------------------------------------------------

from telethon import events
import asyncio
from userbot.events import register 
from userbot import bot, CMD_HELP
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors.rpcerrorlist import YouBlockedUserError
import os

try:
 import subprocess
except:
 os.system("pip install instantmusic")



os.system("rm -rf *.mp3")


def bruh(name):

    os.system("instantmusic -q -s "+name)

@register(outgoing=True, pattern="^.getsong(?: |$)(.*)")
async def getmusic(so):
    if so.fwd_from:
        return
    await so.client(JoinChannelRequest("t.me/anitimeofficial"))
    song = so.pattern_match.group(1)
    chat = "@SongsForYouBot"
    link = f"/song {song}"
    await so.edit("🔹Ok wait... 📡Searching your song🔸")
    async with bot.conversation(chat) as conv:
          await asyncio.sleep(2)
          await so.edit("📥Downloading...Please wait🤙")
          try:
              msg = await conv.send_message(link)
              response = await conv.get_response()
              respond = await conv.get_response()
              """ - don't spam notif - """
              await bot.send_read_acknowledge(conv.chat_id)
          except YouBlockedUserError:
              await so.edit("Please unblock @SongsForYouBot and try searching again🤐")
              return
          await so.edit("Ohh.. I got something!! Wait sending😋🤙")
          await asyncio.sleep(3)
          await bot.send_file(so.chat_id, respond)
    await so.client.delete_messages(conv.chat_id,
                                       [msg.id, response.id, respond.id])
    await so.delete()

#-------------------------------------------------------------------------------

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
          
#-------------------------------------------------------------------------------
       
import datetime
import asyncio
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError, UserAlreadyParticipantError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from userbot.utils import admin_cmd

@borg.on(admin_cmd("sdd ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    d_link = event.pattern_match.group(1)
    if ".com" not in d_link:
        await event.edit("` I need a link to download something pro.`**(._.)**")
    else:
        await event.edit("🎶**Initiating Download!**🎶")
    bot = "@DeezLoadBot"
    
    async with borg.conversation("@DeezLoadBot") as conv:
          try:
              await conv.send_message("/start")
              response = await conv.get_response()
              try:
                  await borg(ImportChatInviteRequest('AAAAAFZPuYvdW1A8mrT8Pg'))
              except UserAlreadyParticipantError:
                  await asyncio.sleep(0.00000069420)
              await conv.send_message(d_link)
              details = await conv.get_response()
              await borg.send_message(event.chat_id, details)
              await conv.get_response()
              songh = await conv.get_response()
              await borg.send_file(event.chat_id, songh, caption="🔆**Here's the requested song!**🔆\n`Check out` [HellBot](https://t.me/HellBot_Official)")
              await event.delete()
          except YouBlockedUserError:
              await event.edit("**Error:** `unblock` @DeezLoadBot `and retry!`")
    
    
CMD_HELP.update({
        "songs":
        "`.song song name`\
            \nUsage:For searching songs from youtube\
            \n\n`.getsong` Song Title\
            \nUsage:Download song from @SongsForYouBot\
            \n\n`.gaana` Song name\
            \nUsage:Download song from @FindmusicpleaseBot\
            \n\n`.vsong` Song title\
            \nUsage:Downloads video song from youtube\
            \n\n`.sdd` song name\
            \nUsage:Download song from @DeezLoadBot\
            \n\n`.dwlsong` <Spotify/Deezer Link>\
            \nUsage:Download music from Spotify or Deezer."
})