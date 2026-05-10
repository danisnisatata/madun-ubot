import asyncio
import aiohttp
from PyroUbot import *

__MODULE__ = "ʏᴏᴜᴛᴜʙᴇ"
__HELP__ = """
<blockquote><b>ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʏᴏᴜᴛᴜʙᴇ</b>

ᴘᴇʀɪɴᴛᴀʜ:
<code>{0}ʏᴛᴠ</code> [ʟɪɴᴋ] → ᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ ʏᴏᴜᴛᴜʙᴇ.
<code>{0}ʏᴛᴀ</code> [ʟɪɴᴋ] → ᴅᴏᴡɴʟᴏᴀᴅ ᴀᴜᴅɪᴏ ʏᴏᴜᴛᴜʙᴇ.</blockquote>
"""

@PY.UBOT("ytv|yta")
@PY.TOP_CMD
async def _(client, message):
    if len(message.command) < 2:
        return await message.reply_text("<blockquote><b>📖 ᴘᴀɴᴅᴜᴀɴ ᴘᴇɴɢɢᴜɴᴀᴀɴ</b>\n\nᴋᴇᴛɪᴋ: <code>.ʏᴛᴠ [ʟɪɴᴋ]</code> ᴀᴛᴀᴜ <code>.ʏᴛᴀ [ʟɪɴᴋ]</code></blockquote>")

    link = message.text.split(None, 1)[1]
    cmd = message.command[0].lower()
    status_msg = await message.reply_text("<blockquote><b>⌛ sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ʏᴏᴜᴛᴜʙᴇ...</b></blockquote>")

    async with aiohttp.ClientSession() as session:
        try:
            # ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴀᴘɪ ʏᴀɴɢ sᴛᴀʙɪʟ ᴋʜᴜsᴜs ᴜɴᴛᴜᴋ ᴅᴏᴡɴʟᴏᴀᴅᴇʀ
            api_url = f"https://api.botcahx.eu.org/api/dowloader/yt?url={link}&apikey=@iqbalnew77"
            async with session.get(api_url) as resp:
                data = await resp.json()

            # ᴘᴇɴɢᴇᴄᴇᴋᴀɴ ᴀɢᴀʀ ᴛɪᴅᴀᴋ ᴇʀʀᴏʀ 'ʀᴇsᴜʟᴛ'
            if not data.get("status") or "result" not in data:
                return await status_msg.edit("<blockquote><b>❌ ᴀᴘɪ ᴇʀʀᴏʀ:</b> ɢᴀɢᴀʟ ᴍᴇɴɢᴀᴍʙɪʟ ᴅᴀᴛᴀ, ᴘᴀsᴛɪᴋᴀɴ ʟɪɴᴋ ʙᴇɴᴀʀ ᴀᴛᴀᴜ ᴀᴘɪ ᴛɪᴅᴀᴋ ʟɪᴍɪᴛ.</blockquote>")

            res = data["result"]
            
            if "yta" in cmd:
                # ᴋɪʀɪᴍ ᴀᴜᴅɪᴏ (ᴍᴘ3)
                if not res.get("mp3"):
                    return await status_msg.edit("<blockquote><b>❌ ɢᴀɢᴀʟ:</b> ꜰɪʟᴇ ᴍᴘ3 ᴛɪᴅᴀᴋ ᴛᴇʀsᴇᴅɪᴀ ᴜɴᴛᴜᴋ ᴠɪᴅᴇᴏ ɪɴɪ.</blockquote>")
                
                await status_msg.edit("<blockquote><b>📥 ᴍᴇɴɢɪʀɪᴍ ᴀᴜᴅɪᴏ ʏᴏᴜᴛᴜʙᴇ...</b></blockquote>")
                await client.send_audio(
                    chat_id=message.chat.id,
                    audio=res["mp3"],
                    caption=f"<blockquote><b>🎵 ʏᴏᴜᴛᴜʙᴇ ᴀᴜᴅɪᴏ</b>\n\n<b>📌 ᴊᴜᴅᴜʟ:</b> <code>{res.get('title', 'Unknown')}</code></blockquote>"
                )
            else:
                # ᴋɪʀɪᴍ ᴠɪᴅᴇᴏ (ᴍᴘ4)
                if not res.get("mp4"):
                    return await status_msg.edit("<blockquote><b>❌ ɢᴀɢᴀʟ:</b> ꜰɪʟᴇ ᴍᴘ4 ᴛɪᴅᴀᴋ ᴛᴇʀsᴇᴅɪᴀ.</blockquote>")
                
                await status_msg.edit("<blockquote><b>📥 ᴍᴇɴɢɪʀɪᴍ ᴠɪᴅᴇᴏ ʏᴏᴜᴛᴜʙᴇ...</b></blockquote>")
                await client.send_video(
                    chat_id=message.chat.id,
                    video=res["mp4"],
                    caption=f"<blockquote><b>📹 ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ</b>\n\n<b>📌 ᴊᴜᴅᴜʟ:</b> <code>{res.get('title', 'Unknown')}</code></blockquote>"
                )

            await status_msg.delete()

        except Exception as e:
            await status_msg.edit(f"<blockquote><b>⚠️ ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ:</b>\n<code>{str(e)}</code></blockquote>")
            
            