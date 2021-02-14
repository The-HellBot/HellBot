# Made By @Kraken_The_BadASS. Keep Credit if you are gonna copy paste it. LOL NOOBS....
# Happy New Year plugin by Kraken_The_BadASS for Hellbot
# Kangers keep credits...

import random
# credits to kraken, john snow
from asyncio import sleep
# credits to kraken, john snow
import asyncio
# credits to kraken, john snow
from userbot import CMD_HELP, ALIVE_NAME
# credits to kraken, john snow
from hellbot.utils import admin_cmd, edit_or_reply, sudo_cmd
# credits to kraken, john snow
from userbot.cmdhelp import CmdHelp
# credits to kraken, john snow
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "✨ Best Wishes 🥰"
# credits to kraken, john snow
kraken = bot.uid
# credits to kraken, john snow
# credits to kraken, john snow
@bot.on(admin_cmd(pattern="hny$", outgoing=True))
@bot.on(sudo_cmd(pattern="hny$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "Hello!!!")
    await asyncio.sleep(1)
    h = random.randrange(1, 18)
    if h == 1:
        await event.edit(
            f"The new year is a blank book. The pen is in your hands, it is your chance to write a beautiful story for yourself. Happy New Year!\n\n[{DEFAULTUSER}](tg://user?id={kraken})"
        )# credits to kraken, john snow
    if h == 2:
        await event.edit(
            f"Every moment is a fresh beginning. Hope this year be yours\n\n[{DEFAULTUSER}](tg://user?id={kraken})"
        )  # creadit to kraken, john snow    
    if h == 3:
        await event.edit(
            f"Here’s to another year full of joy, laughter, and unforgettable memories with an unforgettable friend! Happy New Year! \n\n[{DEFAULTUSER}](tg://user?id={kraken})"
        )# credits to kraken, john snow
    if h == 4:
        await event.edit(
            f"I hope this year turns out to be the best year of your life and your family too. Happy New Year! \n\n[{DEFAULTUSER}](tg://user?id={kraken})"
        )# credits to kraken, john snow
    if h == 5:
        await event.edit(
            f"May this New Year bring you much joy and fun. May you find peace, love, and success. Happy New Year! \n\n[{DEFAULTUSER}](tg://user?id={kraken})"
        ) # creadit to kraken, john snow    
    if h == 6:
        await event.edit(
            f"New Year’s Day is every man’s birthday. \n\n[{DEFAULTUSER}](tg://user?id={kraken})"
        ) # creadit to kraken, john snow    
    if h == 7:
        await event.edit(
            f"A new year is a chance to make new beginnings and to let go of old regrets. Happy New Year. \n\n[{DEFAULTUSER}](tg://user?id={kraken})"
        ) # creadit to kraken, john snow    
    if h == 8:
        await eventt.edit(
            f"Every woman and man should be born again on the first day of January. Start with a fresh page. \n\n[{DEFAULTUSER}](tg://user?id={kraken})"
        ) # credits to kraken, john snow
    if h == 9:
        await event.edit(
            f"Nights will be dark, but days will be light, wishing your life to be always bright. Happy New Year! \n\n[{DEFAULTUSER}](tg://user?id={kraken})"
        ) # creadit to kraken, john snow    
    if h == 10:
        await event.edit(
            f"May every winter bring the promise of spring and a brighter tomorrow. Happy New Year. \n\n[{DEFAULTUSER}](tg://user?id={kraken})"
        ) # creadit to kraken, john snow    
    if h == 11:
        await event.edit(
            f"Let the old year-end and the New Year begin with the warmest of aspirations. Happy New Year! \n\n[{DEFAULTUSER}](tg://user?id={kraken})"
        ) # creadit to kraken, john snow    
    if h == 12:
        await event.edit(
            f"Happy New Year to My Family and Friends! Cheers to the new year! A year of new blessings! Cheers, darling! \n\n[{DEFAULTUSER}](tg://user?id={kraken})"
        )# credits to kraken, john snow
    if h == 13:
        await event.edit(
            f"Fresh start begins today! Have a sparkling new year! The best is yet to come. \n\n[{DEFAULTUSER}](tg://user?id={kraken})"
        )# credits to kraken, john snow
    if h == 14:
        await event.edit(
            f"Here’s to the next chapter! New year, new beginnings! Goodbye 2020, Hello 2021 \n\n[{DEFAULTUSER}](tg://user?id={kraken})"
        ) # creadit to kraken, john snow    
    if h == 15:
        await event.edit(
            f"New year, new chapter, Sparkle your way into the new year! Have a happy new year!\n\n[{DEFAULTUSER}](tg://user?id={kraken})"
        ) # credits to kraken, john snow
    if h == 16:
        await event.edit(
            f"Fresh start. New adventures, here we go! Make way for 2021\nNew Year, New Hope! New adventure around the corner! \n\n[{DEFAULTUSER}](tg://user?id={kraken})"
        ) # credits to kraken, john snow
    if h == 17:
        await event.edit(
            f"May this new year be filled with love and cheer! 2021 will be YOUR year! Out with the old, In with the new \n\n[{DEFAULTUSER}](tg://user?id={kraken})"
        ) # credits to kraken, john snow
    if h == 18:
        await event.edit(
            f"New year, new plans, new memories to be made. Here’s to the future. To a new year of new possibilities. Wishing you holiday cheer and a happy new year! \n\n[{DEFAULTUSER}](tg://user?id={kraken})"
        ) # credits to kraken, john snow
    if h == 19:
        await event.edit(
            f"365 new days. 365 new chances.\nHere’s to giving and living!\nNew year, new attitude!\nHave a prosperous New Year!\nWishing you a happy healthy new year\nMay the new year bless you with health, wealth, and happiness. \n\n[{DEFAULTUSER}](tg://user?id={kraken})"
       ) # credits to kraken, john snow
# credits to kraken, john snow
CmdHelp("new_year").add_command(
  "hny", None, "Wishes happy new year on behalf of you"
).add()
# credits to kraken, john snow