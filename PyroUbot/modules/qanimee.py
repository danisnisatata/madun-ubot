import requests
import random
from PyroUbot import *

__MODULE__ = "ϙᴜᴏᴛᴇs ᴀɴɪᴍᴇ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ϙᴜᴏᴛᴇs ᴀɴɪᴍᴇ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ǫᴀɴɪᴍᴇ</code>

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴɢᴀᴍʙɪʟ ᴋᴀᴛᴀ-ᴋᴀᴛᴀ ʙɪᴊᴀᴋ ᴅᴀɴ ᴍᴏᴛɪᴠᴀsɪ ᴅᴀʀɪ ʙᴇʀʙᴀɢᴀɪ ᴋᴀʀᴀᴋᴛᴇʀ ᴀɴɪᴍᴇ.</blockquote>
"""

@PY.UBOT("qanime")
@PY.TOP_CMD
async def quotes_anime_handler(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)

    status_msg = await message.reply_text(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇɴᴄᴀʀɪ ɪɴsᴘɪʀᴀsɪ ᴀɴɪᴍᴇ...</b></blockquote>")
    
    API_URL = "https://api.siputzx.my.id/api/r/quotesanime"
    
    try:
        response = requests.get(API_URL, timeout=15)
        data = response.json()
        
        if data.get("status") and data.get("data"):
            quotes_list = data.get("data")
            # Mengambil satu quotes secara acak agar lebih eksklusif
            q = random.choice(quotes_list)
            
            result = (
                f"<blockquote><b>{brhsl} ϙᴜᴏᴛᴇs ᴀɴɪᴍᴇ ᴘʀᴇᴍɪᴜᴍ</b>\n\n"
                f"<b>ᚗ ᴋᴀʀᴀᴋᴛᴇʀ :</b> <code>{q['karakter']}</code>\n"
                f"<b>ᚗ ᴀɴɪᴍᴇ :</b> <code>{q['anime']}</code>\n"
                f"<b>ᚗ ᴇᴘɪsᴏᴅᴇ :</b> <code>{q['episode']}</code>\n\n"
                f"<b>⌭ ǫᴜᴏᴛᴇs :</b>\n<i>“{q['quotes']}”</i>\n\n"
                f"<b>ᚗ ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>"
            )
            
            await status_msg.edit(result)
        else:
            await status_msg.edit(f"<blockquote><b>{ggl} ɢᴀɢᴀʟ ᴍᴇɴɢᴀᴍʙɪʟ ᴅᴀᴛᴀ ǫᴜᴏᴛᴇs.</b></blockquote>")
    
    except Exception as e:
        await status_msg.edit(f"<blockquote><b>{ggl} ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ:</b>\n<code>{str(e)}</code></blockquote>")
        