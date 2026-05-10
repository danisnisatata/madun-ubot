import os
import requests
import asyncio
from PyroUbot import *

__MODULE__ = "ʟᴏɢᴏ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʟᴏɢᴏ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴀᴠᴇɴɢᴇʀs</code> [ᴛᴇᴋs]
ᚗ <code>{0}ʟɪᴏɴ</code> [ᴛᴇᴋs]
ᚗ <code>{0}ɴɪɴᴊᴀ</code> [ᴛᴇᴋs]
ᚗ <code>{0}ᴊᴏᴋᴇʀ</code> [ᴛᴇᴋs]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇᴍʙᴜᴀᴛ ʟᴏɢᴏ ᴄᴜsᴛᴏᴍ ᴅᴇɴɢᴀɴ ᴛᴇᴋs sᴇsᴜᴀɪ ᴋᴇɪɴɢɪɴᴀɴ.</blockquote>
"""

API_KEY = "@iqbalnew77"

async def process_image_command(client, message, api_url, command_name):
    prs_emo = await EMO.PROSES(client)
    brhsl_emo = await EMO.BERHASIL(client)
    ggl_emo = await EMO.GAGAL(client)
    
    args = get_arg(message)
    if not args:
        return await message.reply_text(
            f"<blockquote><b>{ggl_emo} ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ᴛᴇᴋs!</b>\nᚗ ᴄᴏɴᴛᴏʜ: <code>.{command_name} ɪǫʙᴀʟ</code></blockquote>"
        )

    status_msg = await message.reply_text(f"<blockquote><b>{prs_emo} sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ʟᴏɢᴏ...</b></blockquote>")

    def fetch_image():
        params = {"text": args, "apikey": API_KEY}
        try:
            response = requests.get(api_url, params=params, timeout=30)
            if response.headers.get("Content-Type", "").startswith("image/"):
                return response.content
            return None
        except:
            return None

    loop = asyncio.get_event_loop()
    image_content = await loop.run_in_executor(None, fetch_image)

    if image_content:
        temp_file = f"{command_name}_{message.from_user.id}.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)
        
        await message.reply_photo(
            photo=temp_file,
            caption=f"<blockquote><b>{brhsl_emo} ʟᴏɢᴏ {command_name.upper()} sᴇʟᴇsᴀɪ!</b>\n\n<b>ᚗ ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>"
        )
        os.remove(temp_file)
        await status_msg.delete()
    else:
        await status_msg.edit(f"<blockquote><b>{ggl_emo} ɢᴀɢᴀʟ ᴍᴇᴍʙᴜᴀᴛ ʟᴏɢᴏ. ᴄᴏɴᴛᴏʜ ʟᴀɢɪ ɴᴀɴᴛɪ!</b></blockquote>")

@PY.UBOT("avengers")
async def avengers_command(client, message):
    api_url = "https://api.betabotz.eu.org/api/textpro/avengers-logo"
    await process_image_command(client, message, api_url, "avengers")

@PY.UBOT("lion")
async def lion_command(client, message):
    api_url = "https://api.betabotz.eu.org/api/textpro/lion-logo"
    await process_image_command(client, message, api_url, "lion")
    
@PY.UBOT("ninja")
async def ninja_command(client, message):
    api_url = "https://api.betabotz.eu.org/api/textpro/ninja-logo"
    await process_image_command(client, message, api_url, "ninja")
    
@PY.UBOT("joker")
async def joker_command(client, message):
    api_url = "https://api.betabotz.eu.org/api/textpro/joker-logo"
    await process_image_command(client, message, api_url, "joker")
    