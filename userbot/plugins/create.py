'''
for bot credits to @pureindialover
'''

from telethon.tl import functions, types

from userbot.events import register

from userbot import CMD_HELP





@register(outgoing=True, pattern="^.create (b|g|c)(?: |$)(.*)")

async def telegraphs(grop):

    """ For .create command, Creating New Group & Channel """

    if not grop.text[0].isalpha() and grop.text[0] not in ("/", "#", "@", "!"):

        if grop.fwd_from:

            return

        type_of_group = grop.pattern_match.group(1)

        group_name = grop.pattern_match.group(2)

        if type_of_group == "b":

            try:

                result = await grop.client(functions.messages.CreateChatRequest(  # pylint:disable=E0602

                    users=["@MRSFRIDAYBOT"],

                    # Not enough users (to create a chat, for example)

                    # Telegram, no longer allows creating a chat with ourselves

                    title=group_name

                ))

                created_chat_id = result.chats[0].id

                await grop.client(functions.messages.DeleteChatUserRequest(

                    chat_id=created_chat_id,

                    user_id="@MRSFRIDAYBOT"

                ))

                result = await grop.client(functions.messages.ExportChatInviteRequest(

                    peer=created_chat_id,

                ))

                await grop.edit("Your `{}` Group Made Boss!. Join [{}]({})".format(group_name, group_name, result.link))

            except Exception as e:  # pylint:disable=C0103,W0703

                await grop.edit(str(e))

        elif type_of_group == "g" or type_of_group == "c":

            try:

                r = await grop.client(functions.channels.CreateChannelRequest(  # pylint:disable=E0602

                    title=group_name,

                    about="Welcome to this Channel boss",

                    megagroup=False if type_of_group == "c" else True

                ))

                created_chat_id = r.chats[0].id

                result = await grop.client(functions.messages.ExportChatInviteRequest(

                    peer=created_chat_id,

                ))

                await grop.edit("Your `{}` Group/Channel Has been made Boss!. Join [{}]({})".format(group_name, group_name, result.link))

            except Exception as e:  # pylint:disable=C0103,W0703

                await grop.edit(str(e))



CMD_HELP.update({

    "create": "\
Create\
\nUsage: Create Channel, Group & Group With Bot.\
\n\n.create g\
\nUsage: Create a Private Group.\
\n\n.create b\
\nUsage: Create a Group with Bot.\
\n\n.create c\
\nUsage: Create a Channel.\
"})
