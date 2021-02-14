import requests
from userbot import CmdHelp
from hellbot.utils import edit_or_reply, admin_cmd, sudo_cmd
import os


@bot.on(admin_cmd(pattern="picgen"))
@bot.on(sudo_cmd(pattern="picgen", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    
    url = "https://thispersondoesnotexist.com/image"
    response = requests.get(url)
    await event.edit("`Creating a fake face...`")
    if response.status_code == 200:
      with open("HELLBOT.jpg", 'wb') as f:
        f.write(response.content)
    
    captin = f"Fake Image By HellBot."
    fole = "HELLBOT.jpg"
    await borg.send_file(event.chat_id, fole, caption=captin)
    await event.delete()
    os.system("rm /root/userbot/HELLBOT.jpg ")