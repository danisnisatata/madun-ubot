import os
import asyncio
import requests
import bs4
import wget
from PyroUbot import *

__MODULE__ = "ɪɴsᴛᴀɢʀᴀᴍ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɪɴsᴛᴀɢʀᴀᴍ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ɪɢ</code> [ʟɪɴᴋ ɪɴsᴛᴀɢʀᴀᴍ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴɢᴜɴᴅᴜʜ ᴠɪᴅᴇᴏ ʀᴇᴇʟs ᴀᴛᴀᴜ ᴘᴏsᴛɪɴɢᴀɴ ᴅᴀʀɪ ɪɴsᴛᴀɢʀᴀᴍ sᴇᴄᴀʀᴀ ᴏᴛᴏᴍᴀᴛɪs.</blockquote>
"""

@PY.UBOT("ig")
async def instagram_downloader_handler(client, message):
    prs_emo = await EMO.PROSES(client)
    brhsl_emo = await EMO.BERHASIL(client)
    ggl_emo = await EMO.GAGAL(client)
    
    args = get_arg(message)
    if not args:
        return await message.reply_text(
            f"<blockquote><b>{ggl_emo} ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ʟɪɴᴋ!</b>\nᚗ ᴄᴏɴᴛᴏʜ: <code>.ɪɢ ʟɪɴᴋ_ɪɢ_ʟᴜ</code></blockquote>"
        )

    status_msg = await message.reply_text(f"<blockquote><b>{prs_emo} sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ᴠɪᴅᴇᴏ...</b></blockquote>")
    
    # Logic ddinstagram converter
    url = args.replace("instagram.com", "ddinstagram.com")
    url = url.replace("==", "%3D%3D")
    final_url = url[:-1] if url.endswith("=") else url

    def download_ig():
        try:
            # Mencoba wget jika direct link bermasalah
            return wget.download(final_url)
        except:
            return None

    try:
        # Coba kirim langsung via ddinstagram (fast method)
        await client.send_video(
            message.chat.id,
            final_url,
            caption=f"<blockquote><b>{brhsl_emo} ɪɴsᴛᴀɢʀᴀᴍ ᴅᴏᴡɴʟᴏᴀᴅᴇʀ sᴇʟᴇsᴀɪ!</b>\n\n<b>ᚗ ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>"
        )
        await status_msg.delete()
    except:
        # Jika gagal, coba download file-nya dulu (slow method)
        loop = asyncio.get_event_loop()
        file_path = await loop.run_in_executor(None, download_ig)
        
        if file_path and os.path.exists(file_path):
            await client.send_video(
                message.chat.id,
                file_path,
                caption=f"<blockquote><b>{brhsl_emo} ɪɴsᴛᴀɢʀᴀᴍ ᴅᴏᴡɴʟᴏᴀᴅᴇʀ sᴇʟᴇsᴀɪ!</b>\n\n<b>ᚗ ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>"
            )
            os.remove(file_path)
            await status_msg.delete()
        else:
            await status_msg.edit(
                f"<blockquote><b>{ggl_emo} ɢᴀɢᴀʟ ᴍᴇɴɢᴜɴᴅᴜʜ ᴠɪᴅᴇᴏ!</b>\nᚗ ᴘᴀsᴛɪᴋᴀɴ ʟɪɴᴋ ᴠᴀʟɪᴅ ᴅᴀɴ ᴀᴋᴜɴ ᴛɪᴅᴀᴋ ᴘʀɪᴠᴀᴛᴇ.</blockquote>"
            )
            