"""Type `.poto` for get **All profile pics of that User**
\n Or type `.poto (number)` to get the **desired number of photo of a User** .
"""


import logging

from hellbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp

name = "Profile Photos"

@bot.on(admin_cmd(pattern="poto ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="poto ?(.*)", allow_sudo=True))
async def potocmd(event):
    """Gets the profile photos of replied users, channels or chats"""
    uid = "".join(event.raw_text.split(maxsplit=1)[1:])
    user = await event.get_reply_message()
    chat = event.input_chat
    if user:
        photos = await event.client.get_profile_photos(user.sender)
        u = True
    else:
        photos = await event.client.get_profile_photos(chat)
        u = False
    if uid.strip() == "":
        uid = 1
        if int(uid) <= (len(photos)):
            send_photos = await event.client.download_media(photos[uid - 1])
            await event.client.send_file(event.chat_id, send_photos)
        else:
            await edit_or_reply(
                event, "No photo found of this NIBBA. Now u Die!"
            )
            await asyncio.sleep(2)
            return
    elif uid.strip() == "all":
        if len(photos) > 0:
            await event.client.send_file(event.chat_id, photos)
        else:
            try:
                if u is True:
                    photo = await event.client.download_profile_photo(user.sender)
                else:
                    photo = await event.client.download_profile_photo(event.input_chat)
                await event.client.send_file(event.chat_id, photo)
            except a:
                await edit_or_reply(event, "**This user has no photos!**")
                return
    else:
        try:
            uid = int(uid)
            if uid <= 0:
                await edit_or_reply(
                    event, "```number Invalid!``` **Are you komedy Me ?**"
                )
                return
        except BaseException:
            await edit_or_reply(event, "Are you komedy me ?")
            return
        if int(uid) <= (len(photos)):
            send_photos = await event.client.download_media(photos[uid - 1])
            await event.client.send_file(event.chat_id, send_photos)
        else:
            await edit_or_reply(
                event, "No photo found of this NIBBA. Now u Die!"
            )
            await asyncio.sleep(2)
            return

CmdHelp("poto").add_command(
  "poto", "<all> / <desired pp number>", "Reply to user to get his/her profile pic. Use .poto <number> to get desired profile pic else use .poto all to get all profile pic(s). If you dont reply to a user then it gets group pics."
).add_command(
  "ppg", "<reply>", "Gets the user's 1st profile pic. But this time with a caption. Try it yourself..."
).add()