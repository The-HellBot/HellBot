#Ported to @HellBot_Official
#Made by @Kraken_The_BadASS
#ISKO BHI LELE MADARCHOD. KHUD APNI MAA CHUDWATE REHTE HO.....

import asyncio
from userbot.utils import admin_cmd

@borg.on(admin_cmd(pattern="hnd (.*)"))
async def _(event):
    name = event.pattern_match.group(1)
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(6)
    animation_chars = [
        "👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿\n👉🏿                                          👈🏿\n👉🏿                                          👈🏿\n👉🏿                                          👈🏿\n👉🏿                                          👈🏿\n👉🏿                                          👈🏿\n👉🏿                                          👈🏿\n👉🏿                                          👈🏿\n👉🏿                                          👈🏿\n👉🏿                                          👈🏿\n👉🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👈🏿",
        "👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾\n👉🏾                                  👈🏾\n👉🏾                                  👈🏾\n👉🏾                                  👈🏾\n👉🏾                                  👈🏾\n👉🏾                                  👈🏾\n👉🏾                                  👈🏾\n👉🏾                                  👈🏾\n👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾",
        "👇🏽👇🏽👇🏽👇🏽👇🏽👇🏽👇🏽\n👉🏽                        👈🏽\n👉🏽                        👈🏽\n👉🏽                        👈🏽\n👉🏽                        👈🏽\n👉🏽                        👈🏽\n👆🏽👆🏽👆🏽👆🏽👆🏽👆🏽👆🏽",
        "👇🏼👇🏼👇🏼👇🏼👇🏼\n👉🏼              👈🏼\n👉🏼              👈🏼\n👉🏼              👈🏼\n👆🏼👆🏼👆🏼👆🏼👆🏼",
        f"👇🏻👇🏻👇🏻\n{name}\n👆🏻👆🏻👆🏻",
        f"👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿\n👉🏿👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👈🏿\n👉🏿👉🏾👇🏽👇🏽👇🏽👇🏽👇🏽👇🏽👇🏽👈🏾👈🏿\n👉🏿👉🏾👉🏽👇🏼👇🏼👇🏼👇🏼👇🏼👈🏽👈🏾👈🏿\n👉🏿👉🏾👉🏽👉🏼👇🏻👇🏻👇🏻👈🏼👈🏽👈🏾👈🏿\n👉🏿  {name}  👈🏿\n👉🏿👉🏾👉🏽👉🏼👆🏻👆🏻👆🏻👈🏼👈🏽👈🏾👈🏿\n👉🏿👉🏾👉🏽👆🏼👆🏼👆🏼👆🏼👆🏼👈🏽👈🏾👈🏿\n👉🏿👉🏾👆🏽👆🏽👆🏽👆🏽👆🏽👆🏽👆🏽👈🏾👈🏿\n👉🏿👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👈🏿\n👉🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👈🏿",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 6])
