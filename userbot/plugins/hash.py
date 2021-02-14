# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module containing hash and encode/decode commands. """

from subprocess import PIPE
from subprocess import run as runapp

import pybase64

#from userbot import CMD_HELP
from hellbot.utils import errors_handler, admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp

@bot.on(admin_cmd(pattern="hash (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="hash (.*)", allow_sudo=True))
@errors_handler
async def gethash(hash_q):
    if hash_q.fwd_from:
        return
    """ For .hash command, find the md5, sha1, sha256, sha512 of the string. """
    hashtxt_ = hash_q.pattern_match.group(1)
    hashtxt = open("hashdis.txt", "w+")
    hashtxt.write(hashtxt_)
    hashtxt.close()
    md5 = runapp(["md5sum", "hashdis.txt"], stdout=PIPE)
    md5 = md5.stdout.decode()
    sha1 = runapp(["sha1sum", "hashdis.txt"], stdout=PIPE)
    sha1 = sha1.stdout.decode()
    sha256 = runapp(["sha256sum", "hashdis.txt"], stdout=PIPE)
    sha256 = sha256.stdout.decode()
    sha512 = runapp(["sha512sum", "hashdis.txt"], stdout=PIPE)
    runapp(["rm", "hashdis.txt"], stdout=PIPE)
    sha512 = sha512.stdout.decode()
    ans = (
        "Text: `"
        + hashtxt_
        + "`\nMD5: `"
        + md5
        + "`SHA1: `"
        + sha1
        + "`SHA256: `"
        + sha256
        + "`SHA512: `"
        + sha512[:-1]
        + "`"
    )
    if len(ans) > 4096:
        hashfile = open("hashes.txt", "w+")
        hashfile.write(ans)
        hashfile.close()
        await hash_q.client.send_file(
            hash_q.chat_id,
            "hashes.txt",
            reply_to=hash_q.id,
            caption="`It's too big, sending a text file instead. `",
        )
        runapp(["rm", "hashes.txt"], stdout=PIPE)
    else:
        await hash_q.reply(ans)


@bot.on(admin_cmd(pattern="hbase (en|de) (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="hbase (en|de) (.*)", allow_sudo=True))
@errors_handler
async def endecrypt(query):
    if query.fwd_from:
        return
    """ For .base64 command, find the base64 encoding of the given string. """
    if query.pattern_match.group(1) == "en":
        lething = str(pybase64.b64encode(bytes(query.pattern_match.group(2), "utf-8")))[
            2:
        ]
        await query.reply("Shhh! It's Encoded: `" + lething[:-1] + "`")
    else:
        lething = str(
            pybase64.b64decode(
                bytes(query.pattern_match.group(2), "utf-8"), validate=True
            )
        )[2:]
        await query.reply("Decoded: `" + lething[:-1] + "`")


CmdHelp("hash").add_command(
  "hash", "<query>", "Finds the md5, sha1, sha256, sha512 of the string when written into a txt file"
).add_command(
  "hbase en", "<query>", "Finds the base64 encoding of the given string"
).add_command(
  "hbase de", "<query>", "Finds the base64 decoding of the given string"
).add()
