import asyncio

import coffeehouse
from coffeehouse.lydia import LydiaAI
from telethon import events

from hellbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp

# Non-SQL Mode
ACC_LYDIA = {}
SESSION_ID = {}

if Var.LYDIA_API_KEY:
    api_key = Var.LYDIA_API_KEY
    api_client = coffeehouse.API(api_key)
    Lydia = LydiaAI(api_client)


@bot.on(admin_cmd(pattern="repcf", outgoing=True))
@bot.on(sudo_cmd(pattern="repcf", allow_sudo=True))
async def repcf(event):
    if event.fwd_from:
        return
    await edit_or_reply(event, "Processing...")
    try:
        session = Lydia.create_session()
        session_id = session.id
        reply = await event.get_reply_message()
        msg = reply.text
        text_rep = session.think_thought((session_id, msg))
        await edit_or_reply(event, " {0}".format(text_rep))
    except Exception as e:
        await edit_or_reply(event, str(e))


@bot.on(admin_cmd(pattern="eai", outgoing=True))
@bot.on(sudo_cmd(pattern="eai", allow_sudo=True))
async def addcf(event):
    if event.fwd_from:
        return
    await edit_or_reply(event, "Running on Non-SQL mode for now...")
    await asyncio.sleep(3)
    await edit_or_reply(event, "Processing...")
    reply_msg = await event.get_reply_message()
    if reply_msg:
        session = Lydia.create_session()
        session_id = session.id
        ACC_LYDIA.update({str(event.chat_id) + " " + str(reply_msg.sender_id): session})
        SESSION_ID.update(
            {str(event.chat_id) + " " + str(reply_msg.sender_id): session_id}
        )
        await edit_or_reply(event, 
            "Lydia successfully enabled for user: {} in chat: {}".format(
                str(reply_msg.sender_id), str(event.chat_id)
            )
        )
    else:
        await edit_or_reply(event, "Reply to a user to activate Lydia AI on them")


@bot.on(admin_cmd(pattern="dai", outgoing=True))
@bot.on(sudo_cmd(pattern="dai", allow_sudo=True))
async def remcf(event):
    if event.fwd_from:
        return
    await edit_or_reply(event, "Running on Non-SQL mode for now...")
    await asyncio.sleep(3)
    await edit_or_reply(event, "Processing...")
    reply_msg = await event.get_reply_message()
    try:
        del ACC_LYDIA[str(event.chat_id) + " " + str(reply_msg.sender_id)]
        del SESSION_ID[str(event.chat_id) + " " + str(reply_msg.sender_id)]
        await edit_or_reply(event, 
            "Lydia successfully disabled for user: {} in chat: {}".format(
                str(reply_msg.sender_id), str(event.chat_id)
            )
        )
    except KeyError:
        await edit_or_reply(event, "This person does not have Lydia activated on him/her.")


@bot.on(events.NewMessage(incoming=True))
async def user(event):
    event.text
    try:
        session = ACC_LYDIA[str(event.chat_id) + " " + str(event.sender_id)]
        session_id = SESSION_ID[str(event.chat_id) + " " + str(event.sender_id)]
        msg = event.text
        async with event.client.action(event.chat_id, "typing"):
            text_rep = session.think_thought((session_id, msg))
            wait_time = 0
            for i in range(len(text_rep)):
                wait_time = wait_time + 0.1
            await asyncio.sleep(wait_time)
            await event.reply(text_rep)
    except KeyError:
        return

CmdHelp("lydia").add_command(
  "eai", "<reply to user>", "Your bot will auto reply to the tagged user. Until you disables it."
).add_command(
  "dai", "<reply to user>", "Your bot will stop auto reply to the tagged user (if enabled)."
).add()
