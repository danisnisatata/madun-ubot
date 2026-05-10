import os
import requests
import asyncio
import mimetypes
from PyroUbot import *

__MODULE__ = "ᴍᴇᴅɪᴀғɪʀᴇ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴍᴇᴅɪᴀғɪʀᴇ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴍꜰ</code> [ʟɪɴᴋ]
ᚗ <code>{0}ᴍᴇᴅɪᴀғɪʀᴇ</code> [ʟɪɴᴋ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴɢᴜɴᴅᴜʜ ꜰɪʟᴇ ᴅᴀʀɪ ʟɪɴᴋ ᴍᴇᴅɪᴀꜰɪʀᴇ sᴇᴄᴀʀᴀ ᴏᴛᴏᴍᴀᴛɪs.</blockquote>
"""

@PY.UBOT("mediafire|mf")
async def mediafire_handler(client, message):
    prs_emo = await EMO.PROSES(client)
    brhsl_emo = await EMO.BERHASIL(client)
    ggl_emo = await EMO.GAGAL(client)
    
    args = get_arg(message)
    if not args:
        return await message.reply_text(
            f"<blockquote><b>{ggl_emo} ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ᴜʀʟ ᴍᴇᴅɪᴀꜰɪʀᴇ!</b>\nᚗ ᴄᴏɴᴛᴏʜ: <code>.ᴍꜰ [ʟɪɴᴋ]</code></blockquote>", 
            quote=True
        )

    status_msg = await message.reply_text(f"<blockquote><b>{prs_emo} sᴇᴅᴀɴɢ ᴍᴇɴᴄᴀʀɪ ɪɴꜰᴏʀᴍᴀsɪ ꜰɪʟᴇ...</b></blockquote>", quote=True)
    api_url = f"https://api.botcahx.eu.org/api/dowloader/mediafire?url={args}&apikey=@iqbalnew77"

    def get_data():
        try: return requests.get(api_url).json()
        except: return None

    loop = asyncio.get_event_loop()
    data = await loop.run_in_executor(None, get_data)

    if data and data.get("status") and "result" in data:
        file_info = data["result"]
        filename = file_info["filename"]
        filesize = file_info["filesize"]
        file_url = file_info["url"]

        await status_msg.edit(f"<blockquote><b>{prs_emo} sᴇᴅᴀɴɢ ᴍᴇɴɢᴜɴᴅᴜʜ ꜰɪʟᴇ...</b>\n\n<b>ᚗ ɴᴀᴍᴀ :</b> <code>{filename}</code>\n<b>ᚗ ᴜᴋᴜʀᴀɴ :</b> <code>{filesize}</code></blockquote>")

        def download_file():
            path = f"./{filename}"
            with requests.get(file_url, stream=True) as r:
                r.raise_for_status()
                with open(path, "wb") as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
            return path

        try:
            file_path = await loop.run_in_executor(None, download_file)
            mime_type, _ = mimetypes.guess_type(file_path)
            
            caption = f"<blockquote><b>{brhsl_emo} ꜰɪʟᴇ ʙᴇʀʜᴀsɪʟ ᴅɪᴜɴᴅᴜʜ!</b>\n\n<b>ᚗ ɴᴀᴍᴀ :</b> <code>{filename}</code>\n<b>ᚗ ᴜᴋᴜʀᴀɴ :</b> <code>{filesize}</code>\n\n<b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>"

            if mime_type:
                if mime_type.startswith("image"):
                    await message.reply_photo(file_path, caption=caption)
                elif mime_type.startswith("video"):
                    await message.reply_video(file_path, caption=caption)
                elif mime_type.startswith("audio"):
                    await message.reply_audio(file_path, caption=caption)
                else:
                    await message.reply_document(file_path, caption=caption)
            else:
                await message.reply_document(file_path, caption=caption)

            if os.path.exists(file_path):
                os.remove(file_path)
            await status_msg.delete()

        except Exception as e:
            await status_msg.edit(f"<blockquote><b>{ggl_emo} ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ sᴀᴀᴛ ᴍᴇɴɢᴜɴᴅᴜʜ:</b>\n<code>{str(e)}</code></blockquote>")
    else:
        await status_msg.edit(f"<blockquote><b>{ggl_emo} ɢᴀɢᴀʟ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ɪɴꜰᴏʀᴍᴀsɪ ꜰɪʟᴇ. ᴘᴀsᴛɪᴋᴀɴ ʟɪɴᴋ ᴠᴀʟɪᴅ!</b></blockquote>")
        