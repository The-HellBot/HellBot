# †hê Hêllẞø†
This is a userbot made for telegram. I made this userbot with help of all other userbots available in telegram. All credits goes to its Respective Owners....

This is the one and only official HellBot Userbot made by [@Kraken_The_BadASS](https://t.me/kraken_the_badass) Also join support channel and group :- https://t.me/HellBot_Official Enjoy Your Bot!!💝


# The owner would not be responsible for any kind of bans due to the bot...


# For any query:-
### [Join Here For Any Query](https://t.me/hellbot_official)

# FORK AT YOUR OWN RISK
## Installing

### The Easy Way

<a href="https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FHellBoy-OP%2FHellBot&template=https%3A%2F%2Fgithub.com%2FHellBoy-OP%2FHellBot" rel="nofollow" style="background-color: initial; box-sizing: border-box; color: #0366d6; text-decoration-line: none;"><img alt="Deploy" data-canonical-src="https://www.herokucdn.com/deploy/button.svg" src="https://camo.githubusercontent.com/83b0e95b38892b49184e07ad572c94c8038323fb/68747470733a2f2f7777772e6865726f6b7563646e2e636f6d2f6465706c6f792f627574746f6e2e737667" style="border-style: none; box-sizing: initial; max-width: 100%;" /></a></div>
# Generate String Session From Below Links:-

### [String #1](https://Hellbot.hellboyop.repl.run)

### [String #2](https://Hellbot2.hellboyop.repl.run)

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
