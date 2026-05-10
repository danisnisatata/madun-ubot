import requests
from io import BytesIO
from PyroUbot import *

__MODULE__ = "ǫʀᴄᴏᴅᴇ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ǫʀᴄᴏᴅᴇ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ǫʀɢᴇɴ</code> [ᴛᴇᴋs]
ᚗ <code>{0}ǫʀʀᴇᴀᴅ</code> [ʀᴇᴘʟʏ ᴍᴇᴅɪᴀ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴɢᴜʙᴀʜ ᴛᴇᴋs ᴍᴇɴᴊᴀᴅɪ ɢᴀᴍʙᴀʀ ǫʀᴄᴏᴅᴇ ᴀᴛᴀᴜ ᴍᴇᴍʙᴀᴄᴀ ɪsɪ ᴅᴀʀɪ sᴇʙᴜᴀʜ ǫʀᴄᴏᴅᴇ.</blockquote>
"""

@PY.UBOT("qrgen")
@PY.TOP_CMD
async def qr_gen_handler(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)
    
    args = get_arg(message)
    if not args:
        return await message.reply_text(f"<blockquote><b>{ggl} ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ᴛᴇᴋs ᴀᴛᴀᴜ ʟɪɴᴋ!</b></blockquote>")
    
    status_msg = await message.reply_text(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇᴍʙᴜᴀᴛ ǫʀᴄᴏᴅᴇ...</b></blockquote>")
    
    api_url = f"https://api.siputzx.my.id/api/tools/qrgen?text={args}"
    
    try:
        res = requests.get(api_url)
        if res.status_code == 200:
            qr_img = BytesIO(res.content)
            qr_img.name = "qrcode.png"
            await client.send_photo(
                message.chat.id,
                qr_img,
                caption=f"<blockquote><b>{brhsl} ǫʀᴄᴏᴅᴇ ʙᴇʀʜᴀsɪʟ ᴅɪʙᴜᴀᴛ</b>\n\n<b>ᚗ ɪsɪ :</b> <code>{args}</code>\n<b>ᚗ ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>"
            )
            await status_msg.delete()
        else:
            await status_msg.edit(f"<blockquote><b>{ggl} ɢᴀɢᴀʟ ᴍᴇɴɢʜᴜʙᴜɴɢɪ sᴇʀᴠᴇʀ ᴀᴘɪ.</b></blockquote>")
    except Exception as e:
        await status_msg.edit(f"<blockquote><b>{ggl} ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ:</b> <code>{str(e)}</code></blockquote>")

@PY.UBOT("qrread")
@PY.TOP_CMD
async def qr_read_handler(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)
    
    replied = message.reply_to_message
    if not replied or not (replied.photo or replied.document):
        return await message.reply_text(f"<blockquote><b>{ggl} ᴍᴏʜᴏɴ ʙᴀʟᴀs ᴋᴇ ɢᴀᴍʙᴀʀ ǫʀᴄᴏᴅᴇ!</b></blockquote>")
    
    status_msg = await message.reply_text(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇᴍʙᴀᴄᴀ ǫʀᴄᴏᴅᴇ...</b></blockquote>")
    
    try:
        # Download ke memory
        media = await client.download_media(replied)
        
        # Upload ke hosting sementara untuk di read API
        # (Asumsi menggunakan API siputzx/dewatermark logic atau sejenisnya)
        # Sederhananya kita gunakan multipart post ke API Reader
        with open(media, "rb") as f:
            res = requests.post("https://api.siputzx.my.id/api/tools/qrread", files={"file": f})
        
        import os
        os.remove(media)
        
        if res.status_code == 200:
            data = res.json()
            # Sesuaikan dengan struktur JSON API yang dipakai
            hasil = data.get("result") or data.get("data")
            if hasil:
                await status_msg.edit(
                    f"<blockquote><b>{brhsl} ʜᴀsɪʟ ʙᴀᴄᴀ ǫʀᴄᴏᴅᴇ</b>\n\n"
                    f"<b>ᚗ ɪsɪ :</b> <code>{hasil}</code>\n\n"
                    f"<b>⌭ sᴛᴀᴛᴜs :</b> sᴜᴋsᴇs ᴛᴇʀʙᴀᴄᴀ</blockquote>"
                )
            else:
                await status_msg.edit(f"<blockquote><b>{ggl} ǫʀᴄᴏᴅᴇ ᴛɪᴅᴀᴋ ᴛᴇʀᴅᴇᴛᴇᴋsɪ ᴀᴛᴀᴜ ᴋᴏsᴏɴɢ.</b></blockquote>")
        else:
            await status_msg.edit(f"<blockquote><b>{ggl} sᴇʀᴠᴇʀ ɢᴀɢᴀʟ ᴍᴇᴍᴘʀᴏsᴇs ɢᴀᴍʙᴀʀ.</b></blockquote>")
            
    except Exception as e:
        await status_msg.edit(f"<blockquote><b>{ggl} ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ:</b> <code>{str(e)}</code></blockquote>")
        

