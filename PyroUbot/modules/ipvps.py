import asyncio
import requests
from PyroUbot import *

__MODULE__ = "ɪᴘ ɪɴꜰᴏ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɪᴘ ɪɴꜰᴏ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ɪᴘɪɴꜰᴏ</code> [ᴀʟᴀᴍᴀᴛ_ɪᴘ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇʟᴀᴄᴀᴋ ɪɴꜰᴏʀᴍᴀsɪ ᴅᴇᴛᴀɪʟ, ʟᴏᴋᴀsɪ, ᴅᴀɴ ɪsᴘ ᴅᴀʀɪ ᴀʟᴀᴍᴀᴛ ɪᴘ.</blockquote>
"""

@PY.UBOT("ipinfo")
@PY.TOP_CMD
async def ipinfo_handler(client, message):
    prs_emo = await EMO.PROSES(client)
    brhsl_emo = await EMO.BERHASIL(client)
    ggl_emo = await EMO.GAGAL(client)
    
    args = get_arg(message)
    if not args:
        return await message.reply_text(
            f"<blockquote><b>{ggl_emo} ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ᴀʟᴀᴍᴀᴛ ɪᴘ!</b>\nᚗ ᴄᴏɴᴛᴏʜ: <code>.ɪᴘɪɴꜰᴏ 8.8.8.8</code></blockquote>"
        )

    status_msg = await message.reply_text(f"<blockquote><b>{prs_emo} sᴇᴅᴀɴɢ ᴍᴇʟᴀᴄᴀᴋ ᴀʟᴀᴍᴀᴛ ɪᴘ...</b></blockquote>")

    def fetch_ip():
        try:
            url = f"http://ip-api.com/json/{args}"
            return requests.get(url, timeout=10).json()
        except:
            return None

    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, fetch_ip)

    if response and response.get("status") == "success":
        res = f"""
<blockquote><b>🌐 ɪɴꜰᴏʀᴍᴀsɪ ᴀʟᴀᴍᴀᴛ ɪᴘ</b>

<b>ᚗ ɪᴘ :</b> <code>{response.get('query')}</code>
<b>ᚗ ɴᴇɢᴀʀᴀ :</b> <code>{response.get('country')}</code>
<b>ᚗ ᴋᴏᴛᴀ :</b> <code>{response.get('city')}</code>
<b>ᚗ ɪsᴘ :</b> <code>{response.get('isp')}</code>
<b>ᚗ ʟᴀᴛ/ʟᴏɴ :</b> <code>{response.get('lat')}, {response.get('lon')}</code>
<b>ᚗ ᴛɪᴍᴇᴢᴏɴᴇ :</b> <code>{response.get('timezone')}</code>

<b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>"""
        await status_msg.edit(res)
    else:
        msg = response.get('message') if response else "sᴇʀᴠᴇʀ ᴛɪᴅᴀᴋ ᴍᴇʀᴇsᴘᴏɴ"
        await status_msg.edit(f"<blockquote><b>{ggl_emo} ɢᴀɢᴀʟ ᴍᴇʟᴀᴄᴀᴋ ɪᴘ:</b>\n<code>{msg}</code></blockquote>")
        