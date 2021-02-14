import requests

from hellbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp


@bot.on(admin_cmd(pattern="ytube (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="ytube (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = (
        "https://da.gd/s?url=https://www.youtube.com/results?search_query={}".format(
            input_str.replace(" ", "+")
        )
    )
    response_api = requests.get(sample_url).text
    if response_api:
        await edit_or_reply(event, "Let me **UThoob** that for you:\n👉 [{}]({})\n`Thank me later 😉` ".format(
                input_str, response_api.rstrip()
            )
        )
    else:
        await edit_or_reply(event, "Something went wrong. Please try again later.")


@bot.on(admin_cmd(pattern="ddg (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="ddg (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = (
        "https://da.gd/s?url=https://duckduckgo.com/?q={}&t=h_&ia=about".format(
            input_str.replace(" ", "+")
        )
    )
    response_api = requests.get(sample_url).text
    if response_api:
        await edit_or_reply(event, "Let me **duckduckgo** that for you:\n👉 [{}]({})\n`Thank me later 😉` ".format(
                input_str, response_api.rstrip()
            )
        )
    else:
        await edit_or_reply(event, "Something went wrong. Please try again later.")


@bot.on(admin_cmd(pattern="altn (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="altn (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/s?url=https://www.altnews.in/?s={}".format(
        input_str.replace(" ", "+")
    )
    response_api = requests.get(sample_url).text
    if response_api:
        await edit_or_reply(event, "Let me **altnews** that for you:\n👉 [{}]({})\n`Thank me later 😉` ".format(
                input_str, response_api.rstrip()
            )
        )
    else:
        await edit_or_reply(event, "Something went wrong. Please try again later.")


@bot.on(admin_cmd(pattern="var (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="var (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = (
        "https://da.gd/s?url=https://dashboard.heroku.com/apps/{}/settings".format(
            input_str.replace(" ", "+")
        )
    )
    response_api = requests.get(sample_url).text
    if response_api:
        await edit_or_reply(event, "Let me **var** that for you:\n👉 [{}]({})\n`Thank me later 😉` ".format(
                input_str, response_api.rstrip()
            )
        )
    else:
        await edit_or_reply(event, "Something went wrong. Please try again later.")


@bot.on(admin_cmd(pattern="lmlog (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="lmlog (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/s?url=https://dashboard.heroku.com/apps/{}/logs".format(
        input_str.replace(" ", "+")
    )
    response_api = requests.get(sample_url).text
    if response_api:
        await edit_or_reply(event, "Let me **log** that for you:\n👉 [{}]({})\n`Thank me later 😉` ".format(
                input_str, response_api.rstrip()
            )
        )
    else:
        await edit_or_reply(event, "Something went wrong. Please try again later.")


@bot.on(admin_cmd(pattern="hacc (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="hacc (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/s?url=https://dashboard.heroku.com/account/{}".format(
        input_str.replace(" ", "+")
    )
    response_api = requests.get(sample_url).text
    if response_api:
        await edit_or_reply(event, "Let me **Heroku Account** that for you:\n👉 [{}]({})\n`Thank me later 😉` ".format(
                input_str, response_api.rstrip()
            )
        )
    else:
        await edit_or_reply(event, "Something went wrong. Please try again later.")


@bot.on(admin_cmd(pattern="lmkp (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="lmkp (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/s?url=https://indiankanoon.org/search/?formInput={}+sortby%3Amostrecent".format(
        input_str.replace(" ", "+")
    )
    response_api = requests.get(sample_url).text
    if response_api:
        await edit_or_reply(event, "Let me **Indiankanoon.com : Place** that for you:\n👉 [{}]({})\n`Thank me later 😉` ".format(
                input_str, response_api.rstrip()
            )
        )
    else:
        await edit_or_reply(event, "Something went wrong. Please try again later.")


@bot.on(admin_cmd(pattern="gem (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="gem (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/s?url=https://mkp.gem.gov.in/search?q={}&sort_type=created_at_desc&_xhr=1".format(
        input_str.replace(" ", "+")
    )
    response_api = requests.get(sample_url).text
    if response_api:
        await edit_or_reply(event, "Let me **gem.gov.in** that for you:\n👉 [{}]({})\n`Thank me later 😉` ".format(
                input_str, response_api.rstrip()
            )
        )
    else:
        await edit_or_reply(event, "Something went wrong. Please try again later.")


@bot.on(admin_cmd(pattern="rchiv (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="rchiv (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/s?url=https://web.archive.org/web/*/{}".format(
        input_str.replace(" ", "+")
    )
    response_api = requests.get(sample_url).text
    if response_api:
        await edit_or_reply(event, "Let me run your link on wayback machine that for you:\n👉 [{}]({})\n`Thank me later 😉` ".format(
                input_str, response_api.rstrip()
            )
        )
    else:
        await edit_or_reply(event, "Something went wrong. Please try again later.")


CmdHelp("search").add_command(
  "rchiv", "<query>", "Gives you the archive link of given query from WayBack Machine"
).add_command(
  "gem", "<query>", "Gives you the link of given query from Government e-Marketplace (gem.gov.in)"
).add_command(
  "lmkp", "<query>", "Gives you the link of given query from Indiankanoon.org"
).add_command(
  "hacc", None, "Redirects you to your heroku account"
).add_command(
  "lmlog", None, "Redirects you to your app's log page"
).add_command(
  "var", None, "Redirects you to your app's var section"
).add_command(
  "ytube", "<query>", "Gives you the link of given query from youthube"
).add_command(
  "altn", "<query>", "Gives you the link for given query from Alt News"
).add_command(
  "ddg", "<query>", "Gives you the link for given query from Duckduckgo"
).add()