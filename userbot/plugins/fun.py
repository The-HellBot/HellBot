import random
from random import choice
import requests
import re
import time

from cowpy import cow
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName

from hellbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp

#✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓#

RUNSREACTS = [
    "`Runs to Thanos`",
    "`Runs far, far away from earth`",
    "`Running faster than usian bolt coz I'mma Bot`",
    "`Runs to Marie`",
    "`This Group is too cancerous to deal with.`",
    "`Cya bois`",
    "`I am a mad person. Plox Ban me.`",
    "`I go away`",
    "`I am just walking off, coz me is too fat.`",
    "`I Fugged off!`",
]
GAALI_STR = [
    "`Madarchod Randi ke bacche.Oye bosdike madarchod bhen ke lode tere gand me lohe ka danda garam karke dalu randwe tujhetho gali ke kutte gand pe chut rakh ke katenge me bata raha hu tere lode pe madhu makkhi Katelode ke ando pe Road roller chale tu kab bathroom me muthne Jaye tho Tera loda ghir Jaye fir tere ando me se lizard ke bacche nikle teko kidnap Kare aur childporn banaye maa ke chuttad ke lode tere saat Johnny sins rape Kare aur jab wo teko anal de tab loda andar fas Jaye bkl tere jhaat pe waxing karunga me dhek lio fir jab tu chillayega na tab tere muh me Mai gai ka gobar dalunga sale tere gand ke balo pe tel laga ke jala du me teko Anaconda leke gand me dalu tho muh se nikle maa ke lode hamesha chutiyo jaisa bartav kartha he tu maa ke Dai chawal drugs tere gand Me dalunga thi tatti nahi nikle maa darchod kabhi teko Marne ka mouka mil gaya na tho bas I'll do my best to get that tatti outof you aur tere jaise chutio ko is duniya me jagaha bhi nahi maa ke lode bandarchod tere gand me chitiya Kate wo bhi bullet ants maadarchod samj nahi aaraha tere baap NE teko kya khake paida kiya Tha kesa chutiya he tu rand ke bacche teko shadi me khana khane na mile teko gand pe 4 thappad mare sab log aur blade se likhe I want anal madarchod bosdike maccharki tatte ke baal chutiye maa ke chut pe ghode ka Lund tere gand me jaltha hu koila Dale bhen ke lode MAA KI CHUT MAI TALWAR DUNGA BC CHUT FAT JAEGI AUR USME SE ITNA KHOON NIKLEGA MZA AJAEGA DEKHNE KA SALE MAA KE BHOSDE SE BAHR AJA FIR BAAP SE ZUBAN DA TERI MAA KI CHUT CHOD CHOD KE BHOSDABNADU MADARCHOD AUR USKE UPAR CENENT LAGADU KI TERE JESA GANDU INSAAN KABHI BAHR NA A SKE ESI GANDI CHUT MAI SE LODA LASUN MADRCHOD TERI MAA KI CHUT GASTI AMA KA CHUTIA BACHA TERI MAA KO CHOD CHOD K PAGAL KAR DUNGA MAA K LODY KISI SASTIII RANDII K BACHY TERI MAA KI CHOOT MAIN TEER MAARUN GANDU HARAMI TERI COLLEGE JATI BAJI KA ROAD PEY RAPE KARONGANDU KI OLAAD HARAM KI NASAL PAPA HUN TERA BHEN PESH KAR AB PAPA KO TERI MAA KKALE KUSS MAIN KIS`",
    "`Main roz teri behno ki banjar chut me apna lawda daalke andar haryali lata tha magar aaj unke ke baare me sunke mujhe bhut afsos huwa..ki unko ab bada loudha chahye..ab mera balatkaaari lawda lagataar 4 ghante tk apne muh me kon rakhega..vo teri behne hi thi jo apni kaali magar rasilli chut mere saamne khol deti aur zameen pe naagin ki tarah rengne lgti thi jaise ki kisine unki chut pe naariyal tod diya ho vo b bada wala mumbai ka naariyal..apni chennal maa ko b nhi bhej rahe mere paas to main kaixe tum logo se vaada karu ki main teri maa chodd dungaw..ab agar tun sach me chahta hai ki main tum dono k mc ki chut me dhammal karu to mera lawda apne muh me rakho aur kaho Sameer hamare sage papa hain... Aur agar tb b the apni maa ki kaali chut mere saamne nahi rakhi to tumhare ghar me ghuske tumhari maa ka balatkaar kar dungaw jaixe delhi me huwa tha...ab teri chudi hui kuttiyo ki tarah apni gaand hilaate hue mere aage kalapna mt ni to tumhari fatti bhoxdi me 100 ched karunga`",
    "`Taare hai Asmaan me very very bright jaat na jla bskd dekh le apni hight.`",
    "`Zindagi ki na toote lari iski lulli hoti nhi khadi`",
    "`Kbhi kbhi meri dil me khyaal ata hai ayse chutiyo ko kon paida kr jata hai😂.`",
    "`Saawan ka mahina pawan kare shor jake gand mara bskd kahi aur.`",
    "`Dil ke armaa ansuon me beh jaye tum bskd ke chutiye hi reh gye.`",
    "`Ishq Se Tabiyat Ne Zeest Ka Mazaa aya maine is lodu ko randi khane me paya.`",
    "`Mirza galib ki yeh khani hai tu bhosdika hai yeh sab ki jubani hai.`",
    "`Mashoor Rand, Ne Arz Kiya Hai. Aane Wale Aate Hai, Jaane Wale Jaate Hai. Yaade Bas Unki Reh Jaati Hai, Jo G**Nd Sujaa Ke Jaate Hai`",
    "`Pani kam hai matke me gand marlunga jhatke me.`",
    "`Aand kitne bhi bade ho, lund ke niche hi rehte hai`",
    "`Tum Ameer hum gareeb hum jhopdiwale Tum bhosiwale`",
    "`Sisi Bhari Gulab ki padi palang ke pass chodne wale chod gye ab q baitha udaas`",
    "`Phuloo Ka Raja Gulaab Kaato me Rehta hai Jeewan ka Nirmata jaato me rehta hai😂`",
    "`Chude hue maal ko yaad mt krna Jo Chut na de usse kabhi friyad mt karna jise chudna hai wo chud ke rhegi bekar me muth maar ke apni jindagi barbaad mt krna`",
    "`Gand mare gandu Chut mare Chutiya Sabse accha mutti 2 mint me chutti😛`",
    "`Marzi Ka Sex Pap Nahi Hota.. Piche Se Dalne Wala Kabhi Baap Nahi Hota.. Condom Zarur Lagana Mere Dost Qki.. Sex K Waqt Popat Ke Pass Dimag Nahi Hota.`",
    "`Uss Ne Hothon Se Chhu Kar Lowd* Pe Nasha Kar Diya; Lu*D Ki Baat To Aur Thi, Uss Ne To Jhato* Ko Bhi Khada Kar Diya!`",
]
RAPE_STRINGS = [
    "`Rape Done Drink The Cum`",
    "`EK baat yaad rkhio, Chut ka Chakkar matlab maut se takkar`",
    "`The user has been successfully raped`",
    "`Dekho Bhaiyya esa hai! Izzat bachailo apni warna Gaand maar lenge tumhari`",
    "`Relax your Rear, ders nothing to fear,The Rape train is finally here`",
    "`Rape coming... Raped! haha 😆`",
    "`Kitni baar Rape krvyega mujhse?`",
    "`Tu Randi hai Sabko pta hai😂`",
    "`Don't rape too much bossdk, else problem....`",
    "`Tu sasti rendi hai Sabko pta hai😂`",
    "`Lodu Andha hai kya Yaha tera rape ho raha hai aur tu abhi tak yahi gaand mara raha hai lulz`",
]
ABUSE_STRINGS = [
    "`Madharchod`",
    "`Gaandu`",
    "`Chutiya he rah jaye ga`",
    "`Ja be Gaandu`",
    "`Ma ka Bhodsa madharchod`",
    "`mml`",
    "`You MotherFukcer`",
    "`Muh Me Lega Bhosdike ?`",
    "`Abee tu tiktok wala chakka h na?`",
    "`Jaa naa madarchod`",
    "`Teri maa meri malllll`",
    "`Tu wahi h naa jo roz apni maa chudata hai?`",
]
HIABUSE_STR = [
    "Maderchod- MOTHERFUCKER",
    "Bhosadike-BORN FROM A ROTTEN PUSSY",
    "Bhen chod-Sister fucker",
    "Bhadhava- Pimp",
    "Bhadhava- Pimp",
    "Chodu- Fucker",
    "Chutiya- Fucker, bastard",
    "Gaand- ASS",
    "Gaandu-Asshole",
    "Gadha, Bakland- Idiot",
    "Lauda, Lund- Penis, dick, cock",
    "Hijra- Gay, Transsexual",
    "Kuttiya- Bitch",
    "Paad- FART",
    "Randi- HOOKER",
    "Saala kutta- Bloody dog",
    "Saali kutti- Bloody bitch",
    "Tatti- Shit",
    "Kamina- bastard",
    "Chut ke pasine mein talay huye bhajiye- Snack fried in pussy sweat",
    "Chut ke dhakkan- Pussy lid",
    "Chut ke gulam- Pussy whipped",
    "Chutiya ka bheja ghas khane gaya hai- idiot’s brain has gone to eat grass",
    "Choot marani ka- Pussy whipped",
    "Choot ka baal- Hair of vagina",
    "Chipkali ke jhaat ke baal- Lizard’s cunt hairs",
    "Chipkali ke jhaat ke paseene- Sweat of Lizard’s pubic hair",
    "Chipkali ke gaand ke pasine-  Sweat of a lizard’s ass",
    "Chipkali ke chut ke pasine- Sweat of reptiles cunt",
    "Chipkali ki bhigi chut- Wet pussy of a wall lizard",
    "Chinaal ke gadde ke nipple ke baal ke joon- Prostitute’s breast’s nipple’s hair’s lice",
    "Chullu bhar muth mein doob mar-  Drown yourself in a handful of semen",
    "Cuntmama- Vaginal uncle",
    "Chhed- Vagina,Hole",
    "Apni gaand mein muthi daal- Put your fist up your ass",
    "Apni lund choos- Go and suck your own dick",
    "Apni ma ko ja choos- Go suck your mom",
    "Bhen ke laude- Sister’s dick",
    "Bhen ke takke: Go and suck your sister’s balls",
    "Abla naari tera buble bhaari-  woman, your tits are huge",
    "Bhonsri-Waalaa- You fucker",
    "Bhadwe ka awlat- Son of a pimp",
    "Bhains ki aulad- Son of a buffalo",
    "Buddha Khoosat- Old fart",
    "Bol teri gand kaise maru- let me know how to fuck you in the ass",
    "Bur ki chatani- Ketchup of cunt",
    "Chunni- Clit",
    "Chinaal- Whore",
    "Chudai khana- Whore house",
    "Chudan chuda- Fucking games",
    "Chut ka pujari- pussy worshipper",
    "Chut ka bhoot- Vaginal Ghost",
    "Gaand ka makhan- Butter from the ass",
    "Gaand main lassan- Garlic in ass",
    "Gaand main danda- Stick in ass",
    "Gaand main keera- Bug up your ass",
    "Gaand mein bambu- A bambooup your ass",
    "Gaandfat- Busted ass",
    "Pote kitne bhi bade ho, lund ke niche hi rehte hai- However big the balls might be, they have to stay beneath the penis",
    "Hazaar lund teri gaand main-Thousand dicks in your ass",
    "Jhat ke baal- Pubic hair",
    "Jhaant ke pissu- Bug of pubic hair",
    "Kadak Mall- Sexy Girl",
    "Kali Choot Ke Safaid Jhaat- White hair of a black pussy",
    "Khotey ki aulda- Son of donkey",
    "Kutte ka awlat- Son of a dog",
    "Kutte ki jat- Breed of dog",
    "Kutte ke tatte- Dog’s balls",
    "Kutte ke poot, teri maa ki choot-  Son of a dog, your mother’s pussy",
    "Lavde ke bal- Hair on your penis",
    "muh mei lele: Suck my dick",
    "Lund Chus: Suck dick",
    "Lund Ke Pasine- Sweat of dick",
    "Meri Gand Ka Khatmal: Bug of my Ass",
    "Moot, Mootna- Piss off",
    "Najayaz paidaish- Illegitimately born",
    "Randi khana- whore house",
    "Sadi hui gaand- Stinking ass",
    "Teri gaand main kute ka lund- A dog’s dick in your ass",
    "Teri maa ka bhosda- Your mother’s breasts",
    "Teri maa ki chut- Your mother’s pussy",
    "Tere gaand mein keede paday- May worms infest your ass-hole",
    "Ullu ke pathe- Idiot",
  ]
GEY_STRINGS = [
    "`you gey bsdk`",
    "`you gey`",
    "`you gey in the house`",
    "`you chakka`",
    "`you gey gey gey gey gey gey gey gey`",
    "`you gey go away`",
    "`bhago bhenchod gay aaya`"
]
RENDISTR = [
    "`I Know Uh ez Rendi Bhay Dont show Your Randi Pesa Here`",
    "`Jag Suna suna laage Sab #maderchod bhay`",
    "`you talking behind meh wew uh iz my fan now bhay`",
    "`Wanna pass in Life Goto BRAZZER.CAM BHAY`",
    "`Uh iz Pro i iz noob your boob is landi uh are Randi`",
    "`Sellers Nasa calling Uh bhay😆`",
    "`Badwoo ki yojna behan bna ke ch*da uh iz badwa its your yozja?`",
    "`CHAND PE CHADA HAI CHANDYAAN KA GHODA TERA NAAM HAI MANSUR TU HAI BEHAN KA LOD*😂`",
    "`Jab se dil lga baithe tanhai me maa chu*da baithe wo kho gyi kisi aur ke pyar hum apne hi jaato me aag lga baithe`",
    "`Chadii ke ander se lal pani kha se ata hai ky teri masuka ka bhosda bhi paan khata hai😂`",
    "`Sun bhosdi ke By anonyCrew MOHABBAT KE SIWA AUR BHI GAM HAI JAMANE ME BSDK GAND PAHAT JATI HAI PAISA KAMANE ME`",
    "`Thaan liya tha Sayri nhi krege Unka pichwada dekha Alfaaz nikal gye`",
    "`Ravivaar ko dekha Chand Ka Tukra Itna Baar Dekha par Jaath na Ukra`",
    "`Katal kro Tir se Talwar me Ky Rkkha hai Maal Chodo Sari Me Salwar me Ky Rkkha hai`",
]
NOOBSTR = [
    "`YOU PRO NIMBA DONT MESS WIDH MEH`",
    "`Haha yes`",
    "`NOOB NIMBA TRYING TO BE FAMOUS KEK`",
    "`Sometimes one middle finger isn’t enough to let someone know how you feel. That’s why you have two hands`",
    "`Some Nimbas need to open their small minds instead of their big mouths`",
    "`UH DONT KNOW MEH SO STAY AWAY LAWDE`",
    "`Kysa kysaaaa haaan? Phir MAAR nhi Khayega tu?`",
    "`Zikr Jinka hota hai galiyo meh woh bhosdika ajj paya gya naliyo me`",
]
PRO_STRINGS = [
    "`This gey is pro as phack.`",
    "`Proness Lebel: 6969696969`",
    "`Itna pro banda dekhlia bc, ab to marna hoga.`",
    "`U iz pro but i iz ur DAD, KeK`",
    "`NOOB NIMBA TRYING TO BE FAMOUS KEK`",
    "`Sometimes one middle finger isnâ€™t enough to let someone know how you feel. Thatâ€™s why you have two hands`",
    "`Some Nimbas need to open their small minds instead of their big mouths`",
    "Pros here. Nubs laik me leave -_-.",
    "`UH DONT KNOW MEH SO STAY AWAY LAWDE`",
    "`Kysa kysaaaa haaan? Phir MAAR nhi Khayega tu?`",
    "`Zikr Jinka hota hai galiyo meh woh bhosdika ajj paya gya naliyo me`",
]
CHU_STRINGS = [
    "`Taare hai Asmaan me very very bright jaat na jla bskd dekh le apni hight.`",
    "`jindagi ki na toote lari iski lulli hoti nhi khadi`",
    "`Kbhi kbhi meri dil me khyaal ata hai ayse chutiyo ko kon paida kr jata hai😂.`",
    "`Saawan ka mahina pawan kare shor jake gand mara bskd kahi aur.`",
    "`Dil ke armaa ansuon me beh jaye tum bskd ke chutiye hi reh gye.`",
    "`Ishq Se Tabiyat Ne Zeest Ka Mazaa aya maine is lodu ko randi khane me paya.`",
    "`Mirza galib ki yeh khani hai tu bhosdika hai yeh sab ki jubani hai.`",
    "`Ek dora hai ek nora hai charo taraf kohra hi kohra hai ye sabse bada behan ka lawda hai.`",
    "`Phool murjhate achhe nahi lagte aap land khujate acche nahi lagte yehi umar hai chodne ki yaaro aap bathroom mein hilaate acche nahi lagte.`",
    "`Badi hasrat thi ki khole iski maa ki salwaar ka  nara par iski maa ki berukhi dekho ki aagayi nangi dobara.`",
    "`Na jaane konsi shilajit hai iski maa ki yadon mein jab bhi sochta hun jhanajhana jaata hun.`",
    "`Yaara Teri Yaari Pe Mujhe Shak Nahi Tha; Lekin Sabne Teri Gaand Maari, Kya Mera Koi Haq Nahi Tha.`",
    "`Yehi to kamal hai hamara baap bante ho tum aur naam aata hai humara.`",
    "`Chinti chadi pahad pe angrejon ka jamana tha lund ki pistol thi chut pe nishana tha.`",
    "`Bhola khada bich bazaar fut fut kr roye  gaand  Maar Sab Chal Diyo Paisa Diyo N Koye.`",
    "`Pani kam hain  matke mein gand mardunga jhatke mein.`",
    "`Duniya haseeno ka mela fir bhi mera chutiya dost akela.`",
    "`8 ko kehte hain hindi mein aath ja bsdk tu ja ke kutiya ki chaat.`",
    "`Purani baatein bhool ja mera lund pakad ke jhool ja.`",
    "`Permanent hai pakka tera baap chaka.`",
    "`Yaar azab tera nakhra ghazab tera style hai gand dhone ki tameez nahi haath mein mobile hain.`",
]
FUK_STRINGS = [
    "`It's better to let someone think you are an Idiot than to open your mouth and prove it.`",
    "`Talking to a liberal is like trying to explain social media to a 70 years old`",
    "`CHAND PE HAI APUN LAWDE.`",
    "`Pehle main tereko chakna dega, fir daru pilayega, fir jab aap dimag se nahi L*nd se sochoge, tab bolega..`",
    "`Pardhan mantri se number liya, parliament apne :__;baap ka hai...`",
    "`Cachaa Ooo bhosdi wale Chacha`",
    "`Aaisi Londiya Chodiye, L*nd Ka Aapa Khoye, Auro Se Chudi Na Ho, Biwi Wo Hi Hoye`",
    "`Nachoo Bhosdike Nachoo`",
    "`Jinda toh jaat ke baal bhi hai`",
    "`Sab ko pta tu randi ka baccha hai (its just a joke)`",
]
THANOS_STRINGS = [
    "`Mashoor Rand, Ne Arz Kiya Hai. Aane Wale Aate Hai, Jaane Wale Jaate Hai. Yaade Bas Unki Reh Jaati Hai, Jo G**Nd Sujaa Ke Jaate Hai`",
    "`Pani kam hai matkey me ga*d mardunga teri ek jatke me`",
    "`Aand kitne bhi bade ho, lund ke niche hi rehte hai`",
    "`Tum Ameer hum gareeb hum jhopdiwale Tum bhosiwale`",
    "`Sisi Bhari Gulab ki padi palang ke pass chodne wale chod gye ab q baitha udaas`",
    "`Phuloo Ka Raja Gulaab Kaato me Rehta hai Jeewan ka Nirmata jaato me rehta hai😂`",
    "`Chude hue maal ko yaad mt krna Jo Chut na de usse kabhi friyad mt karna jise chudna hai wo chud ke rhegi bekar me muth maar ke apni jindagi barbaad mt krna`",
    "`Gand mare gandu Chut mare Chutiya Sabse accha mutti 2 mint me chutti😛`",
    "`Marzi Ka Sex Pap Nahi Hota.. Piche Se Dalne Wala Kabhi Baap Nahi Hota.. Condom Zarur Lagana Mere Dost Qki.. Sex K Waqt Popat Ke Pass Dimag Nahi Hota.`",
    "`Uss Ne Hothon Se Chhu Kar Lowd* Pe Nasha Kar Diya; Lu*D Ki Baat To Aur Thi, Uss Ne To Jhato* Ko Bhi Khada Kar Diya!`",
]
INSULT_STRINGS = [
    "`Owww ... Such a stupid idiot.`",
    "`Don't drink and type.`",
    "`Command not found. Just like your brain.`",
    "`Bot rule 544 section 9 prevents me from replying to stupid humans like you.`",
    "`Sorry, we do not sell brains.`",
    "`Believe me you are not normal.`",
    "`I bet your brain feels as good as new, seeing that you never use it.`",
    "`If I wanted to kill myself I'd climb your ego and jump to your IQ.`",
    "`You didn't evolve from apes, they evolved from you.`",
    "`What language are you speaking? Cause it sounds like bullshit.`",
    "`You are proof that evolution CAN go in reverse.`",
    "`I would ask you how old you are but I know you can't count that high.`",
    "`As an outsider, what do you think of the human race?`",
    "`Ordinarily people live and learn. You just live.`",
    "`Keep talking, someday you'll say something intelligent!.......(I doubt it though)`",
    "`Everyone has the right to be stupid but you are abusing the privilege.`",
    "`I'm sorry I hurt your feelings when I called you stupid. I thought you already knew that.`",
    "`You should try tasting cyanide.`",
    "`You should try sleeping forever.`",
    "`Pick up a gun and shoot yourself.`",
    "`Try bathing with Hydrochloric Acid instead of water.`",
    "`Go Green! Stop inhaling Oxygen.`",
    "`God was searching for you. You should leave to meet him.`",
    "`You should Volunteer for target in an firing range.`",
    "`Try playing catch and throw with RDX its fun.`",
    "`People like you are the reason we have middle fingers.`",
    "`When your mom dropped you off at the school, she got a ticket for littering.`",
    "`You’re so ugly that when you cry, the tears roll down the back of your head…just to avoid your face.`",
    "`If you’re talking behind my back then you’re in a perfect position to kiss my a**!.`",
]
# ===========================================
@bot.on(admin_cmd(pattern=f"randi$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"randi$", allow_sudo=True))
async def rendi(e):
   txt = random.choice(RENDISTR)
   await edit_or_reply(e, txt)
   
   
@bot.on(admin_cmd(pattern=f"habuse$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"habuse$", allow_sudo=True))
async def thenus(e):
   txt = random.choice(THANOS_STRINGS)
   await edit_or_reply(e, txt)
   
   
@bot.on(admin_cmd(pattern=f"fuk$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"fuk$", allow_sudo=True))
async def tapatap(e):
   txt = random.choice(FUK_STRINGS)
   await edit_or_reply(e, txt)
   
   
@bot.on(admin_cmd(pattern=f"chu$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"chu$", allow_sudo=True))
async def chut(e):
   txt = random.choice(CHU_STRINGS)
   await edit_or_reply(e, txt)
   
   
@bot.on(admin_cmd(pattern=f"noob$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"noob$", allow_sudo=True))
async def nub(e):
   txt = random.choice(NOOBSTR)
   await edit_or_reply(e, txt)


@bot.on(admin_cmd(pattern=f"run$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"run$", allow_sudo=True))
async def metoo(e):
    txt = random.choice(RUNSREACTS)
    await edit_or_reply(e, txt)


@bot.on(admin_cmd(pattern=f"gali$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"gali$", allow_sudo=True))
async def metoo(e):
    txt = random.choice(GAALI_STR)
    await edit_or_reply(e, txt)


@bot.on(admin_cmd(pattern=f"rape$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"rape$", allow_sudo=True))
async def metoo(e):
    txt = random.choice(RAPE_STRINGS)
    await edit_or_reply(e, txt)


@bot.on(admin_cmd(pattern=f"abuse$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"abuse$", allow_sudo=True))
async def metoo(e):
    txt = random.choice(ABUSE_STRINGS)
    await edit_or_reply(e, txt)


@bot.on(admin_cmd(pattern=f"gey$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"gey$", allow_sudo=True))
async def metoo(e):
    txt = random.choice(GEY_STRINGS)
    await edit_or_reply(e, txt)


@bot.on(admin_cmd(pattern=f"piro$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"piro$", allow_sudo=True))
async def metoo(e):
    txt = random.choice(PRO_STRINGS)
    await edit_or_reply(e, txt)


@bot.on(admin_cmd(pattern=f"insult$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"insult$", allow_sudo=True))
async def metoo(e):
    txt = random.choice(INSULT_STRINGS)
    await edit_or_reply(e, txt)

@bot.on(admin_cmd(pattern=f"hiabuse$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"hiabuse$", allow_sudo=True))
async def metoo(e):
    txt = random.choice(HIABUSE_STR)
    await edit_or_reply(e, txt)


CmdHelp("fun").add_command(
  'insult', None, 'Sends some random insulting lines'
).add_command(
  'piro', None, 'Sends some random lines for "piro" guys'
).add_command(
  'gey', None, 'Sends some random lines for geys (°^°)'
).add_command(
  'abuse', None, 'Abuse the cunts'
).add_command(
  'rape', None, 'No offence. Use and see -_-'
).add_command(
  'gali', None, 'You know what this cmd is'
).add_command(
  'run', None, 'Chala jaa bhosdike'
).add_command(
  'hiabuse', None, 'Abuses in Hindi as well as English OwO'
).add_command(
  'randi', None, 'Are you rendi?'
).add_command(
  'habuse', None, 'Some of the abusive shayris'
).add_command(
  'fuk', None, 'Use and see bruh'
).add_command(
  'chu', None, 'Use and see'
).add_command(
  'noob', None, 'Fuckin Noobs'
).add()
