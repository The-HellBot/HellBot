# HellBot
This is the one and only official HellBot Userbot made by [@Kraken_The_BadASS](https://t.me/kraken_the_badass) Also join support channel and group :- https://t.me/HellBot_Official Enjoy Your Bot!!💝
# Hêllẞø†
This is a userbot made for telegram. I made this userbot with help of all other userbots available in telegram. Credits To It's Respective Owners.
 
# The owner would not be responsible for any kind of bans due to the bot.


For any query
# https://t.me/hellbot_official

# FORK AT YOUR OWN RISK
# Installing

### The Easy Way

[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

### Get String Session From Here:-

[String #1](https://Hellbot.hellboyop.repl.run)
[String #2](https://hellbot2-1.hellboyop.repl.run)

• Enter Your Phone Number with your Country Code (E.X. For India It's +91)

• Paste the OTP you received on Telegram.

• Your String Session is stored in Saved Message of your Telegram Account.


### The Normal Way

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
