# PLUGIN MADE BY DANGEROUSJATT
# KEEP CREDIT
# MADE FOR HELLBOT
# BY TEAM HELLBOT

import math

from hellbot.utils import admin_cmd, sudo_cmd, edit_or_reply

from userbot import CmdHelp
from userbot import bot as hellbot


@hellbot.on(admin_cmd(pattern="sin ?(.*)"))
@hellbot.on(sudo_cmd(pattern="sin ?(.*)", allow_sudo=True))
async def findsin(event):
    input_str = int(event.pattern_match.group(1))
    output = math.sin(input_str)
    await event.edit(f"**Value of Sin** `{input_str}`\n== `{output}`")


@hellbot.on(admin_cmd(pattern="cos ?(.*)"))
@hellbot.on(sudo_cmd(pattern="cos ?(.*)", allow_sudo=True))
async def find_cos(event):
    input_str = int(event.pattern_match.group(1))
    output = math.cos(input_str)
    await event.edit(f"**Value of Cos** `{input_str}`\n== `{output}`")


@hellbot.on(admin_cmd(pattern="tan ?(.*)"))
@hellbot.on(sudo_cmd(pattern="tan ?(.*)", allow_sudo=True))
async def find_tan(event):
    input_str = int(event.pattern_match.group(1))
    output = math.tan(input_str)
    await event.edit(f"**Value of Tan** `{input_str}`\n== `{output}`")


@hellbot.on(admin_cmd(pattern="cosec ?(.*)"))
@hellbot.on(sudo_cmd(pattern="cosec ?(.*)", allow_sudo=True))
async def find_csc(event):
    input_str = float(event.pattern_match.group(1))
    output = mpmath.csc(input_str)
    await event.edit(f"**Value of Cosec** `{input_str}`\n== `{output}`")


@hellbot.on(admin_cmd(pattern="sec ?(.*)"))
@hellbot.on(sudo_cmd(pattern="sec ?(.*)", allow_sudo=True))
async def find_sec(event):
    input_str = float(event.pattern_match.group(1))
    output = mpmath.sec(input_str)
    await event.edit(f"**Value of Sec** `{input_str}`\n== `{output}`")


@hellbot.on(admin_cmd(pattern="cot ?(.*)"))
@hellbot.on(sudo_cmd(pattern="cot ?(.*)", allow_sudo=True))
async def find_cot(event):
    input_str = float(event.pattern_match.group(1))
    output = mpmath.cot(input_str)
    await event.edit(f"**Value of Cot** `{input_str}`\n== `{output}`")


@hellbot.on(admin_cmd(pattern="square ?(.*)"))
@hellbot.on(sudo_cmd(pattern="square ?(.*)", allow_sudo=True))
async def square(event):
    input_str = float(event.pattern_match.group(1))
    output = input_str * input_str
    await event.edit(f"**Square of** `{input_str}`\n== `{output}`")


@hellbot.on(admin_cmd(pattern="cube ?(.*)"))
@hellbot.on(sudo_cmd(pattern="cube ?(.*)", allow_sudo=True))
async def cube(event):
    input_str = float(event.pattern_match.group(1))  # DANGEROUSJATT
    output = input_str * input_str * input_str
    await event.edit(f"**Cube of** `{input_str}`\n== `{output}`")


CmdHelp("maths").add_command(
  "cube", "<query>", "Gives the cube of given number"
).add_command(
  "square", "<query>", "Gives the square of given number"
).add_command(
  "cot", "<query>", "Gives the cot of given query"
).add_command(
  "sec", "<query>", "Gives the sec of given query"
).add_command(
  "cosec", "<query>", "Gives the cosec of given query"
).add_command(
  "tan", "<query>", "Gives the tan of given query"
).add_command(
  "sin", "<query>", "Gives the sin of given query"
).add_command(
  "cos", "<query>", "Gives the cos of given query"
).add()