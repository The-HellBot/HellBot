from telethon.sync import TelegramClient
from telethon.sessions import StringSession
print("")
print("""Welcome To HellBot String Generator By HellBot Official""")
print("""Kindly Enter Your Details To Continue ! """)

API_KEY = input("API_KEY: ")
API_HASH = input("API_HASH: ")

while True:
 try:
  with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
   print(
       "String Sent To Your Saved Message, Store It To A Safe Place!! "
   )
   print("")
   session = client.session.save()
   client.send_message(
       "me",
       f"Here is your TELEGRAM STRING SESSION\n(Tap to copy it)👇 \n\n {session} \n\n And Visit @HellBot_Official For Any Help !"
   )

   print(
       "Thanks for Choosing HellBot Have A Good Time....Note That When You Terminate the Old Session ComeBack And Genrate A New String Session Old One Wont Work"
   )
 except:
  print("")
  print(
      "Wrong phone number \n make sure its with correct country code. Example : +919961998999 ! Kindly Retry"
  )
  print("")
  continue
 break
