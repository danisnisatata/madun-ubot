from pyrogram import Client, filters
import requests
from PyroUbot import *

__MODULE__ = "ᴛɪᴋᴛᴏᴋ sᴇᴀʀᴄʜ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴛɪᴋᴛᴏᴋ sᴇᴀʀᴄʜ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴛᴛsᴇᴀʀᴄʜ</code> [ǫᴜᴇʀʏ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴᴄᴀʀɪ ᴠɪᴅᴇᴏ ᴛɪᴋᴛᴏᴋ ʙᴇʀᴅᴀsᴀʀᴋᴀɴ ᴋᴀᴛᴀ ᴋᴜɴᴄɪ ʏᴀɴɢ ᴅɪɪɴɢɪɴᴋᴀɴ.</blockquote>
"""

API_KEY = "@iqbalnew77"

@PY.UBOT("tiktoksearch|tts|ttsearch")
@PY.TOP_CMD
async def tiktok_search(client, message):
    if len(message.command) < 2:
        return await message.reply("<blockquote><b>❌ ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ᴋᴀᴛᴀ ᴋᴜɴᴄɪ!\nᴄᴏɴᴛᴏʜ: <code>.ᴛᴛsᴇᴀʀᴄʜ</code> [ᴄᴇᴡᴇᴋ ᴄᴀɴᴛɪᴋ]</b></blockquote>")

    query = " ".join(message.command[1:])
    status_msg = await message.reply("<blockquote><b>🔍 sᴇᴅᴀɴɢ ᴍᴇɴᴄᴀʀɪ ᴠɪᴅᴇᴏ ᴛɪᴋᴛᴏᴋ...</b></blockquote>")

    url = f"https://api.botcahx.eu.org/api/search/tiktoks?query={query}&apikey={API_KEY}"
    
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return await status_msg.edit("<blockquote><b>❌ ɢᴀɢᴀʟ ᴍᴇɴɢᴀᴍʙɪʟ ᴅᴀᴛᴀ ᴅᴀʀɪ ᴀᴘɪ.</b></blockquote>")

        data = response.json()
        if not data.get("status") or not data.get("result", {}).get("data"):
            return await status_msg.edit("<blockquote><b>❌ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ ᴠɪᴅᴇᴏ ᴜɴᴛᴜᴋ ǫᴜᴇʀʏ ᴛᴇʀsᴇʙᴜᴛ.</b></blockquote>")

        video = data["result"]["data"][0]
        caption = (
            f"<blockquote><b>🎬 ʜᴀsɪʟ ᴘᴇɴᴄᴀʀɪᴀɴ ᴛɪᴋᴛᴏᴋ</b>\n\n"
            f"<b>• ᴊᴜᴅᴜʟ:</b> <code>{video['title']}</code>\n"
            f"<b>• ᴡɪʟᴀʏᴀʜ:</b> <code>{video['region']}</code>\n"
            f"<b>• ᴍᴜsɪᴋ:</b> <code>{video['music_info']['title']}</code>\n"
            f"<b>• ᴘᴇɴᴏɴᴛᴏɴ:</b> <code>{video['play_count']}</code>\n"
            f"<b>• sᴜᴋᴀ:</b> <code>{video['digg_count']}</code>\n"
            f"<b>• ᴋᴏᴍᴇɴᴛᴀʀ:</b> <code>{video['comment_count']}</code>\n\n"
            f"<b>🔗 <a href='{video['play']}'>ᴛᴏɴᴛᴏɴ ᴅɪ ᴛɪᴋᴛᴏᴋ</a></b></blockquote>"
        )

        await status_msg.edit("<blockquote><b>📥 sᴇᴅᴀɴɢ ᴍᴇɴɢɪʀɪᴍ ᴠɪᴅᴇᴏ...</b></blockquote>")
        await message.reply_video(video["play"], caption=caption)
        await status_msg.delete()

    except Exception as e:
        await status_msg.edit(f"<blockquote><b>⚠️ ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ:</b>\n<code>{str(e)}</code></blockquote>")
        