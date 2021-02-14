
import asyncio
import io
import time
import os
import sys
import traceback

from hellbot.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot import *
from userbot.cmdhelp import CmdHelp

@bot.on(admin_cmd(pattern="exec(?: |$|\n)(.*)", command="exec"))
@bot.on(sudo_cmd(pattern="exec(?: |$|\n)(.*)", command="exec", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    cmd = "".join(event.text.split(maxsplit=1)[1:])
    if not cmd:
        return await edit_delete(event, "`What should i execute?..`")
    hellevent = await edit_or_reply(event, "`Executing.....`")
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    result = str(stdout.decode().strip()) + str(stderr.decode().strip())
    helluser = await event.client.get_me()
    if helluser.username:
        curruser = helluser.username
    else:
        curruser = "hellbot"
    uid = os.geteuid()
    if uid == 0:
        cresult = f"`{curruser}:~#` `{cmd}`\n`{result}`"
    else:
        cresult = f"`{curruser}:~$` `{cmd}`\n`{result}`"
    await edit_or_reply(
        event,
        text=cresult,
        aslink=True,
        linktext=f"**•  Exec : **\n`{cmd}` \n\n**•  Result : **\n",
    )
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "Terminal command " + cmd + " was executed sucessfully.",
        )


@bot.on(admin_cmd(pattern="eval(?: |$|\n)(.*)", command="eval"))
@bot.on(sudo_cmd(pattern="eval(?: |$|\n)(.*)", command="eval", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    cmd = "".join(event.text.split(maxsplit=1)[1:])
    if not cmd:
        return await edit_delete(event, "`What should i run ?..`")
    hellevent = await edit_or_reply(event, "`Running ...`")
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None
    try:
        await aexec(cmd, event)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"
    final_output = f"**•  Eval : **\n`{cmd}` \n\n**•  Result : **\n`{evaluation}` \n"
    await edit_or_reply(
        hellevent,
        text=final_output,
        aslink=True,
        linktext=f"**•  Eval : **\n`{cmd}` \n\n**•  Result : **\n",
    )
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "eval command " + cmd + " was executed sucessfully.",
        )


async def aexec(code, smessatatus):
    message = event = smessatatus
    p = lambda _x: print(yaml_format(_x))
    reply = await event.get_reply_message()
    exec(
        f"async def __aexec(message, event , reply, client, p, chat): "
        + "".join(f"\n {l}" for l in code.split("\n"))
    )
    return await locals()["__aexec"](
        message, event, reply, message.client, p, message.chat_id
    )


@bot.on(admin_cmd(pattern="bash ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="bash ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    PROCESS_RUN_TIME = 100
    cmd = event.pattern_match.group(1)
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    e = stderr.decode()
    if not e:
        e = "No Error"
    o = stdout.decode()
    if not o:
        o = "**Tip**: \n`If you want to see the results of your code, I suggest printing them to stdout.`"
    else:
        _o = o.split("\n")
        o = "`\n".join(_o)
    OUTPUT = f"**QUERY:**\n__Command:__\n`{cmd}` \n__PID:__\n`{process.pid}`\n\n**stderr:** \n`{e}`\n**Output:**\n{o}"
    if len(OUTPUT) > 4095:
        with io.BytesIO(str.encode(OUTPUT)) as out_file:
            out_file.name = "exec.text"
            await bot.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=cmd,
                reply_to=reply_to_id,
            )
            await event.delete()
    await edit_or_reply(event, OUTPUT)
    

CmdHelp("evaluators").add_command(
  'eval', '<expr>', 'Execute python script'
).add_command(
  'exec', '<command>', 'Execute a Terminal command on HellBot server and shows details'
).add_command(
  'bash', '<query>', 'Bash your codes on linux and gives the output in current chat'
).add()