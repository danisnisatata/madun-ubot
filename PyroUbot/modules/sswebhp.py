import os
import requests
from PyroUbot import *

__MODULE__ = "ss ᴡᴇʙ ʜᴘ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ss ᴡᴇʙ ʜᴘ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ssʜᴘ</code> [ʟɪɴᴋ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴɢᴀᴍʙɪʟ sᴄʀᴇᴇɴsʜᴏᴛ ᴡᴇʙsɪᴛᴇ ᴅᴇɴɢᴀɴ ᴛᴀᴍᴘɪʟᴀɴ ᴍᴏʙɪʟᴇ/ʜᴘ.</blockquote>
"""

def get_ssweb_image(url):
    api_url = "https://api.botcahx.eu.org/api/tools/sshp"
    params = {
        "url": url,
        "device": "desktop",
        "apikey": "@iqbalnew77"
    }
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        if response.headers.get("Content-Type", "").startswith("image/"):
            return response.content
        return None
    except Exception:
        return None

@PY.UBOT("sshp")
@PY.TOP_CMD
async def screenshot_handler(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)
    
    args = get_arg(message)
    if not args:
        return await message.reply_text(f"<blockquote><b>{ggl} ᴍᴀɴᴀ ᴜʀʟ ɴʏᴀ ʙᴏs!</b></blockquote>")

    url = args.strip()
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    status_msg = await message.reply_text(f"<blockquote><b>{prs} ᴘʀᴏsᴇs sᴄʀᴇᴇɴsʜᴏᴛ ʜᴘ ᴋɪɴɢᴢ...</b></blockquote>")

    image_data = get_ssweb_image(url)
    if not image_data:
        return await status_msg.edit(f"<blockquote><b>{ggl} ɢᴀɢᴀʟ ᴍᴇɴɢᴀᴍʙɪʟ sᴄʀᴇᴇɴsʜᴏᴛ.</b></blockquote>")

    filepath = "ss_hp.jpg"
    with open(filepath, "wb") as file:
        file.write(image_data)

    await client.send_photo(
        message.chat.id, 
        photo=filepath, 
        caption=f"<blockquote><b>{brhsl} ss ᴡᴇʙ ʜᴘ sᴇʟᴇsᴀɪ</b>\nᚗ ᴛᴀᴜᴛᴀɴ : <code>{url}</code></blockquote>",
        reply_to_message_id=message.id
    )
    
    await status_msg.delete()
    if os.path.exists(filepath):
        os.remove(filepath)
        