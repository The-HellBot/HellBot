from telethon.sessions import StringSession
from telethon.sync import TelegramClient
import random
from colorama import Fore, Style


kraken = """                                                                                            
HHHHHHHHH     HHHHHHHHH                   lllllll lllllll       BBBBBBBBBBBBBBBBB                             tttt          
H:::::::H     H:::::::H                   l:::::l l:::::l       B::::::::::::::::B                         ttt:::t          
H:::::::H     H:::::::H                   l:::::l l:::::l       B::::::BBBBBB:::::B                        t:::::t          
HH::::::H     H::::::HH                   l:::::l l:::::l       BB:::::B     B:::::B                       t:::::t          
  H:::::H     H:::::H      eeeeeeeeeeee    l::::l  l::::l         B::::B     B:::::B   ooooooooooo   ttttttt:::::ttttttt    
  H:::::H     H:::::H    ee::::::::::::ee  l::::l  l::::l         B::::B     B:::::B oo:::::::::::oo t:::::::::::::::::t    
  H::::::HHHHH::::::H   e::::::eeeee:::::eel::::l  l::::l         B::::BBBBBB:::::B o:::::::::::::::ot:::::::::::::::::t    
  H:::::::::::::::::H  e::::::e     e:::::el::::l  l::::l         B:::::::::::::BB  o:::::ooooo:::::otttttt:::::::tttttt    
  H:::::::::::::::::H  e:::::::eeeee::::::el::::l  l::::l         B::::BBBBBB:::::B o::::o     o::::o      t:::::t          
  H::::::HHHHH::::::H  e:::::::::::::::::e l::::l  l::::l         B::::B     B:::::Bo::::o     o::::o      t:::::t          
  H:::::H     H:::::H  e::::::eeeeeeeeeee  l::::l  l::::l         B::::B     B:::::Bo::::o     o::::o      t:::::t          
  H:::::H     H:::::H  e:::::::e           l::::l  l::::l         B::::B     B:::::Bo::::o     o::::o      t:::::t    tttttt
HH::::::H     H::::::HHe::::::::e         l::::::ll::::::l      BB:::::BBBBBB::::::Bo:::::ooooo:::::o      t::::::tttt:::::t
H:::::::H     H:::::::H e::::::::eeeeeeee l::::::ll::::::l      B:::::::::::::::::B o:::::::::::::::o      tt::::::::::::::t
H:::::::H     H:::::::H  ee:::::::::::::e l::::::ll::::::l      B::::::::::::::::B   oo:::::::::::oo         tt:::::::::::tt
HHHHHHHHH     HHHHHHHHH    eeeeeeeeeeeeee llllllllllllllll      BBBBBBBBBBBBBBBBB      ooooooooooo             ttttttttttt  
"""
                                                                                                            
print("")
print(Style.BRIGHT + For.GREEN + kraken)
print("""Welcome To HellBot String Generator By @Kraken_The_BadASS""")
print("""Kindly Enter Your Details To Continue ! """)

API_KEY = input("API_KEY: ")
API_HASH = input("API_HASH: ")

while True:
    try:
        with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
            print("String Sent To Your Saved Message, Store It To A Safe Place!! ")
            print("")
            session = client.session.save()
            client.send_message(
                "me",
                f"Here is your TELEGRAM STRING SESSION\n(Tap to copy it)👇 \n\n `{session}` \n\n And Visit @HellBot_Official For Any Help !",
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
