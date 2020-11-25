from covid import Covid
from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot import CMD_HELP
from userbot.helpers.functions import covidindia

@bot.on(admin_cmd(pattern="covid(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="covid(?: |$)(.*)", allow_sudo=True))
async def corona(event):
    if event.pattern_match.group(1):
        country = (event.pattern_match.group(1)).title()
    else:
        country = "World"
    hellevent = await edit_or_reply(event, "`collecting data...........`")
    covid = Covid(source="worldometers")
    try:
        country_data = covid.get_status_by_country_name(country)
    except ValueError:
        country_data = ""
    if country_data:
        kraken1 = country_data["confirmed"] + country_data["new_cases"]
        kraken2 = country_data["deaths"] + country_data["new_deaths"]
        data = ""
        data += f"\nConfirmed   : <code>{kraken1}</code>"
        data += f"\nActive           : <code>{country_data['active']}</code>"
        data += f"\nDeaths         : <code>{kraken2}</code>"
        data += f"\nCritical          : <code>{country_data['critical']}</code>"
        data += f"\nRecovered   : <code>{country_data['recovered']}</code>"
        data += f"\nTotal tests    : <code>{country_data['total_tests']}</code>"
        data += f"\nNew Cases   : <code>{country_data['new_cases']}</code>"
        data += f"\nNew Deaths : <code>{country_data['new_deaths']}</code>"
        await hellevent.edit(
            "<b>Corona Virus Info of {}:\n{}</b>".format(country, data),
            parse_mode="html",
        )
    else:
        data = await covidindia(country)
        if data:
            hell1 = int(data["new_positive"]) - int(data["positive"])
            hell2 = int(data["new_death"]) - int(data["death"])
            hell3 = int(data["new_cured"]) - int(data["cured"])
            result = f"<b>Corona virus info of {data['state_name']}\
                \n\nConfirmed   : <code>{data['new_positive']}</code>\
                \nActive           : <code>{data['new_active']}</code>\
                \nDeaths         : <code>{data['new_death']}</code>\
                \nRecovered   : <code>{data['new_cured']}</code>\
                \nNew Cases   : <code>{hell1}</code>\
                \nNew Deaths : <code>{hell2}</code>\
                \nNew cured  : <code>{hell3}</code> </b>"
            await hellevent.edit(result, parse_mode="html")
        else:
            await edit_delete(
                hellevent,
                "`Corona Virus Info of {} is not avaiable or unable to fetch`".format(
                    country
                ),
                5,
            )


CMD_HELP.update(
    {
        "covid": "**Plugin : **`covid`\
        \n\n**Syntax : **`.covid <country name>`\
        \n**Function :** __Get an information about covid-19 data in the given country.__\
        \n\n**Syntax : **`.covid <state name>`\
        \n**Function :** __Get an information about covid-19 data in the given state of India only.__\
        "
    }
)
