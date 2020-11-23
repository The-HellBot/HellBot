[![Codacy Badge](https://api.codacy.com/project/badge/Grade/f7c51539e67b483bb8d7749acca51d3a)](https://app.codacy.com/gh/HellBoy-OP/HellBot?utm_source=github.com&utm_medium=referral&utm_content=HellBoy-OP/HellBot&utm_campaign=Badge_Grade_Settings)
[![Python 3.6](https://img.shields.io/badge/Python-3.6%20or%20newer-blue.svg)](https://www.python.org/downloads/release/python-360/)
![GitHub repo size](https://img.shields.io/github/repo-size/HellBoy-OP/Hellbot)
[![HitCount](http://hits.dwyl.com/HellBoy-OP/HellBot.svg)](http://hits.dwyl.com/HellBoy-OP/HellBot)
[![Contact Me](https://img.shields.io/badge/Telegram-Contact%20Me-informational)](https://t.me/kraken_the_badass)


# †hê Hêllẞø†
This is a userbot made for telegram. I made this userbot with help of all other userbots available in telegram. All credits goes to its Respective Owners....

This is the one and only official HellBot Userbot made by [@Kraken_The_BadASS](https://t.me/kraken_the_badass) Also join support channel and group :- https://t.me/HellBot_Official Enjoy Your Bot!!💝
[![HellBot logo](https://telegra.ph/file/2165457cc7e428ff64919.jpg)](https://t.me/hellbot_official)


# The owner would not be responsible for any kind of bans due to the bot...


# For any query:-
### [Join Here For Any Query](https://t.me/hellbot_official)

# FORK AT YOUR OWN RISK
## Installing

### The Easy Way
[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/HellBoy-OP/HellBot/tree/master)

# Credits👀
### • [JaaduBot](https://github.com/Amberyt/JaaduBot)
## One and only. Others with some misfuntioning brain stay out from this SUPER POWERFULL BOT😏

## The Normal Way

Simply clone the repository and run the main file:
```sh
git clone https://github.com/HellBoy-OP/HellBot
cd HellBot
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
# <Create local_config.py with variables as given below>
python3 -m userbot
```

An example `local_config.py` file could be:

**Not All of the variables are mandatory**

__The Userbot should work by setting only the first two variables__

```python3
from heroku_config import Var

class Development(Var):
  APP_ID = 6
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
```

### UniBorg Configuration

The UniBorg Config is situated in `userbot/uniborgConfig.py`.

**Heroku Configuration**
Simply just leave the Config as it is.

**Local Configuration**
Fortunately there are no Mandatory vars for the UniBorg Support Config.

## Mandatory Vars

- Only two of the environment variables are mandatory.
- This is because of `telethon.errors.rpc_error_list.ApiIdPublishedFloodError`
    - `APP_ID`:   You can get this value from https://my.telegram.org
    - `API_HASH`:   You can get this value from https://my.telegram.org
- The userbot will not work without setting the mandatory vars.
