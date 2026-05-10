import asyncio
import requests
from PyroUbot import *

__MODULE__ = "ʜᴀᴘᴘʏᴍᴏᴅ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʜᴀᴘᴘʏᴍᴏᴅ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ʜᴍᴏᴅ</code> [ɴᴀᴍᴀ_ᴀᴘʟɪᴋᴀsɪ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴᴄᴀʀɪ ʟɪɴᴋ ᴅᴏᴡɴʟᴏᴀᴅ ᴀᴘʟɪᴋᴀsɪ ᴅᴀɴ ɢᴀᴍᴇ ᴍᴏᴅ ᴀɴᴅʀᴏɪᴅ ᴅɪ ʜᴀᴘᴘʏᴍᴏᴅ.</blockquote>
"""

@PY.UBOT("hmod")
async def happymod_handler(client, message):
    prs_emo = await EMO.PROSES(client)
    brhsl_emo = await EMO.BERHASIL(client)
    ggl_emo = await EMO.GAGAL(client)
    
    args = get_arg(message)
    if not args:
        return await message.reply_text(
            f"<blockquote><b>{ggl_emo} ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ɴᴀᴍᴀ ᴀᴘʟɪᴋᴀsɪ!</b>\nᚗ ᴄᴏɴᴛᴏʜ: <code>.ʜᴍᴏᴅ ᴍɪɴᴇᴄʀᴀꜰᴛ</code></blockquote>"
        )

    status_msg = await message.reply_text(f"<blockquote><b>{prs_emo} sᴇᴅᴀɴɢ ᴍᴇɴᴄᴀʀɪ ᴍᴏᴅ ᴀᴘᴋ...</b></blockquote>")

    def fetch_happymod():
        try:
            # Menggunakan apikey lu yang sudah terpasang
            api_url = f"https://api.botcahx.eu.org/api/search/happymod?query={args}&apikey=@iqbalnew77"
            response = requests.get(api_url, timeout=15)
            return response.json()
        except:
            return None

    loop = asyncio.get_event_loop()
    data = await loop.run_in_executor(None, fetch_happymod)

    if data and data.get("status") and "result" in data:
        results = data["result"][:5] # Ambil 5 hasil teratas biar gak kepanjangan
        res_text = f"<blockquote><b>🔍 ʜᴀsɪʟ ᴘᴇɴᴄᴀʀɪᴀɴ ʜᴀᴘᴘʏᴍᴏᴅ</b>\n\n"
        
        for item in results:
            res_text += (
                f"<b>ᚗ ɴᴀᴍᴀ :</b> <code>{item['title']}</code>\n"
                f"<b>ᚗ ʀᴀᴛɪɴɢ :</b> <code>⭐ {item['rating']}</code>\n"
                f"<b>ᚗ ʟɪɴᴋ :</b> <a href='{item['link']}'>[ ᴅᴏᴡɴʟᴏᴀᴅ ᴅɪ sɪɴɪ ]</a>\n\n"
            )
        
        res_text += f"<b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>"
        await status_msg.edit(res_text, disable_web_page_preview=True)
    else:
        await status_msg.edit(f"<blockquote><b>{ggl_emo} ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ ʜᴀsɪʟ ᴜɴᴛᴜᴋ ᴘᴇɴᴄᴀʀɪᴀɴ ᴛᴇʀsᴇʙᴜᴛ!</b></blockquote>")
        