"""HellBot Help Command"""

from userbot import *
from userbot.cmdhelp import CmdHelp
from userbot.utils import *


@bot.on(admin_cmd(pattern=r"help(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern=r"help(?: |$)(.*)", allow_sudo=True))
async def hellbott(event):
    """ .plinfo cmd """
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CmdHelp:
            await event.edit(str(CmdHelp[args]))
        else:
            await event.edit(["NEED_PLUGIN"])
    else:
        string = ""
        sayfa = [
            sorted(list(CmdHelp))[i : i + 5]
            for i in range(0, len(sorted(list(CmdHelp))), 5)
        ]

        for i in sayfa:
            string += f"`▶️ `"
            for sira, a in enumerate(i):
                string += "`" + str(a)
                if sira == i.index(i[-1]):
                    string += "`"
                else:
                    string += "`, "
            string += "\n"
        await event.edit(["NEED_MODULE"] + "\n\n" + string)
