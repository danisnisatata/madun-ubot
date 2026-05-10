from PyroUbot import *

__MODULE__ = "ǫʀ ᴄᴏᴅᴇ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ǫʀ ᴄᴏᴅᴇ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ǫʀ</code> [ᴛᴇᴋs/ʟɪɴᴋ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴɢᴜʙᴀʜ ᴛᴇᴋs ᴀᴛᴀᴜ ᴛᴀᴜᴛᴀɴ ᴍᴇɴᴊᴀᴅɪ ɢᴀᴍʙᴀʀ ǫʀ ᴄᴏᴅᴇ ʏᴀɴɢ ᴘʀᴇsɪsɪ.</blockquote>
"""

@PY.UBOT("qr")
@PY.TOP_CMD
async def qr_handler(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)

    args = get_arg(message)
    if not args:
        return await message.reply_text(f"<blockquote><b>{ggl} ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ᴛᴇᴋs ᴀᴛᴀᴜ ʟɪɴᴋ!</b></blockquote>")

    status_msg = await message.reply_text(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇᴍʙᴜᴀᴛ ǫʀ ᴄᴏᴅᴇ...</b></blockquote>")

    # Menggunakan Google Charts API (Stable & Fast)
    qr_url = f"https://chart.googleapis.com/chart?cht=qr&chl={args}&chs=500x500&choe=UTF-8&chld=L|2"
    
    try:
        await client.send_photo(
            message.chat.id, 
            qr_url, 
            caption=f"<blockquote><b>{brhsl} ǫʀ ᴄᴏᴅᴇ ʙᴇʀʜᴀsɪʟ ᴅɪʙᴜᴀᴛ</b>\n\n<b>ᚗ ɪsɪ :</b> <code>{args}</code>\n<b>ᚗ ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>"
        )
        await status_msg.delete()
    except Exception as e:
        await status_msg.edit(f"<blockquote><b>{ggl} ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ:</b>\n<code>{str(e)}</code></blockquote>")
        