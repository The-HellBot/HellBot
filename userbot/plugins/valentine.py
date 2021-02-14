import asyncio
import random
from asyncio import sleep

from hellbot import CmdHelp, bot as hellbot, ALIVE_NAME
from hellbot.utils import admin_cmd, sudo_cmd, edit_or_reply as eor

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Your Lover"

kraken = hellbot.uid

hell = f"[{DEFAULTUSER}](tg://user?id={kraken})"

@hellbot.on(admin_cmd(pattern="hvd$"))
@hellbot.on(sudo_cmd(pattern="hvd$", allow_sudo=True))
async def love(event):
    if event.fwd_from:
        return
    input_str = "♥ Valentine's Day ♥"
    await event.edit(f"❤️🧡💛💚💙💜🤎🖤🤍\n    {input_str}    \n🤍🖤🤎💜💙💚💛🧡❤️")
    await sleep(1)
    await event.edit(f"🧡💛💚💙💜🤎🖤🤍❤️\n    {input_str}    \n❤️🤍🖤🤎💜💙💚💛🧡")
    await sleep(1)
    await event.edit(f"💛💚💙💜🤎🖤🤍❤️🧡\n    {input_str}    \n🧡❤️🤍🖤🤎💜💙💚💛")
    await sleep(1)
    await event.edit(f"💚💙💜🤎🖤🤍❤️🧡💛\n    {input_str}    \n💛🧡❤️🤍🖤🤎💜💙💚")
    await sleep(1)
    await event.edit(f"💙💜🤎🖤🤍❤️🧡💛💚\n    {input_str}    \n💚💛🧡❤️🤍🖤🤎💜💙")
    await sleep(1)
    await event.edit(f"💜🤎🖤🤍❤️🧡💛💚💙\n    {input_str}    \n💙💚💛🧡❤️🤍🖤🤎💜")
    await sleep(1)
    await event.edit(f"🤎🖤🤍❤️🧡💛💚💙💜\n    {input_str}    \n💜💙💚💛🧡❤️🤍🖤🤎")
    await sleep(1)
    await event.edit(f"🖤🤍❤️🧡💛💚💙💜🤎\n    {input_str}    \n🤎💜💙💚💛🧡❤️🤍🖤")
    await sleep(1)
    await event.edit(f"🤍❤️🧡💛💚💙💜🤎🖤\n    {input_str}    \n🖤🤎💜💙💚💛🧡❤️🤍")
    await sleep(2)
    await event.edit("__**HAPPY VALENTINE'S DAY**__ [❤️](https://telegra.ph/file/4d51f6a5d98ba94ae2af7.jpg)", link_preview=True)
    
    
@hellbot.on(admin_cmd(pattern="vday$"))
@hellbot.on(sudo_cmd(pattern="vday$", allow_sudo=True))
async def gif(event):
    if event.fwd_from:
        return
    event = await eor(event, "❤️❤️")
    await sleep(1)
    x = random.randrange(1, 21)
    if x == 1:
        await event.edit(f"My love for you \nSets my heart on fire \nand makes each day of my life \nSo special \n\n [✍️](https://telegra.ph/file/688abc98761f031128b9b.jpg) {hell}", link_preview=True)
    if x == 2:
        await event.edit(f"What I Need to live \nhas been given to me \nby the earth. Why I need \nto live has been given to\nme by you \n\n [✍️](https://telegra.ph/file/b6ab919f97283fc0d8c39.jpg) {hell}", link_preview=True)
    if x == 3:
        await event.edit(f"I Loved You Yesterday\n      I Love You Still\nI Always Have... \n       I Always Will\n\n [✍️](https://telegra.ph/file/d889a29342b97ecc1327a.jpg) {hell}", link_preview=True)
    if x == 4:
        await event.edit(f"My Days And Nights \nAre spent thinking of you \nMy dreams have come true\nNow that you are in my life\n\n [✍️](https://telegra.ph/file/9c63c4ae22c5353c0e681.jpg) {hell}", link_preview=True)
    if x == 5:
         await event.edit(f"I will always be \nthere for you, \nwill you be there \nfor me...\n\n [✍️](https://telegra.ph/file/1d335e658d16be01c0453.jpg) {hell}", link_preview=True)
    if x == 6:
        await event.edit(f"If I never MET you, I wouldn't LIKE you. \nIf I didn't LIKE you, I wouldn't LOVE you. \nIf I didn't LOVE you, I wouldn't MISS you. \n   **BUT I DID, I DO, AND I WILL... **\n\n [✍️](https://telegra.ph/file/0cda352205a74b1498cff.jpg) {hell}", link_preview=True)
    if x == 7:
        await event.edit(f"Thinking of you! \nDreaming of You! \nHugging you! \nMissing you! \nWishing you! \nI Love You! \n\n [✍️](https://telegra.ph/file/90554d3c4169a8cb8d04e.jpg) {hell}", link_preview=True)
    if x == 8:
        await event.edit(f"Anyone can catch your eye \nBut it takes \nSomeone special \nto catch your heart\n\n [✍️](https://telegra.ph/file/4b9d922e701a7184d098b.jpg) {hell}", link_preview=True)
    if x == 9:
        await event.edit(f"I love your warm smile \nAnd your kind, thoughtful way, \nLove the joy that you bring \nTo my life every day.\n\n [✍️](https://telegra.ph/file/e3d4401a919d8d81be4d4.jpg) {hell}", link_preview=True)
    if x == 10:
        await event.edit(f"I feel the happiest \nwhen I think about you \ncoz I love you. \nHappy Valentine’s Day!\n\n [✍️](https://telegra.ph/file/5e42aae4ad6b80cecf8e1.jpg) {hell}", link_preview=True)
    if x == 11:
        await event.edit(f"It still seems \nlike magic every time \nI remember how love softly \ntouched our hearts, \nbringing them together. \n\n[✍️](https://telegra.ph/file/88827f774d6b3b80d1183.jpg) {hell}", link_preview=True)
    if x == 12:
        await event.edit(f"I’ve fallen in love many times… always with you\n\n [✍️](https://telegra.ph/file/f19f0f60374f271d05aa1.jpg) {hell}", link_preview=True)
    if x == 13:
        await event.edit(f"I have one wish for Valentine’s Day. I want you wrapped up in a big bow. \n\n [✍️](https://telegra.ph/file/d8f73ed0a08fbfbbd0a6c.jpg) {hell}", link_preview=True)
    if x == 14:
        await event.edit(f"I asked God for a flower, he gave me a bouquet. \nI asked God for a minute, he gave me a day. \nI asked God for true love, he gave me that too. \nI asked for an angel and he gave me you.\n\n [✍️](https://telegra.ph/file/d0a11115399c161139abe.jpg) {hell}", link_preview=True)
    if x == 15:
        await event.edit(f"I don’t just love you. I love that I get to have you as my Valentine. \n\n [✍️](https://telegra.ph/file/f11bc438df9608d182e0d.jpg) {hell}", link_preview=True)
    if x == 16:
        await event.edit(f"You are my heart, my soul, my treasure,\nMy today, my tomorrow, my forever,\nMy everything!\n\n [✍️](https://telegra.ph/file/40fecb698ebb0caa202f8.jpg) {hell}", link_preview=True)
    if x == 17:
        await event.edit(f"Your eyes, your smile.\nYour touch, your kiss.\nYour promise, your words.\nOur everlasting bliss.\n\n [✍️](https://telegra.ph/file/0c72466dfe4c616754e84.jpg) {hell}", link_preview=True)
    if x == 18:
        await event.edit(f"I cherish every minute that I spend with you! And I am so blessed that I can. \n\n [✍️](https://telegra.ph/file/6d68acc1bd43a8690a228.jpg) {hell}", link_preview=True)
    if x == 19:
        await event.edit(f"Happy Valentine’s Day to the sweetest valentine I could want. You are my sweetheart, and I am glad you’re mine.\n\n [✍️](https://telegra.ph/file/26b052f976a7b5d3ca554.jpg) {hell}", link_preview=True)
    if x == 20:
        await event.edit(f"God has created you only for me, because he knows no one can love you more than me! Happy Valentine’s Day!\n\n [✍️](https://telegra.ph/file/b34e2679ff3cbb6225917.jpg) {hell}", link_preview=True)
    if x == 21:
        await event.edit(f"May this Valentine’s Day be filled with love, understanding, and contentment as you journey through life with those you hold dear. \n\n [✍️](https://telegra.ph/file/ae6dc5b359691d71f2d26.jpg) {hell}", link_preview=True)
        
CmdHelp("valentine").add_command(
  "vday", None, "Sends a random valentine's day quote with picture."
).add_command(
  "hvd", None, "Valentine's Day Animation."
).add()
