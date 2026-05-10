import os
import aiohttp
from PyroUbot import *

__MODULE__ = "ᴛɪᴋᴛᴏᴋ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴛɪᴋᴛᴏᴋ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴛᴛ</code> [ʟɪɴᴋ] → ᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ ɴᴏ ᴡᴍ.
ᚗ <code>{0}ᴛᴛᴍᴘ3</code> [ʟɪɴᴋ] → ᴅᴏᴡɴʟᴏᴀᴅ ᴍᴜsɪᴋ sᴀᴊᴀ.

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴɢᴜɴᴅᴜʜ ᴍᴇᴅɪᴀ ᴅᴀʀɪ ᴛɪᴋᴛᴏᴋ ᴛᴀɴᴘᴀ ᴛᴀɴᴅᴀ ᴀɪʀ.</blockquote>
"""

@PY.UBOT("tt|ttmp3")
@PY.TOP_CMD
async def _(client, message):
    if len(message.command) < 2:
        return await message.reply_text("<blockquote><b>📖 ᴘᴀɴᴅᴜᴀɴ</b>\n\nᴋᴇᴛɪᴋ: <code>.ᴛᴛ</code> [ʟɪɴᴋ_ᴛɪᴋᴛᴏᴋ]</blockquote>")

    link = message.text.split(None, 1)[1]
    cmd = message.command[0].lower()
    
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    
    status_msg = await message.reply_text(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ᴛɪᴋᴛᴏᴋ...</b></blockquote>")

    async with aiohttp.ClientSession() as session:
        try:
            # ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴀᴘɪ ʙᴏᴛᴄᴀʜx ᴅᴇɴɢᴀɴ ᴀᴘɪᴋᴇʏ ʟᴜ
            api_url = f"https://api.botcahx.eu.org/api/dowloader/tiktok?url={link}&apikey=@iqbalnew77"
            async with session.get(api_url) as resp:
                data = await resp.json()

            if not data.get("status") or "result" not in data:
                return await status_msg.edit(f"<blockquote><b>{ggl} ᴀᴘɪ ᴇʀʀᴏʀ:</b> ɢᴀɢᴀʟ ᴍᴇɴɢᴀᴍʙɪʟ ᴅᴀᴛᴀ.</blockquote>")

            res = data["result"]
            author = res.get("author", {}).get("nickname", "ᴜɴᴋɴᴏᴡɴ")
            
            if cmd == "ttmp3":
                # ᴅᴏᴡɴʟᴏᴀᴅ ᴍᴜsɪᴋ
                audio_url = res.get("audio")
                if not audio_url:
                    return await status_msg.edit(f"<blockquote><b>{ggl} ᴀᴜᴅɪᴏ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ.</b></blockquote>")
                
                await status_msg.edit(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇɴɢɪʀɪᴍ ᴍᴜsɪᴋ...</b></blockquote>")
                await client.send_audio(
                    chat_id=message.chat.id,
                    audio=audio_url,
                    caption=f"<blockquote><b>{brhsl} ᴛɪᴋᴛᴏᴋ ᴍᴜsɪᴄ</b>\n\n<b>👤 ᴀʀᴛɪs:</b> <code>{author}</code></blockquote>"
                )
            else:
                # ᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ ɴᴏ ᴡᴍ
                video_list = res.get("video", [])
                video_url = video_list[0] if video_list else None
                
                if not video_url:
                    return await status_msg.edit(f"<blockquote><b>{ggl} ᴠɪᴅᴇᴏ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ.</b></blockquote>")
                
                await status_msg.edit(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇɴɢɪʀɪᴍ ᴠɪᴅᴇᴏ...</b></blockquote>")
                desc = res.get("desc", "ɴᴏ ᴅᴇsᴄʀɪᴘᴛɪᴏɴ")
                await client.send_video(
                    chat_id=message.chat.id,
                    video=video_url,
                    caption=f"<blockquote><b>{brhsl} ᴛɪᴋᴛᴏᴋ ɴᴏ ᴡᴍ</b>\n\n<b>👤 ᴜsᴇʀ:</b> <code>{author}</code>\n<b>📝 ᴅᴇsᴄ:</b> <code>{desc}</code></blockquote>"
                )

            await status_msg.delete()

        except Exception as e:
            await status_msg.edit(f"<blockquote><b>⚠️ ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ:</b>\n<code>{str(e)}</code></blockquote>")
              