"""Get Poll Info on non supported clients
Syntax: .get_poll"""
from hellbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp


@bot.on(admin_cmd(pattern="get_poll$", outgoing=True))
@bot.on(sudo_cmd(pattern="get_poll$", allow_sudo=True))
async def _(event):
    reply_message = await event.get_reply_message()
    if reply_message.media is None:
        await edit_or_reply(event, "Please reply to a media_type == @gPoll to view the questions and answers"
        )
    elif reply_message.media.poll is None:
        await edit_or_reply(event, "Please reply to a media_type == @gPoll to view the questions and answers"
        )
    else:
        media = reply_message.media
        poll = media.poll
        closed_status = poll.closed
        answers = poll.answers
        question = poll.question
        edit_caption = """Poll is Closed: {}
Question: {}
Answers: \n""".format(
            closed_status, question
        )
        if closed_status:
            results = media.results
            i = 0
            for result in results.results:
                edit_caption += "{}> {}    {}\n".format(
                    result.option, answers[i].text, result.voters
                )
                i += 1
            edit_caption += "Total Voters: {}".format(results.total_voters)
        else:
            for answer in answers:
                edit_caption += "{}> {}\n".format(answer.option, answer.text)
        await edit_or_reply(event, edit_caption)

CmdHelp("polls").add_command(
  "get_poll", "<reply>", "Gets the details about the replied poll."
).add()