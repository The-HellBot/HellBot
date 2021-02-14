# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module for purging unneeded messages(usually spam or ot). """

from asyncio import sleep

from telethon.errors import rpcbaseerrors

from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP
from hellbot.utils import admin_cmd, errors_handler, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp



@bot.on(admin_cmd(pattern=r"purge", outgoing=True))
@bot.on(sudo_cmd(pattern=r"purge", allow_sudo=True))
@errors_handler
async def fastpurger(purg):
    """ For .purge command, purge all messages starting from the reply. """
    chat = await purg.get_input_chat()
    msgs = []
    count = 0

    async for msg in purg.client.iter_messages(chat, min_id=purg.reply_to_msg_id):
        msgs.append(msg)
        count = count + 1
        msgs.append(purg.reply_to_msg_id)
        if len(msgs) == 100:
            await purg.client.delete_messages(chat, msgs)
            msgs = []

    if msgs:
        await purg.client.delete_messages(chat, msgs)
    done = await purg.client.send_message(
        purg.chat_id,
        "`Fast purge complete!\n`Purged " + str(count) + " messages.",
    )

    if BOTLOG:
        await purg.client.send_message(
            BOTLOG_CHATID, "Purge of " + str(count) + " messages done successfully."
        )
    await sleep(2)
    await done.delete()


# @register(outgoing=True, pattern="^.purgeme")
@bot.on(admin_cmd(pattern=r"purgeme", outgoing=True))
@bot.on(sudo_cmd(pattern=r"purgeme", allow_sudo=True))
@errors_handler
async def purgeme(delme):
    """ For .purgeme, delete x count of your latest message."""
    message = delme.text
    count = int(message[9:])
    i = 1

    async for message in delme.client.iter_messages(delme.chat_id, from_user="me"):
        if i > count + 1:
            break
        i = i + 1
        await message.delete()

    smsg = await delme.client.send_message(
        delme.chat_id,
        "`Purge complete!` Purged " + str(count) + " messages.",
    )
    if BOTLOG:
        await delme.client.send_message(
            BOTLOG_CHATID, "Purge of " + str(count) + " messages done successfully."
        )
    await sleep(2)
    i = 1
    await smsg.delete()


@bot.on(admin_cmd(pattern=r"sd", outgoing=True))
@bot.on(sudo_cmd(pattern=r"sd", allow_sudo=True))
@errors_handler
async def selfdestruct(destroy):
    """ For .sd command, make seflf-destructable messages. """
    message = destroy.text
    counter = int(message[4:6])
    text = str(destroy.text[6:])
    await destroy.delete()
    smsg = await destroy.client.send_message(destroy.chat_id, text)
    await sleep(counter)
    await smsg.delete()
    if BOTLOG:
        await destroy.client.send_message(BOTLOG_CHATID, "sd query done successfully")