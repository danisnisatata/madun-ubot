import os
import aiohttp
from PyroUbot import *

__MODULE__ = "sʜᴀᴢᴀᴍ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sʜᴀᴢᴀᴍ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ꜰɪɴᴅ</code> [ʀᴇᴘʟʏ ᴀᴜᴅɪᴏ/ᴠɪᴅᴇᴏ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴᴄᴀʀɪ ᴊᴜᴅᴜʟ ʟᴀɢᴜ ᴅᴀɴ ɴᴀᴍᴀ ᴀʀᴛɪs ᴍᴇʟᴀʟᴜɪ sᴜᴀʀᴀ ᴅᴀʀɪ ꜰɪʟᴇ ʏᴀɴɢ ᴅɪ-ʀᴇᴘʟʏ.</blockquote>
"""

@PY.UBOT("find")
@PY.TOP_CMD
async def shazam_handler(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)

    # Validasi reply
    if not message.reply_to_message or not (
        message.reply_to_message.audio or 
        message.reply_to_message.voice or 
        message.reply_to_message.video
    ):
        return await message.reply_text(
            f"<blockquote><b>{ggl} ɢᴀɢᴀʟ!</b>\nᚗ ʙᴀʟᴀs ᴋᴇ ᴀᴜᴅɪᴏ, ᴠᴏɪᴄᴇ, ᴀᴛᴀᴜ ᴠɪᴅᴇᴏ ʏᴀɴɢ ᴀᴅᴀ sᴜᴀʀᴀɴʏᴀ.</blockquote>"
        )

    status_msg = await message.reply_text(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇɴᴅᴇɴɢᴀʀᴋᴀɴ ᴅᴀɴ ᴍᴇɴɢᴀɴᴀʟɪsɪs...</b></blockquote>")
    
    # Download file ke VPS sementara
    file_path = await message.reply_to_message.download()

    async with aiohttp.ClientSession() as session:
        try:
            data = aiohttp.FormData()
            data.add_field('file', open(file_path, 'rb'))
            
            api_url = f"https://api.botcahx.eu.org/api/tools/shazam?apikey=@iqbalnew77"
            async with session.post(api_url, data=data) as resp:
                result_data = await resp.json()

            if not result_data.get("status") or "result" not in result_data:
                return await status_msg.edit(f"<blockquote><b>{ggl} ᴛɪᴅᴀᴋ ᴅɪᴋᴇɴᴀʟɪ!</b>\nᚗ ᴍᴀᴀꜰ, ᴊᴜᴅᴜʟ ʟᴀɢᴜ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ ᴅᴀʟᴀᴍ ᴅᴀᴛᴀʙᴀsᴇ.</blockquote>")

            res = result_data["result"]
            title = res.get('title', 'ᴜɴᴋɴᴏᴡɴ')
            artist = res.get('artists', 'ᴜɴᴋɴᴏᴡɴ')
            album = res.get('album', '-')
            
            text = (
                f"<blockquote><b>{brhsl} ʟᴀɢᴜ ᴅɪᴛᴇᴍᴜᴋᴀɴ!</b>\n\n"
                f"<b>ᚗ ᴊᴜᴅᴜʟ :</b> <code>{title}</code>\n"
                f"<b>ᚗ ᴀʀᴛɪs :</b> <code>{artist}</code>\n"
                f"<b>ᚗ ᴀʟʙᴜᴍ :</b> <code>{album}</code>\n\n"
                f"<i>ɢᴜɴᴀᴋᴀɴ .sᴘᴏᴛɪꜰʏ ᴜɴᴛᴜᴋ ᴍᴇɴɢᴜɴᴅᴜʜ ʟᴀɢᴜ ɪɴɪ!</i></blockquote>"
            )
            await status_msg.edit(text)

        except Exception as e:
            await status_msg.edit(f"<blockquote><b>{ggl} ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ:</b>\n<code>{str(e)}</code></blockquote>")
        
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
                          