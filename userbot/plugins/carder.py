import os
from faker import Faker
import datetime
from telethon import functions, types, events
from telethon.tl.functions.messages import DeleteHistoryRequest
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest

from userbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot import CmdHelp
from userbot import bot as hellbot


@hellbot.on(admin_cmd("gencc$"))
@hellbot.on(sudo_cmd("gencc$", allow_sudo=True))
async def _(hellevent):
    hellcc = Faker()
    hellname = hellcc.name()
    helladre = hellcc.address()
    hellcard = hellcc.credit_card_full()
    
    await edit_or_reply(hellevent, f"__**👤 NAME :- **__\n`{hellname}`\n\n__**🏡 ADDRESS :- **__\n`{helladre}`\n\n__**💸 CARD :- **__\n`{hellcard}`")
    

@hellbot.on(admin_cmd(pattern="bin ?(.*)"))
@hellbot.on(sudo_cmd(pattern="bin ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return 
    input_str = event.pattern_match.group(1)
    chat = "@Carol5_bot"
    await edit_or_reply(event, "`Getting info of your bin... wait a sec`")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1247032902))
              await event.client.send_message(chat, "/bin {}".format(input_str))
              respond = await response 
          except YouBlockedUserError: 
              await event.reply("`You need to unblock` @Carol5_bot `to get this process done`")
              return
          if respond.text.startswith(""):
             await edit_or_reply(event, "`ERROR!`")
          else: 
             
             await event.client.send_message(event.chat_id, respond.message)
    await bot(functions.messages.DeleteHistoryRequest(peer=chat, max_id=0))
    await event.delete()


@hellbot.on(admin_cmd(pattern="vbv ?(.*)"))
@hellbot.on(sudo_cmd(pattern="vbv ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return 
    
    input_str = event.pattern_match.group(1)
    chat = "@Carol5_bot"
    await edit_or_reply(event, "`Ahh! waitt checking`")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1247032902))
              await event.client.send_message(chat, "/vbv {}".format(input_str))
              respond = await response 
          except YouBlockedUserError: 
              await event.reply("`You need to unblock` @Carol5_bot `to get this process done`")
              return
          if respond.text.startswith(""):
             await edit_or_reply(event, "`ERROR!`")
          else: 
              
             await event.client.send_message(event.chat_id, respond.message)
    await bot(functions.messages.DeleteHistoryRequest(peer=chat, max_id=0))
    await event.delete()
    
    
@hellbot.on(admin_cmd(pattern="key ?(.*)"))
@hellbot.on(sudo_cmd(pattern="key ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return 
    
    input_str = event.pattern_match.group(1)
    chat = "@Carol5_bot"
    await edit_or_reply(event, "`Ahh wait! checking`")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1247032902))
              await event.client.send_message(chat, "/key {}".format(input_str))
              response = await response 
          except YouBlockedUserError: 
              await event.reply("`You need to unblock` @Carol5_bot `to get this process done`")
              return
          if response.text.startswith(""):
             await edit_or_reply(event, "`ERROR!`")
          else: 
             await event.client.send_message(event.chat_id, respond.message)
    await bot(functions.messages.DeleteHistoryRequest(peer=chat, max_id=0))
    await event.delete()
 
  
@hellbot.on(admin_cmd(pattern="iban ?(.*)"))
@hellbot.on(sudo_cmd(pattern="iban ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return 
    
    input_str = event.pattern_match.group(1)
    chat = "@Carol5_bot"
    await edit_or_reply(event, "`Ahh wait! checking`")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1247032902))
              await event.client.send_message(chat, "/iban {}".format(input_str))
              response = await response 
          except YouBlockedUserError: 
              await event.reply("`You need to unblock` @Carol5_bot `to get this process done`")
              return
          if response.text.startswith(""):
             await edit_or_reply(event, "`ERROR!`")
          else: 
             await event.client.send_message(event.chat_id, respond.message)
    await bot(functions.messages.DeleteHistoryRequest(peer=chat, max_id=0))
    await event.delete()

    
@hellbot.on(admin_cmd(pattern="ccheck ?(.*)"))
@hellbot.on(sudo_cmd(pattern="ccheck ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return 
    hell_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1247032902))
              await event.client.send_message(chat, f"/ss {hell_input}")
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Please Unblock @carol5_bot")
              return
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)

    
    
CmdHelp("carder").add_command(
  "gencc", None, "Generates fake cc..."
).add_command(
  "ccheck", "<query>", "Checks that the given cc is live or not"
).add_command(
  "iban", "<query>", "Checks that the given IBAN ID is live or not"
).add_command(
  "key", "<query>", "Checks the status of probided key"
).add_command(
  "vbv", "<query>", "Checks the vbv status of given card"
).add_command(
  "bin", "<query>", "Checks that the given bin is valid or not"
).add()