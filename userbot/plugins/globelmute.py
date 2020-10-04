'''
© Sensible Userbot
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
    user_id = reply.from_id
    if user_id == (await borg.get_me()).id:	
        await event.edit(r"Btw Boss!!Why would I Gmute You. You are my Boss!!")	
        return	
    if user_id in Config.SUDO_USERS:	
        await event.edit(	
            "**He has more power than me.**\nPerhaps I can't gmute him.\n\n"	
            "**Why??:** `He is a sudo user`.")	
        return
    if user_id in Config.WHITELIST_USERS:	
        await event.edit(	
            "**He has more Power Of Thor And Hulk.**\nPerhaps I can't gmute him.\n\n"	
            "**WHY??** He is a Whitelist user.")	
        return
    if user_id in Config.SUPPORT_USERS:	
        await event.edit(	
            "**He has Friend as Thanos!!.**\nPerhaps I can't gmute him.\n\n"	
            "**why??:** He is SUPPORT user.")	
        return
    if user_id in Config.DEVLOPERS:	
        await event.edit(	
            "**He my Creator.**\nPerhaps I can't gmute him.\n\n"	
            "**Why??** He is my Creator.")	
        return
    elif event.is_private:
        await event.edit("Putting Duct Tape on that person's mouth!Now Just Shut Up!!")
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
        return await event.edit("Duct Tape is already in this user's mouth😷")
    try:
        mute(userid, "gmute")
    except Exception as e:
        await event.edit("Error occured!\nError is " + str(e))
    else:
        await event.edit("Successfully putted Duct Tape on that person's mouth😷")

#@command(outgoing=True, pattern=r"^.ungmute ?(\d+)?")
@borg.on(admin_cmd(pattern=r"ungmute ?(\d+)?"))
async def endgmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("Removed Duct Tape from that person's mouth!😐")
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
