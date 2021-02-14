# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module for getting the weather of a city. """

import json
from datetime import datetime

import requests
from pytz import country_names as c_n
from pytz import country_timezones as c_tz
from pytz import timezone as tz

from userbot import CMD_HELP
from userbot import OPEN_WEATHER_MAP_APPID as OWM_API
from userbot.events import errors_handler
from hellbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp


# ===== CONSTANT =====
DEFCITY = "Delhi"


# ====================
async def get_tz(con):
    """ Get time zone of the given country. """
    """ Credits: @aragon12 and @zakaryan2004. """
    for c_code in c_n:
        if con == c_n[c_code]:
            return tz(c_tz[c_code][0])
    try:
        if c_n[con]:
            return tz(c_tz[con][0])
    except KeyError:
        return


@bot.on(admin_cmd(pattern="weather(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="weather(?: |$)(.*)", allow_sudo=True))
@errors_handler
async def get_weather(weather):
    """ For .weather command, gets the current weather of a city. """

    if not OWM_API:
        await edit_or_reply(weather, "`Get an API key from` https://openweathermap.org/ `first.`")
        return

    APPID = OWM_API

    if not weather.pattern_match.group(1):
        CITY = DEFCITY
        if not CITY:
            await edit_or_reply(weather, "`Please specify a city or set one as default.`")
            return
    else:
        CITY = weather.pattern_match.group(1)

    timezone_countries = {
        timezone: country
        for country, timezones in c_tz.items()
        for timezone in timezones
    }

    if "," in CITY:
        newcity = CITY.split(",")
        if len(newcity[1]) == 2:
            CITY = newcity[0].strip() + "," + newcity[1].strip()
        else:
            country = await get_tz((newcity[1].strip()).title())
            try:
                countrycode = timezone_countries[f"{country}"]
            except KeyError:
                await edit_or_reply(weather, "`Invalid country.`")
                return
            CITY = newcity[0].strip() + "," + countrycode.strip()

    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={APPID}"
    request = requests.get(url)
    result = json.loads(request.text)

    if request.status_code != 200:
        await edit_or_reply(weather, f"`Invalid country.`")
        return

    cityname = result["name"]
    curtemp = result["main"]["temp"]
    humidity = result["main"]["humidity"]
    min_temp = result["main"]["temp_min"]
    max_temp = result["main"]["temp_max"]
    pressure = result["main"]["pressure"]
    feel = result["main"]["feels_like"]
    desc = result["weather"][0]
    desc = desc["main"]
    country = result["sys"]["country"]
    sunrise = result["sys"]["sunrise"]
    sunset = result["sys"]["sunset"]
    wind = result["wind"]["speed"]
    winddir = result["wind"]["deg"]
    cloud = result["clouds"]["all"]
    ctimezone = tz(c_tz[country][0])
    time = datetime.now(ctimezone).strftime("%A, %I:%M %p")
    fullc_n = c_n[f"{country}"]
    # dirs = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
    #        "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    dirs = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]

    div = 360 / len(dirs)
    funmath = int((winddir + (div / 2)) / div)
    findir = dirs[funmath % len(dirs)]
    kmph = str(wind * 3.6).split(".")
    mph = str(wind * 2.237).split(".")

    def fahrenheit(f):
        temp = str(((f - 273.15) * 9 / 5 + 32)).split(".")
        return temp[0]

    def celsius(c):
        temp = str((c - 273.15)).split(".")
        return temp[0]

    def sun(unix):
        xx = datetime.fromtimestamp(unix, tz=ctimezone).strftime("%I:%M %p")
        return xx

    await edit_or_reply(weather, 
        f"**Temperature:** `{celsius(curtemp)}°C | {fahrenheit(curtemp)}°F`\n"
        + f"**Human Feeling** `{celsius(feel)}°C | {fahrenheit(feel)}°F`\n"
        + f"**Min. Temp.:** `{celsius(min_temp)}°C | {fahrenheit(min_temp)}°F`\n"
        + f"**Max. Temp.:** `{celsius(max_temp)}°C | {fahrenheit(max_temp)}°F`\n"
        + f"**Humidity:** `{humidity}%`\n"
        + f"**Pressure** `{pressure} hPa`\n"
        + f"**Wind:** `{kmph[0]} kmh | {mph[0]} mph, {findir}`\n"
        + f"**Cloud:** `{cloud} %`\n"
        + f"**Sunrise:** `{sun(sunrise)}`\n"
        + f"**Sunset:** `{sun(sunset)}`\n\n\n"
        + f"**{desc}**\n"
        + f"`{cityname}, {fullc_n}`\n"
        + f"`{time}`\n"
    )


#@register(outgoing=True, pattern="^.setcity(?: |$)(.*)")
@bot.on(admin_cmd(pattern="setcity(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="setcity(?: |$)(.*)", allow_sudo=True))
@errors_handler
async def set_default_city(city):
    """ For .ctime command, change the default userbot country for date and time commands. """

    if not OWM_API:
        await edit_or_reply(city, "`Get an API key from` https://openweathermap.org/ `first.`")
        return

    global DEFCITY
    APPID = OWM_API

    if not city.pattern_match.group(1):
        CITY = DEFCITY
        if not CITY:
            await edit_or_reply(city, "`Please specify a city to set one as default.`")
            return
    else:
        CITY = city.pattern_match.group(1)

    timezone_countries = {
        timezone: country
        for country, timezones in c_tz.items()
        for timezone in timezones
    }

    if "," in CITY:
        newcity = CITY.split(",")
        if len(newcity[1]) == 2:
            CITY = newcity[0].strip() + "," + newcity[1].strip()
        else:
            country = await get_tz((newcity[1].strip()).title())
            try:
                countrycode = timezone_countries[f"{country}"]
            except KeyError:
                await edit_or_reply(city, "`Invalid country.`")
                return
            CITY = newcity[0].strip() + "," + countrycode.strip()

    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={APPID}"
    request = requests.get(url)
    result = json.loads(request.text)

    if request.status_code != 200:
        await edit_or_reply(city, f"`Invalid country.`")
        return

    DEFCITY = CITY
    cityname = result["name"]
    country = result["sys"]["country"]

    fullc_n = c_n[f"{country}"]

    await edit_or_reply(city, f"`Set default city as {cityname}, {fullc_n}.`")


CmdHelp("weather").add_command(
  "setcity", "<city>", "Sets your default city so you can just use .weather"
).add_command(
  "weather", "<city>", "Gets the weather of a city"
).add()