import requests
import asyncio
from pyrogram import Client, filters
from PyroUbot import *

__MODULE__ = "ᴛᴡɪᴛᴛᴇʀ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴛᴡɪᴛᴛᴇʀ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴛᴡɪᴛ</code> [ʟɪɴᴋ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ ᴅᴀʀɪ x/ᴛᴡɪᴛᴛᴇʀ ᴍᴇʟᴀʟᴜɪ ᴛᴀᴜᴛᴀɴ.</blockquote>
"""

async def get_twitter_video(url):
    api_url = f"https://api.botcahx.eu.org/api/dowloader/twitter?url={url}&apikey=@iqbalnew77"
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            if data.get("status") and "result" in data:
                video_urls = data["result"].get("url", [])
                if video_urls:
                    # Ambil kualitas HD jika ada, jika tidak ambil yang pertama
                    hd_url = video_urls[0].get("hd")
                    sd_url = video_urls[0].get("sd")
                    return hd_url or sd_url
    except Exception:
        return None
    return None

@PY.UBOT("twit")
@PY.TOP_CMD
async def twitter_download(client, message):
    if len(message.command) < 2:
        return await message.reply_text("<blockquote><b>❌ ɢᴜɴᴀᴋᴀɴ ꜰᴏʀᴍᴀᴛ: <code>.ᴛᴡɪᴛ</code> [ʟɪɴᴋ_ᴛᴡɪᴛᴛᴇʀ]</b></blockquote>")

    twitter_url = message.command[1]
    status_msg = await message.reply_text("<blockquote><b>🔄 sᴇᴅᴀɴɢ ᴍᴇɴɢᴀᴍʙɪʟ ᴠɪᴅᴇᴏ, ᴍᴏʜᴏɴ ᴛᴜɴɢɢᴜ...</b></blockquote>")

    video_url = await get_twitter_video(twitter_url)

    if video_url:
        await status_msg.edit("<blockquote><b>📥 sᴇᴅᴀɴɢ ᴍᴇɴɢɪʀɪᴍ ᴠɪᴅᴇᴏ...</b></blockquote>")
        try:
            await message.reply_video(
                video_url, 
                caption=f"<blockquote><b>✅ ᴠɪᴅᴇᴏ ʙᴇʀʜᴀsɪʟ ᴅɪᴜɴᴅᴜʜ</b>\n\n<b>🔗 sᴏᴜʀᴄᴇ:</b> <a href='{twitter_url}'>ᴛᴡɪᴛᴛᴇʀ/x</a></blockquote>"
            )
            await status_msg.delete()
        except Exception as e:
            await status_msg.edit(f"<blockquote><b>❌ ɢᴀɢᴀʟ ᴍᴇɴɢɪʀɪᴍ ᴠɪᴅᴇᴏ:</b>\n<code>{str(e)}</code></blockquote>")
    else:
        await status_msg.edit("<blockquote><b>❌ ɢᴀɢᴀʟ ᴍᴇɴɢᴀᴍʙɪʟ ᴠɪᴅᴇᴏ. ᴘᴀsᴛɪᴋᴀɴ ʟɪɴᴋ ʙᴇɴᴀʀ ᴀᴛᴀᴜ ᴀᴘɪ ᴛɪᴅᴀᴋ ʟɪᴍɪᴛ.</b></blockquote>")
        