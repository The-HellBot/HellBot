#"""Update UserBot Code (FOR Hêllẞø† USERBOT)
#Syntax: .update
#\nAll Credits goes to © @Kraken_The_BadASS
#\nFor this awasome plugin.\nPorted from PpaperPlane Extended"""

from os import remove, execle, path, makedirs, getenv, environ
from shutil import rmtree
import asyncio
import sys

from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError

from userbot import CMD_HELP, bot 
from userbot.events import admin_cmd

requirements_path = path.join(
    path.dirname(path.dirname(path.dirname(__file__))), 'requirements.txt')

HEROKU_API_KEY = Var.HEROKU_API_KEY
HEROKU_APP_NAME = Var.HEROKU_APP_NAME
GIT_REPO_NAME = "HellBot"
UPSTREAM_REPO_URL = "https://github.com/HellBoy-OP/HellBot.git"

async def gen_chlog(repo, diff):
    ch_log = ''
    d_form = "On " + "%d/%m/%y" + " at " + "%H:%M:%S"
    for c in repo.iter_commits(diff):
        ch_log += f"**#{c.count()}** : {c.committed_datetime.strftime(d_form)} : [{c.summary}]({UPSTREAM_REPO_URL.rstrip('/')}/commit/{c}) by **{c.author}**\n"
    return ch_log


async def updateme_requirements():
    reqs = str(requirements_path)
    try:
        process = await asyncio.create_subprocess_shell(
            ' '.join([sys.executable, "-m", "pip", "install", "-r", reqs]),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE)
        await process.communicate()
        return process.returncode
    except Exception as e:
        return repr(e)


@borg.on(admin_cmd(pattern="update ?(.*)"))
async def upstream(ups):
    "For .update command, check if the bot is up to date, update if specified"
    await ups.edit("**Wait A Sec.... Checking for new update😋**")
    conf = ups.pattern_match.group(1)
    off_repo = UPSTREAM_REPO_URL
    force_updateme = False

    try:
        txt = "`Oops.. Updater cannot continue as "
        txt += "some problems occured`\n\n**LOGTRACE:**\n"
        repo = Repo()
    except NoSuchPathError as error:
        await ups.edit(f'{txt}\n`directory {error} is not found`')
        repo.__del__()
        return
    except GitCommandError as error:
        await ups.edit(f'{txt}\n`Early failure! {error}`')
        repo.__del__()
        return
    except InvalidGitRepositoryError as error:
        if conf != "now":
            await ups.edit(
                f'**New UPDATE available for [[{ac_br}]]({UPSTREAM_REPO_URL}/tree/{ac_br}):**\n\n' + '**CHANGELOG**\n\n' + f'{changelog}'
            )
            return
        repo = Repo.init()
        origin = repo.create_remote('upstream', off_repo)
        origin.fetch()
        force_updateme = True
        repo.create_head('master', origin.refs.master)
        repo.heads.master.set_tracking_branch(origin.refs.master)
        repo.heads.master.checkout(True)

    ac_br = repo.active_branch.name
    if ac_br != 'master':
        await ups.edit(
            f'**[UPDATER]:**` Looks like you are using your own custom branch ({ac_br}). '
            'in that case, Updater is unable to identify '
             'which branch is to be merged. '
            'Please checkout the official branch of Hêllẞø†`')
        repo.__del__()
        return

    try:
        repo.create_remote('upstream', off_repo)
    except BaseException:
        pass

    ups_rem = repo.remote('upstream')
    ups_rem.fetch(ac_br)

    changelog = await gen_chlog(repo, f'HEAD..upstream/{ac_br}')

    if not changelog and not force_updateme:
        await ups.edit(
            f'\n`Your` __Hêllẞø†__ `is`  **up-to-date**  `with`  **[[{ac_br}]]({UPSTREAM_REPO_URL}/tree/{ac_br})**\n')
        repo.__del__()
        return

    if conf != "now" and not force_updateme:
        changelog_str = f'**New UPDATE available for [[{ac_br}]]({UPSTREAM_REPO_URL}/tree/{ac_br}):**\n\n' + '**CHANGELOG**\n\n' + f'{changelog}'
        if len(changelog_str) > 4096:
            await ups.edit("`Changelog is too big, view the file to see it.`")
            file = open("output.txt", "w+")
            file.write(changelog_str)
            file.close()
            await ups.client.send_file(
                ups.chat_id,
                "output.txt",
                reply_to=ups.id,
            )
            remove("output.txt")
        else:
            await ups.edit(changelog_str)
        await ups.respond(f'Do `.update now` to update')
        return

    if force_updateme:
        await ups.edit(
            '`Force-Updating to latest stable Hêllẞø† code, please wait sur😅😅...`')
    else:
        await ups.edit('`Updating your` **Hêllẞø†** `please wait for 10 mins then type .alive/.ping/.awake/.help/.test to see if I am On... \n\n          __Hêllẞø†__')
    # We're in a Heroku Dyno, handle it's memez.
    if Var.HEROKU_API_KEY is not None:
        import heroku3
        heroku = heroku3.from_key(Var.HEROKU_API_KEY)
        heroku_app = None
        heroku_applications = heroku.apps()
        if not Var.HEROKU_APP_NAME:
            await ups.edit('`Please set up the HEROKU_APP_NAME variable to be able to update Hêllẞø†.`')
            repo.__del__()
            return
        for app in heroku_applications:
            if app.name == Var.HEROKU_APP_NAME:
                heroku_app = app
                break
        if heroku_app is None:
            await ups.edit(
                f'{txt}\n`Invalid Heroku credentials for updating Hêllẞø† dyno.`'
            )
            repo.__del__()
            return
        await ups.edit('`Updated Hêllẞø† Successfully Sur🔥🔥\nRestarting, please wait...5 mins...then type .ping to check if I am On!!!😐`'
                       )
        ups_rem.fetch(ac_br)
        repo.git.reset("--hard", "FETCH_HEAD")
        heroku_git_url = heroku_app.git_url.replace(
            "https://", "https://api:" + Var.HEROKU_API_KEY + "@")
        if "heroku" in repo.remotes:
            remote = repo.remote("heroku")
            remote.set_url(heroku_git_url)
        else:
            remote = repo.create_remote("heroku", heroku_git_url)
        try:
            remote.push(refspec="HEAD:refs/heads/master", force=True)
        except GitCommandError as error:
            await ups.edit(f'{txt}\n`Here is the error log:\n{error}`')
            repo.__del__()
            return
        await ups.edit('`Sync Verified Hêllẞø† Successfully Sur🔥🔥\n'
                       'Restarting, please wait...1 mins...then type .ping to check if I am On!!!😐`')
    else:
        # Classic Updater, pretty straightforward.
        try:
            ups_rem.pull(ac_br)
        except GitCommandError:
            repo.git.reset("--hard", "FETCH_HEAD")
        await updateme_requirements()
        await ups.edit('`Successfully Updated!\n'
                       'Bot is restarting... Wait for a minute!`')
        # Spin a new instance of bot
        args = [sys.executable, "-m", "userbot"]
        execle(sys.executable, *args, environ)
        return
