# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import asyncio

from telethon import events

_last_messages = {}


@borg.on(events.NewMessage(outgoing=True))
async def _(event):
    _last_messages[event.chat_id] = event.message


@borg.on(events.NewMessage(pattern=r"\.(fix)?reply", outgoing=True))
async def _(event):
    if not event.is_reply or event.chat_id not in _last_messages:
        return

    message = _last_messages[event.chat_id]
    chat = await event.get_input_chat()
    await asyncio.wait(
        [
            borg.delete_messages(chat, [event.id, message.id]),
            borg.send_message(chat, message, reply_to=event.reply_to_msg_id),
        ]
    )
