import httpx
import random
import asyncio
from PyroUbot import *

__MODULE__ = "ᴡᴏʀʟᴅ-ǫᴜɪᴢ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴡᴏʀʟᴅ-ǫᴜɪᴢ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ʟᴏɢᴏ</code>
ᚗ <code>{0}ᴄᴇᴋʟᴏɢᴏ</code> [ᴊᴀᴡᴀʙᴀɴ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴅᴀᴛᴀʙᴀsᴇ ʟᴏɢᴏ ᴛᴇʀʟᴇɴɢᴋᴀᴘ ᴅɪ ᴅᴜɴɪᴀ (ʙᴏʟᴀ, ᴍᴀᴋᴀɴᴀɴ, ᴘᴀʀꜰᴜᴍ, ᴛᴇᴄʜ).</blockquote>
"""

# DATABASE RAKSASA (Iqbal Offc World Collection)
LOGOS = {
    # === TEMPAT MAKAN & F&B (GLOBAL & INDO) ===
    "McDonalds": "https://logo.clearbit.com/mcdonalds.com?size=500",
    "KFC": "https://logo.clearbit.com/kfc.com?size=500",
    "Starbucks": "https://logo.clearbit.com/starbucks.com?size=500",
    "Burger King": "https://logo.clearbit.com/bk.com?size=500",
    "Pizza Hut": "https://logo.clearbit.com/pizzahut.com?size=500",
    "Dominos Pizza": "https://logo.clearbit.com/dominos.com?size=500",
    "Subway": "https://logo.clearbit.com/subway.com?size=500",
    "HokBen": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_xNqXqS1oX3L9-0Z6-YkF_yvS-WlHh-L_sw&s", # Manual link
    "JCO": "https://logo.clearbit.com/jcoprosco.com?size=500",
    "Chatime": "https://logo.clearbit.com/chatime.com.tw?size=500",
    "Mixue": "https://logo.clearbit.com/mixue.com?size=500",

    # === PARFUM (LOKAL & DESIGNER) ===
    "Braven": "https://logo.clearbit.com/braven.id?size=500",
    "Mykonos": "https://logo.clearbit.com/projectmykonos.com?size=500",
    "Scarlett": "https://logo.clearbit.com/scarlettwhitening.com?size=500",
    "Velixir": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_xNqXqS1oX3L9-0Z6-YkF_yvS-WlHh-L_sw&s",
    "Afnan": "https://logo.clearbit.com/afnan.com?size=500",
    "Jean Paul Gaultier": "https://logo.clearbit.com/jeanpaulgaultier.com?size=500",
    "Dior": "https://logo.clearbit.com/dior.com?size=500",
    "Chanel": "https://logo.clearbit.com/chanel.com?size=500",
    "Creed": "https://logo.clearbit.com/creedfragrance.com?size=500",

    # === CLUB BOLA DUNIA ===
    "Real Madrid": "https://logo.clearbit.com/realmadrid.com?size=500",
    "Manchester City": "https://logo.clearbit.com/mancity.com?size=500",
    "Liverpool": "https://logo.clearbit.com/liverpoolfc.com?size=500",
    "Barcelona": "https://logo.clearbit.com/fcbarcelona.com?size=500",
    "Juventus": "https://logo.clearbit.com/juventus.com?size=500",
    "Paris Saint Germain": "https://logo.clearbit.com/psg.fr?size=500",
    "Manchester United": "https://logo.clearbit.com/manutd.com?size=500",
    "Arsenal": "https://logo.clearbit.com/arsenal.com?size=500",
    "Chelsea": "https://logo.clearbit.com/chelseafc.com?size=500",
    "Bayern Munich": "https://logo.clearbit.com/fcbayern.com?size=500",

    # === BRAND TECH & SOSMED ===
    "Apple": "https://logo.clearbit.com/apple.com?size=500",
    "Google": "https://logo.clearbit.com/google.com?size=500",
    "Microsoft": "https://logo.clearbit.com/microsoft.com?size=500",
    "Tesla": "https://logo.clearbit.com/tesla.com?size=500",
    "Facebook": "https://logo.clearbit.com/facebook.com?size=500",
    "Instagram": "https://logo.clearbit.com/instagram.com?size=500",
    "TikTok": "https://logo.clearbit.com/tiktok.com?size=500",
    "Netflix": "https://logo.clearbit.com/netflix.com?size=500",
    "Youtube": "https://logo.clearbit.com/youtube.com?size=500"
}

@PY.UBOT("logo")
async def logo_handler(client, message):
    emo = "<emoji id=5328247068503114930>🖼️</emoji>" if client.me.is_premium else "🖼️"
    brand, url = random.choice(list(LOGOS.items()))
    
    await set_vars(client.me.id, "ANS_LOGO", brand)
    
    Tm = await message.reply(f"<blockquote><b>{emo} ᴍᴇɴɢᴀᴍʙɪʟ ʟᴏɢᴏ ᴅᴜɴɪᴀ...</b></blockquote>")
    
    try:
        await client.send_photo(
            message.chat.id, 
            url, 
            caption=f"""
<blockquote><b>{emo} ᴛᴇʙᴀᴋ ɪɴɪ ʟᴏɢᴏ ᴀᴘᴀ?</b>

ᚗ <b>ᴋᴀᴛᴇɢᴏʀɪ :</b> <code>ᴡᴏʀʟᴅ ʟᴏɢᴏ (ɪǫʙᴀʟ ᴏғғᴄ)</code>
ᚗ <b>ᴡᴀᴋᴛᴜ :</b> <code>30 ᴅᴇᴛɪᴋ</code>
ᚗ <b>ɢᴜɴᴀᴋᴀɴ :</b> <code>.ᴄᴇᴋʟᴏɢᴏ [ᴊᴀᴡᴀʙᴀɴ]</code></blockquote>"""
        )
        await Tm.delete()
    except:
        await Tm.edit("<blockquote><b>❌ ɢᴀɢᴀʟ ᴍᴇɴᴜɴᴊᴜᴋᴋᴀɴ ʟᴏɢᴏ, ᴄᴏʙᴀ ʟᴀɢɪ!</b></blockquote>")
        return

    # Hint Otomatis (15 Detik)
    await asyncio.sleep(15)
    ans_now = await get_vars(client.me.id, "ANS_LOGO")
    if ans_now:
        hint = f"{ans_now[0]}{ans_now[1]}..."
        await message.reply(f"<blockquote><b>💡 ʜɪɴᴛ :</b> ʙᴇʀᴀᴡᴀʟᴀɴ ᴅᴀʀɪ ʜᴜʀᴜꜰ <code>{hint}</code></blockquote>")

    await asyncio.sleep(15)
    
    # Cek apakah sudah dijawab
    ans_final = await get_vars(client.me.id, "ANS_LOGO")
    if ans_final:
        await message.reply(f"<blockquote><b>⏰ ᴡᴀᴋᴛᴜ ʜᴀʙɪs! ᴊᴀᴡᴀʙᴀɴɴʏᴀ :</b> <code>{ans_final}</code></blockquote>")
        await set_vars(client.me.id, "ANS_LOGO", False)

@PY.UBOT("ceklogo")
async def ceklogo_handler(client, message):
    answer = get_arg(message)
    correct_ans = await get_vars(client.me.id, "ANS_LOGO")
    
    if not correct_ans: return
    
    if not answer:
        return await message.reply("<blockquote><b>ᴊᴀᴡᴀʙᴀɴɴʏᴀ ᴍᴀɴᴀ ᴄᴏ?</b></blockquote>")
    
    # Logic: Fleksibel biar gampang ditebak
    if answer.lower() in correct_ans.lower() or correct_ans.lower() in answer.lower():
        await message.reply(f"<blockquote><b>✅ ɢᴀᴄᴏʀ! ᴊᴀᴡᴀʙᴀɴ ʙᴇɴᴇʀ :</b> <code>{correct_ans}</code></blockquote>")
        await set_vars(client.me.id, "ANS_LOGO", False)
    else:
        await message.reply("<blockquote><b>❌ sᴀʟᴀʜ! ᴄᴏʙᴀ ʟᴀɢɪ ᴄᴏ.</b></blockquote>")
        