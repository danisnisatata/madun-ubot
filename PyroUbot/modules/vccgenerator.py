import requests
from pyrogram import Client, filters
from PyroUbot import *

__MODULE__ = "ᴠᴄᴄ ɢᴇɴᴇʀᴀᴛᴏʀ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴠᴄᴄ ɢᴇɴᴇʀᴀᴛᴏʀ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴠᴄᴄ</code>

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴɢɢᴇɴᴇʀᴀᴛᴇ ᴅᴀᴛᴀ ꜰᴀᴋᴇ ᴠᴄᴄ (ᴍᴀsᴛᴇʀᴄᴀʀᴅ) ᴜɴᴛᴜᴋ ᴋᴇᴘᴇʀʟᴜᴀɴ ᴛᴇsᴛɪɴɢ.</blockquote>
"""

@PY.UBOT("vcc")
@PY.TOP_CMD
async def generate_vcc(client, message):
    status_msg = await message.reply_text("<blockquote><b>🔄 ɢᴇɴᴇʀᴀᴛɪɴɢ ᴠᴄᴄ, ᴍᴏʜᴏɴ ᴛᴜɴɢɢᴜ...</b></blockquote>")
    API_URL = "https://api.siputzx.my.id/api/tools/vcc-generator"
    params = {
        "type": "MasterCard",
        "count": 5
    }
    
    try:
        response = requests.get(API_URL, params=params)
        data = response.json()
        
        if data.get("status"):
            vcc_list = data.get("data", [])
            result = "<blockquote><b>💳 ʜᴀsɪʟ ɢᴇɴᴇʀᴀᴛᴇ ᴠᴄᴄ</b></blockquote>\n\n"
            
            for vcc in vcc_list:
                result += (
                    f"<blockquote>"
                    f"<b>• ɴᴏᴍᴏʀ ᴋᴀʀᴛᴜ:</b> <code>{vcc['cardNumber']}</code>\n"
                    f"<b>• ᴇxᴘ ᴅᴀᴛᴇ:</b> <code>{vcc['expirationDate']}</code>\n"
                    f"<b>• ʜᴏʟᴅᴇʀ:</b> <code>{vcc['cardholderName']}</code>\n"
                    f"<b>• ᴄᴠᴠ:</b> <code>{vcc['cvv']}</code>"
                    f"</blockquote>\n"
                )
            
            await status_msg.edit(result)
        else:
            await status_msg.edit("<blockquote><b>❌ ɢᴀɢᴀʟ ᴍᴇɴɢᴀᴍʙɪʟ ᴅᴀᴛᴀ ᴠᴄᴄ.</b></blockquote>")
    
    except Exception as e:
        await status_msg.edit(f"<blockquote><b>⚠️ ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ:</b>\n<code>{str(e)}</code></blockquote>")
        