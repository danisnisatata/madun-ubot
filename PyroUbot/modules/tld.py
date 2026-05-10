import aiohttp
from PyroUbot import *

__MODULE__ = "ᴛʟᴅ ᴄʜᴇᴄᴋ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴛʟᴅ ᴄʜᴇᴄᴋ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴛʟᴅ</code> [ᴇᴋsᴛᴇɴsɪ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴᴄᴇᴋ ɪɴꜰᴏʀᴍᴀsɪ ᴇᴋsᴛᴇɴsɪ ᴅᴏᴍᴀɪɴ (ᴄᴏɴᴛᴏʜ: .ᴄᴏᴍ, .ɪᴅ, .xʏᴢ).</blockquote>
"""

@PY.UBOT("tld")
@PY.TOP_CMD
async def _(client, message):
    if len(message.command) < 2:
        return await message.reply_text("<blockquote><b>📖 ᴘᴀɴᴅᴜᴀɴ ᴘᴇɴɢɢᴜɴᴀᴀɴ</b>\n\nᴋᴇᴛɪᴋ <code>.ᴛʟᴅ</code> [ᴄᴏᴍ] ᴀᴛᴀᴜ <code>.ᴛʟᴅ</code> [ɪᴅ] ᴜɴᴛᴜᴋ ᴄᴇᴋ ɪɴꜰᴏ ᴅᴏᴍᴀɪɴ.</blockquote>")

    query = message.command[1].replace(".", "").lower()
    status_msg = await message.reply_text("<blockquote><b>🔍 sᴇᴅᴀɴɢ ᴍᴇɴᴄᴀʀɪ ɪɴꜰᴏʀᴍᴀsɪ ᴇᴋsᴛᴇɴsɪ...</b></blockquote>")

    try:
        # Menggunakan API IANA/Public Data untuk info TLD
        url = f"https://rdap.iana.org/domain/{query}"
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status != 200:
                    return await status_msg.edit(f"<blockquote><b>❌ ᴇᴋsᴛᴇɴsɪ <code>.{query}</code> ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ ᴀᴛᴀᴜ ᴛɪᴅᴀᴋ ᴛᴇʀᴅᴀꜰᴛᴀʀ.</b></blockquote>")
                data = await resp.json()

        # Mengambil data teknis
        handle = data.get("handle", "ɴ/ᴀ")
        status = ", ".join(data.get("status", ["ᴜɴᴋɴᴏᴡɴ"]))
        whois = data.get("port43", "ɴ/ᴀ")

        hasil = (
            f"<blockquote><b>🌐 ɪɴꜰᴏʀᴍᴀsɪ ᴛʟᴅ (ᴅᴏᴍᴀɪɴ)</b>\n\n"
            f"<b>• ᴇᴋsᴛᴇɴsɪ:</b> <code>.{query.upper()}</code>\n"
            f"<b>• ᴘᴇɴᴅᴀꜰᴛᴀʀ:</b> <code>{handle}</code>\n"
            f"<b>• sᴛᴀᴛᴜs:</b> <code>{status}</code>\n"
            f"<b>• ᴡʜᴏɪs sᴇʀᴠᴇʀ:</b> <code>{whois}</code>\n\n"
            f"<b>💡 ᴄᴀᴛᴀᴛᴀɴ:</b>\n"
            f"<i>ᴅᴀᴛᴀ ɪɴɪ ᴠᴀʟɪᴅ ʙᴇʀᴅᴀsᴀʀᴋᴀɴ ᴄᴀᴛᴀᴛᴀɴ ɪᴀɴᴀ.</i></blockquote>"
        )
        await status_msg.edit(hasil)

    except Exception as e:
        await status_msg.edit(f"<blockquote><b>⚠️ ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ:</b>\n<code>{str(e)}</code></blockquote>")
         