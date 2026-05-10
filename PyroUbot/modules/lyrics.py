import os
import requests
import asyncio
from PyroUbot import *

__MODULE__ = "ʟʏʀɪᴄs"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʟʏʀɪᴄs ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ʟʏʀɪᴄs</code> [ᴊᴜᴅᴜʟ ʟᴀɢᴜ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴᴄᴀʀɪ ʟɪʀɪᴋ ʟᴀɢᴜ sᴇᴄᴀʀᴀ ᴏᴛᴏᴍᴀᴛɪs ᴠɪᴀ ᴀᴘɪ.</blockquote>
"""

@PY.UBOT("lyrics")
async def lyrics_handler(client, message):
    prs_emo = await EMO.PROSES(client)
    brhsl_emo = await EMO.BERHASIL(client)
    ggl_emo = await EMO.GAGAL(client)
    
    args = get_arg(message)
    if not args:
        return await message.reply_text(
            f"<blockquote><b>{ggl_emo} ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ᴊᴜᴅᴜʟ ʟᴀɢᴜ!</b>\nᚗ ᴄᴏɴᴛᴏʜ: <code>.ʟʏʀɪᴄs sᴇᴘɪɴɢɢᴀʟ ᴋᴇɴᴀɴɢᴀɴ</code></blockquote>"
        )

    status_msg = await message.reply_text(f"<blockquote><b>{prs_emo} sᴇᴅᴀɴɢ ᴍᴇɴᴄᴀʀɪ ʟɪʀɪᴋ...</b></blockquote>")
    
    # Masukkan args ke dalam query API
    api_url = f"https://api.betabotz.eu.org/api/search/lirik?lirik={args}&apikey=@iqbalnew77"

    def fetch_lyrics():
        try:
            return requests.get(api_url, timeout=10).json()
        except:
            return None

    loop = asyncio.get_event_loop()
    data = await loop.run_in_executor(None, fetch_lyrics)

    if data and data.get("status") and "result" in data:
        hasil = data['result']
        lirik_text = hasil.get('lyrics', 'ʟɪʀɪᴋ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ.')
        judul = hasil.get('title', args.upper())
        
        # Gambar default bertema musik
        photo_url = "https://cdn.vectorstock.com/i/1000v/71/92/music-lyrics-logo-mark-for-concert-vector-35117192.jpg"
        
        caption = f"""
<blockquote><b>{brhsl_emo} ʟʏʀɪᴄs : {judul}</b>

{lirik_text}

<b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>
"""
        try:
            # Kirim foto dengan lirik di caption (jika lirik tidak terlalu panjang)
            # Jika lirik sangat panjang (>1024 char), kirim sebagai teks biasa agar tidak error
            if len(caption) > 1024:
                await status_msg.edit(caption)
            else:
                await client.send_photo(message.chat.id, photo=photo_url, caption=caption)
                await status_msg.delete()
        except Exception as e:
            await status_msg.edit(f"<blockquote><b>{ggl_emo} ᴇʀʀᴏʀ:</b> <code>{str(e)}</code></blockquote>")
    else:
        await status_msg.edit(f"<blockquote><b>{ggl_emo} ʟɪʀɪᴋ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ ᴀᴛᴀᴜ ᴀᴘɪ ᴇʀʀᴏʀ.</b></blockquote>")
        