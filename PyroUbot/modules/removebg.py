import io
import os
import requests
from PyroUbot import *

__MODULE__ = "ʀᴇᴍᴏᴠᴇʙɢ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʀᴇᴍᴏᴠᴇʙɢ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ʀᴍʙɢ</code> [ʀᴇᴘʟʏ ꜰᴏᴛᴏ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴɢʜᴀᴘᴜs ʟᴀᴛᴀʀ ʙᴇʟᴀᴋᴀɴɢ ɢᴀᴍʙᴀʀ ᴍᴇɴᴊᴀᴅɪ ᴛʀᴀɴsᴘᴀʀᴀɴ (ᴘɴɢ).</blockquote>
"""

async def ReTrieveFile(input_file_name):
    headers = {"X-API-Key": RMBG_API}
    files = {"image_file": (input_file_name, open(input_file_name, "rb"))}
    return requests.post(
        "https://api.remove.bg/v1.0/removebg",
        headers=headers,
        files=files,
        allow_redirects=True,
        stream=True,
    )

@PY.UBOT("rmbg")
@PY.TOP_CMD
async def rbg_handler(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)

    if RMBG_API is None:
        return await message.reply_text(f"<blockquote><b>{ggl} API ᴋᴇʏ ʀᴇᴍᴏᴠᴇ.ʙɢ ʙᴇʟᴜᴍ ᴅɪsᴇᴛᴛɪɴɢ!</b></blockquote>")

    if not message.reply_to_message or not message.reply_to_message.photo:
        return await message.reply_text(f"<blockquote><b>{ggl} ᴍᴏʜᴏɴ ʙᴀʟᴀs ᴋᴇ ꜰᴏᴛᴏ ʏᴀɴɢ ɪɴɢɪɴ ᴅɪʜᴀᴘᴜs ʙɢ-ɴʏᴀ.</b></blockquote>")

    status_msg = await message.reply_text(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇɴɢʜᴀᴘᴜs ʟᴀᴛᴀʀ ʙᴇʟᴀᴋᴀɴɢ...</b></blockquote>")

    try:
        downloaded_file = await client.download_media(message.reply_to_message)
        response = await ReTrieveFile(downloaded_file)
        os.remove(downloaded_file)

        if response.status_code != 200:
            return await status_msg.edit(f"<blockquote><b>{ggl} ᴇʀʀᴏʀ:</b> <code>{response.json().get('errors')[0].get('title')}</code></blockquote>")

        with io.BytesIO(response.content) as out_file:
            out_file.name = "rbg.png"
            await client.send_document(
                message.chat.id,
                document=out_file,
                caption=f"<blockquote><b>{brhsl} ʙᴀᴄᴋɢʀᴏᴜɴᴅ ʙᴇʀʜᴀsɪʟ ᴅɪʜᴀᴘᴜs</b>\n<b>ᚗ ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>",
                reply_to_message_id=message.id,
            )
            await status_msg.delete()

    except Exception as e:
        await status_msg.edit(f"<blockquote><b>{ggl} ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ:</b> <code>{str(e)}</code></blockquote>")
        