import aiohttp
from bs4 import BeautifulSoup
from PyroUbot import *

__MODULE__ = "ᴀʟᴋɪᴛᴀʙ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀʟᴋɪᴛᴀʙ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴀʟᴋɪᴛᴀʙ</code> [ǫᴜᴇʀʏ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴᴄᴀʀɪ ᴀʏᴀᴛ ᴅᴀɴ ᴘᴀsᴀʟ ᴅᴀʀɪ ᴀʟᴋɪᴛᴀʙ ʙᴇʀᴅᴀsᴀʀᴋᴀɴ ᴋᴀᴛᴀ ᴋᴜɴᴄɪ.</blockquote>
"""

@PY.UBOT("alkitab")
@PY.TOP_CMD
async def alkitab_handler(client, message):
    prs_emo = await EMO.PROSES(client)
    brhsl_emo = await EMO.BERHASIL(client)
    ggl_emo = await EMO.GAGAL(client)
    
    args = get_arg(message)
    if not args:
        return await message.reply_text(
            f"<blockquote><b>{ggl_emo} ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ǫᴜᴇʀʏ!</b>\nᚗ ᴄᴏɴᴛᴏʜ: <code>.ᴀʟᴋɪᴛᴀʙ ᴋᴇᴊᴀᴅɪᴀɴ</code></blockquote>"
        )

    status_msg = await message.reply_text(f"<blockquote><b>{prs_emo} sᴇᴅᴀɴɢ ᴍᴇɴᴄᴀʀɪ ᴀʏᴀᴛ...</b></blockquote>")
    
    url = f"https://alkitab.me/search?q={args}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url, timeout=15) as response:
                if response.status != 200:
                    return await status_msg.edit(f"<blockquote><b>{ggl_emo} ɢᴀɢᴀʟ ᴍᴇɴɢʜᴜʙᴜɴɢɪ sᴇʀᴠᴇʀ!</b></blockquote>")
                
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                
                results = []
                for div in soup.find_all('div', class_='vw'):
                    p_tag = div.find('p')
                    a_tag = div.find('a')
                    if p_tag and a_tag:
                        teks = p_tag.get_text(strip=True)
                        title = a_tag.get_text(strip=True)
                        results.append({'teks': teks, 'title': title})

                if not results:
                    return await status_msg.edit(f"<blockquote><b>{ggl_emo} ᴛɪᴅᴀᴋ ᴀᴅᴀ ʜᴀsɪʟ ᴜɴᴛᴜᴋ :</b> <code>{args}</code></blockquote>")

                # Batasi hasil agar tidak kepanjangan (limit 5 ayat teratas)
                output = f"<blockquote><b>📖 ʜᴀsɪʟ ᴘᴇɴᴄᴀʀɪᴀɴ ᴀʟᴋɪᴛᴀʙ</b></blockquote>\n\n"
                for v in results[:5]:
                    output += f"<blockquote><b>{v['title']}</b>\n{v['teks']}</blockquote>\n"
                
                output += f"<b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ"
                
                await status_msg.edit(output)

    except Exception as e:
        await status_msg.edit(f"<blockquote><b>{ggl_emo} ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ:</b>\n<code>{str(e)}</code></blockquote>")
        