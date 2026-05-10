import os
import asyncio
from telegraph import upload_file
from PyroUbot import *

__MODULE__ = "ᴛᴇʟᴇɢʀᴀᴘʜ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴛᴇʟᴇɢʀᴀᴘʜ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴛɢ</code> [ʙᴀʟᴀs ᴍᴇᴅɪᴀ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴɢᴜɴɢɢᴀʜ ꜰᴏᴛᴏ ᴀᴛᴀᴜ ᴠɪᴅᴇᴏ ᴘᴇɴᴅᴇᴋ ᴋᴇ sᴇʀᴠᴇʀ ᴛᴇʟᴇɢʀᴀᴘʜ.
ᚗ ʜᴀsɪʟ ʙᴇʀᴜᴘᴀ ʟɪɴᴋ ʏᴀɴɢ ʙɪsᴀ ᴅɪᴀkses sɪᴀᴘᴀ sᴀᴊᴀ.</blockquote>
"""

@PY.UBOT("tg")
@PY.TOP_CMD
async def telegraph_handler(client, message):
    prs_emo = await EMO.PROSES(client)
    brhsl_emo = await EMO.BERHASIL(client)
    ggl_emo = await EMO.GAGAL(client)
    
    # Panduan jika tidak ada reply media
    if not message.reply_to_message or not message.reply_to_message.media:
        return await message.reply_text(
            f"<blockquote><b>{ggl_emo} ᴘᴀɴᴅᴜᴀɴ ᴛᴇʟᴇɢʀᴀᴘʜ</b>\n\n"
            "ᚗ ʙᴀʟᴀs (ʀᴇᴘʟʏ) ᴘᴀᴅᴀ ꜰᴏᴛᴏ ᴀᴛᴀᴜ ᴠɪᴅᴇᴏ.\n"
            "ᚗ ʟᴀʟᴜ ᴋᴇᴛɪᴋ ᴘᴇʀɪɴᴛᴀʜ : <code>.ᴛɢ</code></blockquote>"
        )

    status_msg = await message.reply_text(f"<blockquote><b>{prs_emo} sᴇᴅᴀɴɢ ᴍᴇɴɢᴜɴɢɢᴀʜ ᴋᴇ ᴛᴇʟᴇɢʀᴀᴘʜ...</b></blockquote>")

    try:
        # Download media ke VPS
        local_path = await client.download_media(message.reply_to_message)
        
        # Proses upload di executor agar tidak blocking
        loop = asyncio.get_event_loop()
        upload_link = await loop.run_in_executor(None, upload_file, local_path)
        
        # Format hasil premium
        hasil_text = (
            f"<blockquote><b>{brhsl_emo} ʙᴇʀʜᴀsɪʟ ᴅɪᴜɴɢɢᴀʜ!</b>\n\n"
            f"<b>ᚗ ʟɪɴᴋ :</b> <a href='https://telegra.ph{upload_link[0]}'>ᴋʟɪᴋ ᴅɪ sɪɴɪ</a>\n\n"
            f"<b>ᚗ ᴀʀᴀʜᴀɴ :</b>\n"
            f"<i>ʟɪɴᴋ ɪɴɪ ʙɪsᴀ ᴅɪɢᴜɴᴀᴋᴀɴ ᴜɴᴛᴜᴋ ᴍᴇᴍᴘᴇʀᴄᴀɴᴛɪᴋ ᴛᴀᴍᴘɪʟᴀɴ ʙʀᴏᴀᴅᴄᴀsᴛ ᴀᴛᴀᴜ ᴛᴏᴍʙᴏʟ ɪɴʟɪɴᴇ.</i>\n\n"
            f"<b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>"
        )
        await status_msg.edit(hasil_text, disable_web_page_preview=False)
        
        # Hapus file sampah
        if os.path.exists(local_path):
            os.remove(local_path)

    except Exception as e:
        await status_msg.edit(f"<blockquote><b>{ggl_emo} ɢᴀɢᴀʟ ᴍᴇɴɢᴜɴɢɢᴀʜ:</b>\n<code>{str(e)}</code></blockquote>")
        