from telethon.utils import pack_bot_file_id


@hellbot_cmd("id", is_args=True)
async def _(hellevent):
    if hellevent.reply_to_msg_id:
        await hellevent.get_input_chat()
        r_msg = await hellevent.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await tgbot.send_message(
                hellevent.chat_id,
                "🔸 **Current Chat ID:** `{}`\n\n🔰 **From User ID:** `{}`\n\n🤖 **Bot API File ID:** `{}`".format(
                    str(hellevent.chat_id), str(r_msg.sender_id), bot_api_file_id
                ),
            )
        else:
            await tgbot.send_message(
                hellevent.chat_id,
                "🔸 **Current Chat ID:** `{}`\n\n🔰 **From User ID:** `{}`".format(
                    str(hellevent.chat_id), str(r_msg.sender_id)
                ),
            )
    else:
        await tgbot.send_message(
            hellevent.chat_id, "🔸 **Current Chat ID:** `{}`".format(str(hellevent.chat_id))
        )
