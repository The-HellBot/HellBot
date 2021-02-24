import asyncio
import io
import os
import re

from telethon import Button, custom, events, functions
import telethon
from telethon.tl.functions.users import GetFullUserRequest
from telethon.utils import pack_bot_file_id

from hellbot import bot
from hellbot.Config import Config
from hellbot.plugins.sql_helper.bl_bot import (
    add_in_db,
    is_id_added,
    removeid,
)
from hellbot.plugins.sql_helper.botusers import add_id_in_db, its_userid
from hellbot.plugins.sql_helper.idadder_sql import (
    add_usersid_in_db,
    already_added,
    get_all_users,
)
hell_logo = "./KRAKEN/hellbot_logo.jpg"

@hellbot_cmd("start", is_args=False)
async def start(event):
    hellbot = await tgbot.get_me()
    bot_id = hellbot.first_name
    bot_un = hellbot.username
    replied_user = await event.client(GetFullUserRequest(event.sender_id))
    firstname = replied_user.user.first_name
    me_here = await bot.get_me()
    my_name = me_here.first_name
    where = event.chat_id
    mypic = Config.BOT_PIC
    welcome_vro = f"👋 **Hey there,** {firstname} **! 💛 It's a pleasure meeting you!💛\n🤖 I Am** {bot_id}**, ✅ Made and Maintained by my Master** \n⚡ [{my_name}](tg://user?id={bot.uid}) ⚡\n**For his personal use. \n🙃 You Can Contact My Master Using Me. Just send me a message and I'll forward it to him 😉 \n\n✨If You Want A Clone Like Me, Then Go Through These Buttons 👇"
    if event.sender_id == bot.uid:
        await tgbot.send_message(
            where,
            message=f"✨✨ Hello My Pero Master, It's {bot_id}, Your Personal Bot! Lemme Know If You Want Something That I Can Do 🙃🙃",
            buttons=[
                [custom.Button.inline("⚡ Bot Users" ⚡, data="bot_users")],
                [custom.Button.inline("✨ Help Cmds ✨", data="gibcmd")],
                [
                    Button.url(
                        "🏘️ Add Me In Group 🏘️", f"t.me/{bot_un}?startgroup=true"
                    )
                ],
            ],
        )
    else:
        if already_added(event.sender_id):
            pass
        elif not already_added(event.sender_id):
            add_usersid_in_db(event.sender_id)
        await tgbot.send_file(
            event.chat_id,
            file=mypic,
            caption=welcome_vro,
            link_preview=False,
            buttons=[
                [custom.Button.inline("🔮 Deploy 🔮", data="deploy")],
                [Button.url("💜 Help 💜", "t.me/Fridayot")],
            ],
        )
        if os.path.exists(mypic):
            os.remove(mypic)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"deploy")))
async def help(event):
    await event.delete()
    if event.query.user_id is not bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message="👋 Hello, You Can Deploy [Hêllẞø†](t.me/hellbot_official) By Following The Steps Given In 🎥 YouTube Video Tutorial.",
            buttons=[
                [Button.url("🎥 Tutotial 🎥", "https://youtu.be/M2FQJq_sHp4")],
                [Button.url("✅ Support ✅", "t.me/HellBot_Official_Chat")],
                [Button.url("⚜️ Channel ⚜️", "t.me/HellBot_Official")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"users")))
async def users(event):
    if event.query.user_id == bot.uid:
        await event.delete()
        total_users = get_all_users()
        users_list = "List Of Total Users In Bot. \n\n"
        for ok_boss in total_users:
            users_list += ("➣ {} \n").format(int(ok_boss.chat_id))
        with io.BytesIO(str.encode(users_list)) as tedt_file:
            tedt_file.name = "userlist.txt"
            await tgbot.send_file(
                event.chat_id,
                tedt_file,
                force_document=True,
                thumb=hell_logo
                caption="Total Users In Your Bot.",
                allow_cache=False,
            )
    else:
        pass


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"gibcmd")))
async def users(event):
    await event.delete()
    help_str = "**Hello, These Are Some Commands...** \n\n➤ /start - Check if I am Alive \n➤ /ping - Check Ping Speed! \n➤ /trt <lang-code> - Translate given word. \n➤ /broadcast - Sends Message To all Users In Bot \n➤ /id - Shows ID of User And Media. \n➤ /addnote - Add Note \n➤ /notes - Shows Notes \n➤ /rmnote - Remove Note \n➤ /alive - Check if Im Alive! \n➤ /ban - Works In Group , Bans A User. \n➤ /unban - Unbans A User in Group \n➤ /promote - Promotes A User \n➤ /demote - Demotes A User \n➤ /pin - Pins A Message \n➤ /stats - Shows Total Users In Bot \n\nYou Can Change Bot Trigger by `.set var BOT_TRIGGER ^your_trigger` \n**[ NOTE ]** ' ^ ' is mandatory."
    await tgbot.send_message(event.chat_id, help_str)


@tgbot.on(events.NewMessage(func=lambda e: e.is_private))
async def all_messages_catcher(event):
    if is_he_added(event.sender_id):
        return
    if event.sender_id == bot.uid:
        return
    if event.raw_text.startswith("/"):
        return
    if Config.FORCE_SUB:
        try:
            result = await tgbot(
                functions.channels.GetParticipantRequest(
                    channel=Config.FORCE_CHANNEL_ID, user_id=event.sender_id
                )
            )
        except telethon.errors.rpcerrorlist.UserNotParticipantError:
            await event.reply(f"**ERROR!!** \n__I Couldn't Forward That Message To My Master. Please Join My Channel First And Then Try Again!__",
                             buttons = [Button.url("😉 Join Channel 😉", Config.FORCE_CHANNEL_USERNAME)])
            return
    await event.get_sender()
    master = await event.forward_to(bot.uid)
    add_me_in_db(master.id, event.sender_id, event.id)


@tgbot.on(events.NewMessage(func=lambda e: e.is_private))
async def sed(event):
    msg = await event.get_reply_message()
    if msg is None:
        return
    msg.id
    msg_s = event.raw_text
    user_id, reply_message_id = his_userid(msg.id)
    if event.sender_id != bot.uid:
        return
    elif event.raw_text.startswith("/"):
        return
    elif event.text is not None and event.media:
        bot_api_file_id = pack_bot_file_id(event.media)
        await tgbot.send_file(
            user_id,
            file=bot_api_file_id,
            caption=event.text,
            reply_to=reply_message_id,
        )
    else:
        msg_s = event.raw_text
        await tgbot.send_message(
            user_id,
            msg_s,
            reply_to=reply_message_id,
        )


@hellbot_cmd("broadcast", is_args=True)
@inevitable
async def retard(event):
    bc_msg = event.pattern_match.group(1)
    usersto = get_all_users()
    error_count = 0
    sent_count = 0
    hmmok = ""
    if bc_msg == None:
        await event.reply("`Looks like you are high on weed 🌚`")
        return
    elif bc_msg == " ":
        await event.reply("`Looks like you are high on weed 🌚`")
        return
    for users_uid in usersto:
        try:
            sent_count += 1
            await tgbot.send_message(int(users_uid.chat_id), bc_msg)
            await asyncio.sleep(0.3)
        except:
            error_count += 1
    await tgbot.send_message(
        event.chat_id,
        f"🗞️ **Broadcast Done \n✅ Success :-** `{sent_count}` **Group/Users.\n❌ Error :-** `{error_count}` \n📊 **Total Groups/Users :-** `{len(usersto)}`",
    )


@hellbot_cmd("stats", is_args=False)
@superior
async def hell_stat(event):
    hell_stat = get_all_users()
    await event.reply(
        f"**Stats Of Your Bot** \nTotal Users In Bot => {len(hell_stat)}"
    )


@hellbot_cmd("help", is_args=False)
@superior
async def help_string(event):
    help_cmds = "**Hello, These Are Some Commands...** \n\n➤ /start - Check if I am Alive \n➤ /ping - Check Ping Speed! \n➤ /trt <lang-code> - Translate given word. \n➤ /broadcast - Sends Message To all Users In Bot \n➤ /id - Shows ID of User And Media. \n➤ /addnote - Add Note \n➤ /notes - Shows Notes \n➤ /rmnote - Remove Note \n➤ /alive - Check if Im Alive! \n➤ /ban - Works In Group , Bans A User. \n➤ /unban - Unbans A User in Group \n➤ /promote - Promotes A User \n➤ /demote - Demotes A User \n➤ /pin - Pins A Message \n➤ /stats - Shows Total Users In Bot \n\nYou Can Change Bot Trigger by `.set var BOT_TRIGGER ^your_trigger` \n**[ NOTE ]** ' ^ ' is mandatory."
    await event.reply(help_cmds)


@hellbot_cmd("block", is_args=False)
@inevitable
async def block(event):
    if event.sender_id == bot.uid:
        msg = await event.get_reply_message()
        user_id, reply_message_id = his_userid(msg.id)
    if is_he_added(user_id):
        await event.reply("User Already Blocked...")
    elif not is_he_added(user_id):
        add_nibba_in_db(user_id)
        await event.reply("Blocked this retard.")
        block_pic = "https://telegra.ph/file/cb91752dee175f840da21.mp4"
        await tgbot.send_file(
            event.chat_id,
            file=block_pic,
            caption="You Have Been Blocked By My Master.",
            link_preview=False,
            )


@hellbot_cmd("unblock", is_args=False)
@inevitable
async def unblock(event):
    if event.sender_id == bot.uid:
        msg = await event.get_reply_message()
        msg.id
        event.raw_text
        user_id, reply_message_id = his_userid(msg.id)
    if not is_he_added(user_id):
        await event.reply("This User Is Not Even Blocked")
    elif is_he_added(user_id):
        removenibba(user_id)
        await event.reply("Unblocked This User...")
        unblock_pic = "https://telegra.ph/file/02783c70055b8b14635e5.mp4"
        await tgbot.send_file(
            event.chat_id,
            file=unblock_pic,
            caption="Yay!! You have been unblocked by my master now✨✨",
            link_preview=False,
            )
