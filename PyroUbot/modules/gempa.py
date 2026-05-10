import os
import httpx
from PyroUbot import *

__MODULE__ = "ɢᴇᴍᴘᴀ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɢᴇᴍᴘᴀ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ɢᴇᴍᴘᴀ</code>

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴɢᴀᴍʙɪʟ ɪɴꜰᴏʀᴍᴀsɪ ᴛᴇʀᴋɪɴɪ ᴛᴇɴᴛᴀɴɢ ɢᴇᴍᴘᴀ ʙᴜᴍɪ ᴅᴀʀɪ sᴇʀᴠᴇʀ ʙᴍᴋɢ.</blockquote>
"""

@PY.UBOT("gempa")
@PY.TOP_CMD
async def gempa_handler(client, message):
    prs_emo = await EMO.PROSES(client)
    brhsl_emo = await EMO.BERHASIL(client)
    ggl_emo = await EMO.GAGAL(client)
    
    status_msg = await message.reply_text(f"<blockquote><b>{prs_emo} sᴇᴅᴀɴɢ ᴍᴇɴɢᴀᴍʙɪʟ ᴅᴀᴛᴀ ʙᴍᴋɢ...</b></blockquote>")
    
    # API Link dengan apikey lu
    api_url = "https://api.botcahx.eu.org/api/search/gempa?apikey=@iqbalnew77"
    # Logo BMKG atau Gambar Peta Gempa
    photo_url = "https://warning.bmkg.go.id/img/logo-bmkg.png"
    
    try:
        async with httpx.AsyncClient() as session:
            response = await session.get(api_url, timeout=20)
            if response.status_code != 200:
                return await status_msg.edit(f"<blockquote><b>{ggl_emo} ɢᴀɢᴀʟ ᴍᴇɴɢʜᴜʙᴜɴɢɪ sᴇʀᴠᴇʀ ᴀᴘɪ!</b></blockquote>")
            
            data = response.json()
            if not data.get("status"):
                return await status_msg.edit(f"<blockquote><b>{ggl_emo} ᴅᴀᴛᴀ ɢᴇᴍᴘᴀ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ.</b></blockquote>")
            
            hasil = data['result']['result']
            
            # Format Caption ala Iqbal Ubot Premium
            caption = (
                f"<blockquote><b>🚨 ɪɴꜰᴏ ɢᴇᴍᴘᴀ ᴛᴇʀᴋɪɴɪ</b>\n\n"
                f"<b>ᚗ ᴡɪʟᴀʏᴀʜ :</b> <code>{hasil['Wilayah']}</code>\n"
                f"<b>ᚗ ᴍᴀɢɴɪᴛᴜᴅᴏ :</b> <code>{hasil['Magnitudo']}</code>\n"
                f"<b>ᚗ ᴋᴇᴅᴀʟᴀᴍᴀɴ :</b> <code>{hasil['Kedalaman']}</code>\n"
                f"<b>ᚗ ᴘᴏᴛᴇɴsɪ :</b> <code>{hasil['Potensi']}</code>\n"
                f"<b>ᚗ ᴋᴏᴏʀᴅɪɴᴀᴛ :</b> <code>{hasil['Lintang']}, {hasil['Bujur']}</code>\n"
                f"<b>ᚗ ᴡᴀᴋᴛᴜ :</b> <code>{hasil['tanggal']} | {hasil['jam']}</code>\n\n"
                f"<b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>"
            )
            
            # Download foto secara asinkron
            res_photo = await session.get(photo_url)
            photo_path = f"gempa_{message.id}.png"
            with open(photo_path, "wb") as f:
                f.write(res_photo.content)
            
            await client.send_photo(
                message.chat.id,
                photo=photo_path,
                caption=caption,
                reply_to_message_id=message.id
            )
            await status_msg.delete()
            
            if os.path.exists(photo_path):
                os.remove(photo_path)
                
    except Exception as e:
        await status_msg.edit(f"<blockquote><b>{ggl_emo} ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ:</b>\n<code>{str(e)}</code></blockquote>")
        