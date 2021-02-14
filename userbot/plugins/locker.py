from telethon.tl.functions.messages import EditChatDefaultBannedRightsRequest
from telethon.tl.types import ChatBannedRights

from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import errors_handler, register
from hellbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp


DEFAULTUSER = (
    str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"
)

kraken = bot.uid

@bot.on(admin_cmd(pattern=r"lock ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern=r"lock ?(.*)", allow_sudo=True))
@errors_handler
async def locks(event):
    input_str = event.pattern_match.group(1).lower()
    peer_id = event.chat_id
    msg = None
    media = None
    sticker = None
    gif = None
    gamee = None
    ainline = None
    gpoll = None
    adduser = None
    cpin = None
    changeinfo = None
    if input_str == "msg":
        msg = True
        what = "messages"
    elif input_str == "media":
        media = True
        what = "media"
    elif input_str == "sticker":
        sticker = True
        what = "stickers"
    elif input_str == "gif":
        gif = True
        what = "GIFs"
    elif input_str == "game":
        gamee = True
        what = "games"
    elif input_str == "inline":
        ainline = True
        what = "inline bots"
    elif input_str == "poll":
        gpoll = True
        what = "polls"
    elif input_str == "invite":
        adduser = True
        what = "invites"
    elif input_str == "pin":
        cpin = True
        what = "pins"
    elif input_str == "info":
        changeinfo = True
        what = "chat info"
    elif input_str == "all":
        msg = True
        media = True
        sticker = True
        gif = True
        gamee = True
        ainline = True
        gpoll = True
        adduser = True
        cpin = True
        changeinfo = True
        what = "everything"
    else:
        if not input_str:
            await edit_or_reply(event, "`Need something to lock sur!!`🚶")
            return
        else:
            await edit_or_reply(event, f"🤐 `Invalid lock type:` {input_str}")
            return

    lock_rights = ChatBannedRights(
        until_date=None,
        send_messages=msg,
        send_media=media,
        send_stickers=sticker,
        send_gifs=gif,
        send_games=gamee,
        send_inline=ainline,
        send_polls=gpoll,
        invite_users=adduser,
        pin_messages=cpin,
        change_info=changeinfo,
    )
    try:
        await event.client(
            EditChatDefaultBannedRightsRequest(peer=peer_id, banned_rights=lock_rights)
        )
        await edit_or_reply(event, f"[{DEFAULTUSER}](tg://user?id={kraken}) Locked `{what}` \n__Cause its Rest Time Nimba!!__")
    except BaseException as e:
        await edit_or_reply(event, f"`Do I have proper rights for that ??`\n**Error:** {str(e)}")
        return


@bot.on(admin_cmd(pattern="unlock ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="unlock ?(.*)", allow_sudo=True))
@errors_handler
async def rem_locks(event):
    input_str = event.pattern_match.group(1).lower()
    peer_id = event.chat_id
    msg = None
    media = None
    sticker = None
    gif = None
    gamee = None
    ainline = None
    gpoll = None
    adduser = None
    cpin = None
    changeinfo = None
    if input_str == "msg":
        msg = False
        what = "messages"
    elif input_str == "media":
        media = False
        what = "media"
    elif input_str == "sticker":
        sticker = False
        what = "stickers"
    elif input_str == "gif":
        gif = False
        what = "GIFs"
    elif input_str == "game":
        gamee = False
        what = "games"
    elif input_str == "inline":
        ainline = False
        what = "inline bots"
    elif input_str == "poll":
        gpoll = False
        what = "polls"
    elif input_str == "invite":
        adduser = False
        what = "invites"
    elif input_str == "pin":
        cpin = False
        what = "pins"
    elif input_str == "info":
        changeinfo = False
        what = "chat info"
    elif input_str == "all":
        msg = False
        media = False
        sticker = False
        gif = False
        gamee = False
        ainline = False
        gpoll = False
        adduser = False
        cpin = False
        changeinfo = False
        what = "everything"
    else:
        if not input_str:
            await edit_or_reply(event, "`I need something to unlock sur!!`🚶")
            return
        else:
            await edit_or_reply(event, f"🤐 `Invalid unlock type:` {input_str}")
            return

    unlock_rights = ChatBannedRights(
        until_date=None,
        send_messages=msg,
        send_media=media,
        send_stickers=sticker,
        send_gifs=gif,
        send_games=gamee,
        send_inline=ainline,
        send_polls=gpoll,
        invite_users=adduser,
        pin_messages=cpin,
        change_info=changeinfo,
    )
    try:
        await event.client(
            EditChatDefaultBannedRightsRequest(
                peer=peer_id, banned_rights=unlock_rights
            )
        )
        await edit_or_reply(event, f"[{DEFAULTUSER}](tg://user?id={kraken}) Unlocked `{what}` \n__Now Start Chit Chat !!__")
    except BaseException as e:
        await edit_or_reply(event, f"`Do I have proper rights for that ??`\n**Error:** {str(e)}")
        return

@bot.on(admin_cmd(pattern="ltype$"))
@bot.on(sudo_cmd(pattern="ltype$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "Lock Types")
    await event.edit("**Following are the lock types :** \n\n• all\n• msg\n• media\n• sticker\n• gif\n• game\n• inline\n• poll\n• invite\n• pin\n• info\n")


CmdHelp("locker").add_command(
  "lock", "<lock type>", "Locks the mentioned lock type in current chat. You can Get all lock type by using '.ltype'."
).add_command(
  "unlock", "<lock type>", "Unlocks the mentioned lock type in current chat. You can Get all lock types by using '.ltype'."
).add_command(
  "ltype", None, "Use this to get the list of lock types..."
).add()