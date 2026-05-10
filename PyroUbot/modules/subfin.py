import re
import aiohttp
from PyroUbot import *
from pyrogram.types import Message

__MODULE__ = "sᴜʙғɪɴᴅᴇʀ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴜʙғɪɴᴅᴇʀ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}sᴜʙꜰɪɴ</code> [ᴅᴏᴍᴀɪɴ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴᴄᴀʀɪ ᴅᴀꜰᴛᴀʀ sᴜʙᴅᴏᴍᴀɪɴ ᴅᴀʀɪ ᴅᴏᴍᴀɪɴ ᴜᴛᴀᴍᴀ.</blockquote>
"""

API_KEY = "@iqbalnew77" 
API_URL = "https://api.botcahx.eu.org/api/tools/subdomain-finder"

async def get_subdomains(domain):
    """ᴍᴇɴɢᴀᴍʙɪʟ ᴅᴀꜰᴛᴀʀ sᴜʙᴅᴏᴍᴀɪɴ ᴅᴀʀɪ ᴀᴘɪ."""
    params = {"query": domain, "apikey": API_KEY}
    async with aiohttp.ClientSession() as session:
        async with session.get(API_URL, params=params) as response:
            if response.status == 200:
                data = await response.json()
                if data.get("status") and "result" in data:
                    return data["result"]
    return None

@PY.UBOT("subfin")
@PY.TOP_CMD
async def subfinder(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    
    command_parts = message.text.split(maxsplit=1)

    if len(command_parts) < 2:
        return await message.reply("<blockquote><b>❌ ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ᴅᴏᴍᴀɪɴ!\nᴄᴏɴᴛᴏʜ: <code>.sᴜʙꜰɪɴ</code> ɢᴏᴏɢʟᴇ.ᴄᴏᴍ</b></blockquote>")

    domain = command_parts[1].strip()

    if not re.match(r"^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", domain):
        return await message.reply(f"<blockquote><b>{ggl} ᴅᴏᴍᴀɪɴ ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ!</b></blockquote>")

    status_msg = await message.reply(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇɴᴄᴀʀɪ sᴜʙᴅᴏᴍᴀɪɴ ᴅᴀʀɪ <code>{domain}</code>...</b></blockquote>")

    subdomains = await get_subdomains(domain)

    if subdomains:
        result_text = f"<blockquote><b>{brhsl} sᴜʙᴅᴏᴍᴀɪɴ ꜰᴏᴜɴᴅ: <code>{domain}</code></b>\n\n"
        result_text += "\n".join(f"<b>ᚗ</b> <code>{sub}</code>" for sub in subdomains[:50]) # Limit 50 agar tidak kena limit karakter
        result_text += "</blockquote>"
        await status_msg.edit(result_text)
    else:
        await status_msg.edit(f"<blockquote><b>{ggl} ɢᴀɢᴀʟ ᴍᴇɴᴄᴀʀɪ sᴜʙᴅᴏᴍᴀɪɴ ᴀᴛᴀᴜ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ.</b></blockquote>")
        