#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K
import asyncio

from hellbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp


@bot.on(admin_cmd(pattern="type (.*)"))
@bot.on(sudo_cmd(pattern="type (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    # https://t.me/AnotherGroup/176551
    input_str = event.pattern_match.group(1)
    shiiinabot = "\u2060"
    for i in range(601):
        shiiinabot += "\u2060"
    try:
        await edit_or_reply(event, shiiinabot)
    except Exception as e:
        logger.warn(str(e))
    typing_symbol = "_"
    DELAY_BETWEEN_EDITS = 0.3
    previous_text = ""
    await edit_or_reply(event, typing_symbol)
    await asyncio.sleep(DELAY_BETWEEN_EDITS)
    for character in input_str:
        previous_text = previous_text + "" + character
        typing_text = previous_text + "" + typing_symbol
        try:
            await edit_or_reply(event, typing_text)
        except Exception as e:
            logger.warn(str(e))
        await asyncio.sleep(DELAY_BETWEEN_EDITS)
        try:
            await edit_or_reply(event, previous_text)
        except Exception as e:
            logger.warn(str(e))
        await asyncio.sleep(DELAY_BETWEEN_EDITS)


CmdHelp("type").add_command(
  "type", "<text>", "A typing animation for given text. Try it out yourself"
).add()