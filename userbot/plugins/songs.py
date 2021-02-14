# Originally made by @rkpavi for @javes05
# porting to hellbot by @kraken_the_badass...
# first userbot to port javes song module...
# keep credit if u wanna kang...
# else u are a gay...no doubt in that....


import asyncio
import re
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import bot
from hellbot.utils import admin_cmd, sudo_cmd, edit_or_reply, progress
from userbot.cmdhelp import CmdHelp
from userbot.helpers.functions import deEmojify

@bot.on(admin_cmd(pattern="lyrics(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="lyrics(?: |$)(.*)", allow_sudo=True))
async def nope(kraken):
    hell = kraken.pattern_match.group(1)
    if not hell:
        if kraken.is_reply:
            (await kraken.get_reply_message()).message
        else:
            await kraken.edit(
                "`Sir please give some query to search and download it for you..!`"
            )
            return

    troll = await bot.inline_query("iLyricsBot", f"{(deEmojify(hell))}")

    await troll[0].click(
        kraken.chat_id,
        reply_to=kraken.reply_to_msg_id,
        silent=True if kraken.is_reply else False,
        hide_via=True,
    )

    await kraken.delete()

#>>>>>>>>>>>>>>>>>>✓✓✓✓✓<<<<<<<<<<<<<<<<<<<

@bot.on(admin_cmd(pattern="gaana ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="gaana ?(.*)", allow_sudo=True))
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

            await conv.send_message(song)

            response = await conv.get_response()

            if response.text.startswith("Sorry"):

                await bot.send_read_acknowledge(conv.chat_id)

                return await gaana.edit(f"Sorry, can't find {song}")

            await conv.get_response()

            lavde = await conv.get_response()

        except YouBlockedUserError:

            await gaana.edit(
                "```Please unblock``` @FindmusicpleaseBot``` and try again```"
            )

            return

        await gaana.edit("`Sending Your Music...wait!!! 😉😎`")

        await bot.send_file(gaana.chat_id, lavde)

        await bot.send_read_acknowledge(conv.chat_id)

    await gaana.delete()


# -------------------------------------------------------------------------------


import json
import os
import time

from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import DocumentAttributeAudio
from youtube_dl import YoutubeDL
from youtube_dl.utils import (
    ContentTooShortError,
    DownloadError,
    ExtractorError,
    GeoRestrictedError,
    MaxDownloadsReached,
    PostProcessingError,
    UnavailableVideoError,
    XAttrMetadataError,
)

try:

    from youtubesearchpython import SearchVideos

except:
    os.system("pip install pip install youtube-search-python")
    from youtubesearchpython import SearchVideos


@bot.on(admin_cmd(pattern="song(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="song(?: |$)(.*)", allow_sudo=True))
async def download_video(v_url):

    lazy = v_url
    sender = await lazy.get_sender()
    me = await lazy.client.get_me()

    if not sender.id == me.id:
        rkp = await edit_or_reply(lazy, "`Wait. Processing your request....`")
    else:
        rkp = await edit_or_reply(lazy, "`Wait. Processing your request....`")
    url = v_url.pattern_match.group(1)
    if not url:
        return await rkp.edit("**Error** \n__Usage:__ `song <song name>`")
    search = SearchVideos(url, offset=1, mode="json", max_results=1)
    test = search.result()
    p = json.loads(test)
    q = p.get("search_result")
    try:
        url = q[0]["link"]
    except:
        return await rkp.edit("`Failed to process your request....`")
    type = "audio"
    await rkp.edit("Request processed. **Downloading Now!!!**")
    if type == "audio":
        opts = {
            "format": "bestaudio",
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "writethumbnail": True,
            "prefer_ffmpeg": True,
            "geo_bypass": True,
            "nocheckcertificate": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "320",
                }
            ],
            "outtmpl": "%(id)s.mp3",
            "quiet": True,
            "logtostderr": False,
        }
        video = False
        song = True
    try:
        await rkp.edit("**Fetching Song**")
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
        await rkp.edit(
            f"🎶 Preparing to upload song 🎶 :-\
        \n\n**{rip_data['title']}**\
        \nby __{rip_data['uploader']}__"
        )
        await v_url.client.send_file(
            v_url.chat_id,
            f"{rip_data['id']}.mp3",
            supports_streaming=True,
            attributes=[
                DocumentAttributeAudio(
                    duration=int(rip_data["duration"]),
                    title=str(rip_data["title"]),
                    performer=str(rip_data["uploader"]),
                )
            ],
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(d, t, v_url, c_time, "Uploading..", f"{rip_data['title']}.mp3")
            ),
        )
        os.remove(f"{rip_data['id']}.mp3")
        await v_url.delete()
    elif video:
        await rkp.edit(
            f"🎶 Preparing to upload song 🎶 :-\
        \n\n**{rip_data['title']}**\
        \nby __{rip_data['uploader']}__"
        )
        await v_url.client.send_file(
            v_url.chat_id,
            f"{rip_data['id']}.mp4",
            supports_streaming=True,
            caption=url,
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(d, t, v_url, c_time, "Uploading..", f"{rip_data['title']}.mp4")
            ),
        )
        os.remove(f"{rip_data['id']}.mp4")
        await rkp.delete()


@bot.on(admin_cmd(pattern="vsong(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="vsong(?: |$)(.*)", allow_sudo=True))
async def download_video(v_url):
    lazy = v_url
    sender = await lazy.get_sender()
    me = await lazy.client.get_me()
    if not sender.id == me.id:
        rkp = await edit_or_reply(lazy, "Processing video song request....")
    else:
        rkp = await edit_or_reply(lazy, "Processing video song request....")
    url = v_url.pattern_match.group(1)
    if not url:
        return await rkp.edit("**Error** \n__Usage:__ `vsong <song name>`")
    search = SearchVideos(url, offset=1, mode="json", max_results=1)
    test = search.result()
    p = json.loads(test)
    q = p.get("search_result")
    try:
        url = q[0]["link"]
    except:
        return await rkp.edit("`failed to find`")
    type = "audio"
    await rkp.edit("Video Song Request Processed. **Downloading Now!!**")
    if type == "audio":
        opts = {
            "format": "best",
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "prefer_ffmpeg": True,
            "geo_bypass": True,
            "nocheckcertificate": True,
            "postprocessors": [
                {"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}
            ],
            "outtmpl": "%(id)s.mp4",
            "logtostderr": False,
            "quiet": True,
        }
        song = False
        video = True
    try:
        await rkp.edit("Fetching Video Song")
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
        await rkp.edit(
            f"🎶 Preparing to upload video song 🎶 :-\
        \n\n**{rip_data['title']}**\
        \nby __{rip_data['uploader']}__"
        )
        await v_url.client.send_file(
            v_url.chat_id,
            f"{rip_data['id']}.mp3",
            supports_streaming=True,
            attributes=[
                DocumentAttributeAudio(
                    duration=int(rip_data["duration"]),
                    title=str(rip_data["title"]),
                    performer=str(rip_data["uploader"]),
                )
            ],
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(d, t, v_url, c_time, "Uploading..", f"{rip_data['title']}.mp3")
            ),
        )
        os.remove(f"{rip_data['id']}.mp3")
        await v_url.delete()
    elif video:
        await rkp.edit(
            f"🎶 Preparing to upload video song 🎶 :-\
        \n\n**{rip_data['title']}**\
        \nby __{rip_data['uploader']}__"
        )
        await v_url.client.send_file(
            v_url.chat_id,
            f"{rip_data['id']}.mp4",
            supports_streaming=True,
            caption=rip_data["title"],
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(d, t, v_url, c_time, "Uploading..", f"{rip_data['title']}.mp4")
            ),
        )
        os.remove(f"{rip_data['id']}.mp4")
        await rkp.delete()


# -------------------------------------------------------------------------------
import os
from telethon.tl.functions.channels import JoinChannelRequest

try:
    pass
except:
    os.system("pip install instantmusic")


os.system("rm -rf *.mp3")


def bruh(name):

    os.system("instantmusic -q -s " + name)



@bot.on(admin_cmd(pattern="getsong(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="getsong(?: |$)(.*)", allow_sudo=True))
async def getmusic(so):
    if so.fwd_from:
        return
    await so.client(JoinChannelRequest("t.me/anitimeofficial"))
    song = so.pattern_match.group(1)
    chat = "@SongsForYouBot"
    link = f"/song {song}"
    await edit_or_reply(so, "🔹Ok wait... 📡Searching your song🔸")
    async with bot.conversation(chat) as conv:
        await asyncio.sleep(2)
        await edit_or_reply(so, "📥Downloading...Please wait🤙")
        try:
            msg = await conv.send_message(link)
            response = await conv.get_response()
            respond = await conv.get_response()
            """ - don't spam notif - """
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await edit_or_reply(so, "Please unblock @SongsForYouBot and try searching again🤐")
            return
        await edit_or_reply(so, "Ohh.. I got something!! Wait sending😋🤙")
        await asyncio.sleep(3)
        await bot.send_file(so.chat_id, respond)
    await so.client.delete_messages(conv.chat_id, [msg.id, response.id, respond.id])
    await so.delete()


# -------------------------------------------------------------------------------

import asyncio
import os

from telethon.errors.rpcerrorlist import YouBlockedUserError

try:
    pass
except:
    os.system("pip install instantmusic")


os.system("rm -rf *.mp3")


def bruh(name):

    os.system("instantmusic -q -s " + name)


@bot.on(admin_cmd(pattern="dwlsong(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="dwlsong(?: |$)(.*)", allow_sudo=True))
async def DeezLoader(Deezlod):
    if Deezlod.fwd_from:
        return
    d_link = Deezlod.pattern_match.group(1)
    if ".com" not in d_link:
        await edit_or_reply(Deezlod, "` I need a link to download something pro.`**(._.)**")
    else:
        await edit_or_reply(Deezlod, "**Initiating Download!**")
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
            await edit_or_reply(Deezlod, "**Error:** `unblock` @DeezLoadBot `and retry!`")
            return
        await bot.send_file(Deezlod.chat_id, song, caption=details.text)
        await Deezlod.client.delete_messages(
            conv.chat_id, [msg_start.id, response.id, r.id, msg.id, details.id, song.id]
        )
        await Deezlod.delete()


# -------------------------------------------------------------------------------


from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    YouBlockedUserError,
)
from telethon.tl.functions.messages import ImportChatInviteRequest


@bot.on(admin_cmd(pattern="sdd ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="sdd?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    d_link = event.pattern_match.group(1)
    if ".com" not in d_link:
        await event.edit("` I need a link to download something pro.`**(._.)**")
    else:
        await event.edit("🎶**Initiating Download!**🎶")

    async with borg.conversation("@DeezLoadBot") as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            try:
                await borg(ImportChatInviteRequest("AAAAAFZPuYvdW1A8mrT8Pg"))
            except UserAlreadyParticipantError:
                await asyncio.sleep(0.00000069420)
            await conv.send_message(d_link)
            details = await conv.get_response()
            await borg.send_message(event.chat_id, details)
            await conv.get_response()
            songh = await conv.get_response()
            await borg.send_file(
                event.chat_id,
                songh,
                caption="🔆**Here's the requested song!**🔆\n`Check out` [HellBot](https://t.me/HellBot_Official)",
            )
            await event.delete()
        except YouBlockedUserError:
            await event.edit("**Error:** `unblock` @DeezLoadBot `and retry!`")

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
CmdHelp("songs").add_command(
  "song", "<song name>", "Searches the song from youtube and upload in current chat in audio(.mp3) format. •Highest Quality"
).add_command(
  "vsong", "<song name>", "Searches the song from youtube and upload in current chat in video(.mp4) format. •Highest Quality"
).add_command(
  "getsong", "<song name>", "Searches song from a local tg bot @Songsforyoubot and sends the music in current chat"
).add_command(
  "gaana", "<song name>", "Searches song from a local tg bot @FindmusicpleaseBot and sends the music in current chat"
).add_command(
  "sdd", "<song link>", "Downloads the song from given link"
).add_command(
  "dwlsong", "<song link>", "Same as .sdd but downloads from spotify and deezer"
).add_command(
  "lyrics", "<song name>", "Sends the lyrics of given song."
).add()
