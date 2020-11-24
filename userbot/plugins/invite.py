#Originally made by @rekcah for @javes05
#porting to hellbot by @kraken_the_badass...
#i asked rekcah before porting...not like other kangers....
#keep credit if u wanna kang...
#else u are a gay...no doubt in that....

#--------------------------------------------------------------------------------------------------------------------------------

import asyncio, time, io, math, os, logging, asyncio, shutil, re, subprocess, json
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from base64 import b64decode
from userbot.utils import admin_cmd
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User
from telethon.tl import functions, types
from telethon.tl.functions.messages import GetHistoryRequest, CheckChatInviteRequest, GetFullChatRequest
from telethon.errors import (ChannelInvalidError, ChannelPrivateError, ChannelPublicGroupNaError, InviteHashEmptyError, InviteHashExpiredError, InviteHashInvalidError)
from telethon.tl.functions.channels import GetFullChannelRequest, GetParticipantsRequest
from telethon.errors import FloodWaitError
from time import sleep
from html import unescape
from urllib.parse import quote_plus
from urllib.error import HTTPError
from telethon import events
from requests import get
from html import unescape
from re import findall
from asyncio import sleep
from telethon.errors.rpcerrorlist import YouBlockedUserError
import random

async def get_chatinfo(event):
    chat = event.pattern_match.group(1)
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id
    try:
        chat_info = await event.client(GetFullChatRequest(chat))
    except:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await event.reply("`Invalid channel/group`")
            return None
        except ChannelPrivateError:
            await event.reply("`This is a private channel/group or I am banned from there`")
            return None
        except ChannelPublicGroupNaError:
            await event.reply("`Channel or supergroup doesn't exist`")
            return None
        except (TypeError, ValueError) as err:
            await event.reply("`Invalid channel/group`")
            return None
    return chat_info



def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    full_name = ' '.join(names)
    return full_name


@borg.on(admin_cmd(pattern=r"inviteall ?(.*)"))
async def get_users(event):   
    sender = await event.get_sender() ; me = await event.client.get_me()
    if not sender.id == me.id:
        hell = await event.reply("`processing...`")
    else:
    	hell = await event.edit("`processing...`")
    kraken = await get_chatinfo(event) ; chat = await event.get_chat()
    if event.is_private:
              return await hell.edit("`Sorry, Can add users here`")    
    s = 0 ; f = 0 ; error = 'None'   
  
    await hell.edit("**TerminalStatus**\n\n`Collecting Users.......`")
    async for user in event.client.iter_participants(kraken.full_chat.id):
                try:
                    if error.startswith("Too"):
                        return await hell.edit(f"**Terminal Finished With Error**\n(`May Got Limit Error from telethon Please try agin Later`)\n**Error** : \n`{error}`\n\n• Invited `{s}` people \n• Failed to Invite `{f}` people")
                    await event.client(functions.channels.InviteToChannelRequest(channel=chat,users=[user.id]))
                    s = s + 1                                                    
                    await hell.edit(f"**Terminal Running...**\n\n• Invited `{s}` people \n• Failed to Invite `{f}` people\n\n**× LastError:** `{error}`")                
                except Exception as e:
                    error = str(e) ; f = f + 1             
    return await hell.edit(f"**Terminal Finished** \n\n• Successfully Invited `{s}` people \n• failed to invite `{f}` people")


@bot.on(admin_cmd(pattern="add ?(.*)"))
@bot.on(sudo_cmd(pattern="add ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    to_add_users = event.pattern_match.group(1)
    if event.is_private:
        await edit_delete(
            event, "`.add` users to a chat, not to a Private Message", 5
        )
    else:
        if not event.is_channel and event.is_group:
            # https://lonamiwebs.github.io/Telethon/methods/messages/add_chat_user.html
            for user_id in to_add_users.split(" "):
                try:
                    await event.client(
                        functions.messages.AddChatUserRequest(
                            chat_id=event.chat_id, user_id=user_id, fwd_limit=1000000
                        )
                    )
                except Exception as e:
                    await edit_delete(event, f"`{str(e)}`", 5)
        else:
            # https://lonamiwebs.github.io/Telethon/methods/channels/invite_to_channel.html
            for user_id in to_add_users.split(" "):
                try:
                    await event.client(
                        functions.channels.InviteToChannelRequest(
                            channel=event.chat_id, users=[user_id]
                        )
                    )
                except Exception as e:
                    await edit_delete(event, f"`{str(e)}`", 5)

        await edit_or_reply(event, f"`Added {to_add_users} Successfully😄`")


CMD_HELP.update(
    {
        "invite": """**Plugin : **`invite`
  •  **Syntax : **`.add username(s)/userid(s)`
  •  **Function : **__Add the given user/users to the group where u used the command__
  •  **Syntax : **`.inviteall groups username`
  •  **Function : **__Scrapes users from the given chat to your group__
"""
    }
)
