import os
import base64
import requests
from pyrogram import Client, filters
from PyroUbot import *

__MODULE__ = "ɢɪᴛʜᴜʙ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɢɪᴛʜᴜʙ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴜᴘɢʜ</code> [ᴇᴍᴀɪʟ] [ᴘᴀssᴡᴏʀᴅ]
ᚗ ʀᴇᴘʟʏ ꜰɪʟᴇ ʏᴀɴɢ ɪɴɢɪɴ ᴅɪᴜɴɢɢᴀʜ.

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴɢᴜɴɢɢᴀʜ ꜰɪʟᴇ ᴋᴇ ʀᴇᴘᴏsɪᴛᴏʀʏ ɢɪᴛʜᴜʙ ᴀɴᴅᴀ.</blockquote>
"""

GITHUB_API = "https://api.github.com"
user_sessions = {}  # ᴍᴇɴʏɪᴍᴘᴀɴ sᴇsɪ ᴜsᴇʀ sᴇᴍᴇɴᴛᴀʀᴀ

@PY.UBOT("upgh")
@PY.TOP_CMD
async def github_login(client, message):
    args = message.text.split(maxsplit=2)
    if len(args) < 3:
        return await message.reply_text("<blockquote><b>⚠️ ʜᴀʀᴀᴘ ᴍᴀsᴜᴋᴋᴀɴ ᴇᴍᴀɪʟ ᴅᴀɴ ᴘᴀssᴡᴏʀᴅ!\nᴄᴏɴᴛᴏʜ: <code>.ᴜᴘɢʜ</code> [ᴇᴍᴀɪʟ] [ᴘᴀssᴡᴏʀᴅ]</b></blockquote>")
    
    email = args[1]
    password = args[2]
    
    status_msg = await message.reply_text("<blockquote><b>🔄 sᴇᴅᴀɴɢ ᴍᴇɴᴄᴏʙᴀ ʟᴏɢɪɴ...</b></blockquote>")
    
    # ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ᴛᴏᴋᴇɴ ᴀᴋsᴇs ᴅᴇɴɢᴀɴ ʙᴀsɪᴄ ᴀᴜᴛʜ
    auth = base64.b64encode(f"{email}:{password}".encode()).decode()
    headers = {"Authorization": f"Basic {auth}"}
    
    try:
        user_response = requests.get(f"{GITHUB_API}/user", headers=headers)
        if user_response.status_code != 200:
            return await status_msg.edit("<blockquote><b>🚫 ʟᴏɢɪɴ ɢᴀɢᴀʟ. ᴘᴀsᴛɪᴋᴀɴ ᴇᴍᴀɪʟ ᴅᴀɴ ᴘᴀssᴡᴏʀᴅ ʙᴇɴᴀʀ.</b></blockquote>")
        
        user_data = user_response.json()
        username = user_data["login"]
        user_sessions[message.from_user.id] = {"email": email, "password": password, "username": username}
        
        await status_msg.edit(f"<blockquote><b>✅ ʟᴏɢɪɴ ʙᴇʀʜᴀsɪʟ!\n👤 ɢɪᴛʜᴜʙ ᴜsᴇʀ: <code>{username}</code>\n🔹 sɪʟᴀᴋᴀɴ ʀᴇᴘʟʏ ꜰɪʟᴇ ʏᴀɴɢ ɪɴɢɪɴ ᴅɪ-ᴜᴘʟᴏᴀᴅ.</b></blockquote>")
    except Exception as e:
        await status_msg.edit(f"<blockquote><b>⚠️ ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ:</b>\n<code>{str(e)}</code></blockquote>")

# ᴜsᴇ ᴄᴜsᴛᴏᴍ ʜᴀɴᴅʟᴇʀ ᴛᴏ ᴅᴇᴛᴇᴄᴛ ʀᴇᴘʟʏ ꜰɪʟᴇ
@PY.UBOT("ugh") # ᴘᴀᴋᴇ ᴄᴍᴅ ᴘᴇᴍɪɴᴄᴜ ʙɪᴀʀ ɢᴀᴋ ᴛᴀʙʀᴀᴋᴀɴ
@PY.TOP_CMD
async def upload_to_github(client, message):
    user_id = message.from_user.id
    if user_id not in user_sessions:
        return await message.reply_text("<blockquote><b>⚠️ ᴀɴᴅᴀ ʙᴇʟᴜᴍ ʟᴏɢɪɴ! ɢᴜɴᴀᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ <code>.ᴜᴘɢʜ</code> ᴛᴇʀʟᴇʙɪʜ ᴅᴀʜᴜʟᴜ.</b></blockquote>")
    
    if not message.reply_to_message or not message.reply_to_message.document:
        return await message.reply_text("<blockquote><b>❌ sɪʟᴀᴋᴀɴ ʀᴇᴘʟʏ ᴋᴇ ꜰɪʟᴇ ʏᴀɴɢ ɪɴɢɪɴ ᴅɪᴜɴɢɢᴀʜ ᴅᴇɴɢᴀɴ ᴘᴇʀɪɴᴛᴀʜ <code>.ᴜɢʜ</code></b></blockquote>")

    status_msg = await message.reply_text("<blockquote><b>🔄 sᴇᴅᴀɴɢ ᴍᴇɴɢᴜɴɢɢᴀʜ ꜰɪʟᴇ ᴋᴇ ɢɪᴛʜᴜʙ...</b></blockquote>")
    user_data = user_sessions[user_id]
    email, password, username = user_data["email"], user_data["password"], user_data["username"]

    file_path = await message.reply_to_message.download()
    file_name = os.path.basename(file_path)
    
    try:
        with open(file_path, "rb") as f:
            file_content = f.read()
        
        encoded_content = base64.b64encode(file_content).decode()
        repo_name = "ᴜsᴇʀʙᴏᴛᴜᴘʟᴏᴀᴅs"
        target_path = f"uploads/{file_name}"
        auth = base64.b64encode(f"{email}:{password}".encode()).decode()
        headers = {"Authorization": f"Basic {auth}"}
        
        # ᴄᴇᴋ ʀᴇᴘᴏ
        repo_check = requests.get(f"{GITHUB_API}/repos/{username}/{repo_name}", headers=headers)
        if repo_check.status_code == 404:
            requests.post(f"{GITHUB_API}/user/repos", json={"name": repo_name, "private": False}, headers=headers)
        
        # ᴜᴘʟᴏᴀᴅ
        upload_url = f"{GITHUB_API}/repos/{username}/{repo_name}/contents/{target_path}"
        upload_data = {"message": f"ᴜᴘʟᴏᴀᴅ {file_name}", "content": encoded_content}
        upload_response = requests.put(upload_url, json=upload_data, headers=headers)
        
        if upload_response.status_code in [201, 200]:
            file_url = upload_response.json()["content"]["html_url"]
            await status_msg.edit(f"<blockquote><b>✅ ꜰɪʟᴇ ʙᴇʀʜᴀsɪʟ ᴅɪᴜɴɢɢᴀʜ!\n\n🔗 ᴛᴀᴜᴛᴀɴ:</b> <a href='{file_url}'>ʟɪʜᴀᴛ ᴅɪ ɢɪᴛʜᴜʙ</a></blockquote>", disable_web_page_preview=True)
        else:
            await status_msg.edit("<blockquote><b>🚫 ɢᴀɢᴀʟ ᴍᴇɴɢᴜɴɢɢᴀʜ ꜰɪʟᴇ.</b></blockquote>")
            
    except Exception as e:
        await status_msg.edit(f"<blockquote><b>⚠️ ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ:</b>\n<code>{str(e)}</code></blockquote>")
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)
            