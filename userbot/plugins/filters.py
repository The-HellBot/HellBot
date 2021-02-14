"""Filters
Available Commands:
.savefilter
.listfilters
.clearfilter"""
import asyncio
import re
from telethon import events, utils
from telethon.tl import types
from hellbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp
from userbot.plugins.sql_helper.filter_sql import get_filter, add_filter, remove_filter, get_all_filters, remove_all_filters


DELETE_TIMEOUT = 0
TYPE_TEXT = 0
TYPE_PHOTO = 1
TYPE_DOCUMENT = 2


global last_triggered_filters
last_triggered_filters = {}  # pylint:disable=E0602

@bot.on(admin_cmd(incoming=True))
async def on_snip(event):
    global last_triggered_filters
    name = event.raw_text
    if event.chat_id in last_triggered_filters:
        if name in last_triggered_filters[event.chat_id]:
            # avoid userbot spam
            # "I demand rights for us bots, we are equal to you humans." -Henri Koivuneva (t.me/UserbotTesting/2698)
            return False
    snips = get_all_filters(event.chat_id)
    if snips:
        for snip in snips:
            pattern = r"( |^|[^\w])" + re.escape(snip.keyword) + r"( |$|[^\w])"
            if re.search(pattern, name, flags=re.IGNORECASE):
                if snip.snip_type == TYPE_PHOTO:
                    media = types.InputPhoto(
                        int(snip.media_id),
                        int(snip.media_access_hash),
                        snip.media_file_reference
                    )
                elif snip.snip_type == TYPE_DOCUMENT:
                    media = types.InputDocument(
                        int(snip.media_id),
                        int(snip.media_access_hash),
                        snip.media_file_reference
                    )
                else:
                    media = None
                message_id = event.message.id
                if event.reply_to_msg_id:
                    message_id = event.reply_to_msg_id
                await event.reply(
                    snip.reply,
                    file=media
                )
                if event.chat_id not in last_triggered_filters:
                    last_triggered_filters[event.chat_id] = []
                last_triggered_filters[event.chat_id].append(name)
                await asyncio.sleep(DELETE_TIMEOUT)
                last_triggered_filters[event.chat_id].remove(name)


@bot.on(admin_cmd(pattern="savefilter (.*)"))
@bot.on(sudo_cmd(pattern="savefilter (.*)", allow_sudo=True))
async def on_snip_save(event):
    if event.fwd_from:
        return
    name = event.pattern_match.group(1)
    msg = await event.get_reply_message()
    if msg:
        snip = {'type': TYPE_TEXT, 'text': msg.message or ''}
        if msg.media:
            media = None
            if isinstance(msg.media, types.MessageMediaPhoto):
                media = utils.get_input_photo(msg.media.photo)
                snip['type'] = TYPE_PHOTO
            elif isinstance(msg.media, types.MessageMediaDocument):
                media = utils.get_input_document(msg.media.document)
                snip['type'] = TYPE_DOCUMENT
            if media:
                snip['id'] = media.id
                snip['hash'] = media.access_hash
                snip['fr'] = media.file_reference
        add_filter(event.chat_id, name, snip['text'], snip['type'], snip.get('id'), snip.get('hash'), snip.get('fr'))
        await edit_or_reply(event, f"Filter `{name}` saved successfully. Get it with `{name}`")
    else:
        await edit_or_reply(event, "Reply to a message with `savefilter keyword` to save the filter")


@bot.on(admin_cmd(pattern="listfilter$"))
@bot.on(sudo_cmd(pattern="listfilter$", allow_sudo=True))
async def on_snip_list(event):
    if event.fwd_from:
        return
    all_snips = get_all_filters(event.chat_id)
    OUT_STR = "Available Filters in the Current Chat:\n"
    if len(all_snips) > 0:
        for a_snip in all_snips:
            OUT_STR += f"👉 {a_snip.keyword} \n"
    else:
        OUT_STR = "No Filters. Start Saving using `.savefilter`"
    if len(OUT_STR) > 4096:
        with io.BytesIO(str.encode(OUT_STR)) as out_file:
            out_file.name = "filters.text"
            await bot.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption="Available Filters in the Current Chat",
                reply_to=event
            )
            await event.delete()
    else:
        await edit_or_reply(event, OUT_STR)


@bot.on(admin_cmd(pattern="stop (.*)"))
@bot.on(sudo_cmd(pattern="stop (.*)", allow_sudo=True))
async def on_snip_delete(event):
    if event.fwd_from:
        return
    name = event.pattern_match.group(1)
    remove_filter(event.chat_id, name)
    await edit_or_reply(event, f"Filter `{name}` deleted successfully")


@bot.on(admin_cmd(pattern="clearallfilters$"))
@bot.on(sudo_cmd(pattern="clearallfilters$", allow_sudo=True))
async def on_all_snip_delete(event):
    if event.fwd_from:
        return
    remove_all_filters(event.chat_id)
    await edit_or_reply(event, f"All the Filters **in current chat** deleted successfully")
    
CmdHelp("filters").add_command(
  'savefilter', 'reply to a msg with keyword', 'Saves the replied msg as a reply to keyword. The bot will reply that msg wheneverthe keyword is mentioned.'
).add_command(
  'listfilter', None, 'Lists all the filters in chat'
).add_command(
  'clearallfilters', None, 'Deletes all the filter saved in a chat.'
).add_command(
  'stop', 'keyword of saved filter', 'Stops reply to the keyword mentioned.'
).add()
