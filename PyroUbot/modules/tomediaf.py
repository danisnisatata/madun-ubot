import os
import aiohttp
import filetype
from io import BytesIO
from PyroUbot import *

__MODULE__ = "ᴛᴏ ᴍᴇᴅɪᴀꜰɪʀᴇ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴛᴏ ᴍᴇᴅɪᴀꜰɪʀᴇ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴛᴏᴍᴇᴅɪᴀꜰ</code> [ʀᴇᴘʟʏ ꜰɪʟᴇ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴɢᴜɴɢɢᴀʜ ꜰɪʟᴇ ᴋᴇ ᴍᴇᴅɪᴀꜰɪʀᴇ ᴍᴇʟᴀʟᴜɪ ʀᴇᴘʟʏ ᴍᴇᴅɪᴀ.</blockquote>
"""

async def upload_file(buffer: BytesIO) -> str:
    kind = filetype.guess(buffer)
    if kind is None:
        raise ValueError("ᴄᴀɴɴᴏᴛ ᴅᴇᴛᴇʀᴍɪɴᴇ ꜰɪʟᴇ ᴛʏᴘᴇ")
    ext = kind.extension

    buffer.seek(0)
    form = aiohttp.FormData()
    form.add_field(
        'fileToUpload',
        buffer,
        filename='file.' + ext,
        content_type=kind.mime
    )
    form.add_field('reqtype', 'fileupload')

    async with aiohttp.ClientSession() as session:
        # Note: Menggunakan API endpoint Mediafire sesuai logic awal lu
        async with session.post('https://www.mediafire.com/api/1.5/file/upload.php', data=form) as response:
            if response.status != 200:
                raise Exception(f"ꜰᴀɪʟᴇᴅ ᴛᴏ ᴜᴘʟᴏᴀᴅ ꜰɪʟᴇ: {response.status}")
            return await response.text()

@PY.UBOT("tomediaf|tm")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    
    reply_message = message.reply_to_message
    if reply_message and (reply_message.media or reply_message.document):
        status_msg = await message.reply(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇɴɢᴜɴɢɢᴀʜ ᴋᴇ ᴍᴇᴅɪᴀꜰɪʀᴇ...</b></blockquote>")
        downloaded_file = await reply_message.download()
        
        try:
            with open(downloaded_file, 'rb') as f:
                buffer = BytesIO(f.read())
                media_url = await upload_file(buffer)
                
                # Format hasil yang lebih mewah
                await status_msg.edit(
                    f"<blockquote><b>{brhsl} ʙᴇʀʜᴀsɪʟ ᴅɪᴜɴɢɢᴀʜ!</b>\n\n"
                    f"<b>🔗 ᴛᴀᴜᴛᴀɴ:</b> <a href='{media_url.strip()}'>ʟɪɴᴋ ɴʏᴀ ᴋɪɴɢᴢ</a></blockquote>",
                    disable_web_page_preview=True
                )
        except Exception as e:
            await status_msg.edit(f"<blockquote><b>{ggl} ᴇʀʀᴏʀ:</b> <code>{str(e)}</code></blockquote>")
        finally:
            if os.path.exists(downloaded_file):
                os.remove(downloaded_file)
    else:
        await message.reply(f"<blockquote><b>{ggl} ᴍᴀɴᴀ ꜰɪʟᴇ ɴʏᴀ ʙᴊɪʀᴛᴛ, ʀᴇᴘʟʏ ᴅᴜʟᴜ!</b></blockquote>")
        