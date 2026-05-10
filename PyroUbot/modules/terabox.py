import requests
from pyrogram import Client, filters
from PyroUbot import *

__MODULE__ = "ᴛᴇʀᴀʙᴏx"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴛᴇʀᴀʙᴏx ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴛᴇʀᴀʙᴏx</code> [ʟɪɴᴋ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴɢᴀᴍʙɪʟ ᴛᴀᴜᴛᴀɴ ᴜɴᴅᴜʜᴀɴ ᴠɪᴅᴇᴏ ᴀᴛᴀᴜ ꜰɪʟᴇ ᴅᴀʀɪ ᴛᴇʀᴀʙᴏx.</blockquote>
"""

@PY.UBOT("terabox")
@PY.TOP_CMD
async def terabox_handler(client, message):
    if len(message.command) < 2:
        return await message.reply_text("<blockquote><b>❌ ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ᴛᴀᴜᴛᴀɴ!\nᴄᴏɴᴛᴏʜ : <code>.ᴛᴇʀᴀʙᴏx</code> [ʟɪɴᴋ_ᴛᴇʀᴀʙᴏx]</b></blockquote>")
    
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    
    status_msg = await message.reply_text(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇɴɢᴀᴍʙɪʟ ᴅᴀᴛᴀ ᴛᴇʀᴀʙᴏx...</b></blockquote>")
    
    url = message.command[1]
    api_url = f"https://api.botcahx.eu.org/api/download/terabox?url={url}&apikey=@iqbalnew77"
    
    try:
        response = requests.get(api_url)
        if response.status_code != 200:
            return await status_msg.edit(f"<blockquote><b>{ggl} ɢᴀɢᴀʟ ᴍᴇɴɢᴀᴍʙɪʟ ᴅᴀᴛᴀ ᴅᴀʀɪ ᴀᴘɪ.</b></blockquote>")
        
        data = response.json()
        if not data.get("status"):
            return await status_msg.edit(f"<blockquote><b>{ggl} ᴀᴘɪ ᴍᴇɴᴏʟᴀᴋ ᴘᴇʀᴍɪɴᴛᴀᴀɴ, ᴘᴀsᴛɪᴋᴀɴ ʟɪɴᴋ ᴠᴀʟɪᴅ.</b></blockquote>")
        
        result_text = f"<blockquote><b>{brhsl} ᴅᴀꜰᴛᴀʀ ꜰɪʟᴇ ᴛᴇʀᴀʙᴏx:</b>\n\n"
        for item in data.get("result", []):
            name = item.get("name", "ᴜɴᴋɴᴏᴡɴ")
            files = item.get("files", [])
            
            result_text += f"<b>📁 ꜰᴏʟᴅᴇʀ:</b> <code>{name}</code>\n"
            for file in files:
                filename = file.get("filename", "ᴜɴᴋɴᴏᴡɴ")
                size = file.get("size", "0")
                dl_url = file.get("url", "#")
                result_text += (
                    f"  <b>├ 🎬 ꜰɪʟᴇ:</b> <code>{filename}</code>\n"
                    f"  <b>├ ⚖️ ᴜᴋᴜʀᴀɴ:</b> <code>{size}</code>\n"
                    f"  <b>└ 🔗 ᴛᴀᴜᴛᴀɴ:</b> <a href='{dl_url}'>ᴋʟɪᴋ ᴅɪ sɪɴɪ</a>\n\n"
                )
        result_text += "</blockquote>"
        
        await status_msg.edit(result_text, disable_web_page_preview=True)
        
    except Exception as e:
        await status_msg.edit(f"<blockquote><b>⚠️ ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ:</b>\n<code>{str(e)}</code></blockquote>")
        