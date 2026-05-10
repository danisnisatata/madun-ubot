import asyncio
import os
import requests
from PyroUbot import *

__MODULE__ = "ʀᴇᴍɪɴɪ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʀᴇᴍɪɴɪ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ʜᴅ</code> [ʙᴀʟᴀs ꜰᴏᴛᴏ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴɢᴜʙᴀʜ ꜰᴏᴛᴏ ʙᴜʀᴀᴍ ᴍᴇɴᴊᴀᴅɪ ᴋᴜᴀʟɪᴛᴀs ʜɪɢʜ ᴅᴇꜰɪɴɪᴛɪᴏɴ (ʜᴅ).</blockquote>
"""

def remini_engine(image_path, model_type="enhance"):
    url = f"https://inferenceengine.vyro.ai/{model_type}"
    with open(image_path, "rb") as img_file:
        files = {
            "model_version": (None, "1"),
            "image": ("enhance_image_body.jpg", img_file, "image/jpeg"),
        }
        headers = {
            "User-Agent": "okhttp/4.9.3",
            "Connection": "Keep-Alive",
        }
        response = requests.post(url, files=files, headers=headers, timeout=60)

    if response.status_code == 200:
        return response.content
    else:
        return None

@PY.UBOT("remini|hd")
@PY.TOP_CMD
async def remini_handler(client, message):
    prs_emo = await EMO.PROSES(client)
    brhsl_emo = await EMO.BERHASIL(client)
    ggl_emo = await EMO.GAGAL(client)
    
    ureply = message.reply_to_message
    if not ureply or not ureply.photo:
        return await message.reply_text(f"<blockquote><b>{ggl_emo} ᴍᴏʜᴏɴ ʙᴀʟᴀs ᴋᴇ ꜰᴏᴛᴏ ʏᴀɴɢ ɪɴɢɪɴ ᴅɪᴘᴇʀᴊᴇʟᴀs!</b></blockquote>")

    status_msg = await message.reply_text(f"<blockquote><b>{prs_emo} sᴇᴅᴀɴɢ ᴍᴇɴɪɴɢᴋᴀᴛᴋᴀɴ ᴋᴜᴀʟɪᴛᴀs ꜰᴏᴛᴏ...</b></blockquote>")

    try:
        # Download foto ke lokal
        file_path = await client.download_media(ureply)
        
        # Proses engine di executor biar gak blocking
        loop = asyncio.get_event_loop()
        enhanced_data = await loop.run_in_executor(None, remini_engine, file_path)

        if enhanced_data:
            output_path = "remini_result.jpg"
            with open(output_path, "wb") as f:
                f.write(enhanced_data)

            await client.send_photo(
                message.chat.id,
                photo=output_path,
                caption=f"<blockquote><b>{brhsl_emo} ᴘʀᴏsᴇs ʜᴅ sᴇʟᴇsᴀɪ!</b>\n\n<b>ᚗ ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>",
                reply_to_message_id=message.id,
            )
            await status_msg.delete()
            if os.path.exists(output_path): os.remove(output_path)
        else:
            await status_msg.edit(f"<blockquote><b>{ggl_emo} ɢᴀɢᴀʟ ᴍᴇɴɢʜᴜʙᴜɴɢɪ sᴇʀᴠᴇʀ ʀᴇᴍɪɴɪ!</b></blockquote>")

        if os.path.exists(file_path): os.remove(file_path)
            
    except Exception as e:
        await status_msg.edit(f"<blockquote><b>{ggl_emo} ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ:</b>\n<code>{str(e)}</code></blockquote>")
        