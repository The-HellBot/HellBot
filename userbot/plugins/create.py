# Made By @Kraken_The_BadASS
# Keep Credits else gay....

"""Create Private Groups
Available Commands:
.create (b|g) GroupName"""
from telethon.tl import functions
from telethon.tl.types import MessageEntityMentionName

from userbot import CMD_HELP
from hellbot.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp

@bot.on(admin_cmd(pattern="create (b|g|c) (.*)"))  # pylint:disable=E0602
@bot.on(sudo_cmd(pattern="create (b|g|c) (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    type_of_group = event.pattern_match.group(1)
    group_name = event.pattern_match.group(2)
    event = await edit_or_reply(event, "Creating wait sar.....")
    if type_of_group == "b":
        try:
            result = await event.client(
                functions.messages.CreateChatRequest(  # pylint:disable=E0602
                    users=["@sarah_robot"],
                    # Not enough users (to create a chat, for example)
                    # Telegram, no longer allows creating a chat with ourselves
                    title=group_name,
                )
            )
            created_chat_id = result.chats[0].id
            await event.client(
                functions.messages.DeleteChatUserRequest(
                    chat_id=created_chat_id, user_id="@sarah_robot"
                )
            )
            result = await event.client(
                functions.messages.ExportChatInviteRequest(
                    peer=created_chat_id,
                )
            )
            await event.edit(
                "Group `{}` created successfully. Join {}".format(
                    group_name, result.link
                )
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            await event.edit(str(e))
    elif type_of_group in ["g", "c"]:
        try:
            r = await event.client(
                functions.channels.CreateChannelRequest(
                    title=group_name,
                    about="Created By Hêllẞø†",
                    megagroup=type_of_group != "c",
                )
            )

            created_chat_id = r.chats[0].id
            result = await event.client(
                functions.messages.ExportChatInviteRequest(
                    peer=created_chat_id,
                )
            )
            await event.edit(
                "Channel `{}` created successfully. Join {}".format(
                    group_name, result.link
                )
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            await event.edit(str(e))
    else:
        await event.edit("Read `.plinfo create` to know how to use me")

@bot.on(admin_cmd(pattern="link(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="link(?: |$)(.*)", allow_sudo=True))
async def permalink(mention):
    if mention.fwd_from:
        return
    """ For .link command, generates a link to the user's PM with a custom text. """
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id}) \n\n\n  ☝️ Tap To See ☝️")
    else:
        tag = (
            user.first_name.replace("\u2060", "") if user.first_name else user.username
        )
        await edit_or_reply(mention, f"[{tag}](tg://user?id={user.id}) \n\n ☝️ Tap to See ☝️")


async def get_user_from_event(event):
    """ Get the user from argument or replied message. """
    args = event.pattern_match.group(1).split(":", 1)
    extra = None
    if event.reply_to_msg_id and not len(args) == 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]

        if user.isnumeric():
            user = int(user)

        if not user:
            await event.edit("`Pass the user's username, id or reply!`")
            return

        if event.message.entities:
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


async def get_user_from_id(user, event):
    if isinstance(user, str):
        user = int(user)

    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None

    return user_obj


CmdHelp("create").add_command(
  'create b', 'Name of your grp', 'Creates a super and send you link'
).add_command(
  'create g', 'Name of your grp', 'Creates a private grp and send you link'
).add_command(
  'create c', 'Name of your channel', 'Creates a channel and sends you link'
).add_command(
  'link', '<reply> <text>', 'Makes a permanent link of tagged user with a custom text'
).add()
