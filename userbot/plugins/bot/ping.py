import time
from datetime import datetime

START_TIME = datetime.now()

@hellbot_cmd("ping", is_args=False)
@pitaji
async def _(hell):
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await tgbot.send_message(
        hell.chat_id,
        f"**˜”*°• ρσηg •°*”˜**\n   **✈** Ping:- `{ms}` \n   **✈** Uptime:- `{str(datetime.now() - START_TIME).split('.')[0]}`",
    )
