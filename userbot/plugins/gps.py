# Made by @mrconfused
# help from @sunda005 and @SpEcHIDe
# don't edit credits

from geopy.geocoders import Nominatim
from telethon.tl import types

from hellbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from hellbot import CmdHelp

@bot.on(admin_cmd(pattern="gps ?(.*)"))
@bot.on(sudo_cmd(pattern="gps ?(.*)", allow_sudo=True))
async def gps(event):
    if event.fwd_from:
        return
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    input_str = event.pattern_match.group(1)

    if not input_str:
        return await edit_or_reply(event, "What should i find? Give me location.🤨")

    await edit_or_reply(event, "Finding😁")

    geolocator = Nominatim(user_agent="catuserbot")
    geoloc = geolocator.geocode(input_str)

    if geoloc:
        lon = geoloc.longitude
        lat = geoloc.latitude
        await reply_to_id.reply(
            input_str, file=types.InputMediaGeoPoint(types.InputGeoPoint(lat, lon))
        )
        await event.delete()
    else:
        await edit_or_reply(event, "I coudn't find it😫")

CmdHelp("gps").add_command(
  "gps", "<place name>", "Gives the location of searched place"
).add()
