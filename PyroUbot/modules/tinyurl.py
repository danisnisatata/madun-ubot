import aiohttp
from PyroUbot import *

__MODULE__ = "sʜᴏʀᴛᴇɴᴇʀ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sʜᴏʀᴛᴇɴᴇʀ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}sʜᴏʀᴛ</code> [ʟɪɴᴋ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇᴍᴇɴᴅᴇᴋᴋᴀɴ ᴛᴀᴜᴛᴀɴ ʏᴀɴɢ ᴘᴀɴᴊᴀɴɢ ᴍᴇɴᴊᴀᴅɪ ʟᴇʙɪʜ sɪɴɢᴋᴀᴛ.</blockquote>
"""

@PY.UBOT("short")
@PY.TOP_CMD
async def _(client, message):
    if len(message.command) < 2:
        return await message.reply_text("<blockquote><b>❌ ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ᴛᴀᴜᴛᴀɴ!\nᴄᴏɴᴛᴏʜ: <code>.sʜᴏʀᴛ</code> [ʟɪɴᴋ_ᴀɴᴅᴀ]</b></blockquote>")

    link = message.text.split(None, 1)[1]
    status_msg = await message.reply_text("<blockquote><b>🔗 sᴇᴅᴀɴɢ ᴍᴇᴍᴇɴᴅᴇᴋᴋᴀɴ ᴛᴀᴜᴛᴀɴ...</b></blockquote>")

    try:
        async with aiohttp.ClientSession() as session:
            # Menggunakan API TinyURL (Tanpa Key)
            async with session.get(f"http://tinyurl.com/api-create.php?url={link}") as resp:
                short_link = await resp.text()

        if "http" in short_link:
            hasil = (
                f"<blockquote><b>✅ ᴛᴀᴜᴛᴀɴ ʙᴇʀʜᴀsɪʟ ᴅɪᴘᴇɴᴅᴇᴋᴋᴀɴ</b>\n\n"
                f"<b>• sʜᴏʀᴛ ʟɪɴᴋ:</b> <code>{short_link}</code></blockquote>"
            )
            await status_msg.edit(hasil)
        else:
            await status_msg.edit("<blockquote><b>❌ ɢᴀɢᴀʟ!</b>\nᴘᴀsᴛɪᴋᴀɴ ᴛᴀᴜᴛᴀɴ ʏᴀɴɢ ᴀɴᴅᴀ ᴍᴀsᴜᴋᴋᴀɴ ᴠᴀʟɪᴅ.</blockquote>")
            
    except Exception as e:
        await status_msg.edit(f"<blockquote><b>⚠️ ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ:</b>\n<code>{str(e)}</code></blockquote>")
        