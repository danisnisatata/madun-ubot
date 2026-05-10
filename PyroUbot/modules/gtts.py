import os
import httpx
from PyroUbot import *

__MODULE__ = "ɢᴛᴛs"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɢᴛᴛs ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴛᴛs</code> [ᴛᴇᴋs]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴɢᴜʙᴀʜ ᴛᴇᴋs ᴍᴇɴᴊᴀᴅɪ ᴘᴇsᴀɴ sᴜᴀʀᴀ (ɢᴏᴏɢʟᴇ ᴠᴏɪᴄᴇ).
ᚗ sᴜᴀʀᴀ ᴅᴇꜰᴀᴜʟᴛ ᴀᴅᴀʟᴀʜ ʙᴀʜᴀsᴀ ɪɴᴅᴏɴᴇsɪᴀ.</blockquote>
"""

@PY.UBOT("tts")
@PY.TOP_CMD
async def gtts_handler(client, message):
    prs_emo = await EMO.PROSES(client)
    brhsl_emo = await EMO.BERHASIL(client)
    ggl_emo = await EMO.GAGAL(client)
    
    args = get_arg(message)
    if not args:
        # Jika tidak ada teks, coba ambil dari pesan yang di-reply
        if message.reply_to_message and message.reply_to_message.text:
            args = message.reply_to_message.text
        else:
            return await message.reply_text(
                f"<blockquote><b>{ggl_emo} ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ᴛᴇᴋs!</b>\nᚗ ᴄᴏɴᴛᴏʜ: <code>.ᴛᴛs ʜᴀʟᴏ ʙᴏsǫᴜ</code></blockquote>"
            )

    status_msg = await message.reply_text(f"<blockquote><b>{prs_emo} sᴇᴅᴀɴɢ ᴍᴇɴɢᴜʙᴀʜ ᴛᴇᴋs ᴋᴇ sᴜᴀʀᴀ...</b></blockquote>")
    
    # Encode teks untuk URL
    encoded_text = args.replace(" ", "%20")
    # API Google TTS (tl=id untuk bahasa Indonesia)
    tts_url = f"https://translate.google.com/translate_tts?ie=UTF-8&q={encoded_text}&tl=id&client=tw-ob"
    
    file_name = f"tts_{message.id}.mp3"
    
    try:
        async with httpx.AsyncClient() as session:
            res = await session.get(tts_url, timeout=20)
            if res.status_code != 200:
                return await status_msg.edit(f"<blockquote><b>{ggl_emo} ɢᴀɢᴀʟ ᴍᴇɴɢᴀᴍʙɪʟ sᴜᴀʀᴀ ᴅᴀʀɪ ɢᴏᴏɢʟᴇ!</b></blockquote>")
            
            with open(file_name, "wb") as f:
                f.write(res.content)
            
        await client.send_voice(
            message.chat.id,
            voice=file_name,
            caption=f"<blockquote><b>{brhsl_emo} ᴛᴇxᴛ-ᴛᴏ-sᴘᴇᴇᴄʜ sᴇʟᴇsᴀɪ!</b>\n\n<b>ᚗ ᴛᴇᴋs :</b> <code>{args[:50]}...</code>\n<b>ᚗ ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>",
            reply_to_message_id=message.id
        )
        await status_msg.delete()
        
    except Exception as e:
        await status_msg.edit(f"<blockquote><b>{ggl_emo} ᴇʀʀᴏʀ:</b>\n<code>{str(e)}</code></blockquote>")
    
    finally:
        if os.path.exists(file_name):
            os.remove(file_name)
            