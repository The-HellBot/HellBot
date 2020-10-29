#Ascii module by @kraken_the_badass for @hellbot_official
#A over powerful bot
#I know u will kang... 
#GTFO!! MOTHERFUCKER!!!!!!!!!!!


import datetime
import asyncio
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError, UserAlreadyParticipantError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from userbot.utils import admin_cmd
from userbot import CMD_HELP 

@borg.on(admin_cmd(pattern="ascii ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("Reply to any user message.😒🤐")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.media:
       await event.edit("Reply to media message😒🤐")
       return
    chat = "@asciiart_bot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("Reply to actual users message.😒🤐")
       return
    await event.edit("Wait making ASCII...🤓🔥")
    # For HellBot
    async with borg.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=164766745))
              await borg.send_message(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Please unblock @asciiart_bot and try again🤐")
              return
          if response.text.startswith("Forward"):
             await event.edit("Cn you kindly disable your forward privacy settings for good?😒")
          else: 
             await borg.send_file(event.chat_id, response.message.media)  
                
# For HellBot
CMD_HELP.update({"ascii": "`.ascii` reply to any image file:\
      \nUSAGE:makes an image ascii style, try out your own.\
      "
})          
