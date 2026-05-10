import asyncio
import requests
import os
import time as time_module
import aiohttp
from PyroUbot import *

__MODULE__ = "sᴏᴜɴᴅᴄʟᴏᴜᴅ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴏᴜɴᴅᴄʟᴏᴜᴅ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}sᴄ</code> [ʟɪɴᴋ sᴏᴜɴᴅᴄʟᴏᴜᴅ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴɢᴜɴᴅᴜʜ ᴍᴜsɪᴋ ᴅᴀʀɪ sᴏᴜɴᴅᴄʟᴏᴜᴅ ᴍᴇʟᴀʟᴜɪ ᴛᴀᴜᴛᴀɴ ʏᴀɴɢ ᴅɪʙᴇʀɪᴋᴀɴ.</blockquote>
"""

APIKEY = "@iqbalnew77"

async def download_file(url, path):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                with open(path, 'wb') as f:
                    f.write(await response.read())
                return True
            return False

@PY.UBOT("sc")
@PY.TOP_CMD
async def soundcloud_handler(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)
    
    args = get_arg(message)
    if not args:
        return await message.reply(
            f"<blockquote><b>{ggl} ʜᴀʀᴀᴘ ᴍᴀsᴜᴋᴋᴀɴ ʟɪɴᴋ!\nᴄᴏɴᴛᴏʜ: <code>.sᴄ</code> [ʟɪɴᴋ]</b></blockquote>"
        )

    status_msg = await message.reply(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ᴘᴇʀᴍɪɴᴛᴀᴀɴ...</b></blockquote>")
    
    api_url = f"https://api.betabotz.eu.org/api/download/soundcloud?url={args}&apikey={APIKEY}"
    
    try:
        res = requests.get(api_url, timeout=15).json()
        
        if not res.get("status"):
            return await status_msg.edit(f"<blockquote><b>{ggl} ɢᴀɢᴀʟ ᴍᴇɴɢᴀᴍʙɪʟ ᴅᴀᴛᴀ ᴅᴀʀɪ API.</b></blockquote>")
        
        result = res.get("result", {})
        music_url = result.get("url")
        title = result.get("title", "sᴏᴜɴᴅᴄʟᴏᴜᴅ ᴛʀᴀᴄᴋ")
        thumbnail = result.get("thumbnail")

        if not music_url:
            return await status_msg.edit(f"<blockquote><b>{ggl} ᴜʀʟ ᴍᴜsɪᴋ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ.</b></blockquote>")

        await status_msg.edit(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇɴɢᴜɴᴅᴜʜ ᴍᴜsɪᴋ...</b></blockquote>")
        
        music_path = f"sc_{int(time_module.time())}.mp3"
        thumb_path = f"sc_thumb_{int(time_module.time())}.jpg" if thumbnail else None

        if await download_file(music_url, music_path):
            if thumb_path:
                await download_file(thumbnail, thumb_path)
            
            await status_msg.edit(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇɴɢɪʀɪᴍ ᴀᴜᴅɪᴏ...</b></blockquote>")
            
            await client.send_audio(
                message.chat.id,
                music_path,
                thumb=thumb_path,
                caption=f"<blockquote><b>{brhsl} sᴏᴜɴᴅᴄʟᴏᴜᴅ ᴅᴏᴡɴʟᴏᴀᴅᴇʀ</b>\n\n<b>ᚗ ᴊᴜᴅᴜʟ :</b> <code>{title}</code>\n<b>ᚗ ᴜʀʟ :</b> <a href='{args}'>ᴋʟɪᴋ ᴅɪsɪɴɪ</a>\n<b>ᚗ ʙʏ :</b> {client.me.mention}</blockquote>"
            )
            
            if os.path.exists(music_path): os.remove(music_path)
            if thumb_path and os.path.exists(thumb_path): os.remove(thumb_path)
            await status_msg.delete()
        else:
            await status_msg.edit(f"<blockquote><b>{ggl} ɢᴀɢᴀʟ ᴍᴇɴɢᴜɴᴅᴜʜ ꜰɪʟᴇ ᴀᴜᴅɪᴏ.</b></blockquote>")

    except Exception as e:
        await status_msg.edit(f"<blockquote><b>{ggl} ᴇʀʀᴏʀ:</b> <code>{str(e)}</code></blockquote>")
        