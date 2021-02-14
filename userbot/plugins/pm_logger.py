"""Log Pm messages into a private group

"""
import asyncio
import logging
import os
import sys
from asyncio import sleep

from telethon import events

from userbot import BOTLOG, BOTLOG_CHATID, bot
from userbot.Config import Config
from hellbot.utils import admin_cmd, register
from userbot.cmdhelp import CmdHelp

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.WARN
)

NO_PM_LOG_USERS = []

BOTLOG = True
BOTLOG_CHATID = Config.PM_LOGGR_BOT_API_ID


@bot.on(admin_cmd(pattern=r"save(?: |$)([\s\S]*)", outgoing=True))
async def log(log_text):
    """ For .log command, forwards a message or the command argument to the bot logs group """
    if BOTLOG:
        if log_text.reply_to_msg_id:
            reply_msg = await log_text.get_reply_message()
            await reply_msg.forward_to(BOTLOG_CHATID)
        elif log_text.pattern_match.group(1):
            user = f"#LOG / Chat ID: {log_text.chat_id}\n\n"
            textx = user + log_text.pattern_match.group(1)
            await bot.send_message(BOTLOG_CHATID, textx)
        else:
            await log_text.edit("`What am I supposed to save?`")
            return
        await log_text.edit("`Saved Successfully`")
    else:
        await log_text.edit("`This feature requires Logging to be enabled!`")
    await sleep(2)
    await log_text.delete()


@bot.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def monito_p_m_s(event):
    sender = await event.get_sender()
    if Config.NC_LOG_P_M_S and not sender.bot:
        chat = await event.get_chat()
        if chat.id not in NO_PM_LOG_USERS and chat.id != bot.uid:
            try:
                e = await bot.get_entity(int(Config.PM_LOGGR_BOT_API_ID))
                fwd_message = await bot.forward_messages(e, event.message, silent=True)
            except Exception as e:
                # logger.warn(str(e))
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
                print(e)


@bot.on(admin_cmd(pattern="elog ?(.*)"))
async def set_no_log_p_m(event):
    if Config.PM_LOGGR_BOT_API_ID is not None:
        event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private:
            if chat.id in NO_PM_LOG_USERS:
                NO_PM_LOG_USERS.remove(chat.id)
                await event.edit("Will Log Messages from this chat")
                await asyncio.sleep(3)
                await event.delete()


@bot.on(admin_cmd(pattern="nlog ?(.*)"))
async def set_no_log_p_m(event):
    if Config.PM_LOGGR_BOT_API_ID is not None:
        event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private:
            if chat.id not in NO_PM_LOG_USERS:
                NO_PM_LOG_USERS.append(chat.id)
                await event.edit("Won't Log Messages from this chat")
                await asyncio.sleep(3)
                await event.delete()

CmdHelp("pm_logger").add_command(
  "save", "<reply>", "Saves the replied message to your pm logger group/channel"
).add_command(
  "elog", "<chat>", "Enables logging pm messages from the selected chat."
).add_command(
  "nlog", "<chat>", "Disables logging pm messages from the selected chat. Use .elog to enable it again."
).add()