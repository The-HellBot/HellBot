## Mandatory Imports
```python3
None
```
There is None Mandatory Imports. Because Var, bot and command are already automatically imported.

## Explanation
The Mandatory Imports are now automatically imported.

### Formation
Now I will show a short script to show the formation of the desired script.
```python3
from hellbot.utils import admin_cmd, sudo_cmd, edit_or_reply as eor
from hellbot import CmdHelp

@bot.on(admin_cmd(pattern="hello$", outgoing=True))
@bot.on(sudo_cmd(pattern="hello$", allow_sudo=True))
async def hello_world(event):
    if event.fwd_from:
        return
    await eor(event, "**HELLO WORLD**")

CmdHelp("hello").add_command(
  "hello", None, "Hello World Edit."
).add
```
