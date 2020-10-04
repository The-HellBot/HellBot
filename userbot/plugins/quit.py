
"""
.quit
"""
from telethon.tl.functions.channels import LeaveChannelRequest
from userbot.utils import admin_cmd
import time

@borg.on(admin_cmd("quit", outgoing=True))
async def leave(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`I am leaving this chat😒..koi ni hai yaha apna I hate you all🙄..huh!!`")
        time.sleep(3)
        if '-' in str(e.chat_id):
            await borg(LeaveChannelRequest(e.chat_id))
        else:
            await e.edit('`Mere pyaare boss ye chat nahi hai..thoda soch samajh kar command dijiye..🤥`')
