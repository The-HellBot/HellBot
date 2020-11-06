#Originally made by @rekcah for @javes05

#porting to hellbot by @kraken_the_badass...

#i asked rekcah before porting...not like other kangers....
#keep credit if u wanna kang...
#else u are a gay...no doubt in that....


from userbot.utils import admin_cmd

@borg.on(admin_cmd(pattern=r"inviteall ?(.*)"))

async def get_users(event):   
    sender = await event.get_sender() ; me = await event.client.get_me()
    if not sender.id == me.id:
        hell = await event.reply("`processing...`")
    else:
    	hell = await event.edit("`processing...`")
    kraken = await get_chatinfo(event) ; chat = await event.get_chat()
    if event.is_private:
              return await hell.edit("`Sorry, Can't add users here`")    
    s = 0 ; f = 0 ; error = 'None'   

    await hell.edit("**TerminalStatus**\n\n`Collecting Users.......`")
    async for user in event.client.iter_participants(kraken.full_chat.id):
                try:
                    if error.startswith("Too"):
                        return await hell.edit(f"**Terminal Finished With Error**\n(`May Got Limit Error from telethon Please try agin Later`)\n**Error** : \n`{error}`\n\n• Invited `{s}` people \n• Failed to Invite `{f}` people")
                    await event.client(functions.channels.InviteToChannelRequest(channel=chat,users=[user.id]))
                    s = s + 1                                                    
                    await hell.edit(f"**Terminal Running...**\n\n• Invited `{s}` people \n• Failed to Invite `{f}` people\n\n**× LastError:** `{error}`")                
                except Exception as e:
                    error = str(e) ; f = f + 1             
    return await hell.edit(f"**Terminal Finished** \n\n• Successfully Invited `{s}` people \n• failed to invite `{f}` people")

