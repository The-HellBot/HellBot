# ported from uniborg by @spechide

import asyncio
import os
import time
from datetime import datetime

from hellbot.utils import admin_cmd, sudo_cmd, progress
from userbot import CMD_HELP
from userbot.cmdhelp import CmdHelp

FF_MPEG_DOWN_LOAD_MEDIA_PATH = "./downloads/hellbot.media.ffmpeg"

async def reply_id(event):
    reply_to_id = None
    if event.sender_id in Config.SUDO_USERS:
        reply_to_id = event.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    return reply_to_id

def media_type(message):
    if message and message.photo:
        media = "Photo"
    elif message and message.audio:
        media = "Audio"
    elif message and message.voice:
        media = "Voice"
    elif message and message.video_note:
        media = "Round Video"
    elif message and message.gif:
        media = "Gif"
    elif message and message.sticker:
        media = "Sticker"
    elif message and message.video:
        media = "Video"
    elif message and message.document:
        media = "Document"
    else:
        media = None
    return media
    

@bot.on(admin_cmd(pattern="ffmpegsave$"))
@bot.on(sudo_cmd(pattern="ffmpegsave$", allow_sudo=True))
async def ff_mpeg_trim_cmd(event):
    if event.fwd_from:
        return
    if not os.path.exists(FF_MPEG_DOWN_LOAD_MEDIA_PATH):
        reply_message = await event.get_reply_message()
        if reply_message:
            start = datetime.now()
            media = media_type(reply_message)
            if media not in ["Video", "Audio", "Voice", "Round Video", "Gif"]:
                return await edit_delete(event, "`Only media files are supported`", 5)
            hellevent = await edit_or_reply(event, "`Saving the file...`")
            try:
                c_time = time.time()
                downloaded_file_name = await event.client.download_media(
                    reply_message,
                    FF_MPEG_DOWN_LOAD_MEDIA_PATH,
                    progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                        progress(d, t, hellevent, c_time, "trying to download")
                    ),
                )
            except Exception as e:
                await hellevent.edit(str(e))
            else:
                end = datetime.now()
                ms = (end - start).seconds
                await hellevent.edit(
                    f"Saved file to `{downloaded_file_name}` in `{ms}` seconds."
                )
        else:
            await edit_delete(event, "`Reply to a any media file`")
    else:
        await edit_delete(
            event,
            f"A media file already exists in path. Please remove the media and try again!\n`.ffmpegclear`",
        )


@bot.on(admin_cmd(pattern="vtrim"))
@bot.on(sudo_cmd(pattern="vtrim", allow_sudo=True))
async def ff_mpeg_trim_cmd(event):
    if event.fwd_from:
        return
    if not os.path.exists(FF_MPEG_DOWN_LOAD_MEDIA_PATH):
        await edit_delete(
            event,
            f"a media file needs to be download, and save to the following path: `{FF_MPEG_DOWN_LOAD_MEDIA_PATH}`",
        )
        return
    reply_to_id = await reply_id(event)
    hellevent = await edit_or_reply(event, "`Triming the media......`")
    current_message_text = event.raw_text
    cmt = current_message_text.split(" ")
    start = datetime.now()
    if len(cmt) == 3:
        # output should be video
        cmd, start_time, end_time = cmt
        o = await cult_small_video(
            FF_MPEG_DOWN_LOAD_MEDIA_PATH,
            Config.TMP_DOWNLOAD_DIRECTORY,
            start_time,
            end_time,
        )
        if o is None:
            return await edit_delete(
                hellevent, f"**Error : **`Can't complete the process`"
            )
        try:
            c_time = time.time()
            await event.client.send_file(
                event.chat_id,
                o,
                caption=" ".join(cmt[1:]),
                force_document=False,
                supports_streaming=True,
                allow_cache=False,
                reply_to=reply_to_id,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, hellevent, c_time, "trying to upload")
                ),
            )
            os.remove(o)
        except Exception as e:
            return await edit_delete(hellevent, f"**Error : **`{e}`")
    elif len(cmt) == 2:
        # output should be image
        cmd, start_time = cmt
        o = await take_screen_shot(
            FF_MPEG_DOWN_LOAD_MEDIA_PATH, Config.TMP_DOWNLOAD_DIRECTORY, start_time
        )
        if o is None:
            return await edit_delete(
                hellevent, f"**Error : **`Can't complete the process`"
            )
        try:
            c_time = time.time()
            await event.client.send_file(
                event.chat_id,
                o,
                caption=" ".join(cmt[1:]),
                force_document=True,
                supports_streaming=True,
                allow_cache=False,
                reply_to=event.message.id,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, hellevent, c_time, "trying to upload")
                ),
            )
            os.remove(o)
        except Exception as e:
            return await edit_delete(hellevent, f"**Error : **`{e}`")
    else:
        await edit_delete(hellevent, "RTFM")
        return
    end = datetime.now()
    ms = (end - start).seconds
    await edit_delete(hellevent, f"`Completed Process in {ms} seconds`", 3)


@bot.on(admin_cmd(pattern="atrim"))
@bot.on(sudo_cmd(pattern="atrim", allow_sudo=True))
async def ff_mpeg_trim_cmd(event):
    if event.fwd_from:
        return
    if not os.path.exists(FF_MPEG_DOWN_LOAD_MEDIA_PATH):
        await edit_delete(
            event,
            f"a media file needs to be download, and save to the following path: `{FF_MPEG_DOWN_LOAD_MEDIA_PATH}`",
        )
        return
    reply_to_id = await reply_id(event)
    hellevent = await edit_or_reply(event, "`Triming the media...........`")
    current_message_text = event.raw_text
    cmt = current_message_text.split(" ")
    start = datetime.now()
    out_put_file_name = os.path.join(
        Config.TMP_DOWNLOAD_DIRECTORY, f"{str(round(time.time()))}.mp3"
    )
    if len(cmt) == 3:
        # output should be audio
        cmd, start_time, end_time = cmt
        o = await cult_small_video(
            FF_MPEG_DOWN_LOAD_MEDIA_PATH,
            Config.TMP_DOWNLOAD_DIRECTORY,
            start_time,
            end_time,
            out_put_file_name,
        )
        if o is None:
            return await edit_delete(
                hellevent, f"**Error : **`Can't complete the process`"
            )
        try:
            c_time = time.time()
            await event.client.send_file(
                event.chat_id,
                o,
                caption=" ".join(cmt[1:]),
                force_document=False,
                supports_streaming=True,
                allow_cache=False,
                reply_to=reply_to_id,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, hellevent, c_time, "trying to upload")
                ),
            )
            os.remove(o)
        except Exception as e:
            return await edit_delete(hellevent, f"**Error : **`{e}`")
    else:
        await edit_delete(hellevent, "RTFM")
        return
    end = datetime.now()
    ms = (end - start).seconds
    await edit_delete(hellevent, f"`Completed Process in {ms} seconds`", 3)


@bot.on(admin_cmd(pattern="ffmpegclear$"))
@bot.on(sudo_cmd(pattern="ffmpegclear$", allow_sudo=True))
async def ff_mpeg_trim_cmd(event):
    if event.fwd_from:
        return
    if not os.path.exists(FF_MPEG_DOWN_LOAD_MEDIA_PATH):
        await edit_delete(event, "`There is no media saved in bot for triming`")
    else:
        os.remove(FF_MPEG_DOWN_LOAD_MEDIA_PATH)
        await edit_delete(
            event,
            "`The media saved in bot for triming is deleted now . you can save now new one `",
        )


async def take_screen_shot(video_file, output_directory, ttl):
    # https://stackoverflow.com/a/13891070/4723940
    out_put_file_name = os.path.join(output_directory, f"{str(time.time())}.jpg")
    file_genertor_command = [
        "ffmpeg",
        "-ss",
        str(ttl),
        "-i",
        video_file,
        "-vframes",
        "1",
        out_put_file_name,
    ]
    # width = "90"
    process = await asyncio.create_subprocess_exec(
        *file_genertor_command,
        # stdout must a pipe to be accessible as process.stdout
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    # Wait for the subprocess to finish
    await process.communicate()
    if os.path.lexists(out_put_file_name):
        return out_put_file_name
    return None


# https://github.com/Nekmo/telegram-upload/blob/master/telegram_upload/video.py#L26


async def cult_small_video(
    video_file, output_directory, start_time, end_time, out_put_file_name=None
):
    # https://stackoverflow.com/a/13891070/4723940
    out_put_file_name = out_put_file_name or os.path.join(
        output_directory, f"{str(round(time.time()))}.mp4"
    )
    file_genertor_command = [
        "ffmpeg",
        "-i",
        video_file,
        "-ss",
        start_time,
        "-to",
        end_time,
        "-async",
        "1",
        "-strict",
        "-2",
        out_put_file_name,
    ]
    process = await asyncio.create_subprocess_exec(
        *file_genertor_command,
        # stdout must a pipe to be accessible as process.stdout
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    # Wait for the subprocess to finish
    await process.communicate()
    if os.path.lexists(out_put_file_name):
        return out_put_file_name
    return None

CmdHelp("ff_mpeg").add_command(
  'ffmpegsave', '<reply to a media>', 'Saves the media file in bot to trim mutliple times'
).add_command(
  'vtrim <time>', None, 'Sends you the screenshot of the video at the given specific time'
).add_command(
  'vtrim starttime endtime', None, 'Trims the saved media with specific given time interval and outputs as video'
).add_command(
  'atrim <starttime> <endtime>', None, 'Trims the saved media with specific given time interval and output as audio'
).add_command(
  'ffmpegclear', None, 'Deletes the saved media. So you can save new one🚶'
).add()
