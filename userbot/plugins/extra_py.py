import os
from pathlib import Path

from telethon.tl.types import InputMessagesFilterDocument

from hellbot.utils import admin_cmd, load_module
from var import Var
from userbot.cmdhelp import CmdHelp

@borg.on(admin_cmd(pattern="extdl$", outgoing=True))
async def install(event):
    if event.fwd_from:
        return
    chat = Var.PLUGIN_CHANNEL
    documentss = await borg.get_messages(chat, None, filter=InputMessagesFilterDocument)
    total = int(documentss.total)
    total_doxx = range(0, total)
    await event.delete()
    for ixo in total_doxx:
        mxo = documentss[ixo].id
        downloaded_file_name = await event.client.download_media(
            await borg.get_messages(chat, ids=mxo), "userbot/plugins/"
        )
        if "(" not in downloaded_file_name:
            path1 = Path(downloaded_file_name)
            shortname = path1.stem
            load_module(shortname.replace(".py", ""))
            await borg.send_message(
                event.chat_id,
                "Installed Plugin `{}` successfully.".format(
                    os.path.basename(downloaded_file_name)
                ),
            )
        else:
            await borg.send_message(
                event.chat_id,
                "Plugin `{}` has been pre-installed and cannot be installed.".format(
                    os.path.basename(downloaded_file_name)
                ),
            )


@borg.on(admin_cmd("installall (.*)"))
async def install(event):
    if event.fwd_from:
        return
    chat = event.pattern_match.group(1)
    await event.edit(
        f"Starting To Install Plugins From {chat} ! Check PRIVATE GROUP for More Info !"
    )
    documentss = await borg.get_messages(chat, None, filter=InputMessagesFilterDocument)
    total = int(documentss.total)
    total_doxx = range(0, total)
    for ixo in total_doxx:
        mxo = documentss[ixo].id
        downloaded_file_name = await event.client.download_media(
            await borg.get_messages(chat, ids=mxo), "userbot/plugins/"
        )
        if "(" not in downloaded_file_name:
            path1 = Path(downloaded_file_name)
            shortname = path1.stem
            load_module(shortname.replace(".py", ""))
            sed = f"Installing Plugins From {chat}"
            logger.info(sed)
            await borg.send_message(
                event.chat_id,
                "Installed Plugin `{}` successfully.".format(
                    os.path.basename(downloaded_file_name)
                ),
            )
        else:
            await borg.send_message(
                event.chat_id,
                "Plugin `{}` has been pre-installed and cannot be installed.".format(
                    os.path.basename(downloaded_file_name)
                ),
            )

CmdHelp("extra_py").add_command(
  'extdl', None, 'Installs all plugins from the channal which id is in PLUGIN_CHANNEL variable'
).add_command(
  'installall', '<channel/grp username>', 'Installs all the plugins in provided channel / group. (May get floodwait error)'
).add()