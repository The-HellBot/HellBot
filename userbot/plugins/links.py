import requests

from userbot import CMD_HELP
from hellbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp


@bot.on(admin_cmd(pattern="dns (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="dns (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/dns/{}".format(input_str)
    response_api = requests.get(sample_url).text
    if response_api:
        await edit_or_reply(event, "DNS records of [This link]({}) are \n{}".format(input_str, response_api, link_preview=False))
    else:
        await edit_or_reply(event, "i can't seem to find [this link]({}) on the internet".format(input_str, link_preview=False))


@bot.on(admin_cmd(pattern="url (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="url (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/s?url={}".format(input_str)
    response_api = requests.get(sample_url).text
    if response_api:
        await edit_or_reply(event, "Generated [short link]({}) \nOf [this link]({})".format(response_api, input_str, link_preview=True))
    else:
        await edit_or_reply(event, "something is wrong. please try again later.")


@bot.on(admin_cmd(pattern="unshort (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="unshort (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if not input_str.startswith("http"):
        input_str = "http://" + input_str
    r = requests.get(input_str, allow_redirects=False)
    if str(r.status_code).startswith("3"):
        await edit_or_reply(event, "Input URL: [Short Link]({}) \nReDirected URL: [Long link]({})".format(input_str, r.headers["Location"], link_preview=False)
        )
    else:
        await edit_or_reply(event, 
            "Input URL [short link]({}) returned status_code {}".format(input_str, r.status_code)
        )


CmdHelp("links").add_command(
  "dns", "<link>", "Shows you Domain Name System (DNS) of the given link", ".dns google.com"
).add_command(
  "unshort", "<link>", "Unshortens the given short link"
).add_command(
  "url", "<link>", "Shortens the given long link"
).add()
