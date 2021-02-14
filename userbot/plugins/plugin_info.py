# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot plugin_info command """

from userbot import CMD_HELP
from hellbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp


@bot.on(admin_cmd(pattern=r"plinfo(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern=r"plinfo(?: |$)(.*)", allow_sudo=True))
async def info(event):
    """ For .plinfo command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CmdHelp:
            await edit_or_reply(event, str(CmdHelp[args]))
        else:
            await edit_or_reply(event, "Please specify a valid plugin name.")
    else:
        await edit_or_reply(event, "Please specify which plugin do you want help for !!\
            \nUsage: .plinfo <plugin name>"
        )
        string = ""
        for i in CmdHelp:
            string += "`" + str(i)
            string += "`\n"
        await event.reply(string)

CmdHelp("plugin_info").add_command(
  "plinfo", "<plugin name>", "Gives the info triggered plugin. Every Commands with its usage and how to use.."
).add()
