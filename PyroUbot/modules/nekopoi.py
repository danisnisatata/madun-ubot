import aiohttp
from PyroUbot import *

__MODULE__ = "ɴᴇᴋᴏᴘᴏɪ"
__HELP__ = """
<blockquote><b>ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɴᴇᴋᴏᴘᴏɪ</b>

ᴘᴇʀɪɴᴛᴀʜ:
<code>{0}nekopoi</code> [ᴊᴜᴅᴜʟ]
ᴄᴏɴᴛᴏʜ: <code>{0}nekopoi overflow</code></blockquote>
"""

@PY.UBOT("nekopoi")
@PY.TOP_CMD
async def _(client, message):
    # Cek apakah ada nama judul setelah perintah .nekopoi
    if len(message.command) < 2:
        return await message.reply("<blockquote><b>❓ ɴᴀᴍᴀ ᴀᴘᴀ ʏᴀɴɢ ᴍᴀᴜ ᴅɪᴄᴀʀɪ, ᴋɪɴɢ?</b>\n\nᴄᴏɴᴛᴏʜ: <code>.nekopoi overflow</code></blockquote>")

    # Ambil nama judul dari input user
    query = " ".join(message.command[1:])
    status_msg = await message.reply_text(f"<blockquote><b>🔍 sᴇᴅᴀɴɢ ᴍᴇɴɢᴀᴍʙɪʟ ᴀsᴜᴘᴀɴ: {query}...</b></blockquote>")
    
    # Pake endpoint search biar lebih akurat sesuai nama yang diminta
    api_url = f"https://api.botcahx.eu.org/api/webzone/nekopoi?query={query}&apikey=@iqbalnew77"
    
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(api_url) as resp:
                if resp.status != 200:
                    return await status_msg.edit(f"<blockquote><b>❌ sᴇʀᴠᴇʀ ᴇʀʀᴏʀ ({resp.status})</b></blockquote>")
                
                content_type = resp.headers.get('Content-Type', '')
                if 'application/json' not in content_type:
                    return await status_msg.edit("<blockquote><b>⚠️ API ʟᴀɢɪ ʙᴇʀᴍᴀsᴀʟᴀʜ/ᴍᴇɴɢɪʀɪᴍ ʜᴛᴍʟ.</b></blockquote>")
                
                data = await resp.json()
            
            if not data.get("status") or not data.get("result"):
                return await status_msg.edit(f"<blockquote><b>❌ ᴊᴜᴅᴜʟ '{query}' ɢᴀᴋ ᴋᴇᴛᴇᴍᴜ, ᴋɪɴɢ!</b></blockquote>")
            
            # Ambil maksimal 5 hasil biar gak kepanjangan
            results = data["result"][:5]
            res_text = f"<blockquote><b>🔞 ɴᴇᴋᴏᴘᴏɪ sᴇᴀʀᴄʜ ʀᴇsᴜʟᴛ</b></blockquote>\n\n"
            
            for i, item in enumerate(results, 1):
                title = item.get("title", "No Title")
                link = item.get("url", "#")
                res_text += f"<blockquote><b>{i}. {title}</b>\n🔗 <a href='{link}'>ᴛᴏɴᴛᴏɴ ᴅɪ sɪɴɪ</a></blockquote>\n"
            
            res_text += f"\n<b>🔎 ʜᴀsɪʟ ᴘᴇɴᴄᴀʀɪᴀɴ: {query}</b>"
            await status_msg.edit(res_text, disable_web_page_preview=True)
            
        except Exception as e:
            await status_msg.edit(f"<blockquote><b>⚠️ ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ:</b>\n<code>{str(e)}</code></blockquote>")
            