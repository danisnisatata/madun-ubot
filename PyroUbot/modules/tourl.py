import os
import aiohttp
import filetype
from io import BytesIO
from PyroUbot import *

__MODULE__ = "ᴛᴏᴜʀʟ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴛᴏᴜʀʟ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴛᴏᴜʀʟ</code> [ʀᴇᴘʟʏ ᴍᴇᴅɪᴀ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴɢᴜɴɢɢᴀʜ ᴍᴇᴅɪᴀ ᴋᴇ ᴛᴀᴜᴛᴀɴ ᴘᴜʙʟɪᴋ (ᴄᴀᴛʙᴏx).</blockquote>
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
        async with session.post('https://ibb.co.com/user/api.php', data=form) as response:
            if response.status != 200:
                raise Exception(f"ꜰᴀɪʟᴇᴅ ᴛᴏ ᴜᴘʟᴏᴀᴅ ꜰɪʟᴇ: {response.status}")
            return await response.text()

async def tourl_handler(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    
    reply_message = message.reply_to_message
    if reply_message and reply_message.media:
        status_msg = await message.reply(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇɴɢᴜɴɢɢᴀʜ ᴍᴇᴅɪᴀ...</b></blockquote>")
        downloaded_file = await reply_message.download()
        
        try:
            with open(downloaded_file, 'rb') as f:
                buffer = BytesIO(f.read())
                media_url = await upload_file(buffer)
                await status_msg.edit(
                    f"<blockquote><b>{brhsl} ʙᴇʀʜᴀsɪʟ ᴅɪᴜɴɢɢᴀʜ!</b>\n\n"
                    f"<b>🔗 ᴛᴀᴜᴛᴀɴ:</b> <a href='{media_url.strip()}'>ᴋʟɪᴋ ᴅɪ sɪɴɪ</a></blockquote>",
                    disable_web_page_preview=True
                )
        except Exception as e:
            await status_msg.edit(f"<blockquote><b>{ggl} ᴇʀʀᴏʀ:</b> <code>{str(e)}</code></blockquote>")
        finally:
            if os.path.exists(downloaded_file):
                os.remove(downloaded_file)
    else:
        await message.reply(f"<blockquote><b>{ggl} ᴍᴏʜᴏɴ ʙᴀʟᴀs ᴋᴇ ᴍᴇᴅɪᴀ ᴜɴᴛᴜᴋ ᴍᴇɴɢᴜɴɢɢᴀʜ!</b></blockquote>")

@PY.UBOT("tourl|tg")
@PY.TOP_CMD
async def _(client, message):
    await tourl_handler(client, message)

@PY.BOT("tourl|tg")
async def _(client, message):
    await tourl_handler(client, message)
    