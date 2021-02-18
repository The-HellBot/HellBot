import emoji
from googletrans import Translator
from google_trans_new import google_translator
import requests
from deep_translator import GoogleTranslator
from googletrans import LANGUAGES
from langdetect import detect

@hellbot_cmd("trt", is_args=True)
async def _(hell):
    input_str = hell.pattern_match.group(1)
    if hell.reply_to_msg_id:
        previous_message = await hell.get_reply_message()
        text = previous_message.message
        lan = input_str or "en"
    elif "|" in input_str:
        lan, text = input_str.split("|")
    else:
        await tgbot.send_message(
            hell.chat_id, "`/trt LanguageCode` as reply to a message"
        )
        return
    text = emoji.demojize(text.strip())
    lan = lan.strip()
    translator = google_translator()
    translated = translator.translate(text, lang_tgt=lan)
    lmao_bruh = text
    lmao = detect(text)
    after_tr_text = lmao
    source_lan = LANGUAGES[after_tr_text]
    transl_lan = LANGUAGES[lan]
    output_str = f"""**TRANSLATED**
**From ({source_lan})**:
`{text}`

**To ({transl_lan})**:
`{translated}`"""
      
    try:
        await tgbot.send_message(hell.chat_id, output_str)
    except Exception:
        await tgbot.send_message(hell.chat_id, "Something Went Wrong 🤔")
