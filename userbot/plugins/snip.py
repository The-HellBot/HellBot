from telethon import events

from userbot import BOTLOG_CHATID
from userbot.plugins.sql_helper.snips_sql import add_snip, get_snips, get_all_snips, remove_snip
from userbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp

#======================IMPORTS======================

hell_users = [bot.uid]
if Config.SUDO_USERS:
    for user in Config.SUDO_USERS:
        hell_users.append(user)

@bot.on(events.NewMessage(pattern=r"\#(\S+)", from_users=hell_users))
async def incom_note(getnt):
    try:
        if not (await getnt.get_sender()).bot:
            notename = getnt.text[1:]
            note = get_snips(notename)
            message_id_to_reply = getnt.message.reply_to_msg_id
            if not message_id_to_reply:
                message_id_to_reply = None
            if note:
                if note.f_mesg_id:
                    msg_o = await bot.get_messages(
                        entity=BOTLOG_CHATID, ids=int(note.f_mesg_id)
                    )
                    await getnt.delete()
                    await bot.send_message(
                        getnt.chat_id,
                        msg_o,
                        reply_to=message_id_to_reply,
                        link_preview=False,
                    )
                elif note.reply:
                    await getnt.delete()
                    await bot.send_message(
                        getnt.chat_id,
                        note.reply,
                        reply_to=message_id_to_reply,
                        link_preview=False,
                    )
    except AttributeError:
        pass

#=========================CONSTANTS=========================

@bot.on(admin_cmd(pattern=r"snips (\w*)"))
@bot.on(sudo_cmd(pattern=r"snips (\w*)", allow_sudo=True))
async def add_snip(fltr):
    keyword = fltr.pattern_match.group(1)
    string = fltr.text.partition(keyword)[2]
    msg = await fltr.get_reply_message()
    msg_id = None
    if msg and msg.media and not string:
        if BOTLOG_CHATID:
            await bot.send_message(
                BOTLOG_CHATID,
                f"#NOTE\
                  \nKEYWORD: `#{keyword}`\
                  \n\nThe following message is saved as the snip in your bot , do NOT delete it !!",
            )
            msg_o = await bot.forward_messages(
                entity=BOTLOG_CHATID, messages=msg, from_peer=fltr.chat_id, silent=True
            )
            msg_id = msg_o.id
        else:
            await edit_or_reply(
                fltr,
                "Saving media as data for the note requires the `PRIVATE_GROUP_BOT_API_ID` to be set.",
            )
            return
    elif fltr.reply_to_msg_id and not string:
        rep_msg = await fltr.get_reply_message()
        string = rep_msg.text
    success = "Note {} is successfully {}. Use` #{} `to get it"
    if add_snip(keyword, string, msg_id) is False:
        remove_snip(keyword)
        if add_snip(keyword, string, msg_id) is False:
            return await edit_or_reply(
                fltr, f"Error in saving the given snip {keyword}"
            )
        return await edit_or_reply(fltr, success.format(keyword, "updated", keyword))
    return await edit_or_reply(fltr, success.format(keyword, "added", keyword))


@bot.on(admin_cmd(pattern="snipl$"))
@bot.on(sudo_cmd(pattern=r"snipl$", allow_sudo=True))
async def on_snip_list(event):
    message = "There are no saved notes in this chat"
    notes = get_all_snips()
    for note in notes:
        if message == "There are no saved notes in this chat":
            message = "Notes saved in this chat:\n"
        message += "👉 `#{}`\n".format(note.keyword)
    if len(message) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(message)) as out_file:
            out_file.name = "snips.text"
            await bot.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption="Available Snips",
                reply_to=event,
            )
            await event.delete()
    else:
        await edit_or_reply(event, message)


@bot.on(admin_cmd(pattern=r"snipd (\S+)"))
@bot.on(sudo_cmd(pattern=r"snipd (\S+)", allow_sudo=True))
async def on_snip_delete(event):
    name = event.pattern_match.group(1)
    hellsnip = get_snips(name)
    if hellsnip:
        remove_snip(name)
    else:
        return await edit_or_reply(
            event, f"Are you sure that #{name} is saved as snip?"
        )
    await edit_or_reply(event, "snip #{} deleted successfully".format(name))



CmdHelp("snip").add_command(
  "snips", "<reply to a message> <notename>", "Saves the replied message as a note with the notename. Works on almost all type of messages. To get the saved snip, type #<notename>"
).add_command(
  "snipl", None, "Gets all saved notes in a chat"
).add_command(
  "snipd", "<notename>", "Deletes the specified note"
).add()