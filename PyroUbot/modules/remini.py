import requests
import os
from PyroUbot import *

__MODULE__ = "ʀᴇᴍɪɴɪ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʀᴇᴍɪɴɪ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ʀᴇᴍɪɴɪ</code> [ʀᴇᴘʟʏ ꜰᴏᴛᴏ]
ᚗ <code>{0}ʜᴅ</code> [ʀᴇᴘʟʏ ꜰᴏᴛᴏ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴᴊᴇʀɴɪʜᴋᴀɴ ɢᴀᴍʙᴀʀ ʏᴀɴɢ ʙᴜʀᴀᴍ ᴍᴇɴᴊᴀᴅɪ ᴋᴜᴀʟɪᴛᴀs ʜᴅ (ꜰᴜʟʟ ᴘʀᴇᴍɪᴜᴍ).</blockquote>
"""

@PY.UBOT("remini|hd")
@PY.TOP_CMD
async def remini_handler(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)

    # Validasi: Harus reply ke foto
    if not message.reply_to_message or not message.reply_to_message.photo:
        return await message.reply_text(f"<blockquote><b>{ggl} ᴍᴏʜᴏɴ ʙᴀʟᴀs ᴋᴇ ꜰᴏᴛᴏ ʏᴀɴɢ ɪɴɢɪɴ ᴅɪᴊᴇʀɴɪʜᴋᴀɴ!</b></blockquote>")

    status_msg = await message.reply_text(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ᴍᴇɴᴊᴀᴅɪ ʜᴅ...</b></blockquote>")

    file_path = None
    try:
        # Download foto ke VPS
        file_path = await message.reply_to_message.download()
        
        api_key = "@iqbalnew77"
        api_url = f"https://api.botcahx.eu.org/api/maker/remini?apikey={api_key}"
        
        # Upload ke API
        with open(file_path, "rb") as img_file:
            files = {"file": img_file}
            response = requests.post(api_url, files=files)

        if response.status_code == 200:
            res_data = response.json()
            
            if res_data.get("status") is True:
                image_hd_url = res_data.get("result")
                
                await client.send_photo(
                    chat_id=message.chat.id,
                    photo=image_hd_url,
                    caption=f"<blockquote><b>{brhsl} ɢᴀᴍʙᴀʀ ʙᴇʀʜᴀsɪʟ ᴅɪᴊᴇʀɴɪʜᴋᴀɴ</b>\n\n<b>⌭ sᴛᴀᴛᴜs :</b> ꜰᴜʟʟ ʜᴅ ᴘʀᴇᴍɪᴜᴍ\n<b>ᚗ ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>",
                    reply_to_message_id=message.id
                )
                await status_msg.delete()
            else:
                await status_msg.edit(f"<blockquote><b>{ggl} ɢᴀɢᴀʟ ᴍᴇᴍᴘʀᴏsᴇs, ᴍᴜɴɢᴋɪɴ ʟɪᴍɪᴛ API ʜᴀʙɪs.</b></blockquote>")
        else:
            await status_msg.edit(f"<blockquote><b>{ggl} sᴇʀᴠᴇʀ API ᴇʀʀᴏʀ:</b> <code>{response.status_code}</code></blockquote>")

    except Exception as e:
        await status_msg.edit(f"<blockquote><b>{ggl} ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ:</b>\n<code>{str(e)}</code></blockquote>")
    
    finally:
        # Bersihkan file sampah di VPS
        if file_path and os.path.exists(file_path):
            os.remove(file_path)
            