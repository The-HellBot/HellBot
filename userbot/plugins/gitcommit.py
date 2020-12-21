"""
GITHUB File Uploader Plugin for userbot. Heroku Automation should be Enabled. Else u r not that lazy // For lazy people
Instructions:- Set GITHUB_ACCESS_TOKEN and GIT_REPO_NAME Variables in Heroku vars First
usage:- .commit reply_to_any_plugin //can be any type of file too. but for plugin must be in .py 
"""


import os
import time
from datetime import datetime

from github import Github

from userbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp

GIT_TEMP_DIR = "./userbot/temp/"

@bot.on(admin_cmd(pattern=r"commit"))
@bot.on(sudo_cmd(pattern=r"commit"))
async def download(event):
    if event.fwd_from:
        return
    if Var.GITHUB_ACCESS_TOKEN is None:
        await edit_or_reply(event, "`Please ADD Proper Access Token from github.com`")
        return
    if Var.GIT_REPO_NAME is None:
        await edit_or_reply(event, "`Please ADD Proper Github Repo Name of HellBot`")
        return
    hellbot = await edit_or_reply(event, "Processing ...")
    if not os.path.isdir(GIT_TEMP_DIR):
        os.makedirs(GIT_TEMP_DIR)
    start = datetime.now()
    reply_message = await event.get_reply_message()
    try:
        time.time()
        print("Downloading to TEMP directory")
        downloaded_file_name = await bot.download_media(
            reply_message.media, GIT_TEMP_DIR
        )
    except Exception as e:
        await hellbot.edit(str(e))
    else:
        end = datetime.now()
        ms = (end - start).seconds
        await event.delete()
        await hellbot.edit(
            "Downloaded to `{}` in {} seconds.".format(downloaded_file_name, ms)
        )
        await hellbot.edit("Committing to Github....")
        await git_commit(downloaded_file_name, hellbot)


async def git_commit(file_name, hellbot):
    content_list = []
    access_token = Var.GITHUB_ACCESS_TOKEN
    g = Github(access_token)
    file = open(file_name, "r", encoding="utf-8")
    commit_data = file.read()
    repo = g.get_repo(Var.GIT_REPO_NAME)
    print(repo.name)
    create_file = True
    contents = repo.get_contents("")
    for content_file in contents:
        content_list.append(str(content_file))
        print(content_file)
    for i in content_list:
        create_file = True
        if i == 'ContentFile(path="' + file_name + '")':
            return await hellbot.edit("`File Already Exists`")
            create_file = False
    file_name = "userbot/plugins/" + file_name
    if create_file == True:
        file_name = file_name.replace("./userbot/temp/", "")
        print(file_name)
        try:
            repo.create_file(
                file_name, "Uploaded New Plugin", commit_data, branch="master"
            )
            print("Committed File")
            ccess = Var.GIT_REPO_NAME
            ccess = ccess.strip()
            await hellbot.edit(
                f"`Commited On Your Github Repo`\n\n[Your STDPLUGINS](https://github.com/{ccess}/tree/master/userbot/plugins/)"
            )
        except:
            print("Cannot Create Plugin")
            await hellbot.edit("Cannot Upload Plugin")
    else:
        return await hellbot.edit("`Committed Suicide`")
        
        
CmdHelp("github").add_command(
  'commit', '<reply to a file>', 'Uploads the file on github repo as provided in Heroku Var "GIT_REPO_NAME". In short makes a commit to git repo from Userbot'
).add_command(
  'github', '<git username>', 'Fetches the details of the given git username'
).add()