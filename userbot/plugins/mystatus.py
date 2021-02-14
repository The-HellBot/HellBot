import os
import urllib

from telethon.tl import functions
from hellbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp


OFFLINE_TAG = "[•OFFLINE•]"
ONLINE_TAG = "[•ONLINE•]"
PROFILE_IMAGE = os.environ.get(
    "PROFILE_IMAGE", "https://telegra.ph/file/9f0638dbfa028162a8682.jpg"
)


@bot.on(admin_cmd(pattern="offline", outgoing=True))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    user_it = "me"
    user = await event.client.get_entity(user_it)
    if user.first_name.startswith(OFFLINE_TAG):
        await edit_or_reply(event, "**Already in Offline Mode.**")
        return
    await edit_or_reply(event, "**Changing Profile to Offline...**")
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):  # pylint:disable=E0602
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)  # pylint:disable=E0602
    urllib.request.urlretrieve(
        "https://telegra.ph/file/249f27d5b52a87babcb3f.jpg", "donottouch.jpg"
    )
    photo = "donottouch.jpg"
    if photo:
        file = await event.client.upload_file(photo)
        try:
            await borg(functions.photos.UploadProfilePhotoRequest(file))
        except Exception as e:  # pylint:disable=C0103,W0703
            await edit_or_reply(event, str(e))
        else:
            await edit_or_reply(event, "**Changed profile to OffLine.**")
    try:
        os.system("rm -fr donottouch.jpg")
    except Exception as e:  # pylint:disable=C0103,W0703
        logger.warn(str(e))  # pylint:disable=E0602
    last_name = ""
    first_name = OFFLINE_TAG
    try:
        await borg(
            functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                last_name=last_name, first_name=first_name
            )
        )
        result = "**`{} {}`\nI am Offline now.**".format(first_name, last_name)
        await edit_or_reply(event, result)
    except Exception as e:  # pylint:disable=C0103,W0703
        await edit_or_reply(event, str(e))


@bot.on(admin_cmd(pattern="online", outgoing=True))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    user_it = "me"
    user = await event.client.get_entity(user_it)
    if user.first_name.startswith(OFFLINE_TAG):
        await edit_or_reply(event, "**Changing Profile to Online...**")
    else:
        await edit_or_reply(event, "**Already Online.**")
        return
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):  # pylint:disable=E0602
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)  # pylint:disable=E0602
    urllib.request.urlretrieve(PROFILE_IMAGE, "donottouch.jpg")
    photo = "donottouch.jpg"
    if photo:
        file = await event.client.upload_file(photo)
        try:
            await borg(functions.photos.UploadProfilePhotoRequest(file))
        except Exception as e:  # pylint:disable=C0103,W0703
            await edit_or_reply(event, str(e))
        else:
            await edit_or_reply(event, "**Changed profile to Online.**")
    try:
        os.system("rm -fr donottouch.jpg")
    except Exception as e:  # pylint:disable=C0103,W0703
        logger.warn(str(e))  # pylint:disable=E0602
    first_name = ONLINE_TAG
    last_name = ""
    try:
        await borg(
            functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                last_name=last_name, first_name=first_name
            )
        )
        result = "**`{} {}`\nI am Online !**".format(first_name, last_name)
        await edit_or_reply(event, result)
    except Exception as e:  # pylint:disable=C0103,W0703
        await edit_or_reply(event, str(e))

CmdHelp("mystatus").add_command(
  "online", None, "Remove Offline Tag from your name and change profile pic to vars PROFILE_IMAGE."
).add_command(
  "offline", None, "Add an offline tag in your name and change profile pic to black."
).add()