import json
import os
import subprocess

import requests
from hellbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp


@bot.on(admin_cmd(pattern="labstack ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="labstack ?(.*)", allow_sudo=True))
async def labstack(event):
    if event.fwd_from:
        return
    await event.edit("Processing...")
    input_str = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    if input_str:
        filebase = input_str
    elif reply:
        filebase = await event.client.download_media(
            reply.media, Var.TEMP_DOWNLOAD_DIRECTORY
        )
    else:
        await edit_or_reply(event, "Reply to a media file or provide a directory to upload the file to labstack"
        )
        return
    filesize = os.path.getsize(filebase)
    filename = os.path.basename(filebase)
    headers2 = {"Up-User-ID": "IZfFbjUcgoo3Ao3m"}
    files2 = {
        "ttl": 604800,
        "files": [{"name": filename, "type": "", "size": filesize}],
    }
    r2 = requests.post(
        "https://up.labstack.com/api/v1/links", json=files2, headers=headers2
    )
    r2json = json.loads(r2.text)

    url = "https://up.labstack.com/api/v1/links/{}/send".format(r2json["code"])
    max_days = 7
    command_to_exec = [
        "curl",
        "-F",
        "files=@" + filebase,
        "-H",
        "Transfer-Encoding: chunked",
        "-H",
        "Up-User-ID: IZfFbjUcgoo3Ao3m",
        url,
    ]
    try:
        logger.info(command_to_exec)
        t_response = subprocess.check_output(command_to_exec, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as exc:
        logger.info("Status : FAIL", exc.returncode, exc.output)
        await edit_or_reply(event, exc.output.decode("UTF-8"))
        return
    else:
        logger.info(t_response)
        t_response_arry = "https://up.labstack.com/api/v1/links/{}/receive".format(
            r2json["code"]
        )
    await edit_or_reply(event, t_response_arry + "\nMax Days:" + str(max_days), link_preview=False
    )

CmdHelp("labstack").add_command(
  "labstack", "<reply to media>", "Makes a direct download link of the replied media for a limited time"
).add()