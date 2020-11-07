#Making it easy....
#thanks to @ranger_op

import os
import re
import time
import urllib.request
import zipfile
from random import choice

import PIL.ImageOps
import requests
from PIL import Image, ImageDraw, ImageFont
from telethon.tl.types import Channel, PollAnswer
from validators.url import url



#convertion..

def convert_toimage(image):
    img = Image.open(image)
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save("./temp/temp.jpg", "jpeg")
    os.remove(image)
    return "./temp/temp.jpg"


async def convert_tosticker(image):
    img = Image.open(image)
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save("./temp/temp.webp", "webp")
    os.remove(image)
    return "./temp/temp.webp"
    
async def invert_colors(imagefile, endname):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.invert(image)
    inverted_image.save(endname)


async def flip_image(imagefile, endname):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.flip(image)
    inverted_image.save(endname)


async def grayscale(imagefile, endname):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.grayscale(image)
    inverted_image.save(endname)


async def mirror_file(imagefile, endname):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.mirror(image)
    inverted_image.save(endname)


async def solarize(imagefile, endname):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.solarize(image, threshold=128)
    inverted_image.save(endname)
    
    
#tweets....
#source - https://nekobot.xyz/api

    
async def iphonex(text):
    r = requests.get(f"https://nekobot.xyz/api/imagegen?type=iphonex&url={text}").json()
    kraken = r.get("message")
    hellurl = url(kraken)
    if not hellurl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(kraken).content)
    img = Image.open("temp.png").convert("RGB")
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


async def baguette(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=baguette&url={text}"
    ).json()
    kraken = r.get("message")
    hellurl = url(kraken)
    if not hellurl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(kraken).content)
    img = Image.open("temp.png").convert("RGB")
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"
    
    
async def threats(text):
    r = requests.get(f"https://nekobot.xyz/api/imagegen?type=threats&url={text}").json()
    kraken = r.get("message")
    hellurl = url(kraken)
    if not hellurl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(kraken).content)
    img = Image.open("temp.png")
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


async def lolice(text):
    r = requests.get(f"https://nekobot.xyz/api/imagegen?type=lolice&url={text}").json()
    kraken = r.get("message")
    hellurl = url(kraken)
    if not hellurl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(kraken).content)
    img = Image.open("temp.png")
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


async def trash(text):
    r = requests.get(f"https://nekobot.xyz/api/imagegen?type=trash&url={text}").json()
    kraken = r.get("message")
    hellurl = url(kraken)
    if not hellurl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(kraken).content)
    img = Image.open("temp.png")
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


async def awooify(text):
    r = requests.get(f"https://nekobot.xyz/api/imagegen?type=awooify&url={text}").json()
    kraken = r.get("message")
    hellurl = url(kraken)
    if not hellurl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(kraken).content)
    img = Image.open("temp.png")
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


async def trap(text1, text2, text3):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=trap&name={text1}&author={text2}&image={text3}"
    ).json()
    kraken = r.get("message")
    hellurl = url(kraken)
    if not hellurl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(kraken).content)
    img = Image.open("temp.png")
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


async def phcomment(text1, text2, text3):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=phcomment&image={text1}&text={text2}&username={text3}"
    ).json()
    kraken = r.get("message")
    hellurl = url(kraken)
    if not hellurl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(kraken).content)
    img = Image.open("temp.png")
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"
