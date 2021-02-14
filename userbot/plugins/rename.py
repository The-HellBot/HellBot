"""Rename Telegram Files
Syntax:
.rename file.name
.rnupload file.name
.rnstreamupload file.name
By @Ck_ATR"""
import os
import subprocess
import time
from datetime import datetime

from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from telethon.tl.types import DocumentAttributeVideo

from hellbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp

thumb_image_path = Config.TMP_DOWNLOAD_DIRECTORY + "/thumb_image.jpg"


def get_video_thumb(file, output=None, width=90):
    metadata = extractMetadata(createParser(file))
    p = subprocess.Popen(
        [
            "ffmpeg",
            "-i",
            file,
            "-ss",
            str(
                int((0, metadata.get("duration").seconds)[metadata.has("duration")] / 2)
            ),
            "-filter:v",
            "scale={}:-1".format(width),
            "-vframes",
            "1",
            output,
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    )
    if not p.returncode and os.path.lexists(file):
        return output


@bot.on(admin_cmd(pattern="rename (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="rename (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    await edit_or_reply(event, 
        "Renaming in process 🙄🙇‍♂️🙇‍♂️🙇‍♀️ It might take some time if file size is big"
    )
    input_str = event.pattern_match.group(1)
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if event.reply_to_msg_id:
        start = datetime.now()
        file_name = input_str
        reply_message = await event.get_reply_message()
        # c_time = time.time()
        to_download_directory = Config.TMP_DOWNLOAD_DIRECTORY
        downloaded_file_name = os.path.join(to_download_directory, file_name)
        downloaded_file_name = await borg.download_media(
            reply_message, downloaded_file_name
        )
        end = datetime.now()
        ms = (end - start).seconds
        if os.path.exists(downloaded_file_name):
            await edit_or_reply(event, 
                "Downloaded to `{}` in {} seconds.".format(downloaded_file_name, ms)
            )
        else:
            await edit_or_reply(event, "Error Occurred\n {}".format(input_str))
    else:
        await edit_or_reply(event, "Syntax // `.rename file.name` as reply to a Telegram media")


@bot.on(admin_cmd(pattern="rnupload (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="rnupload (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    thumb = None
    if os.path.exists(thumb_image_path):
        thumb = thumb_image_path
    await edit_or_reply(event, 
        "Rename & Upload in process 🙄🙇‍♂️🙇‍♂️🙇‍♀️ It might take some time if file size is big"
    )
    input_str = event.pattern_match.group(1)
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if event.reply_to_msg_id:
        start = datetime.now()
        file_name = input_str
        reply_message = await event.get_reply_message()
        to_download_directory = Config.TMP_DOWNLOAD_DIRECTORY
        downloaded_file_name = os.path.join(to_download_directory, file_name)
        downloaded_file_name = await borg.download_media(
            reply_message, downloaded_file_name
        )
        end = datetime.now()
        ms_one = (end - start).seconds
        if os.path.exists(downloaded_file_name):
            time.time()
            await borg.send_file(
                event.chat_id,
                downloaded_file_name,
                force_document=False,
                supports_streaming=False,
                allow_cache=False,
                reply_to=event.message.id,
                thumb=thumb,
            )
            end_two = datetime.now()
            os.remove(downloaded_file_name)
            ms_two = (end_two - end).seconds
            await edit_or_reply(event, 
                "Downloaded in {} seconds. Uploaded in {} seconds.".format(
                    ms_one, ms_two
                )
            )
        else:
            await edit_or_reply(event, "File Not Found {}".format(input_str))
    else:
        await edit_or_reply(event, "Syntax // .rnupload file.name as reply to a Telegram media")


@bot.on(admin_cmd(pattern="rnsupload (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="rnsupload (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    await edit_or_reply(event, 
        "Rename & Upload as Streamable in process 🙄🙇‍♂️🙇‍♂️🙇‍♀️ It might take some time if file size is big"
    )
    input_str = event.pattern_match.group(1)
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if event.reply_to_msg_id:
        start = datetime.now()
        file_name = input_str
        reply_message = await event.get_reply_message()
        time.time()
        to_download_directory = Config.TMP_DOWNLOAD_DIRECTORY
        downloaded_file_name = os.path.join(to_download_directory, file_name)
        downloaded_file_name = await borg.download_media(
            reply_message, downloaded_file_name
        )
        end_one = datetime.now()
        ms_one = (end_one - start).seconds
        if os.path.exists(downloaded_file_name):
            thumb = None
            if not downloaded_file_name.endswith((".mkv", ".mp4", ".mp3", ".flac")):
                await edit_or_reply(event, 
                    "Sorry. But I don't think {} is a streamable file. Please try again.\n**Supported Formats**: MKV, MP4, MP3, FLAC".format(
                        downloaded_file_name
                    )
                )
                return False
            if os.path.exists(thumb_image_path):
                thumb = thumb_image_path
            else:
                thumb = get_video_thumb(downloaded_file_name, thumb_image_path)
            start = datetime.now()
            metadata = extractMetadata(createParser(downloaded_file_name))
            duration = 0
            width = 0
            height = 0
            if metadata.has("duration"):
                duration = metadata.get("duration").seconds
            if os.path.exists(thumb_image_path):
                metadata = extractMetadata(createParser(thumb_image_path))
                if metadata.has("width"):
                    width = metadata.get("width")
                if metadata.has("height"):
                    height = metadata.get("height")
            # Telegram only works with MP4 files
            # this is good, since with MKV files sent as streamable Telegram responds,
            # Bad Request: VIDEO_CONTENT_TYPE_INVALID
            # c_time = time.time()
            try:
                await borg.send_file(
                    event.chat_id,
                    downloaded_file_name,
                    thumb=thumb,
                    caption="reuploaded by [HellBot](https://t.me/hellbot_official_chat)",
                    force_document=False,
                    allow_cache=False,
                    reply_to=event.message.id,
                    attributes=[
                        DocumentAttributeVideo(
                            duration=duration,
                            w=width,
                            h=height,
                            round_message=False,
                            supports_streaming=True,
                        )
                    ],
                )
            except Exception as e:
                await edit_or_reply(event, str(e))
            else:
                end = datetime.now()
                os.remove(downloaded_file_name)
                ms_two = (end - end_one).seconds
                await edit_or_reply(event, 
                    "Downloaded in {} seconds. Uploaded in {} seconds.".format(
                        ms_one, ms_two
                    )
                )
        else:
            await edit_or_reply(event, "File Not Found {}".format(input_str))
    else:
        await edit_or_reply(event, 
            "Syntax // .rnsupload file.name as reply to a Telegram media"
        )

CmdHelp("rename").add_command(
  "rename", "<reply to media> <new name>", "Renames the replied media and downloads it to userbot local storage"
).add_command(
  "rnupload", "<reply to media> <new name>", "Renames the replied media and directly uploads it to the chat"
).add_command(
  "rnsupload", "<reply to media> <new name>", "Renames the replied media and directly upload in streamable format."
).add()