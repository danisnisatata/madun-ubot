import requests
from io import BytesIO
from pyrogram.enums import ChatAction
from PyroUbot import *

__MODULE__ = "ʀᴀɴᴅᴏᴍ ᴋᴜᴄɪɴɢ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʀᴀɴᴅᴏᴍ ᴋᴜᴄɪɴɢ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ʀᴀɴᴅᴏᴍ</code> ᴋᴜᴄɪɴɢ

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴɢɪʀɪᴍᴋᴀɴ ꜰᴏᴛᴏ ᴋᴜᴄɪɴɢ ᴀᴄᴀᴋ ʏᴀɴɢ ʟᴜᴄᴜ ᴅᴀɴ ᴍᴇɴɢɢᴇᴍᴀsᴋᴀɴ.</blockquote>
"""

URLS = {
    "kucing": "https://api.siputzx.my.id/api/r/cats"
}

@PY.UBOT("random")
@PY.TOP_CMD
async def random_cat_handler(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)
    
    args = get_arg(message)
    
    if not args or args.lower() not in URLS:
        return await message.reply_text(
            f"<blockquote><b>{ggl} ǫᴜᴇʀʏ ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ!</b>\nᚗ ɢᴜɴᴀᴋᴀɴ: <code>.ʀᴀɴᴅᴏᴍ ᴋᴜᴄɪɴɢ</code></blockquote>"
        )

    query = args.lower()
    status_msg = await message.reply_text(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇɴᴄᴀʀɪ ᴋᴜᴄɪɴɢ ᴄᴏᴍᴇʟ...</b></blockquote>")
    
    try:
        await client.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
        
        response = requests.get(URLS[query], timeout=15)
        response.raise_for_status()
        
        photo = BytesIO(response.content)
        photo.name = 'cat.jpg'
        
        await client.send_photo(
            message.chat.id, 
            photo, 
            caption=f"<blockquote><b>{brhsl} ʀᴀɴᴅᴏᴍ ᴋᴜᴄɪɴɢ ᴘʀᴇᴍɪᴜᴍ</b>\n<b>ᚗ sᴛᴀᴛᴜs :</b> ᴄᴏᴍᴇʟ ᴋɪɴɢᴢ\n<b>ᚗ ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>"
        )
        await status_msg.delete()
        
    except Exception as e:
        await status_msg.edit(f"<blockquote><b>{ggl} ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ:</b>\n<code>{str(e)}</code></blockquote>")
        