from pyrogram import Client, filters
from pyrogram.types import Message
import requests
from PyroUbot import *

__MODULE__ = "ᴛɪᴋᴛᴏᴋ sᴇᴀʀᴄʜ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴛɪᴋᴛᴏᴋ sᴇᴀʀᴄʜ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴛᴛsᴇᴀʀᴄʜ</code> [ᴋᴀᴛᴀ ᴋᴜɴᴄɪ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴᴄᴀʀɪ ᴠɪᴅᴇᴏ ᴛɪᴋᴛᴏᴋ ʙᴇʀᴅᴀsᴀʀᴋᴀɴ ᴋᴀᴛᴀ ᴋᴜɴᴄɪ.</blockquote>
"""

# Masukkan API Key Anda di sini
NEO_KEY = "M0wHgI" 

@PY.UBOT("ttsearch")
@PY.TOP_CMD
async def tiktok_search(client, message):
    if len(message.command) < 2:
        return await message.reply_text("<blockquote><b>❌ ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ᴋᴀᴛᴀ ᴋᴜɴᴄɪ!\nᴄᴏɴᴛᴏʜ: <code>.ᴛᴛsᴇᴀʀᴄʜ</code> [ᴋᴜᴄɪɴɢ ʟᴜᴄᴜ]</b></blockquote>")

    query = " ".join(message.command[1:])
    status_msg = await message.reply_text("<blockquote><b>🔍 sᴇᴅᴀɴɢ ᴍᴇɴᴄᴀʀɪ ᴠɪᴅᴇᴏ ᴛɪᴋᴛᴏᴋ...</b></blockquote>")

    try:
        res = requests.get(
            "https://api.neoxr.my.id/api/tiktoksearch",
            params={"q": query, "apikey": NEO_KEY}
        )
        data = res.json()

        if res.status_code == 200 and data.get("status") and data.get("data"):
            video_data = data["data"][0]  # Ambil video pertama dari hasil
            video_url = video_data.get("url", "")
            desc = video_data.get("title", "ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴊᴜᴅᴜʟ")
            author = video_data.get("author", {}).get("nickname", "ᴜɴᴋɴᴏᴡɴ")

            result_text = (
                f"<blockquote><b>🎬 ʜᴀsɪʟ ᴘᴇɴᴄᴀʀɪᴀɴ ᴛɪᴋᴛᴏᴋ</b>\n\n"
                f"<b>• ᴘᴇɴᴄɪᴘᴛᴀ:</b> <code>{author}</code>\n"
                f"<b>• ᴅᴇsᴋʀɪᴘsɪ:</b> <i>{desc}</i>\n"
                f"<b>• ᴛᴀᴜᴛᴀɴ:</b> <a href='{video_url}'>ᴛᴏɴᴛᴏɴ ᴠɪᴅᴇᴏ</a></blockquote>"
            )
            await status_msg.edit(result_text, disable_web_page_preview=False)
        else:
            await status_msg.edit("<blockquote><b>❌ ᴠɪᴅᴇᴏ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ ᴀᴛᴀᴜ ᴀᴘɪ ʟɪᴍɪᴛ.</b></blockquote>")
    except Exception as e:
        await status_msg.edit(f"<blockquote><b>⚠️ ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ:</b>\n<code>{str(e)}</code></blockquote>")
        