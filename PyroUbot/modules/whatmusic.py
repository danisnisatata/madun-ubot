import aiohttp
import filetype
import os
import requests
from pyrogram import Client, filters
from pyrogram.types import Message
from PyroUbot import *

__MODULE__ = "ᴡʜᴀᴛ ᴍᴜsɪᴄ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴡʜᴀᴛ ᴍᴜsɪᴄ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴡʜᴀᴛᴍᴜsɪᴄ</code> [ʀᴇᴘʟʏ ᴠɪᴅᴇᴏ/ᴍᴜsɪᴄ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴᴅᴇᴛᴇᴋsɪ ᴊᴜᴅᴜʟ ʟᴀɢᴜ ᴅᴀɴ ᴘᴇɴʏᴀɴʏɪ ᴅᴀʀɪ ᴍᴇᴅɪᴀ ᴍᴇʟᴀʟᴜɪ sᴜᴀʀᴀ.</blockquote>
"""

async def upload_media(m: Message):
    media = await m.reply_to_message.download()
    try:
        ext = "unknown"
        if os.path.exists(media):
            kind = filetype.guess(media)
            if kind:
                ext = kind.extension
        
        form_data = aiohttp.FormData()
        form_data.add_field("fileToUpload", open(media, "rb"), filename=f"file.{ext}")
        form_data.add_field("reqtype", "fileupload")
        
        async with aiohttp.ClientSession() as session:
            async with session.post("https://ibb.co.com/user/api.php", data=form_data) as res:
                if res.status == 200:
                    response_text = await res.text()
                    return response_text.strip()
                else:
                    return None
    except Exception as e:
        print(f"ᴇʀʀᴏʀ sᴀᴀᴛ ᴍᴇɴɢᴜɴɢɢᴀʜ ᴍᴇᴅɪᴀ: {e}")
        return None
    finally:
        if os.path.exists(media):
            os.remove(media)

@PY.UBOT("whatmusic")
async def whatmusic_handler(client, message: Message):
    # Proteksi: Cek apakah reply ke media yang valid
    if not message.reply_to_message or not (message.reply_to_message.video or message.reply_to_message.audio or message.reply_to_message.voice):
        return await message.reply("<blockquote><b>❌ ᴍᴏʜᴏɴ ʙᴀʟᴀs ᴋᴇ ᴠɪᴅᴇᴏ, ᴀᴜᴅɪᴏ, ᴀᴛᴀᴜ ᴘᴇsᴀɴ sᴜᴀʀᴀ!</b></blockquote>")
    
    msg = await message.reply("<blockquote><b>🔄 ᴍᴇɴɢᴜɴɢɢᴀʜ ᴍᴇᴅɪᴀ ᴋᴇ sᴇʀᴠᴇʀ...</b></blockquote>")
    video_url = await upload_media(message)

    if not video_url:
        return await msg.edit("<blockquote><b>❌ ɢᴀɢᴀʟ ᴍᴇɴɢᴜɴɢɢᴀʜ ᴍᴇᴅɪᴀ. sɪʟᴀᴋᴀɴ ᴄᴏʙᴀ ʟᴀɢɪ.</b></blockquote>")
    
    await msg.edit("<blockquote><b>🎵 sᴇᴅᴀɴɢ ᴍᴇɴɢᴀɴᴀʟɪsɪs ᴍᴜsɪᴋ...</b></blockquote>")
    
    # Request ke API
    try:
        response = requests.get(f"https://api.botcax.eu.org/api/tools/whatmusic?url={video_url}&apikey=@iqbalnew77")
        if response.status_code == 200:
            data = response.json()
            if data.get("status"):
                result = data.get("result", "").strip()
                if not result or "undefined" in result.lower():
                    return await msg.edit("<blockquote><b>❌ ᴍᴜsɪᴋ ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴅɪᴋᴇɴᴀʟɪ.</b></blockquote>")
                
                return await msg.edit(
                    f"<blockquote><b>🎶 ʜᴀsɪʟ ᴘᴇɴɢᴇɴᴀʟᴀɴ ᴍᴜsɪᴋ</b>\n\n"
                    f"<code>{result}</code></blockquote>"
                )
            else:
                return await msg.edit("<blockquote><b>❌ ᴍᴜsɪᴋ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ.</b></blockquote>")
        else:
            return await msg.edit(f"<blockquote><b>❌ ᴀᴘɪ ᴇʀʀᴏʀ (sᴛᴀᴛᴜs: {response.status_code})</b></blockquote>")
            
    except Exception as e:
        return await msg.edit(f"<blockquote><b>⚠️ ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ:</b>\n<code>{str(e)}</code></blockquote>")
        
