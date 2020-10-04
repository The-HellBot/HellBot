"""command: .kk"""
"""FUCK OFF"""

from telethon import events
import random
import logging

@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
           input_str = event.pattern_match.group(1)
           if input_str == "kk":                              
                 r = random.randint(0, 3)
                 logger.debug(r)
                 if r == 0:
                     await event.edit("┏━━━┓\n┃┏━━┛\n┃┗━━┓\n┃┏━━┛\n┃┃\n┗┛")
                 else:
                     r == 1            
                     await event.edit("╭━━━╮\n┃╭━━╯\n┃╰━━╮\n┃╭━━╯\n┃┃\n╰╯")
