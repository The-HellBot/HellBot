'''
# © StarkGang
added speciality for sudos if u kang give me credits
'''
from userbot.plugins.sql_helper.mute_sql import is_muted, mute, unmute
import asyncio
from userbot.utils import admin_cmd
from telethon import events
#@command(outgoing=True, pattern=r"^.gmute ?(\d+)?")
@borg.on(admin_cmd(pattern=r"gmute ?(\d+)?"))
async def startgmute(event):
    private = False
    if event.fwd_from:
        return
    reply = await event.get_reply_message()
    user_id = reply.sender_id
    if user_id == (await borg.get_me()).id:	
        await event.edit(r"Boss!BTW!! Why would I Gmute You. You are my Boss😁!!")	
        return	
    if user_id in Config.SUDO_USERS:	
        await event.edit(	
            "**He has more Power than me.**\nPerhaps I can't gmute him ! I Am Sorry Boss!!.\n\n"	
            "**Why ?: ** Because He is sudo user.")	
        return
    elif event.is_private:
        await event.edit("Putting Tape on that person's mouth and Ass!")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit("Please reply to a user or add their into the command to gmute them.")
    chat_id = event.chat_id
    chat = await event.get_chat()
    if is_muted(userid, "gmute"):
        return await event.edit("Duct Tape is already availabe on this user's mouth")
    try:
        mute(userid, "gmute")
    except Exception as e:
        await event.edit("Error occured!\nError is " + str(e))
    else:
        await event.edit("Successfully putted Duct Tape on that person's mouth")

#@command(outgoing=True, pattern=r"^.ungmute ?(\d+)?")
@borg.on(admin_cmd(pattern=r"ungmute ?(\d+)?"))
async def endgmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("Removed Duct Tape from that person's mouth!")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit("Please reply to a user or add their into the command to ungmute them.")
    chat_id = event.chat_id
    if not is_muted(userid, "gmute"):
        return await event.edit("Duct Tape is not on this user's mouth")
    try:
        unmute(userid, "gmute")
    except Exception as e:
        await event.edit("Error occured!\nError is " + str(e))
    else:
        await event.edit("Successfully Removed Duct Tape from that person's mouth")
        
@command(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, "gmute"):
        await event.delete()
