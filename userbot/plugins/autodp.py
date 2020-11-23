#Made By @Kraken_The_BadASS Keep Credits If You Are Goanna Kang This Lol

#And Thanks To The Creator Of Autopic This Script Was Made from Snippets From That Script

#               ⚠️DISCLAIMER⚠️

# USING THIS PLUGIN CAN RESULT IN ACCOUNT BAN + CAS BAN + SPAM BAN + ACCOUNT SUSPENSION . WE DONT CARE ABOUT BAN, SO WE ARR USING THIS.

#Im Not Responsible For Any Ban caused By This

import requests , re , random 
import urllib , os 
from telethon.tl import functions
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from userbot.utils import admin_cmd
import asyncio
from time import sleep

COLLECTION_STRING = [

  "indian-actress-wallpapers",

  "latest-bollywood-actress-wallpapers-2018-hd",

  "bollywood-actress-wallpaper",

  "hd-wallpapers-of-bollywood-actress",

  "new-bollywood-actress-wallpaper-2018"

]

async def animepp():

    os.system("rm -rf donot.jpg")

    rnd = random.randint(0, len(COLLECTION_STRING) - 1)

    pack = COLLECTION_STRING[rnd]

    pc = requests.get("http://getwallpapers.com/collection/" + pack).text

    f = re.compile('/\w+/full.+.jpg')

    f = f.findall(pc)

    fy = "http://getwallpapers.com"+random.choice(f)

    print(fy)

    if not os.path.exists("f.ttf"):

        urllib.request.urlretrieve("https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf","f.ttf")

    urllib.request.urlretrieve(fy,"donottouch.jpg")

@borg.on(admin_cmd(pattern="actressdp ?(.*)"))

async def main(event):

    await event.edit("Activated Actress DP\n\n Enjoy💜")

    while True:

        await animepp()

        file = await event.client.upload_file("donottouch.jpg")  

        await event.client(functions.photos.UploadProfilePhotoRequest( file))

        os.system("rm -rf donottouch.jpg")

        await asyncio.sleep(600) #Edit this to your required needs

#-------------------------------------------------------------------------------

import requests , re , random 
import urllib , os 
from telethon.tl import functions
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from userbot.utils import admin_cmd
import asyncio
from time import sleep

COLLECTION_STRING = [

  "pokemon-serena-wallpaper",

  "anime-girls-wallpapers",

  "sexy-anime-gilr-wallpaper",

  "cute-anime-girl-3d-wallpaper-2018",
  
  "ash-serena-love-wallpaper",

  "anime-girls-wallpapers"

]

async def animepp():

    os.system("rm -rf donot.jpg")

    rnd = random.randint(0, len(COLLECTION_STRING) - 1)

    pack = COLLECTION_STRING[rnd]

    pc = requests.get("http://getwallpapers.com/collection/" + pack).text

    f = re.compile('/\w+/full.+.jpg')

    f = f.findall(pc)

    fy = "http://getwallpapers.com"+random.choice(f)

    print(fy)

    if not os.path.exists("f.ttf"):

        urllib.request.urlretrieve("https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf","f.ttf")

    urllib.request.urlretrieve(fy,"donottouch.jpg")

@borg.on(admin_cmd(pattern="animedp ?(.*)"))

async def main(event):

    await event.edit("Activated Anime DP\n\n Enjoy💜")

    while True:

        await animepp()

        file = await event.client.upload_file("donottouch.jpg")  

        await event.client(functions.photos.UploadProfilePhotoRequest( file))

        os.system("rm -rf donottouch.jpg")

        await asyncio.sleep(600) #Edit this to your required needs

#-------------------------------------------------------------------------------

import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.tl import functions
import asyncio
import shutil

FONT_FILE_TO_USE = "Fonts/digital.ttf"

@command(pattern="^.autopic", outgoing=True)
async def autopic(event):
    downloaded_file_name = "userbot/original_pic.png"
    downloader = SmartDL(Var.DOWNLOAD_PFP_URL_CLOCK, downloaded_file_name, progress_bar=False)
    downloader.start(blocking=False)
    photo = "userbot/photo_pfp.png"
    while not downloader.isFinished():
        place_holder = None
    counter = -30
    while True:
        shutil.copy(downloaded_file_name, photo)
        im = Image.open(photo)
        file_test = im.rotate(counter, expand=False).save(photo, "PNG")
        current_time = datetime.now().strftime("                      \n  Time: %H:%M:%S \n  Date: %d.%m.%y \n                    ")
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 60)
        drawn_text.text((95, 250), current_time, font=fnt, fill=(0, 255, 0))
        img.save(photo)
        file = await bot.upload_file(photo)  # pylint:disable=E0602
        try:
            await bot(functions.photos.UploadProfilePhotoRequest(  # pylint:disable=E0602
                file
            ))
            os.remove(photo)
            counter -= 30
            await asyncio.sleep(60)
        except:
            return

#-------------------------------------------------------------------------------

import requests , re , random 
import urllib , os 
from telethon.tl import functions
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from userbot.utils import admin_cmd
import asyncio
from time import sleep

COLLECTION_STRING = [

  "avengers-logo-wallpaper",

  "avengers-hd-wallpapers-1080p",

  "avengers-iphone-wallpaper",

  "iron-man-wallpaper-1920x1080",

  "iron-man-wallpapers"

]

async def animepp():

    os.system("rm -rf donot.jpg")

    rnd = random.randint(0, len(COLLECTION_STRING) - 1)

    pack = COLLECTION_STRING[rnd]

    pc = requests.get("http://getwallpapers.com/collection/" + pack).text

    f = re.compile('/\w+/full.+.jpg')

    f = f.findall(pc)

    fy = "http://getwallpapers.com"+random.choice(f)

    print(fy)

    if not os.path.exists("f.ttf"):

        urllib.request.urlretrieve("https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf","f.ttf")

    urllib.request.urlretrieve(fy,"donottouch.jpg")

@borg.on(admin_cmd(pattern="avengersdp ?(.*)"))

async def main(event):

    await event.edit("Activated Avengers DP\n Enjoy💜")

    while True:

        await animepp()

        file = await event.client.upload_file("donottouch.jpg")  

        await event.client(functions.photos.UploadProfilePhotoRequest( file))

        os.system("rm -rf donottouch.jpg")

        await asyncio.sleep(600) #Edit this to your required needs

#-------------------------------------------------------------------------------

import requests , re , random 
import urllib , os 
from telethon.tl import functions
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from userbot.utils import admin_cmd
import asyncio
from time import sleep

COLLECTION_STRING = [
  "awesome-batman-wallpapers",
  "batman-arkham-knight-4k-wallpaper",
  "batman-hd-wallpapers-1080p",
  "the-joker-hd-wallpaper",
  "dark-knight-joker-wallpaper"
]

async def animepp():
    os.system("rm -rf donot.jpg")
    rnd = random.randint(0, len(COLLECTION_STRING) - 1)
    pack = COLLECTION_STRING[rnd]
    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile('/\w+/full.+.jpg')
    f = f.findall(pc)
    fy = "http://getwallpapers.com"+random.choice(f)
    print(fy)
    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve("https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf","f.ttf")
    urllib.request.urlretrieve(fy,"donottouch.jpg")
@borg.on(admin_cmd(pattern="batmandp ?(.*)"))
async def main(event):
    await event.edit("Activated Batman DP\n Enjoy💜")
    while True:
        await animepp()
        file = await event.client.upload_file("donottouch.jpg")
        await event.client(functions.photos.DeletePhotosRequest(await event.client.get_profile_photos("me", limit=1)))
        await event.client(functions.photos.UploadProfilePhotoRequest( file))
        os.system("rm -rf donottouch.jpg")
        await asyncio.sleep(600) #Edit this to your required needs

#-------------------------------------------------------------------------------

import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.tl import functions
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd
import asyncio
import shutil 
import random

FONT_FILE_TO_USE = "Fonts/digital.ttf"

DEFAULTUSER = str(ALIVE_NAME)

@borg.on(admin_cmd(pattern="cpp ?(.*)"))

async def autopic(event): 

    await event.edit("Activated Colour Profile Pic\n Enjoy💜") 

    downloaded_file_name = "./HELLBOT/original_pic.png"

    downloader = SmartDL(Var.DOWNLOAD_PFP_URL_CLOCK, downloaded_file_name, progress_bar=False)

    downloader.start(blocking=False)

    photo = "photo_pfp.png"

    while not downloader.isFinished():

        place_holder = None



    while True:

        #RIP Danger zone Here no editing here plox

        R = random.randint(0,256)

        B = random.randint(0,256)

        G = random.randint(0,256)

        FR = (256 - R) 

        FB = (256 - B) 

        FG = (256 - G) 

        shutil.copy(downloaded_file_name, photo)

        image = Image.open(photo)

        image.paste( (R, G, B), [0,0,image.size[0],image.size[1]])

        image.save(photo)

        

        #Edit only Below part ð Or esle u will be responsible ð¤·ââ

        current_time = datetime.now().strftime("\n\n Time: %H:%M:%S \n \n Date: %d/%m/%y")

        img = Image.open(photo)

        drawn_text = ImageDraw.Draw(img)

        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 40)

        ofnt = ImageFont.truetype(FONT_FILE_TO_USE, 40)

        drawn_text.text((200, 400), current_time, font=fnt, fill=(FR,FG,FB))

        drawn_text.text((250, 250), f"{DEFAULTUSER}", font = ofnt, fill=(FR,FG,FB))

        img.save(photo)

        file = await event.client.upload_file(photo)  # pylint:disable=E0602

        try:
            await event.client(functions.photos.DeletePhotosRequest(await event.client.get_profile_photos("me", limit=1)))
            await event.client(functions.photos.UploadProfilePhotoRequest(  # pylint:disable=E0602

                file

            ))

            os.remove(photo)

            await asyncio.sleep(60)

        except:

            return

#-------------------------------------------------------------------------------

import requests , re , random 
import urllib , os 
from telethon.tl import functions
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from userbot.utils import admin_cmd
import asyncio
from time import sleep

COLLECTION_STRINGZ = [

  "star-wars-wallpaper-1080p",

  "4k-sci-fi-wallpaper",

  "star-wars-iphone-6-wallpaper",

  "kylo-ren-wallpaper",

  "darth-vader-wallpaper"

]

async def animepp():

    os.system("rm -rf donot.jpg")

    rnd = random.randint(0, len(COLLECTION_STRINGZ) - 1)

    pack = COLLECTION_STRINGZ[rnd]

    pc = requests.get("http://getwallpapers.com/collection/" + pack).text

    f = re.compile('/\w+/full.+.jpg')

    f = f.findall(pc)

    fy = "http://getwallpapers.com"+random.choice(f)

    print(fy)

    if not os.path.exists("f.ttf"):

        urllib.request.urlretrieve("https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf","f.ttf")

    urllib.request.urlretrieve(fy,"donottouch.jpg")

@borg.on(admin_cmd(pattern="gamersdp ?(.*)"))

async def main(event):

    await event.edit("Activated Gamers DP\n Enjoy💜") 

    while True:

        await animepp()

        file = await event.client.upload_file("donottouch.jpg")  

        await event.client(functions.photos.UploadProfilePhotoRequest( file))

        os.system("rm -rf donottouch.jpg")

        await asyncio.sleep(300) #Edit this to your required needs

#-------------------------------------------------------------------------------

import requests , re , random 
import urllib , os 
from telethon.tl import functions
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from userbot.utils import admin_cmd
import asyncio
from time import sleep

COLLECTION_STRINGZ = [
  "hacker-background"
]

async def animepp():

    os.system("rm -rf donot.jpg")

    rnd = random.randint(0, len(COLLECTION_STRINGZ) - 1)

    pack = COLLECTION_STRINGZ[rnd]

    pc = requests.get("http://getwallpapers.com/collection/" + pack).text

    f = re.compile('/\w+/full.+.jpg')

    f = f.findall(pc)

    fy = "http://getwallpapers.com"+random.choice(f)

    print(fy)

    if not os.path.exists("f.ttf"):

        urllib.request.urlretrieve("https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf","f.ttf")

    urllib.request.urlretrieve(fy,"donottouch.jpg")

@borg.on(admin_cmd(pattern="hackerdp ?(.*)"))

async def main(event):

    await event.edit("Activated Hackers DP\n Enjoy💜")

    while True:

        await animepp()

        file = await event.client.upload_file("donottouch.jpg")  

        await event.client(functions.photos.UploadProfilePhotoRequest( file))

        os.system("rm -rf donottouch.jpg")

        await asyncio.sleep(60) #Edit this to your required needs

#-------------------------------------------------------------------------------

import requests , re , random 
import urllib , os 
from telethon.tl import functions
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from userbot.utils import admin_cmd
import asyncio
from time import sleep

COLLECTION_STRING = [

  "avengers-logo-wallpaper",

  "avengers-hd-wallpapers-1080p",

  "avengers-iphone-wallpaper",

  "iron-man-wallpaper-1920x1080",

  "iron-man-wallpapers",

  "Marvel-Shield-iPhone-Wallpaper",

  "Shield-Logo-Wallpaper",

  "Marvel-Shield-Logo-Wallpaper",

  "Agents-of-Shield-Wallpaper",

  "Agents-of-Shield-iPhone-Wallpaper",

  "Agents-of-Shield-Wallpapers-HD"

  "Thor-Wallpaper-1920x1080",

  "Thor-Wallpapers",

  "Avengers-HD-Wallpapers-1080p",

  "Avengers-Wallpaper-for-Desktop",

   "Avengers-4K-Wallpaper",

  "Avengers-Age-of-Ultron-Wallpaper",

  "Avengers-Civil-War-Wallpaper",

  "Avengers-2-Wallpapers",

  "Avengers-Logo-Wallpaper",

  "Marvel-Avengers-Desktop-Wallpaper",

  "4K-Deadpool-Wallpaper",

  "3D-Deadpool-Logo-Wallpaper",

  "Deadpool-HD-Desktop-Wallpaper",

  "Cool-Deadpool-Wallpaper",

  "Thor-Wallpaper-HD"
  
]

async def animepp():

    os.system("rm -rf donot.jpg")

    rnd = random.randint(0, len(COLLECTION_STRING) - 1)

    pack = COLLECTION_STRING[rnd]

    pc = requests.get("http://getwallpapers.com/collection/" + pack).text

    f = re.compile('/\w+/full.+.jpg')

    f = f.findall(pc)

    fy = "http://getwallpapers.com"+random.choice(f)

    print(fy)

    if not os.path.exists("f.ttf"):

        urllib.request.urlretrieve("https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf","f.ttf")

    urllib.request.urlretrieve(fy,"donottouch.jpg")

@borg.on(admin_cmd(pattern="marveldp ?(.*)"))

async def main(event):

    await event.edit("Activated Marvel DP\n Enjoy💜")

    while True:

        await animepp()

        file = await event.client.upload_file("donottouch.jpg")  

        await event.client(functions.photos.UploadProfilePhotoRequest( file))

        os.system("rm -rf donottouch.jpg")

        await asyncio.sleep(60) #Edit this to your required needs

#-------------------------------------------------------------------------------

import requests , re , random 
import urllib , os 
from telethon.tl import functions
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from userbot.utils import admin_cmd
import asyncio
from time import sleep

COLLECTION_STRING = [
  "Predator-Wallpapers-Backgrounds",
  "Alien-vs-Predator-Wallpaper"
]

async def animepp():
    os.system("rm -rf donot.jpg")
    rnd = random.randint(0, len(COLLECTION_STRING) - 1)
    pack = COLLECTION_STRING[rnd]
    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile('/\w+/full.+.jpg')
    f = f.findall(pc)
    fy = "http://getwallpapers.com"+random.choice(f)
    print(fy)
    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve("https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf","f.ttf")
    urllib.request.urlretrieve(fy,"donottouch.jpg")
    
@borg.on(admin_cmd(pattern="predatordp ?(.*)"))
async def main(event):
    await event.edit("Activated Predetor DP\n Enjoy💜")
    while True:
        await animepp()
        file = await event.client.upload_file("donottouch.jpg")  
        await event.client(functions.photos.DeletePhotosRequest(await event.client.get_profile_photos("me", limit=1)))
        await event.client(functions.photos.UploadProfilePhotoRequest( file))
        os.system("rm -rf donottouch.jpg")
        await asyncio.sleep(120) #Edit this to your required needs

#-------------------------------------------------------------------------------

import requests , re , random 
import urllib , os 
from telethon.tl import functions
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from userbot.utils import admin_cmd
import asyncio
from time import sleep

COLLECTION_STRINGS = [

  "1920x1080-space-wallpapers",

  "4k-space-wallpaper",

  "cool-space-wallpapers-hd",
]

async def animepp():

    os.system("rm -rf donot.jpg")

    rnd = random.randint(0, len(COLLECTION_STRINGS) - 1)

    pack = COLLECTION_STRINGS[rnd]

    pc = requests.get("http://getwallpapers.com/collection/" + pack).text

    f = re.compile('/\w+/full.+.jpg')

    f = f.findall(pc)

    fy = "http://getwallpapers.com"+random.choice(f)

    print(fy)

    if not os.path.exists("f.ttf"):

        urllib.request.urlretrieve("https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf","f.ttf")

    urllib.request.urlretrieve(fy,"friday.jpg")

@borg.on(admin_cmd(pattern="spacedp ?(.*)"))

async def main(event):

    await event.edit("Activated Space DP\n Enjoy💜")
    while True:

        await animepp()

        file = await event.client.upload_file("donottouch.jpg")  

        await event.client(functions.photos.UploadProfilePhotoRequest( file))

        os.system("rm -rf donottouch.jpg")

        await asyncio.sleep(3600) #Edit this to your required needs

#-------------------------------------------------------------------------------

import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.tl import functions
from userbot.utils import admin_cmd
import asyncio
import shutil 
import random, re


FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

#Add telegraph media links of profile pics that are to be used
TELEGRAPH_MEDIA_LINKS = ["https://telegra.ph/file/2eab4f64ead6fbf41bf87.jpg",
                         "https://telegra.ph/file/6bef1ffbaddc5230c2ae1.jpg",
                         "https://telegra.ph/file/a03f035e83098a7c5bded.jpg",
                         "https://telegra.ph/file/f0a230a30b9952f56d2cd.jpg",
                         "https://telegra.ph/file/d00e6bb4b4a483099c992.jpg",
                         "https://telegra.ph/file/1270ed675db61e6c84eea.jpg",
                         "https://telegra.ph/file/32743c9389915b02fdea7.jpg",
                         "https://telegra.ph/file/8c02a1430502bea931ff7.jpg",
                         "https://telegra.ph/file/1ec37d367bb59ac56131d.jpg",
                         "https://telegra.ph/file/e9aeef4fd2e3d0b9e9f24.jpg",
                         "https://telegra.ph/file/28c242ea9f8cf32db4c21.jpg",
                         "https://telegra.ph/file/c089426ca031d1f6297b0.jpg",
                         "https://telegra.ph/file/a196b6c07f0a659daf058.jpg",
                         "https://telegra.ph/file/69f19acd13b1eaf3fc120.jpg"
                        ]
@borg.on(admin_cmd(pattern="survivorpfp ?(.*)"))
async def autopic(event):
    while True:
        piclink = random.randint(0, len(TELEGRAPH_MEDIA_LINKS) - 1)
        AUTOPP = TELEGRAPH_MEDIA_LINKS[piclink]
        downloaded_file_name = "./userbot/original_pic.png"
        downloader = SmartDL(AUTOPP, downloaded_file_name, progress_bar=True)
        downloader.start(blocking=False)
        photo = "photo_pfp.png"
        while not downloader.isFinished():
            place_holder = None
    
    
        shutil.copy(downloaded_file_name, photo)
        im = Image.open(photo)
        current_time = datetime.now().strftime("HellBot \n \nTime: %H:%M:%S \nDate: %d/%m/%y")
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 23)
        drawn_text.text((350, 400), current_time, font=fnt, fill=(230,230,250))
        img.save(photo)
        file = await event.client.upload_file(photo)  # pylint:disable=E0602
        try:
            await event.client(functions.photos.UploadProfilePhotoRequest(  # pylint:disable=E0602
                file
            ))
            os.remove(photo)
            
            await asyncio.sleep(30)
        except:
            return
          
#-------------------------------------------------------------------------------

