# Porting to @Hellbot_official by @Kraken_The_BadASS..........
# Original Credit to @Veryhelpful.
# Edited and ported by @Kraken_The_BadASS
#Credit edit karega to tu 100 baap ka:-)


from telethon import events
import asyncio
import os
import sys
import random
from userbot.utils import admin_cmd

@borg.on(admin_cmd(pattern=r"hflirt$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Hey! Here's a fact about you......")
    await asyncio.sleep(2.3)
    h=(random.randrange(1,8)) 
    if h==1:
        await event.edit("Doctor Ne Advice Kia Hai Ki Sone Se Pahle Apki Pic Dekh Kar Sona Jaroori Hai, Warna Heart Attack Aa Sakta Hai.😨")
    if h==2:
        await event.edit("☺️Ap Itne Cute Ho Ki Agar Mai Msg Na Bhi Karna Chahu.To Bhi Mera Hath Khud Keypad Pr Chalne Lagta Hai😶.")
    if h==3:
        await event.edit("😋Aag joh dil mein lagi hai, usse duniya mein laga doonga main ... joh teri doli uthi, zamaane ko jalaa doonga main😏")
    if h==4:
        await event.edit("Jaldi se koi bhagwan ko bulao kyuki ek pari kho gayi hain aur wo pari yaha mujhse chatting kar rahi hain😛.")
    if h==5:
        await event.edit("Meri aankho 👀ko kuch ho gaya hain, aap per se hat hi nahi rahi hain😶")
    if h==6:
        await event.edit("🤨Aap choro ke rani lagte ho kyuki aapne mera dil chura liya hain😘")
    if h==7:
        await event.edit("👀Aapki aankhe ocean ki tarah blue he aur me usme har baar dub jata hu🙂")
    if h==8:
        await event.edit("📷Aap ek camera ki tarah ho jab bhi aapka photos dekhta hu meri automatic smile aaa jati hain🙈")
        
        
@borg.on(admin_cmd(pattern=r"eflirt$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Hey! Here's a fact about you......")
    await asyncio.sleep(2.3)
    h=(random.randrange(1,12)) 
    if h==1:
        await event.edit("Your lips look lonely would they like to meet mine?")
    if h==2:
        await event.edit("There isn’t a word in the dictionary to describe how beautiful you are")
    if h==3:
        await event.edit("I have had a really bad day and it always makes me feel better to see a pretty girl smile. So, would you smile for me?")
    if h==4:
        await event.edit("I lost my teddy bear can i sleep with you tonight?")
    if h==5:
        await event.edit("I’m no organ donor but I’d be happy to give you my heart.")
    if h==6:
        await event.edit("If I had to rate you out of 10 I’d rate you a 9… because I am the one that you are missing")
    if h==7:
        await event.edit("Can I follow you? Cause my mom told me to follow my dreams")
    if h==8:
        await event.edit("Your hand looks heavy can i hold it for you?")
    if h==9:
        await event.edit("You may fall from the sky, you may fall from a tree, but the best way to fall… is in love with me.")
    if h==10:
        await event.edit("Are you the sun? Because you’re so beautiful it’s blinding me")
    if h==11:
        await event.edit("I should call you Google, because you have everything I’m looking for.")
    if h==12:
        await event.edit("Can you kiss me on the cheek so I can at least say a cute girl kissed me tonight?")
        

@borg.on(admin_cmd(pattern=r"rshay$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Hey! Choosing A Shayri for u from my database 🤙.......")
    await asyncio.sleep(2.3)
    h=(random.randrange(1,25)) 
    if h==1:
        await event.edit("HAMNE TOH BSS DOST KO HI BEWAFA SAMJHA THHA...\nYAHAAN SACCHA PYAAR V SAATH NHI DIYA🥱🥱")
    if h==2:
        await event.edit("Love leads to death 🥱🥱\nOr to a living dead 🥱🥱")
    if h==3:
        await event.edit("BAATEN TU KABHI YE NA BHULNA.....\nKOI TERE KAARANN HAI..MRR RHA 🥱🥱🥱🥱")
    if h==4:
        await event.edit("Ae dost Tere jaise log ko kaat k fekk dange hm\nMeri taraf aae her toofan ko Teri taraff bhej dange hm...\nLekhin tune Jo saath chorrda hamara ......\nKsm SE badnaam krke tujhe nya dost....\n dhoondh lange hum🥱🥱🥱🥱")
    if h==5:
        await event.edit("Bde ajeeb Hain ye Zindagi k raaste.........\nAnjaane modd pe log Mill jaate Hain...khhud ko apna BTA k.....chorrrd jaate Hain...\n. KRTE hai. H baat (Zindagi bhar saath rahenge) interest khtm hone prr......zinda LAASH BNA jaate h🥱🥱🥱")
    if h==6:
        await event.edit("Dill jaisa thha waisa hi reh jaata......\nJitne dard thhey UTNE kaafi thhey.......\nZindagi aap me aake aur tadpaa diya.........\nMillla kya u badnaam krke ....zinda LAASh...... DIYA🙃🙃")
    if h==7:
        await event.edit("DARD SE IS KADAR DOSTI HO GYI.......\nZINDAGI BEDARD SI HO GYI.......\nJALL  GAY WO ASHIYANA.......JO KABHI BNA HI NHI THHA......\nROSHNI TOH CHORRDO..........\nGHAR MEIN JO MOMABATTIE  THHI WO V KHTM HO GYI.........🥱🥱")
    if h==8:
        await event.edit("Zindagi barbaad hai...... Zindagi SE pyaar na Karo.......\nHo raat toh Dinn ka intezaar na Karo.......\nWo Pall v aaega....jiss pal ka INTEZAAR na  ho aako.....\nPRRR uspe kabhi aitbaar na Karo........🥱🥱")
    if h==9:
        await event.edit("Dard k saath rhte hue v dosti nhi Hui\nZindagi bedard si hote hue v nhi Hui\nAashiyana toh jall gya\nPrr  Roshni nhi Hui ..........❤️")
    if h==10:
        await event.edit("ME: DUNIYA ME AISI KYA CHEEZ HAI JO FREE MEI MILTI HAI............\nMAH HEART : DHOKHA ")
    if h==11:
        await event.edit("JO INSAAN AAPKO TADAPTA HUA ....ROTA CHORRD DE NA.......... TOH SAMAJH LENA WO KABHI AAPSE \nPYAAR NHI KRR SKTA.....AGAR KOI PYAAR KAREGA NA......\nTOH WO KABHI AAPKO AISEY NHI CHORRDEGA.......🥱🥱")
    if h==12:
        await event.edit("TOOTE HAIN.....ES TARAH DILL ......\nAWAAZ TKK NA AAI....\nHUM JAISEY JEE RHE H.....\nKOI JEE K TOH BTAAE....🙃🙃")
    if h==13:
        await event.edit("AANKHON ME AANSU LEKE........\nHOTHON SE MUSKURAAE................\nHUM JAISEY JEE RHE HAIN.......\nKLI JEE K TOH BTAAE...🙃🙃")
    if h==14:
        await event.edit("TUJHE KAISEY PTA NA CHALAA.................\nK MAIN TENU PYAAR KRR Di AAN...........\nTUJHE KAISEY PTA NA CHALAA......\nK TERA INTEZAAR KRR DI AAN........🙃")
    if h==15:
        await event.edit("MTT CHORRDNA KISIKO USKE HAAL PE.......\nHO SKTA H.......\nAAPKE ALAWA  USKE PAAS AUR KOI NA HO.......🙃🙃")
    if h==16:
        await event.edit("🙂Kehti Hain Zindagi Pyaar Kar Ke Toh Dekh ,\n Kya Pata Tha Jis Zindagi Ne Pyaar Mein Jeena Sikhaya,\n Aaj Wahi Gir Ke Samhalna Bhi Sikha Gayi☺️")
    if h==17:
        await event.edit("आज कुछ इस कदर याद आयी तेरी ..,\nआँसू गिर पड़े जैसे ...,\nनदी को नया मोड़ मिल गया !!")
    if h==18:
        await event.edit("कभी अपना कहते थे \n आज बेगाना कर गए...\n\nहमसे बात ना करने के लिए \n बहाना कर गए... \nशुक्रिया कैसे करूं तुम्हारा \nसमझ नहीं आ रहा...\nमेरे इस नियाने से दिल को \n**सयाना कर गए...* ")
    if h==19:
        await event.edit("जानती हूँ जवाब देना आसान नही \nपर कोशिश भी नही करते तुम ,\n मेरा हाल जानने की !!")
    if h==20:
        await event.edit("हम हर बिछड़न में नई मुलाकात को ढूंढते है !!\nतुम्हारे बार बार छोड़ जाने की अब ,\nआदत सी हो गयी है !!")
    if h==21:
        await event.edit("सोचते तो तब भी थे हम \nतुम मेरे नही हो सकते !!\nअब भी यकीन कहाँ है \n के तुम कभी मेरे थे !!")
    if h==22:
        await event.edit("पगला है वो ,\nना जाने इतना क्यों प्यार करता है !!\nकुछ बातें मेरी \n  कहने से पहले ही समझ जाता है !! ")    
    if h==23:
        await event.edit("आज कल हाल कुछ  \n Telephone booth की \nतरह हो गया है !!\n लोग आते है बात करते है ,\nऔर बस चले जाते है !")
    if h==24:
        await event.edit("दिल रोकना तो बहोत चाहता है \nमगर रोकेंगे नही ....!\nना तुम हमारे कुछ हो \nऔर हम भी तुम्हारे कुछ नही !!")
    if h==25:
        await event.edit("फर्क नही पड़ता सच मे ,\n कोई आये कोई जाए !!\nबस जो दिल को बार बार \n आदतें लग जाती है ना \nकिसी की ..!!\n बस छुड़ाने में कुछ देर लगती है !!")
        

@borg.on(admin_cmd(pattern=r"ratt$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("🤙")
    await asyncio.sleep(2)
    h=(random.randrange(1,8)) 
    if h==1:
        await event.edit("Dil nhi karta ab\n kisi se dil lagane ko \n bohot aati hai tere jaise \n keh deta hu hoon laut jane ko.")
    if h==2:
        await event.edit("humari hesiyat ka andaza tum ye\n jaan ke laga lo hum kabhi unke \n nahi hote jo har kisi ke ho jate hai ")
    if h==3:
        await event.edit("Attitude तो अपना भी खानदानी है,\nऔर तू मेरे दिल की रानी है, \nइसलिये कह रहा हूँ मान जा, \nक्योंकि अपनी तो करोड़ो दीवानी हैं।")
    if h==4:
        await event.edit("मेरा वाला थोड़ा लेट आयेगा,\n लेकिन जब आयेगा तो लाखो में एक आयेगा।")
    if h==5:
        await event.edit("इतना Attitude न दिखा जिंदगी में तकदीर बदलती रहती है,\n शीशा वहीं रहता है,\n पर तस्वीर बदलती रहती है।")
    if h==6:
        await event.edit("हम से है ज़माना, ज़माने से हम नही,\nकोई हम से नज़रे मिलाये, \nकिसी मे इतना दम नही।")
    if h==7:
        await event.edit("हम तो शौक तलवारों के पाला करते हैं,\nबन्दूकों की ज़िद तो बच्चे किया करते हैं।\nशेर अपना शिकार करते हैं और हम अपने Attitude से वार करते हैं।")
    if h==8:
        await event.edit("शेर अपना शिकार करते हैं\n और हम अपने Attitude से वार करते हैं।")
        

@borg.on(admin_cmd(pattern="gbye ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Hey! Read this and go🙂")
    await asyncio.sleep(2.3)
    h=(random.randrange(1,18))
    if h==1:
        await event.edit(" जिंदगी में तन्हा रहना तो मुमकिन नहीं,\nतेरे साथ चलना दुनिया को गवारा भी नहीं,\nइसलिए, तेरा-मेरा दूर जाना ही बेहतर है।")
    if h==2:
        await event.edit("कुछ दिन साथ चलने वाले,\nथोड़ा और साथ चलने की तमन्ना थी,\nमजबूरी है कहना ही पड़ेगा अलविदा।")#creadit to kraken,sawan
    if h==3:
        await event.edit("न कहा न कुछ सुना, बस चुपके से चल दिए,\nमोहब्बत के उन्होंने सारे मायने बदल दिए,\अब तो तन्हा गलियों में गुजरेगी हर शाम,\nमर भी गए, तो भी नहीं भूलेंगे उनका नाम।")
    if h==4:
        await event.edit("पास थे, तो रोने की वजह बनते थे,\nदूर जाकर शायद मुस्कुराना सीख लें आप।")
    if h==5:
        await event.edit("दोबारा मिलें जिंदगी में यह दुआ करेंगे,\nदूर रहकर भी नजदीक होने की चाह करेंगे।")#creadit to kraken,sawan
    if h==6:
        await event.edit("माफ करना मुझे दूर तो जाना पड़ेगा,\nपास होकर भी तुम्हे अब भूल जाना पड़ेगा।")#creadit to kraken,sawan
    if h==7:
        await event.edit("वो शाम सुहानी थी जो गुजरी तेरे साथ,\nबिन तेरे अब कैसे कटेगी सारी रात,\nसमझ लो तुम भी यह मजबूरी है दिल की,\nनहीं गए, तो कैसे कल फिर होगी मुलाकात।")#creadit to kraken,sawan
    if h==8:
        await eventt.edit("तेरे साथ मुस्कुराना और ठोकरों से संभलना सीखा है,\nआता नहीं अलविदा कहना बस रोकर जताना सीखा है।")
    if h==9:
        await event.edit("यार तेरी दोस्ती को सलाम है,\nअलविदा कहकर भी हंसा दिया,\nयह बस तेरी यारी का कमाल है।")#creadit to kraken,sawan
    if h==10:
        await event.edit("ताउम्र तेरे साथ बीती रातों को फिर याद करेंगे,\nकह सकें अलविदा तुझसे इसलिए मेरे यार,\nआंसू का एक भी कतरा बहाए बिना बात करेंगे।")#creadit to kraken,sawan
    if h==11:
        await event.edit("रूठा जमाना जिंदगी भी रूठी,\nतभी तो तेरे-मेरे बीच ये दूरी छूटी,\nसमझ लेना तुम है ये मेरी मजबूरी,\nवरना न आने देता तेरे-मेरे बीच यह दूरी।")#creadit to kraken,sawan
    if h==12:
        await event.edit("करीब आते-आते तू कुछ दूर सा हो गया है,\nशाम को अलविदा कह तू कहीं गुम सा गया है,\nचाहता हूं मैं करीब होने का एहसास तेरे पर,\nखुशी के खातिर तेरी तुझे अलविदा कह गया हूं।")
    if h==13:
        await event.edit("खुश हूं फिर भी ये आंखे नम हैं,\nन चाहते हुए भी दूर जाने का गम है।")
    if h==14:
        await event.edit("दूर जाने की खबर सुनकर ये धड़कने रुक जाती हैं,\nअलविदा कहने के वक्त यार मेरी आंखें भर आती हैं।")#creadit to kraken,sawan
    if h==15:
        await event.edit(" अब हर लम्हा तुम्हारे बिना सूना सा लगेगा,\nअलविदा कहकर तुम्हारी यादों में जीना पड़ेगा।")
    if h==16:
        await event.edit("अब हलचल है दिल में नई उम्मीद की तलाश के लिए,\nकहना पड़ेगा अलविदा नई मंजिल की तलाश के लिए")
    if h==17:
        await event.edit(" जब तुम जाते हो, तो गुलिस्तां के सभी फूल झड़ जाते हैं,\nसंभलकर कहो अलविदा जाते-जाते पेड़ों से क्यों टकरा जाते हो।")
    if h==18:
        await event.edit(" तिरछी निगाहों से जो देखा उन्होंने,\nतो हम मदहोश हो चले,\nजब पता चला कि वो अलविदा कहने आए,\nतो हम बेहोश हो चले।")
        
        