from telethon.errors import BadRequestError
from telethon.tl.functions.channels import EditAdminRequest, EditBannedRequest
from telethon.tl.functions.messages import UpdatePinnedMessageRequest
from telethon.tl.types import (
    ChatAdminRights,
    ChatBannedRights,
    MessageEntityMentionName,
)

# =================== CONSTANT ===================
PP_TOO_SMOL = "`The image is too small`"
PP_ERROR = "`Failure while processing the image`"
NO_ADMIN = "`I am not an admin! Chutiya sala`"
NO_PERM = (
    "I don't have permission"
)
NO_SQL = "`Running on Non-SQL mode!`"

CHAT_PP_CHANGED = "`Chat Picture Changed Successfully`"
CHAT_PP_ERROR = (
    "`Some issue with updating the pic,`"
    "`maybe coz I'm not an admin,`"
    "`or don't have enough rights.`"
)
INVALID_MEDIA = "`Invalid Media Extension`"

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)

MUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=True)
op_hellbot = tgbot
UNMUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=False)


@hellbot_cmd("ban", is_args=True)
@groups_only
@admin_bot
@is_admin
async def ban(event):
    chat = await event.get_chat()
    chat.admin_rights
    chat.creator
    user, reason = await get_user_from_event(event)
    kraken = await op_hellbot.get_permissions(event.chat_id, user)
    hell_user = user
    user_of_hell = hell_user.first_name
    if kraken.is_admin:
        await event.reply("Wish I Could Ban Admins.")
        return
    if user:
        pass
    else:
        return
    try:
        await event.client(EditBannedRequest(event.chat_id, user.id, BANNED_RIGHTS))
    except BadRequestError:
        await event.reply(f"{NO_PERM} to ban users")
        return
    if reason:
        await event.reply(f"#BAN_EVENT \n\n⚠️ **Banned Retard** {user_of_hell} \n**🗯️ For Reason:** `{reason}`")
    else:
        await event.reply(f"#BAN_EVENT \n\n⚠️ **Banned Retard** {user_of_hell} \n")

#____________________HELLBOT__________________

@hellbot_cmd("unban", is_args=True)
@groups_only
@admin_bot
@is_admin
async def nothanos(event):
    chat = await event.get_chat()
    chat.admin_rights
    chat.creator
    user = await get_user_from_event(event)
    user = user[0]
    if user:
        pass
    else:
        return
    try:
        await event.client(EditBannedRequest(event.chat_id, user.id, UNBAN_RIGHTS))
        await event.reply("#UNBAN_EVENT \n\n⚠️ **Unbanned Successfully. Granting another chance.🚶**")
    except BadRequestError:
        await event.reply(f"{NO_PERM} to unban users")
        return

#____________________HELLBOT__________________

@hellbot_cmd("promote", is_args=True)
@groups_only
@admin_bot
@is_admin
async def promote(event):
    chat = await event.get_chat()
    chat.admin_rights
    chat.creator
    new_rights = ChatAdminRights(
        add_admins=False,
        invite_users=False,
        change_info=False,
        ban_users=True,
        delete_messages=True,
        pin_messages=True,
    )
    user, rank = await get_user_from_event(event)
    kraken = await op_hellbot.get_permissions(event.chat_id, user)
    if kraken.is_admin:
        await event.reply("This user is already an admin!!")
        return
    if not rank:
        rank = "ǟɖʍɨռ"
    if user:
        pass
    else:
        return
    try:
        await event.client(EditAdminRequest(event.chat_id, user.id, new_rights, rank))
        await event.reply("#PROMOTE_EVENT \n\n🔺 **Promoted Successfully! Abb Nacho Bencho 💃🕺**")
    except BadRequestError:
        await event.reply(
            f"{NO_PERM} to promote users"
        )
        return

#____________________HELLBOT__________________

@hellbot_cmd("demote", is_args=True)
@groups_only
@admin_bot
@is_admin
async def demote(event):
    chat = await event.get_chat()
    chat.admin_rights
    chat.creator
    rank = "ǟɖʍɨռ"
    user = await get_user_from_event(event)
    user = user[0]
    if user:
        pass
    else:
        return

    newrights = ChatAdminRights(
        add_admins=None,
        invite_users=None,
        change_info=None,
        ban_users=None,
        delete_messages=None,
        pin_messages=None,
    )
    try:
        await event.client(EditAdminRequest(event.chat_id, user.id, newrights, rank))
    except BadRequestError:
        await event.reply(
            f"{NO_PERM} to demote this user"
        )
        return
    await event.reply("#DEMOTE_EVENT \n\n🔻 **Demoted This User Sucessfully. Better Luck Next Time**")

#____________________HELLBOT__________________

@hellbot_cmd("pin", is_args=True)
@groups_only
@admin_bot
@is_admin
async def pin(event):
    await event.get_chat()
    to_pin = event.reply_to_msg_id
    if not to_pin:
        await event.reply("`Reply to a message to pin it.`")
        return
    options = event.pattern_match.group(1)
    is_silent = True
    if options.lower() == "loud":
        is_silent = False
    try:
        await event.client(UpdatePinnedMessageRequest(event.to_id, to_pin, is_silent))
    except BadRequestError:
        await event.reply(
            f"{NO_PERM} to pin msg"
        )
        return
    await event.reply("#PINNED \n\n📌 **Pinned This Message Successfully**")
    await get_user_from_id(event.from_id, event)

#____________________HELLBOT__________________

@hellbot_cmd("kick", is_args=True)
@groups_only
@admin_bot
@is_admin
async def kick(event):
    chat = await event.get_chat()
    chat.admin_rights
    chat.creator
    user, reason = await get_user_from_event(event)
    kraken = await op_hellbot.get_permissions(event.chat_id, user)
    hell_user = user
    hell_user.first_name
    if kraken.is_admin:
        await event.reply("Kick An Admin! WeW")
        retur
    if not user:
        await event.reply("Sar Mention A User Plz")
        return
    try:
        await event.client.kick_participant(event.chat_id, user.id)
    except:
        await event.reply(f"{NO_PERM} to kick this user")
        return
    if reason:
        await event.reply(
            f"#KICK_EVENT \n\n⚠️ **Kicked** [{user.first_name}](tg://user?id={user.id}) **! \n🗯️ **Reason:** `{reason}`"
        )
    else:
        await event.reply(f"#KICK_EVENT ⚠️ **Kicked** [{user.first_name}](tg://user?id={user.id}) **!**\n")

#____________________HELLBOT__________________

@hellbot_cmd("mute", is_args=True)
@groups_only
@admin_bot
@is_admin
async def mute(event):
    chat = await event.get_chat()
    chat.admin_rights
    chat.creator
    user, reason = await get_user_from_event(event)
    kraken = await op_hellbot.get_permissions(event.chat_id, user)
    hell_user = user
    hell_user.first_name
    if kraken.is_admin:
        await event.reply("How TF Can I mute admins!!")
        retur
    if not user:
        await event.reply("Sar Mention A User Plz")
        return
    try:
        await event.client(EditBannedRequest(event.chat_id, user.id, MUTE_RIGHTS))
    except:
        await event.reply(f"{NO_PERM} to mute users")
        return
    if reason:
        await event.reply(
            f"#MUTE_EVENT \n\n🔇 **Muted** [{user.first_name}](tg://user?id={user.id}) **!\n🗯️ Reason:** `{reason}`"
        )
    else:
        await event.reply(f"#MUTE_EVENT \n\n🔇 **Muted** [{user.first_name}](tg://user?id={user.id}) **!**")

#____________________HELLBOT__________________

@hellbot_cmd("unmute", is_args=True)
@groups_only
@admin_bot
@is_admin
async def mute(event):
    chat = await event.get_chat()
    chat.admin_rights
    chat.creator
    user, reason = await get_user_from_event(event)
    if not user:
        await event.reply("Sar Mention A User Plz")
        return
    try:
        await event.client(EditBannedRequest(event.chat_id, user.id, UNMUTE_RIGHTS))
    except:
        await event.reply(
            f"{NO_PERM} to unmute users"
        )
        return
    if reason:
        await event.reply(
            f"#UNMUTE_EVENT \n\n🔈 **UnMuted** [{user.first_name}](tg://user?id={user.id}) **!\n🗯️ Reason:** `{reason}`"
        )
    else:
        await event.reply(f"#UNMUTE_EVENT \n\n🔈 **Unmute** [{user.first_name}](tg://user?id={user.id}) **!**")

#____________________HELLBOT__________________

async def get_user_from_event(event):
    """ Get the user from argument or replied message. """
    args = event.pattern_match.group(1).split(" ", 1)
    extra = None
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.from_id)
        extra = event.pattern_match.group(1)
    elif args:
        user = args[0]
        if len(args) == 2:
            extra = args[1]

        if user.isnumeric():
            user = int(user)

        if not user:
            await event.reply("`Pass the user's username, id or reply!`")
            return

        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]

            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None

    return user_obj, extra

#____________________HELLBOT__________________

async def get_user_from_id(user, event):
    if isinstance(user, str):
        user = int(user)

    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None

    return user_obj

#____________________HELLBOT__________________