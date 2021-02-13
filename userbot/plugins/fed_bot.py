import logging

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)
import asyncio
import os

from telethon.tl.types import InputMediaUploadedPhoto
from telethon.tl.functions.messages import DeleteHistoryRequest

from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from telethon import functions, types, events
from hellbot import CmdHelp, bot as hellbot
from hellbot.utils import admin_cmd, sudo_cmd, edit_or_reply as eor
from hellbot.Config import Config
from hellbot.plugins.sql_helper.fban_sql import (
    add_channel,
    get_all_channels,
    in_channels,
    rm_channel,
)

logs_id = Config.FBAN_LOGGER_GROUP
bot = "@MissRose_bot"
hell_logo = "./KRAKEN/hellbot_logo.jpg"
# Keep all credits pls
# madewith great effort by @HeisenbergTheDanger
# modified by @kraken_the_badass for fbans


@hellbot.on(admin_cmd(pattern="fban ?(.*)"))
@hellbot.on(sudo_cmd(pattern="fban ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    mssg = await eor(event, "`...`")
    if not event.is_reply:
        await mssg.edit("Reply to a message to start fban....")
        return
    channels = get_all_channels()
    error_count = 0
    sent_count = 0
    await mssg.edit("Fbanning....")
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.sticker or previous_message.poll:
            await mssg.edit("**ERROR !** \nOnly Text Message is supported for fban.")
            return
        if (
            previous_message.gif
            or previous_message.audio
            or previous_message.voice
            or previous_message.video
            or previous_message.video_note
            or previous_message.contact
            or previous_message.game
            or previous_message.geo
            or previous_message.invoice
        ):  # Written by @HeisenbergTheDanger
            await mssg.edit("**ERROR !** \nOnly Text Message is supported for fban.")
            return
        if not previous_message.web_preview and previous_message.photo:
            file = await borg.download_file(previous_message.media)
            uploaded_doc = await borg.upload_file(file, file_name="img.png")
            raw_text = previous_message.text
            for channel in channels:
                try:
                    if previous_message.photo:
                        await borg.send_file(
                            int(channel.chat_id),
                            InputMediaUploadedPhoto(file=uploaded_doc),
                            force_document=False,
                            caption=raw_text,
                            link_preview=False,
                        )

                    sent_count += 1
                    await mssg.edit(
                        f"Fbanned : {sent_count}\nError : {error_count}\nTotal : {len(channels)}",
                    )
                except Exception as error:
                    try:
                        await borg.send_message(
                            logs_id, f"Error in Fbanning at {chat_id}."
                        )
                        await borg.send_message(logs_id, "Error! " + str(error))
                        if (
                            error
                            == "The message cannot be empty unless a file is provided"
                        ):
                            mssg.edit(
                                "**ERROR !** \nOnly Text Message is supported for fban."
                            )
                            return
                    except BaseException:
                        pass
                    error_count += 1
                    await mssg.edit(
                        f"Fbanned : {sent_count}\nError : {error_count}\nTotal : {len(channels)}",
                    )
            await mssg.edit(f"{sent_count} fbans with {error_count} errors.")
            if error_count > 0:
                try:
                    await borg.send_message(logs_id, f"{error_count} Errors")
                except BaseException:
                    pass
        else:
            raw_text = previous_message.text
            for channel in channels:
                try:
                    await borg.send_message(
                        int(channel.chat_id), raw_text, link_preview=False
                    )
                    sent_count += 1
                    await mssg.edit(
                        f"Fbanned : {sent_count}\nError : {error_count}\nTotal : {len(channels)}",
                    )
                except Exception as error:
                    try:
                        await borg.send_message(
                            logs_id, f"Error in Fbanning at {channel.chat_id}."
                        )
                        await borg.send_message(logs_id, "Error! " + str(error))
                        if (
                            error
                            == "The message cannot be empty unless a file is provided"
                        ):
                            mssg.edit(
                                "**ERROR !** \nOnly Text Message is supported for fban."
                            )
                            return
                    except BaseException:
                        pass
                    error_count += 1
                    await mssg.edit(
                        f"Fbanned : {sent_count}\nError : {error_count}\nTotal : {len(channels)}",
                    )
            await mssg.edit(f"{sent_count} fbans with {error_count} errors.")
            if error_count > 0:
                try:
                    await borg.send_message(logs_id, f"{error_count} Errors")
                except BaseException:
                    await mssg.edit("Set up heroku var `FBAN_LOGGER_GROUP` for checking errors.")# Written by @HeisenbergTheDanger

@hellbot.on(admin_cmd(pattern="unfban ?(.*)"))
@hellbot.on(sudo_cmd(pattern="unfban ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    mssg = await eor(event, "`...`")
    if not event.is_reply:
        await mssg.edit("Reply to a message to start unfban....")
        return
    channels = get_all_channels()
    error_count = 0
    sent_count = 0
    await mssg.edit("Unfbanning....")
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.sticker or previous_message.poll:
            await mssg.edit("**ERROR !** \nOnly Text Message is supported for unfban.")
            return
        if (
            previous_message.gif
            or previous_message.audio
            or previous_message.voice
            or previous_message.video
            or previous_message.video_note
            or previous_message.contact
            or previous_message.game
            or previous_message.geo
            or previous_message.invoice
        ):  # Written by @HeisenbergTheDanger
            await mssg.edit("**ERROR !** \nOnly Text Message is supported for unfban.")
            return
        if not previous_message.web_preview and previous_message.photo:
            file = await borg.download_file(previous_message.media)
            uploaded_doc = await borg.upload_file(file, file_name="img.png")
            raw_text = previous_message.text
            for channel in channels:
                try:
                    if previous_message.photo:
                        await borg.send_file(
                            int(channel.chat_id),
                            InputMediaUploadedPhoto(file=uploaded_doc),
                            force_document=False,
                            caption=raw_text,
                            link_preview=False,
                        )

                    sent_count += 1
                    await mssg.edit(
                        f"Unfbanned : {sent_count}\nError : {error_count}\nTotal : {len(channels)}",
                    )
                except Exception as error:
                    try:
                        await borg.send_message(
                            logs_id, f"Error in Unfbanning at {chat_id}."
                        )
                        await borg.send_message(logs_id, "Error! " + str(error))
                        if (
                            error
                            == "The message cannot be empty unless a file is provided"
                        ):
                            mssg.edit(
                                "**ERROR !** \nOnly Text Message is supported for unfban."
                            )
                            return
                    except BaseException:
                        pass
                    error_count += 1
                    await mssg.edit(
                        f"Unfbanned : {sent_count}\nError : {error_count}\nTotal : {len(channels)}",
                    )
            await mssg.edit(f"{sent_count} unfbans with {error_count} errors.")
            if error_count > 0:
                try:
                    await borg.send_message(logs_id, f"{error_count} Errors")
                except BaseException:
                    pass
        else:
            raw_text = previous_message.text
            for channel in channels:
                try:
                    await borg.send_message(
                        int(channel.chat_id), raw_text, link_preview=False
                    )
                    sent_count += 1
                    await mssg.edit(
                        f"Unfbanned : {sent_count}\nError : {error_count}\nTotal : {len(channels)}",
                    )
                except Exception as error:
                    try:
                        await borg.send_message(
                            logs_id, f"Error in Unfbanning at {channel.chat_id}."
                        )
                        await borg.send_message(logs_id, "Error! " + str(error))
                        if (
                            error
                            == "The message cannot be empty unless a file is provided"
                        ):
                            mssg.edit(
                                "**ERROR !** \nOnly Text Message is supported for unfban."
                            )
                            return
                    except BaseException:
                        pass
                    error_count += 1
                    await mssg.edit(
                        f"Unfanned : {sent_count}\nError : {error_count}\nTotal : {len(channels)}",
                    )
            await mssg.edit(f"{sent_count} unfbans with {error_count} errors.")
            if error_count > 0:
                try:
                    await borg.send_message(logs_id, f"{error_count} Errors")
                except BaseException:
                    await mssg.edit("Set up heroku var `FBAN_LOGGER_GROUP` for checking errors.")


@hellbot.on(admin_cmd(pattern=r"fadd ?(.*)"))
@hellbot.on(sudo_cmd(pattern=r"fadd ?(.*)", allow_sudo=True))
async def add_ch(event):
    if event.fwd_from:
        return
    if (
        "addcf" in event.raw_text.lower()
        or "addblacklist" in event.raw_text.lower()
    ):  # fix for ".addcf" in lydia and ".addblacklist"
        return
    if event.reply_to_msg_id:
        await eor(event, "Adding...")
        previous_message = await event.get_reply_message()
        raw_text = previous_message.text
        lines = raw_text.split("\n")
        length = len(lines)
        for line_number in range(1, length - 2):
            channel_id = lines[line_number][4:-1]
            if not in_channels(channel_id):
                add_channel(channel_id)
        await eor(event, "Fban Group added!")
        await asyncio.sleep(3)
        await event.delete()
        return
    chat_id = event.chat_id
    try:
        if int(chat_id) == logs_id:
            return
    except BaseException:
        pass
    if not in_channels(chat_id):
        add_channel(chat_id)
        await eor(event, "`Added to Fban database!`")
        await asyncio.sleep(3)
        await event.delete()
    elif in_channels(chat_id):
        await eor(event, "`Group is already in fban database!`")
        await asyncio.sleep(3)
        await event.delete()


@hellbot.on(admin_cmd(pattern=r"fremove ?(.*)"))
@hellbot.on(sudo_cmd(pattern=r"fremove ?(.*)", allow_sudo=True))
async def remove_ch(event):
    if event.fwd_from:
        return
    chat_id = event.pattern_match.group(1)
    if chat_id == "all":
        await eor(event, "Removing...")
        channels = get_all_channels()
        for channel in channels:
            rm_channel(channel.chat_id)
        await eor(event, "All Fban Database cleared.")
        return
    if in_channels(chat_id):
        rm_channel(chat_id)
        await eor(event, "Removed from fban database")
        await asyncio.sleep(3)
        await event.delete()
    elif in_channels(event.chat_id):
        rm_channel(event.chat_id)
        await eor(event, "Removed from fban database")
        await asyncio.sleep(3)
        await event.delete()
    elif not in_channels(event.chat_id):
        await eor(event, "Group is already removed from fban database. ")
        await asyncio.sleep(3)
        await event.delete()


@hellbot.on(admin_cmd(pattern="fgroups"))
@hellbot.on(sudo_cmd(pattern="fgroups", allow_sudo=True))
async def list(event):
    if event.fwd_from:
        return
    channels = get_all_channels()
    msg = "**Groups in fban database:**\n\n"
    for channel in channels:
        msg += f"=> `{channel.chat_id}`\n"
    msg += f"\nTotal {len(channels)} fed groups.\n"
    msg += f"\n**[ NOTE ] :-** Do .fsearch <grp id> to get the details of that grp if added to fban database."
    if len(msg) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(msg)) as out_file:
            out_file.name = "fedgrp.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption="Fed Groups in database",
                reply_to=event,
            )
            await event.delete()
    else:
        await eor(event, msg)


@hellbot.on(admin_cmd(pattern="fsearch ?(.*)"))
@hellbot.on(sudo_cmd(pattern="fsearch ?(.*)", allow_sudo=True))
async def search(event):
    if event.fwd_from:
        return
    channel_id = event.pattern_match.group(1)
    try:
        channel = await borg.get_entity(int(channel_id))
    except ValueError:
        await eor(event, "Invalid id.")
        return
    except BaseException:
        return
    name = channel.title
    username = channel.username
    if username:
        username = "@" + username
    await eor(event, f"Name : {name}\nUsername: {username}")

#----------------------------------------------------------------------------------------------------------------------------------------------

@hellbot.on(admin_cmd(pattern="newfed ?(.*)", outgoing=True))
@hellbot.on(sudo_cmd(pattern="newfed ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    hell_input = event.pattern_match.group(1)
    chat = "@MissRose_Bot"
    await eor(event, "`Making new fed...`")
    async with borg.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=609517172)
            )
            await event.client.send_message(chat, f"/newfed {hell_input}")
            response = await response
        except YouBlockedUserError:
            await eor(event, "`Please unblock` @MissRose_Bot `and try again`")
            return
        if response.text.startswith("You already have a federation"):
            await event.edit(
                "You already have a federation. Do .renamefed to rename your current fed."
            )
        else:
            await eor(event, f"{response.message.message}")


@hellbot.on(admin_cmd(pattern="renamefed ?(.*)"))
@hellbot.on(sudo_cmd(pattern="renamefed ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return 
    hell_input = event.pattern_match.group(1)
    chat = "@MissRose_Bot"
    await event.edit("`Trying to rename your fed...`")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=609517172))
              await event.client.send_message(chat, f"/renamefed {hell_input}")
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Please Unblock @MissRose_Bot")
              return
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)


@hellbot.on(admin_cmd(pattern="fstat ?(.*)"))
@hellbot.on(sudo_cmd(pattern="fstat ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    hell = await event.edit("`Collecting fstat....`")
    thumb = hell_logo
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        lavde = str(previous_message.sender_id)
        user = f"[user](tg://user?id={lavde})"
    else:
        lavde = event.pattern_match.group(1)
        user = lavde
    if lavde == "":
        await hell.edit(
            "`Need username/id to check fstat`"
        )
        return
    else:
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fedstat " + lavde)
                massive = await conv.get_response()
                if "Looks like" in massive.text:
                    await massive.click(0)
                    await asyncio.sleep(2)
                    massive = await conv.get_response()
                    await hellbot.send_file(
                        event.chat_id,
                        massive,
                        thumb=thumb,
                        caption=f"List of feds {user} has been banned in.\n\n**⚡ [Collected using Hêllẞø†](t.me/hellbot_official) ⚡**",
                    )
                else:
                    await borg.send_message(event.chat_id, massive.text)
                await event.delete()
            except YouBlockedUserError:
                await hell.edit("`Please Unblock` @MissRose_Bot")


@hellbot.on(admin_cmd(pattern="fedinfo ?(.*)"))
@hellbot.on(sudo_cmd(pattern="fedinfo ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    hell = await eor(event, "`Fetching fed info.... please wait`")
    lavde = event.pattern_match.group(1)
    async with borg.conversation(bot) as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message("/fedinfo " + lavde)
            massive = await conv.get_response()
            await hell.edit(massive.text + "\n\n**ʟɛɢɛռɖaʀʏ_ᴀғ_ɦɛʟʟɮօt**")
        except YouBlockedUserError:
            await hell.edit("`Please Unblock` @MissRose_Bot")
            

CmdHelp("fed_bot").add_command(
  "fban", "<reply to a msg>", "Forwards the replied fban msg to all groups added in your Fed Database", "Click` [here](https://telegra.ph/file/ab848eb3a3b4b94dfc726.jpg) `for an example"
).add_command(
  "fsearch", "<grp id>", "Gives out the username and group's name of the given group id.(IF ADDED IN FBAN DATABASE)"
).add_command(
  "fgroups", None, "Gives out the list of group ids you have connected to fban database"
).add_command(
  "fremove", "<group id> or in a group", "Removes the group from your fban database."
).add_command(
  "fremove all", None, "Removes the group from your fban database."
).add_command(
  "fadd", None, "Adds the group in your fban database."
).add_command(
  "unfban", "<reply to msg>", "Forwards the replied` /unfban <id>/<usrname> `to all groups added in your fban database", "reply to a msg (/unfban id/username)"
).add_command(
  "newfed", "<newfed name>", "Makes a federation of Rose bot"
).add_command(
  "renamefed", "<new name>", "Renames the fed of Rose Bot"
).add_command(
  "fstat", "<username/id>", "Gets the fban stats of the user from rose bot federation"
).add_command(
  "fedinfo", "<fed id>", "Gives details of the given fed id"
).add()
