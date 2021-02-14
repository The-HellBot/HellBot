# plugin modified By @No_OnE_Kn0wS_Me
# USING THIS PLUGIN CAN RESULT IN ACCOUNT BAN + CAS BAN + SPAM BAN + ACCOUNT SUSPENSION . WE DONT CARE ABOUT BAN, SO WE ARR USING THIS.

import asyncio
import os
import random
import shutil
from datetime import datetime

from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.tl import functions
from hellbot.utils import admin_cmd

FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

# Add telegraph media links of profile pics that are to be used
TELEGRAPH_MEDIA_LINKS = [
    "https://telegra.ph/file/e354ce72d5cc6a1d27c4d.jpg",
    "https://telegra.ph/file/8f9ff3d743e6707a61489.jpg",
    "https://telegra.ph/file/bfc97f4abc4bec6fe860d.jpg",
    "https://telegra.ph/file/5ef0f060023600ec08c19.jpg",
    "https://telegra.ph/file/a448465a3a8a251170f76.jpg",
    "https://telegra.ph/file/eb0ac1557668a98a38cb6.jpg",
    "https://telegra.ph/file/fdb3691a17a2c91fbe76c.jpg",
    "https://telegra.ph/file/ccdf69ebf6cb85c52a25b.jpg",
    "https://telegra.ph/file/2adffc55ac0c9733ecc7f.jpg",
    "https://telegra.ph/file/faca3b435da33f2f156f1.jpg",
    "https://telegra.ph/file/93d0a48c31e16f036f0e8.jpg",
    "https://telegra.ph/file/9ed89dc742b172a779312.jpg",
    "https://telegra.ph/file/0b4c19a19fb834d922d66.jpg",
    "https://telegra.ph/file/a95a0deb86f642129b067.jpg",
    "https://telegra.ph/file/c4c3d8b5cfc3cc5040833.jpg",
    "https://telegra.ph/file/1e1a1b52b9a313e066a04.jpg",
    "https://telegra.ph/file/a582950a8a259efdcbbc0.jpg",
    "https://telegra.ph/file/9c3a784d45790b193ca36.jpg",
    "https://telegra.ph/file/6aa74b17ae4e7dc46116f.jpg",
    "https://telegra.ph/file/e63cf624d1b68a5c819b6.jpg",
    "https://telegra.ph/file/7e420ad5995952ba1c262.jpg",
    "https://telegra.ph/file/c7a4dc3d2a9a422c19723.jpg",
    "https://telegra.ph/file/163c7eba56fd2e8c266e4.jpg",
    "https://telegra.ph/file/5c87b63ae326b5c3cd713.jpg",
    "https://telegra.ph/file/344ca22b35868c0a7661d.jpg",
    "https://telegra.ph/file/a0ef3e56f558f04a876aa.jpg",
    "https://telegra.ph/file/217b997ad9b5af8b269d0.jpg",
    "https://telegra.ph/file/b3595f99b221c56a5679b.jpg",
    "https://telegra.ph/file/aba7f4b4485c5aae53c52.jpg",
    "https://telegra.ph/file/209ca51dba6c0f1fba85f.jpg",
    "https://telegra.ph/file/2a0505ee2630bd6d7acca.jpg",
    "https://telegra.ph/file/d193d4191012f4aafd4d2.jpg",
    "https://telegra.ph/file/47e2d151984bd54a5d947.jpg",
    "https://telegra.ph/file/2a6c735b47db947b44599.jpg",
    "https://telegra.ph/file/7567774412fb76ceba95c.jpg",
    "https://telegra.ph/file/6dd8b0edec92b24985e13.jpg",
    "https://telegra.ph/file/dcf5e16cc344f1c030469.jpg",
    "https://telegra.ph/file/0718be0bd52a2eb7e36aa.jpg",
    "https://telegra.ph/file/0d7fcb82603b5db683890.jpg",
    "https://telegra.ph/file/44595caa95717f4db4788.jpg",
    "https://telegra.ph/file/f3a063d884d0dcde437e3.jpg",
    "https://telegra.ph/file/733425275da19cbed0822.jpg",
    "https://telegra.ph/file/aff5223e1aa29f212a46a.jpg",
    "https://telegra.ph/file/45ccfa3ef878bea9cfc02.jpg",
    "https://telegra.ph/file/a38aa50d009835177ac16.jpg",
    "https://telegra.ph/file/53e25b1b06f411ec051f0.jpg",
    "https://telegra.ph/file/96e801400487d0a120715.jpg",
    "https://telegra.ph/file/6ae8e799f2acc837e27eb.jpg",
    "https://telegra.ph/file/265ff1cebbb7042bfb5a7.jpg",
    "https://telegra.ph/file/4c8c9cd0751eab99600c9.jpg",
    "https://telegra.ph/file/1c6a5cd6d82f92c646c0f.jpg",
    "https://telegra.ph/file/2c1056c91c8f37fea838a.jpg",
    "https://telegra.ph/file/f140c121d03dfcaf4e951.jpg",
    "https://telegra.ph/file/39f7b5d1d7a3487f6ba69.jpg",
]


@borg.on(admin_cmd(pattern="rpc ?(.*)"))
async def autopic(event):
    while True:
        piclink = random.randint(0, len(TELEGRAPH_MEDIA_LINKS) - 1)
        AUTOPP = TELEGRAPH_MEDIA_LINKS[piclink]
        downloaded_file_name = "./DOWNLOADS/original_pic.png"
        downloader = SmartDL(AUTOPP, downloaded_file_name, progress_bar=True)
        downloader.start(blocking=False)
        photo = "photo_pfp.png"
        while not downloader.isFinished():
            pass

        shutil.copy(downloaded_file_name, photo)
        Image.open(photo)
        current_time = datetime.now().strftime(
            "\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n                                                   Time: %H:%M:%S \n                                                   Date: %d/%m/%y "
        )
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 30)
        drawn_text.text((300, 450), current_time, font=fnt, fill=(255, 255, 255))
        img.save(photo)
        file = await event.client.upload_file(photo)  # pylint:disable=E0602
        try:
            await event.client(
                functions.photos.UploadProfilePhotoRequest(file)  # pylint:disable=E0602
            )
            os.remove(photo)

            await asyncio.sleep(60)
        except:
            return
