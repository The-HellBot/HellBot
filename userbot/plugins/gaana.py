# plugin made by @Kraken_The_BadASS 
# Copyright (C) HellBot 2020.
# if you change these lines you are gay...bc fuck off!
# Copy Paster stay away😑...if you use this code without credit...u gay bitch fuck off...!

from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot.utils import admin_cmd

import asyncio

 

@borg.on(admin_cmd(pattern="gaana ?(.*)"))

async def FindMusicPleaseBot(gaana):

    song = gaana.pattern_match.group(1)

    chat = "@FindMusicPleaseBot"

    if not song:

        return await gaana.edit("```what should i search```")

    await gaana.edit("```Getting Your Music```")

    await asyncio.sleep(2)

    async with bot.conversation(chat) as conv:

        await gaana.edit("`Downloading...Please wait`")

        try:

            msg = await conv.send_message(song)

            response = await conv.get_response()

            if response.text.startswith("Sorry"):

                await bot.send_read_acknowledge(conv.chat_id)

                return await gaana.edit(f"Sorry, can't find {song}")

            respond = await conv.get_response()

            cobra = await conv.get_response()

        except YouBlockedUserError:

            await gaana.edit("```Please unblock``` @FindmusicpleaseBot``` and try again```")

            return

        await gaana.edit("`Sending Your Music...wait!!! 😉😎`")

        await bot.send_file(gaana.chat_id, cobra)

        await bot.send_read_acknowledge(conv.chat_id)

    await gaana.delete()
