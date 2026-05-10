import os
import aiohttp
from PyroUbot import *

__MODULE__ = "ꜰᴀᴄᴇ ᴅᴇᴛᴇᴄᴛ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ꜰᴀᴄᴇ ᴅᴇᴛᴇᴄᴛ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ꜰᴀᴄᴇ</code> [ʀᴇᴘʟʏ ꜰᴏᴛᴏ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴᴅᴇᴛᴇᴋsɪ ᴡᴀᴊᴀʜ, ᴜᴍᴜʀ, ᴅᴀɴ ɢᴇɴᴅᴇʀ ᴅᴀʀɪ sᴇʙᴜᴀʜ ꜰᴏᴛᴏ.</blockquote>
"""

@PY.UBOT("face")
@PY.TOP_CMD
async def _(client, message):
    # Proteksi: Harus reply ke foto
    if not message.reply_to_message or not message.reply_to_message.photo:
        return await message.reply_text("<blockquote><b>❌ ᴍᴏʜᴏɴ ʙᴀʟᴀs ᴋᴇ ꜰᴏᴛᴏ ᴡᴀᴊᴀʜ sᴇsᴇᴏʀᴀɴɢ!</b></blockquote>")

    status = await message.reply_text("<blockquote><b>🔍 sᴇᴅᴀɴɢ ᴍᴇɴɢᴀɴᴀʟɪsɪs ᴡᴀᴊᴀʜ...</b></blockquote>")
    path = await message.reply_to_message.download()

    async with aiohttp.ClientSession() as session:
        try:
            with open(path, 'rb') as f:
                form = aiohttp.FormData()
                form.add_field('file', f)
                api_url = f"https://api.botcahx.eu.org/api/tools/facedetect?apikey=@iqbalnew77"
                async with session.post(api_url, data=form) as resp:
                    data = await resp.json()

            if not data.get("status") or "result" not in data:
                return await status.edit("<blockquote><b>❌ ɢᴀɢᴀʟ!</b>\nᴡᴀᴊᴀʜ ᴛɪᴅᴀᴋ ᴛᴇʀᴅᴇᴛᴇᴋsɪ ᴀᴛᴀᴜ ᴀᴘɪ ʟɪᴍɪᴛ.</blockquote>")

            res = data["result"]
            hasil = (
                f"<blockquote><b>👤 ʜᴀsɪʟ ᴅᴇᴛᴇᴋsɪ ᴡᴀᴊᴀʜ</b>\n\n"
                f"<b>• ᴊᴜᴍʟᴀʜ ᴡᴀᴊᴀʜ:</b> <code>{res.get('face_count', 0)}</code>\n"
                f"<b>• ᴘᴇʀᴋɪʀᴀᴀɴ ᴜᴍᴜʀ:</b> <code>{res.get('age', 'ᴛɪᴅᴀᴋ ᴅɪᴋᴇᴛᴀʜᴜɪ')}</code>\n"
                f"<b>• ɢᴇɴᴅᴇʀ:</b> <code>{res.get('gender', 'ᴛɪᴅᴀᴋ ᴅɪᴋᴇᴛᴀʜᴜɪ')}</code></blockquote>"
            )
            await status.edit(hasil)
        except Exception as e:
            await status.edit(f"<blockquote><b>⚠️ ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ:</b>\n<code>{str(e)}</code></blockquote>")
        finally:
            if os.path.exists(path):
                os.remove(path)
                