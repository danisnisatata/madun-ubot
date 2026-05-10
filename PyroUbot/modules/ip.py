import asyncio
import requests
from base64 import b64decode as kc
from PyroUbot import *

__MODULE__ = "ɪᴘ ᴀᴅᴅʀᴇss"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɪᴘ ᴀᴅᴅʀᴇss ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ɪᴘᴀᴅᴅʀᴇss</code> [ᴀʟᴀᴍᴀᴛ_ɪᴘ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇʟᴀᴄᴀᴋ ʟᴏᴋᴀsɪ ᴅᴇᴛᴀɪʟ, ᴋᴏᴅᴇ ᴘᴏs, ᴅᴀɴ ᴛɪᴍᴇᴢᴏɴᴇ ᴅᴀʀɪ ᴀʟᴀᴍᴀᴛ ɪᴘ.</blockquote>
"""

@PY.UBOT("ipaddress")
@PY.TOP_CMD
async def ip_address_handler(client, message):
    prs_emo = await EMO.PROSES(client)
    brhsl_emo = await EMO.BERHASIL(client)
    ggl_emo = await EMO.GAGAL(client)
    
    # Decode API Key secara aman
    apikey = kc("M0QwN0UyRUFBRjU1OTQwQUY0NDczNEMzRjJBQzdDMUE=").decode("utf-8")
    
    args = get_arg(message)
    if not args:
        return await message.reply_text(
            f"<blockquote><b>{ggl_emo} ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ᴀʟᴀᴍᴀᴛ ɪᴘ!</b>\nᚗ ᴄᴏɴᴛᴏʜ: <code>.ɪᴘᴀᴅᴅʀᴇss 1.1.1.1</code></blockquote>"
        )

    status_msg = await message.reply_text(f"<blockquote><b>{prs_emo} sᴇᴅᴀɴɢ ᴍᴇʟᴀᴄᴀᴋ ᴛᴀʀɢᴇᴛ...</b></blockquote>")

    def fetch_location():
        try:
            url = f"https://api.ip2location.io/?key={apikey}&ip={args}"
            return requests.get(url, timeout=20).json()
        except:
            return None

    loop = asyncio.get_event_loop()
    data = await loop.run_in_executor(None, fetch_location)

    if data and "ip" in data:
        res = f"""
<blockquote><b>🌐 ɪɴꜰᴏʀᴍᴀsɪ ᴀʟᴀᴍᴀᴛ ɪᴘ</b>

<b>ᚗ ɪᴘ ᴀᴅᴅʀᴇss :</b> <code>{data.get('ip')}</code>
<b>ᚗ ᴄᴏᴜɴᴛʀʏ ᴄᴏᴅᴇ :</b> <code>{data.get('country_code')}</code>
<b>ᚗ ᴄᴏᴜɴᴛʀʏ ɴᴀᴍᴇ :</b> <code>{data.get('country_name')}</code>
<b>ᚗ ʀᴇɢɪᴏɴ ɴᴀᴍᴇ :</b> <code>{data.get('region_name')}</code>
<b>ᚗ ᴄɪᴛʏ ɴᴀᴍᴇ :</b> <code>{data.get('city_name')}</code>
<b>ᚗ ᴢɪᴘ ᴄᴏᴅᴇ :</b> <code>{data.get('zip_code')}</code>
<b>ᚗ ᴛɪᴍᴇ ᴢᴏɴᴇ :</b> <code>{data.get('time_zone')}</code>
<b>ᚗ ᴀs/ɪsᴘ :</b> <code>{data.get('as')}</code>

<b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>"""
        await status_msg.edit(res)
    else:
        await status_msg.edit(f"<blockquote><b>{ggl_emo} ɢᴀɢᴀʟ ᴍᴇᴍᴘʀᴏsᴇs ᴅᴀᴛᴀ ɪᴘ. ᴘᴀsᴛɪᴋᴀɴ ɪᴘ ᴠᴀʟɪᴅ!</b></blockquote>")
        