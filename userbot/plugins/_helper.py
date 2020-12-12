from userbot.uniborgConfig import Config

@register(outgoing=True, pattern="^.help")
async def yardim(event):
    tgbotusername = Config.TG_BOT_USER_NAME_BF_HER
    if tgbotusername is not None:
        results = await event.client.inline_query(
            tgbotusername,
            "@HellBot_Official"
        )
        await results[0].click(
            event.chat_id,
            reply_to=event.reply_to_msg_id,
            hide_via=True
        )
        await event.delete()
    else:
        await event.edit(["NO_BOT"])
