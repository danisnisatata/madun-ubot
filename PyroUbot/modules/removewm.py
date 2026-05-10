import aiohttp
import os
import filetype
from PyroUbot import *

__MODULE__ = "ʀᴇᴍᴏᴠᴇ ᴡᴍ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʀᴇᴍᴏᴠᴇ ᴡᴍ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ʀᴇᴍᴏᴠᴇᴡᴍ</code> [ʀᴇᴘʟʏ ꜰᴏᴛᴏ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴɢʜᴀᴘᴜs ᴡᴀᴛᴇʀᴍᴀʀᴋ ᴅᴀʀɪ sᴇʙᴜᴀʜ ɢᴀᴍʙᴀʀ sᴇᴄᴀʀᴀ ᴏᴛᴏᴍᴀᴛɪs ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴀɪ.</blockquote>
"""

async def upload_media_catbox(m):
    media = await m.reply_to_message.download()
    try:
        with open(media, "rb") as file:
            file_data = file.read()
            ext = filetype.guess_extension(file_data) or "jpg"
            
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

@PY.UBOT("removewm")
@PY.TOP_CMD
async def remove_watermark_handler(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)

    if not message.reply_to_message or not message.reply_to_message.photo:
        return await message.reply_text(f"<blockquote><b>{ggl} ᴍᴏʜᴏɴ ʙᴀʟᴀs ᴋᴇ ꜰᴏᴛᴏ ʏᴀɴɢ ɪɴɢɪɴ ᴅɪʜᴀᴘᴜs ᴡᴀᴛᴇʀᴍᴀʀᴋɴʏᴀ!</b></blockquote>")
    
    status_msg = await message.reply_text(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇɴɢᴜɴɢɢᴀʜ ᴅᴀɴ ᴍᴇᴍᴘʀᴏsᴇs...</b></blockquote>")

    url = await upload_media_catbox(message)
    if not url:
        return await status_msg.edit(f"<blockquote><b>{ggl} ɢᴀɢᴀʟ ᴍᴇɴɢᴜɴɢɢᴀʜ ɢᴀᴍʙᴀʀ ᴋᴇ sᴇʀᴠᴇʀ ᴛᴀᴍᴘᴜɴɢᴀɴ.</b></blockquote>")

    api_url = f"https://api.siputzx.my.id/api/tools/dewatermark?url={url}"
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(api_url) as res:
                if res.status == 200:
                    image_data = await res.read()
                    image_path = f"clean_{message.id}.jpg"
                    
                    with open(image_path, "wb") as f:
                        f.write(image_data)

                    await status_msg.delete()
                    await message.reply_photo(
                        image_path, 
                        caption=f"<blockquote><b>{brhsl} ᴡᴀᴛᴇʀᴍᴀʀᴋ ʙᴇʀʜᴀsɪʟ ᴅɪʜᴀᴘᴜs</b>\n\n<b>⌭ sᴛᴀᴛᴜs :</b> ᴘʀᴇᴍɪᴜᴍ ᴄʟᴇᴀɴ\n<b>ᚗ ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>"
                    )
                    os.remove(image_path)
                else:
                    await status_msg.edit(f"<blockquote><b>{ggl} ᴀᴘɪ ᴍᴇɴɢᴀʟᴀᴍɪ ɢᴀɴɢɢᴜᴀɴ ᴀᴛᴀᴜ ʟɪᴍɪᴛ.</b></blockquote>")
        except Exception as e:
            await status_msg.edit(f"<blockquote><b>{ggl} ᴇʀʀᴏʀ:</b> <code>{str(e)}</code></blockquote>")
            