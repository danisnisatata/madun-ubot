import aiohttp
from bs4 import BeautifulSoup
from PyroUbot import *

__MODULE__ = "ᴡɪᴋɪᴘᴇᴅɪᴀ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴡɪᴋɪᴘᴇᴅɪᴀ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴡɪᴋɪ</code> [ǫᴜᴇʀʏ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴᴄᴀʀɪ ɪɴꜰᴏʀᴍᴀsɪ ᴅᴀʀɪ ᴡɪᴋɪᴘᴇᴅɪᴀ ɪɴᴅᴏɴᴇsɪᴀ.</blockquote>
"""

async def wikipedia(query):
    try:
        url = f"https://id.wikipedia.org/wiki/{query}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    return {'status': response.status, 'Pesan': 'ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ'}
                page_content = await response.text()
                soup = BeautifulSoup(page_content, 'html.parser')          
                title = soup.find(id="firstHeading").get_text().strip()    
                
                paragraphs = soup.select('#mw-content-text .mw-parser-output > p')
                content = "\n".join([p.get_text().strip() for p in paragraphs if p.get_text().strip()])
                
                return {
                    'status': response.status,
                    'result': {
                        'judul': title,
                        'isi': content
                    }
                }
    except Exception as e:
        return {'status': 404, 'Pesan': str(e)}


@PY.UBOT("wiki|wikipedia")
async def wiki_handler(client, message):
    text = message.text.split(maxsplit=1)[1] if len(message.command) > 1 else None
    if not text:
        return await message.reply_text('<blockquote><b>❌ ᴄᴏɴᴛᴏʜ : <code>.ᴡɪᴋɪ</code> [ɪsʀᴀᴇʟ]</b></blockquote>')
            
    status_msg = await message.reply_text("<blockquote><b>🔍 sᴇᴅᴀɴɢ ᴍᴇɴᴄᴀʀɪ ᴅɪ ᴡɪᴋɪᴘᴇᴅɪᴀ...</b></blockquote>")
    
    res = await wikipedia(text)    
    if res['status'] == 200:
        result = res['result']
        caption = (
            f"<blockquote><b>📚 ᴊᴜᴅᴜʟ: {result['judul']}</b>\n\n"
            f"<b>📖 ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>\n"
            f"{result['isi']}</blockquote>"
        )

        # Potong jika terlalu panjang untuk caption
        if len(caption) > 1024:
            caption = caption[:1000] + '...'

        try:
            await client.send_photo(
                message.chat.id,
                photo="https://itzpire.com/file/540429176594.jpg",
                caption=caption
            )
            await status_msg.delete()
        except Exception:
            # Jika kirim foto gagal (misal fileID mati), kirim teks aja
            await status_msg.edit(caption)
    else:
        await status_msg.edit('<blockquote><b>❌ ɪɴꜰᴏʀᴍᴀsɪ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ.</b></blockquote>')
        
        