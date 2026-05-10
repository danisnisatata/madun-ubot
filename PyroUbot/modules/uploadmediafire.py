import os
import requests
from pyrogram import Client, filters
from PyroUbot import *

__MODULE__ = "ᴍᴇᴅɪᴀꜰɪʀᴇ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴍᴇᴅɪᴀꜰɪʀᴇ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴍᴇᴅɪᴀꜰɪʀᴇ</code> [ʀᴇᴘʟʏ ꜰɪʟᴇ ᴢɪᴘ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴɢᴜɴɢɢᴀʜ ꜰɪʟᴇ ᴢɪᴘ ᴋᴇ ᴀᴋᴜɴ ᴍᴇᴅɪᴀꜰɪʀᴇ ᴀɴᴅᴀ.</blockquote>
"""

# ɢᴀɴᴛɪ ᴅᴇɴɢᴀɴ ᴀᴘɪ ᴋᴇʏ & ᴇᴍᴀɪʟ ᴍᴇᴅɪᴀꜰɪʀᴇ (ᴊɪᴋᴀ ᴀᴅᴀ)
MEDIAFIRE_EMAIL = "zamsswangsaff@gmail.com"
MEDIAFIRE_PASSWORD = "Nizam20@"

@PY.UBOT("mediafire")
@PY.TOP_CMD
async def _(client, message):
    if not message.reply_to_message or not message.reply_to_message.document:
        return await message.reply_text("<blockquote><b>❌ sɪʟᴀᴋᴀɴ ʙᴀʟᴀs ᴋᴇ ꜰɪʟᴇ ᴢɪᴘ ᴜɴᴛᴜᴋ ᴅɪᴜɴɢɢᴀʜ!</b></blockquote>")

    status_msg = await message.reply_text("<blockquote><b>🔄 sᴇᴅᴀɴɢ ᴍᴇɴɢᴜɴɢɢᴀʜ ꜰɪʟᴇ ᴋᴇ ᴍᴇᴅɪᴀꜰɪʀᴇ...</b></blockquote>")

    # ᴀᴍʙɪʟ ɪɴꜰᴏʀᴍᴀsɪ ꜰɪʟᴇ
    file = message.reply_to_message.document
    file_path = await client.download_media(file)

    if not file_path.endswith(".zip"):
        if os.path.exists(file_path):
            os.remove(file_path)
        return await status_msg.edit("<blockquote><b>❌ ʜᴀɴʏᴀ ꜰɪʟᴇ ᴢɪᴘ ʏᴀɴɢ ʙɪsᴀ ᴅɪᴜɴɢɢᴀʜ!</b></blockquote>")

    try:
        # ʟᴏɢɪɴ ᴋᴇ ᴍᴇᴅɪᴀꜰɪʀᴇ
        login_url = "https://www.mediafire.com/api/1.5/user/get_session_token.php"
        login_params = {
            "email": MEDIAFIRE_EMAIL,
            "password": MEDIAFIRE_PASSWORD,
            "application_id": "42511",  # ɪᴅ ᴀᴘʟɪᴋᴀsɪ ᴍᴇᴅɪᴀꜰɪʀᴇ
            "response_format": "json"
        }
        login_response = requests.get(login_url, params=login_params).json()
        
        if login_response["response"]["result"] != "Success":
            return await status_msg.edit("<blockquote><b>❌ ɢᴀɢᴀʟ ʟᴏɢɪɴ ᴋᴇ ᴍᴇᴅɪᴀꜰɪʀᴇ!</b></blockquote>")

        session_token = login_response["response"]["session_token"]

        # ᴜᴘʟᴏᴀᴅ ꜰɪʟᴇ
        upload_url = "https://www.mediafire.com/api/1.5/upload/simple.php"
        upload_params = {
            "session_token": session_token,
            "response_format": "json"
        }
        
        with open(file_path, "rb") as f:
            files = {"file": f}
            upload_response = requests.post(upload_url, params=upload_params, files=files).json()
        
        if upload_response["response"]["result"] != "Success":
            return await status_msg.edit("<blockquote><b>❌ ɢᴀɢᴀʟ ᴍᴇɴɢᴜɴɢɢᴀʜ ꜰɪʟᴇ!</b></blockquote>")

        file_link = upload_response["response"]["doupload"]["links"]["normal_download"]
        
        result_text = (
            f"<blockquote><b>✅ ʙᴇʀʜᴀsɪʟ ᴅɪᴜɴɢɢᴀʜ!</b>\n\n"
            f"<b>🔗 ᴛᴀᴜᴛᴀɴ:</b> <a href='{file_link}'>ᴅᴏᴡɴʟᴏᴀᴅ ᴅɪ ᴍᴇᴅɪᴀꜰɪʀᴇ</a></blockquote>"
        )
        await status_msg.edit(result_text, disable_web_page_preview=True)
    
    except Exception as e:
        await status_msg.edit(f"<blockquote><b>⚠️ ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ:</b>\n<code>{str(e)}</code></blockquote>")

    finally:
        if os.path.exists(file_path):
            os.remove(file_path)  # ʜᴀᴘᴜs ꜰɪʟᴇ ʟᴏᴋᴀʟ sᴇᴛᴇʟᴀʜ ᴅɪᴜɴɢɢᴀʜ
            