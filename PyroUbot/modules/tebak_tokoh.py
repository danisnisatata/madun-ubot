import httpx
import random
import re
from PyroUbot import *

__MODULE__ = "ᴛᴏᴋᴏʜ ǫᴜɪᴢ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴛᴏᴋᴏʜ ǫᴜɪᴢ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}sɪᴀᴘᴀ</code>
ᚗ <code>{0}ᴊᴛ</code> [ɴᴀᴍᴀ ᴛᴏᴋᴏʜ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ɢᴀᴍᴇ ᴛᴇʙᴀᴋ ᴛᴏᴋᴏʜ ᴅᴜɴɪᴀ ᴅᴇɴɢᴀɴ 𝟻𝟶+ ᴅᴀᴛᴀʙᴀsᴇ.
ᚗ ᴊᴀᴡᴀʙ ᴘᴀᴋᴇ ᴊᴛ ʙɪᴀʀ ɢᴀᴋ ɴᴀʙʀᴀᴋ ᴍᴏᴅᴜʟ ʟᴀɪɴ.</blockquote>
"""

# Database 50 Tokoh Berbobot (Iqbal Offc Selection)
TOKOH = [
    "Albert Einstein", "Nikola Tesla", "Isaac Newton", "Marie Curie", "Stephen Hawking",
    "Steve Jobs", "Bill Gates", "Elon Musk", "Mark Zuckerberg", "Jeff Bezos",
    "B.J. Habibie", "Soekarno", "Mohammad Hatta", "Gajah Mada", "Pangeran Diponegoro",
    "Nelson Mandela", "Mahatma Gandhi", "Abraham Lincoln", "Winston Churchill", "Napoleon Bonaparte",
    "Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Ludwig van Beethoven", "Wolfgang Amadeus Mozart",
    "William Shakespeare", "J.K. Rowling", "Charles Darwin", "Galileo Galilei", "Thomas Alva Edison",
    "Lionel Messi", "Cristiano Ronaldo", "Michael Jordan", "Muhammad Ali", "Pele",
    "Neil Armstrong", "Christopher Columbus", "Marco Polo", "Alexander the Great", "Genghis Khan",
    "Walt Disney", "Charlie Chaplin", "Marilyn Monroe", "Michael Jackson", "Elvis Presley",
    "Barack Obama", "Vladimir Putin", "Donald Trump", "Queen Elizabeth II", "Dalai Lama"
]

@PY.UBOT("siapa")
async def siapa_handler(client, message):
    emo = "<emoji id=5328247068503114930>👤</emoji>" if client.me.is_premium else "👤"
    target = random.choice(TOKOH)
    
    # Simpan jawaban di vars ubot lo
    await set_vars(client.me.id, "ANS_TOKOH", target)
    
    Tm = await message.edit(f"<blockquote><b>{emo} ᴍᴇɴᴄᴀʀɪ ɪɴꜰᴏ ᴛᴏᴋᴏʜ...</b></blockquote>")
    
    async with httpx.AsyncClient() as x:
        r = await x.get(f"https://id.wikipedia.org/api/rest_v1/page/summary/{target.replace(' ', '_')}")
        if r.status_code != 200:
            return await Tm.edit("<blockquote><b>❌ ɢᴀɢᴀʟ ᴀᴍʙɪʟ ᴅᴀᴛᴀ, ᴄᴏʙᴀ ʟᴀɢɪ ᴄᴏ!</b></blockquote>")
            
        data = r.json()
        desc = data.get("extract", "ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴅᴇsᴋʀɪᴘsɪ.")
        
        # Sensor Nama Otomatis (Regex Power)
        names = target.split()
        censored_desc = desc
        for name in names:
            if len(name) > 2:
                pattern = re.compile(re.escape(name), re.IGNORECASE)
                censored_desc = pattern.sub(" [ ᴛᴇʀsᴇɴsᴏʀ ] ", censored_desc)
        
    await Tm.edit(f"""
<blockquote><b>{emo} sɪᴀᴘᴀᴋᴀʜ ᴛᴏᴋᴏʜ ɪɴɪ?</b>

ᚗ <b>ᴄʟᴜᴇ :</b> <code>{censored_desc[:500]}...</code>

<b>ɢᴜɴᴀᴋᴀɴ :</b> <code>.ᴊᴛ [ɴᴀᴍᴀ]</code> ᴜɴᴛᴜᴋ ᴍᴇɴᴇʙᴀᴋ!</blockquote>""")

@PY.UBOT("jt")
async def jawabtokoh_handler(client, message):
    emo_win = "<emoji id=5318553579402173167>✅</emoji>" if client.me.is_premium else "✅"
    emo_lose = "<emoji id=5328212170568434856>❌</emoji>" if client.me.is_premium else "❌"
    
    answer = get_arg(message)
    correct_ans = await get_vars(client.me.id, "ANS_TOKOH")
    
    if not correct_ans:
        return await message.reply("<blockquote><b>ʙᴇʟᴜᴍ ᴀᴅᴀ sᴏᴀʟ, ᴋᴇᴛɪᴋ .sɪᴀᴘᴀ ᴅᴜʟᴜ!</b></blockquote>")
    
    if not answer:
        return await message.reply("<blockquote><b>ᴍᴀsᴜᴋᴋᴀɴ ᴊᴀᴡᴀʙᴀɴɴʏᴀ ᴄᴏ!</b></blockquote>")
        
    # Cek jawaban (Case Insensitive)
    if answer.lower() in correct_ans.lower():
        await message.reply(f"""
<blockquote><b>{emo_win} ᴊᴀᴡᴀʙᴀɴ ʟᴏ ʙᴇɴᴇʀ!</b>

ᚗ <b>ᴛᴏᴋᴏʜ :</b> <code>{correct_ans}</code>
ᚗ <b>ᴘᴏᴡᴇʀᴇᴅ :</b> ɪǫʙᴀʟ ᴏғғᴄ</blockquote>""")
        await set_vars(client.me.id, "ANS_TOKOH", False)
    else:
        await message.reply(f"<blockquote><b>{emo_lose} sᴀʟᴀʜ ᴄᴏ! ᴘɪᴋɪʀ ʟᴀɢɪ.</b></blockquote>")
        