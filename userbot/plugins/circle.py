#Thanks to @TelescopyBot Owner........


import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot.utils import admin_cmd


@bot.on(admin_cmd(r"circle$"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("Reply to a media msg sur......")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.media:
       await event.edit("Reply to media msg sur......")
       return
    chat = "@TelescopyBot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("Yeh kya bawasir hai.... I need actual user.....")
       return
    kraken = await event.edit("Ok I got it🔥🔥")
    async with event.client.conversation(chat) as conv:
          try:     
              await conv.send_message("/start")
              await conv.get_response()
              await conv.send_message(reply_message)
              response = await conv.get_response()
              await event.client.send_read_acknowledge(conv.chat_id)
          except YouBlockedUserError: 
              await kraken.edit("`Please unblock` @TelescopyBot `and try again`")
              return
              await kraken.delete()
          if not response.media:
              await event.client.send_message(event.chat_id, response.message)
          if response.media:
              await event.client.send_file(event.chat_id, response)
