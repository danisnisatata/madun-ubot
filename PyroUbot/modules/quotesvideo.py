import aiohttp
import filetype
import os
import requests
from PyroUbot import *

__MODULE__ = "ϙᴜᴏᴛᴇs ᴠɪᴅᴇᴏ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ϙᴜᴏᴛᴇs ᴠɪᴅᴇᴏ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ǫᴠɪᴅᴇᴏ</code> [ᴛᴇᴋs]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇᴍʙᴜᴀᴛ ᴠɪᴅᴇᴏ ϙᴜᴏᴛᴇs ᴇsᴛᴇᴛɪᴋ sᴇᴘᴇʀᴛɪ ᴛɪᴋᴛᴏᴋ ᴅᴇɴɢᴀɴ ᴛᴇᴋs ᴋᴜsᴛᴏᴍ.</blockquote>
"""

async def upload_media_catbox(m):
    media = await m.reply_to_message.download()
    try:
        with open(media, "rb") as file:
            file_data = file.read()
            ext = filetype.guess_extension(file_data) or "mp4"
        
        form_data = aiohttp.FormData()
        form_data.add_field("fileToUpload", open(media, "rb"), filename=f"file.{ext}")
        form_data.add_field("reqtype", "fileupload")
        
        async with aiohttp.ClientSession() as session:
            async with session.post("https://ibb.co.com/user/api.php", data=form_data) as res:
                if res.status == 200:
                    url = await res.text()
                    return url.strip()
                return None
    except:
        return None
    finally:
        if os.path.exists(media):
            os.remove(media)

@PY.UBOT("qvideo")
@PY.TOP_CMD
async def quotesvideo_handler(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)

    if not message.reply_to_message or not message.reply_to_message.video:
        return await message.reply_text(f"<blockquote><b>{ggl} ᴍᴏʜᴏɴ ʙᴀʟᴀs ᴋᴇ ᴠɪᴅᴇᴏ ʏᴀɴɢ ɪɴɢɪɴ ᴅɪᴊᴀᴅɪᴋᴀɴ ϙᴜᴏᴛᴇs!</b></blockquote>")

    args = get_arg(message)
    if not args:
        return await message.reply_text(f"<blockquote><b>{ggl} ᴍᴀsᴜᴋᴋᴀɴ ᴛᴇᴋs ϙᴜᴏᴛᴇsɴʏᴀ!\nᚗ ᴄᴏɴᴛᴏʜ: <code>.ǫᴠɪᴅᴇᴏ</code> ᴍᴀᴋᴀɴ ᴀʏᴀᴍ</b></blockquote>")

    status_msg = await message.reply_text(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ᴠɪᴅᴇᴏ ϙᴜᴏᴛᴇs...</b></blockquote>")

    video_url = await upload_media_catbox(message)
    if not video_url:
        return await status_msg.edit(f"<blockquote><b>{ggl} ɢᴀɢᴀʟ ᴍᴇɴɢᴜɴɢɢᴀʜ ᴠɪᴅᴇᴏ ᴋᴇ sᴇʀᴠᴇʀ.</b></blockquote>")

    api_url = f"https://api.botcahx.eu.org/api/maker/quotesvideo?url={video_url}&text={args}&apikey=@iqbalnew77"
    
    try:
        res = requests.get(api_url, timeout=30)
        if res.status_code == 200:
            data = res.json()
            if data.get("status") and "result" in data:
                result_url = data["result"]
                await client.send_video(
                    message.chat.id,
                    result_url,
                    caption=f"<blockquote><b>{brhsl} ϙᴜᴏᴛᴇs ᴠɪᴅᴇᴏ ʙᴇʀʜᴀsɪʟ ᴅɪʙᴜᴀᴛ</b>\n\n<b>ᚗ ᴛᴇᴋs :</b> <code>{args}</code>\n<b>ᚗ ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>"
                )
                return await status_msg.delete()
            
        await status_msg.edit(f"<blockquote><b>{ggl} ɢᴀɢᴀʟ ᴍᴇᴍᴘʀᴏsᴇs ᴠɪᴅᴇᴏ ϙᴜᴏᴛᴇs.</b></blockquote>")
    except Exception as e:
        await status_msg.edit(f"<blockquote><b>{ggl} ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ:</b>\n<code>{str(e)}</code></blockquote>")
        