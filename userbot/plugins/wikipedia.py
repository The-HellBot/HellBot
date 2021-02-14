# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""WikiPedia.ORG
Syntax: .wikipedia Query"""

import wikipedia
from hellbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp

@bot.on(admin_cmd(pattern="wikipedia (.*)"))
@bot.on(sudo_cmd(pattern="wikipedia (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    await edit_or_reply(event, "Processing ...")
    input_str = event.pattern_match.group(1)
    result = ""
    results = wikipedia.search(input_str)
    for s in results:
        page = wikipedia.page(s)
        url = page.url
        result += f"> [{s}]({url}) \n"
    await edit_or_reply(event, "WikiPedia **Search**: {} \n\n **Result**: \n\n{}".format(input_str, result)
    )
    
CmdHelp("wikipedia").add_command(
  "wikipedia", "<query>", "Searches for the query from Wikipedia"
).add()
