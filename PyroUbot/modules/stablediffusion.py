import os
import requests
from PyroUbot import *

__MODULE__ = "sᴛᴀʙʟᴇᴅɪғғᴜsɪᴏɴ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴛᴀʙʟᴇᴅɪғғᴜsɪᴏɴ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}sᴅ</code> [ᴛᴇᴋs]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇᴍʙᴜᴀᴛ ɢᴀᴍʙᴀʀ ᴀɪ ʙᴇʀᴅᴀsᴀʀᴋᴀɴ ᴅᴇsᴋʀɪᴘsɪ ᴛᴇᴋs ʟᴜ.</blockquote>
"""

# API Key Botcahx
API_KEY = "@iqbalnew77"

def get_stable_diffusion_image(text):
    url = "https://api.botcahx.eu.org/api/search/stablediffusion"
    params = {
        "text": text,
        "apikey": API_KEY
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        # Cek apakah responnya benar-benar gambar
        if response.headers.get("Content-Type", "").startswith("image/"):
            return response.content
        else:
            return None
    except requests.exceptions.RequestException:
        return None
                                                       
@PY.UBOT("sd")
@PY.TOP_CMD
async def stable_diffusion_cmd(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)
    
    args = get_arg(message)
    if not args:
        return await message.reply_text(f"<blockquote><b>{ggl} ʜᴀʀᴀᴘ ᴍᴀsᴜᴋᴋᴀɴ ᴘʀᴏᴍᴘᴛ ᴛᴇᴋs!\nᴄᴏɴᴛᴏʜ: <code>.sᴅ</code> ᴄᴀᴛ ᴏɴ ᴛʜᴇ ᴍᴏᴏɴ</b></blockquote>")

    request_text = args
    status_msg = await message.reply_text(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇᴍɢʜᴀsɪʟᴋᴀɴ ɢᴀᴍʙᴀʀ ᴀɪ...</b></blockquote>")

    image_content = get_stable_diffusion_image(request_text)
    
    if image_content:
        temp_file = "sd_img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await client.send_photo(
            message.chat.id,
            photo=temp_file,
            caption=f"<blockquote><b>{brhsl} ɢᴀᴍʙᴀʀ ᴀɪ ʙᴇʀʜᴀsɪʟ ᴅɪʙᴜᴀᴛ</b>\nᚗ ᴘʀᴏᴍᴘᴛ : <code>{request_text}</code></blockquote>",
            reply_to_message_id=message.id
        )
        
        await status_msg.delete()
        if os.path.exists(temp_file):
            os.remove(temp_file)
    else:
        await status_msg.edit(f"<blockquote><b>{ggl} ɢᴀɢᴀʟ ᴍᴇɴɢʜᴀsɪʟᴋᴀɴ ɢᴀᴍʙᴀʀ. ᴄᴏʙᴀ ʟᴀɢɪ ɴᴀɴᴛɪ.</b></blockquote>")
        