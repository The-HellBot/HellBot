import datetime
import asyncio
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError, UserAlreadyParticipantError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from userbot.utils import admin_cmd
import time
from userbot import ALIVE_NAME

naam = str(ALIVE_NAME)

bot = "@ceowhitehatcracks"
bluebot = "@ceowhitehatcracks"
freebot = "@ceowhitehatcracks"


@borg.on(admin_cmd("jav ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    sysarg = event.pattern_match.group(1)
    
    if sysarg == "h":
      async with borg.conversation(bot) as conv:
          try:
              await conv.send_message("/start")
              response = await conv.get_response()
              await conv.send_message("/hello")
              audio = await conv.get_response()
              await borg.send_file(event.chat_id, audio, caption="➡️**TO BOSS : **" + naam +"\n`Check This Bot out` [Sensible Userbot](ttps://github.com/spandey112/SensibleUserbot)")
              await event.delete()
          except YouBlockedUserError:
              await event.edit("**Error:** `unblock` @Ceowhitehatcracks `and retry!")
    elif sysarg == "ss":
      async with borg.conversation(bot) as conv:
          try:
              await conv.send_message("/start")
              response = await conv.get_response()
              await conv.send_message("/ss")
              audio = await conv.get_response()
              await borg.send_file(event.chat_id, audio, caption="**CREDITS : Dr.jr Genesis**\n`Check out` [Sensible Userbot Support](t.me/sensible_userbot)")
              await event.delete()
          except YouBlockedUserError:
              await event.edit("**Error:** `unblock` @ceowhitehatcracks `and retry!`")
    elif sysarg == "--h":
      async with borg.conversation(bot) as conv:
          try:
              await conv.send_message("/start")
              response = await conv.get_response()
              await conv.send_message("/help")
              audio = await conv.get_response()
              await borg.send_file(event.chat_id, audio, caption="**Dr.Bot Is Here To Help**\n`Check out` [Sensible Userbot Support](t.me/sensible_userbot)")
              await event.delete()
          except YouBlockedUserError:
              await event.edit("**Error:** `unblock` @ceowhitehatcracks `and retry!`")
    elif sysarg == "npic":
      async with borg.conversation(bot) as conv:
          try:
              await conv.send_message("/start")
              response = await conv.get_response()
              await conv.send_message("/nudepic")
              audio = await conv.get_response()
              await borg.send_file(event.chat_id, audio, caption="**For" + naam +" **\n`Check out` [Sensible Userbot Support](t.me/sensible_userbot)")
              await event.delete()
          except YouBlockedUserError:
              await event.edit("**Error:** `unblock` @sensible_userbot `and retry!`")
    elif sysarg == "rs":
      async with borg.conversation(bot) as conv:
          try:
              await conv.send_message("/start")
              response = await conv.get_response()
              await conv.send_message("/rs")
              audio = await conv.get_response()
              await borg.send_file(event.chat_id, audio, caption="**CREDITS : @CEOWHITEHATCRACKS**\n`Check out` [Sensible Userbot Support](t.me/sensible_userbot)")
              await event.delete()
          except YouBlockedUserError:
              await event.edit("**Error:** `unblock` @ceowhitehatcracks `and retry!`")
    elif sysarg == "ib":
      async with borg.conversation(bot) as conv:
          try:
              await conv.send_message("/start")
              response = await conv.get_response()
              await conv.send_message("/ib")
              audio = await conv.get_response()
              await borg.send_file(event.chat_id, audio, caption="**CREDITS : Ceowhitehatcracks**\n`Check out` [Sensible Userbot](ttps://github.com/spandey112/SensibleUserbot)")
              await event.delete()
          except YouBlockedUserError:
              await event.edit("**Error:** `unblock` @Ceowhitehatcracks `and retry!`")
    elif sysarg == "acc":
      async with borg.conversation(bot) as conv:
          try:
              await conv.send_message("/start")
              response = await conv.get_response()
              await conv.send_message("/acc")
              audio = await conv.get_response()
              await borg.send_file(event.chat_id, audio)
              await event.delete()
          except YouBlockedUserError:
              await event.edit("**Error:** `unblock` @ceowhitehatcracks `and retry!`")
    else:
      await brog.send_message(event.chat_id, "**INVALID** -- FOR HELP COMMAND IS **.jav --h**")
      await event.delete()


