"""Syntax: .whatscrapp as reply to a message copied from @WhatsCRApp"""
from hellbot.utils import *
from userbot.cmdhelp import *
# when you are tight on schedule...
# and also lazy af!!

@bot.on(admin_cmd(pattern="whatscrapp"))
@bot.on(sudo_cmd(pattern="whatscrapp", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        the_real_message = previous_message.text
        event.reply_to_msg_id
        the_real_message = the_real_message.replace("*", "**")
        the_real_message = the_real_message.replace("_", "__")
        await edit_or_reply(event, the_real_message)
    else:
        await edit_or_reply(event, "Reply to a message with `.whatscrapp` to format @WhatsCRApp messages to @Telegram"
        )

CmdHelp("whatscrapp").add_command(
  "whatscrapp", "<reply to a message>", "format @WhatsCRApp messages to @Telegram"
).add()