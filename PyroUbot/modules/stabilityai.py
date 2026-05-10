import os
import requests
from PyroUbot import *

# API Key Konfigurasi
API_KEY = "@iqbalnew77"

__MODULE__ = "sᴛᴀʙɪʟɪᴛʏ ᴀɪ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴛᴀʙɪʟɪᴛʏ ᴀɪ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}sᴛᴀʙɪʟɪᴛʏᴀɪ</code> [ᴛᴇᴋs]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇᴍʙᴜᴀᴛ ɢᴀᴍʙᴀʀ ᴀɪ ʙᴇʀᴋᴜᴀʟɪᴛᴀs ᴛɪɴɢɢɪ ᴅᴇɴɢᴀɴ ᴍᴇsɪɴ sᴛᴀʙɪʟɪᴛʏ ᴀɪ.</blockquote>
"""

def fetch_image(api_url, text):
    params = {"prompt": text, "apikey": API_KEY}
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        if response.headers.get("Content-Type", "").startswith("image/"):
            return response.content
        return None
    except Exception:
        return None

@PY.UBOT("stabilityai")
@PY.TOP_CMD
async def stability_cmd(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)
    
    args = get_arg(message)
    if not args:
        return await message.reply_text(f"<blockquote><b>{ggl} ʜᴀʀᴀᴘ ᴍᴀsᴜᴋᴋᴀɴ ᴘʀᴏᴍᴘᴛ!\nᴄᴏɴᴛᴏʜ: <code>.sᴛᴀʙɪʟɪᴛʏᴀɪ</code> ᴄʏʙᴇʀᴘᴜɴᴋ ᴄɪᴛʏ</b></blockquote>")

    status_msg = await message.reply_text(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇɴɢʜᴀsɪʟᴋᴀɴ ɪᴍᴀᴊɪɴᴀsɪ...</b></blockquote>")
    
    api_url = "https://api.siputzx.my.id/api/ai/stabilityai"
    image_content = fetch_image(api_url, args)
    
    if image_content:
        temp_file = "stability.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)
            
        await client.send_photo(
            message.chat.id,
            photo=temp_file,
            caption=f"<blockquote><b>{brhsl} sᴛᴀʙɪʟɪᴛʏ ᴀɪ ʙᴇʀʜᴀsɪʟ</b>\nᚗ ᴘʀᴏᴍᴘᴛ : <code>{args}</code></blockquote>",
            reply_to_message_id=message.id
        )
        
        await status_msg.delete()
        if os.path.exists(temp_file):
            os.remove(temp_file)
    else:
        await status_msg.edit(f"<blockquote><b>{ggl} ɢᴀɢᴀʟ ᴍᴇɴɢʜᴀsɪʟᴋᴀɴ ɢᴀᴍʙᴀʀ. ᴄᴏʙᴀ ʟᴀɢɪ ɴᴀɴᴛɪ.</b></blockquote>")
        