# Made By @Sur_vivor Keep Credits If You Are Goanna Kang This Lol
# And Thanks To The Creator Of Autopic This Script Was Made from Snippets From That Script

import asyncio
import os
import random
import re
import urllib

import requests
from telethon.tl import functions
from hellbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp


AUTOPFP_PACK = os.environ.get("AUTOPFP_PACK", None)
if AUTOPFP_PACK is None:
    PACK = [
        "Epic-Space-Wallpaper",
        "Acoustic-Guitar-Wallpaper-HD",
        "Taylor-Guitar-Wallpaper",
        "Classical-Music-Wallpapers-for-Desktop",
        "Prs-Guitar-Wallpaper",
        "Iron-Man-Wallpaper-1920x1080",
        "Dodge-Challenger-Black-Hellcat-Wallpaper",
        "V-for-Vendetta-Mask-Wallpaper",
        "Toxic-Mask-Wallpapers",
        "Minion-Desktop-Wallpaper",
        "Epic-1080p-Wallpapers",
        "Japanese-Desktop-Wallpaper",
        "Cool-Gold-Cars-Wallpapers",
        "Pretty-Wallpapers-for-iPhone-Quotes",
        "dark-abstract-wallpaper",
        "abstract-dark-wallpaper",
        "abstract-wallpapers-and-screensavers",
        "roaring-lion-wallpaper",
        "wolves-screensavers-and-wallpaper",
        "cool-wallpaper-for-men",
        "Epic-1080p-Wallpapers",
        "hacker-background",
        "Vietnam-War-Wallpapers",
        "War-of-the-Worlds-Wallpaper",
        "War-Plane-Wallpaper",
        "World-War-Ii-Wallpaper",
        "Cool-War-Wallpapers",
        "World-War-2-Wallpaper-HD",
    ]
else:
    PACK = AUTOPFP_PACK


async def animepp():
    os.system("rm -rf donot.jpg")
    rnd = random.randint(0, len(PACK) - 1)
    pack = PACK[rnd]
    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile("/\w+/full.+.jpg")
    f = f.findall(pc)
    fy = "http://getwallpapers.com" + random.choice(f)
    print(fy)
    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf",
            "f.ttf",
        )
    urllib.request.urlretrieve(fy, "donottouch.jpg")


@bot.on(admin_cmd(pattern="ppr ?(.*)", outgoing=True))
async def main(event):
    await event.edit(
        "**Starting Profile Pic Runner by @HellBot_Official..**"
    )  # Owner @Kraken_The_BadASS
    while True:
        try:
            await animepp()
            file = await event.client.upload_file("donottouch.jpg")
            await event.client(
                functions.photos.DeletePhotosRequest(
                    await event.client.get_profile_photos("me", limit=1)
                )
            )
            await event.client(functions.photos.UploadProfilePhotoRequest(file))
            os.system("rm -rf donottouch.jpg")
        except:
            pass
        await asyncio.sleep(120)  # Edit this to your required needs

CmdHelp("picrunner").add_command(
  "ppr", None, "Auto Profile Pic Runner. Uploads random wallpapers to your profile pic. \nWARNING:- May result in account ban. Use on your own risk"
).add()