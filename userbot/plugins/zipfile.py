import asyncio
import os
import time
import zipfile

from hellbot.utils import admin_cmd, sudo_cmd, edit_or_reply


@bot.on(admin_cmd(pattern="compress ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="compress ?(.*)", allow_sudo=True))
async def _(event):

    if event.fwd_from:

        return

    input_str = event.pattern_match.group(1)

    mone = await edit_or_reply(event, "Processing ...")

    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):

        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)

    if event.reply_to_msg_id:

        reply_message = await event.get_reply_message()

        try:

            time.time()

            downloaded_file_name = await borg.download_media(
                reply_message, Config.TMP_DOWNLOAD_DIRECTORY
            )

            directory_name = downloaded_file_name

            await edit_or_reply(event, "Finish downloading to my local")

            zipfile.ZipFile(directory_name + ".zip", "w", zipfile.ZIP_DEFLATED).write(
                directory_name
            )

            await borg.send_file(
                event.chat_id,
                directory_name + ".zip",
                caption="Zipped By [Hêllẞø†](t.me/hellbot_official)",
                force_document=True,
                allow_cache=False,
                reply_to=event.message.id,
            )

            try:

                os.remove(directory_name + ".zip")

                os.remove(directory_name)

            except:

                pass

            await edit_or_reply(event, "task Completed")

            await asyncio.sleep(3)

            await event.delete()

        except Exception as e:  # pylint:disable=C0103,W0703

            await mone.edit(str(e))

    elif input_str:

        directory_name = input_str

        zipfile.ZipFile(directory_name + ".zip", "w", zipfile.ZIP_DEFLATED).write(
            directory_name
        )

        await edit_or_reply(event, 
            "Local file compressed to `{}`".format(directory_name + ".zip")
        )
