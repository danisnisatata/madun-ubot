import asyncio
from geopy.geocoders import Nominatim
from PyroUbot import *

__MODULE__ = "ɢᴍᴀᴘs"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɢᴍᴀᴘs ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ɢᴘs</code> [ɴᴀᴍᴀ_ᴛᴇᴍᴘᴀᴛ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴᴄᴀʀɪ ʟᴏᴋᴀsɪ ᴅᴀɴ ᴋᴏᴏʀᴅɪɴᴀᴛ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ sᴇʀᴠᴇʀ ɢᴏᴏɢʟᴇ ᴍᴀᴘs.</blockquote>
"""

@PY.UBOT("gps|maps")
@PY.TOP_CMD
async def gps_handler(client, message):
    prs_emo = await EMO.PROSES(client)
    brhsl_emo = await EMO.BERHASIL(client)
    ggl_emo = await EMO.GAGAL(client)
    
    args = get_arg(message)
    if not args:
        return await message.reply_text(
            f"<blockquote><b>{ggl_emo} ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ɴᴀᴍᴀ ᴛᴇᴍᴘᴀᴛ!</b>\nᚗ ᴄᴏɴᴛᴏʜ: <code>.ɢᴘs ᴍᴏɴᴀs</code></blockquote>"
        )

    status_msg = await message.reply_text(f"<blockquote><b>{prs_emo} sᴇᴅᴀɴɢ ᴍᴇɴᴄᴀʀɪ ʟᴏᴋᴀsɪ ᴅɪ sᴇʀᴠᴇʀ...</b></blockquote>")

    def fetch_location():
        try:
            geolocator = Nominatim(user_agent="IqbalUbot")
            return geolocator.geocode(args)
        except:
            return None

    loop = asyncio.get_event_loop()
    geoloc = await loop.run_in_executor(None, fetch_location)

    if geoloc:
        lat = geoloc.latitude
        lon = geoloc.longitude
        address = geoloc.address
        
        await client.send_location(
            message.chat.id,
            latitude=lat,
            longitude=lon,
            reply_to_message_id=message.id
        )
        
        await status_msg.edit(
            f"<blockquote><b>{brhsl_emo} ʟᴏᴋᴀsɪ ᴅɪᴛᴇᴍᴜᴋᴀɴ!</b>\n\n"
            f"<b>ᚗ ᴀʟᴀᴍᴀᴛ :</b> <code>{address}</code>\n"
            f"<b>ᚗ ᴋᴏᴏʀᴅɪɴᴀᴛ :</b> <code>{lat}, {lon}</code>\n\n"
            f"<b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>",
            disable_web_page_preview=True
        )
    else:
        await status_msg.edit(f"<blockquote><b>{ggl_emo} ʟᴏᴋᴀsɪ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ!</b>\nᚗ ᴘᴀsᴛɪᴋᴀɴ ɴᴀᴍᴀ ᴛᴇᴍᴘᴀᴛ ʙᴇɴᴀʀ.</blockquote>")
        