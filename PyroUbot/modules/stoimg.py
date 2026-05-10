import os
from PyroUbot import *

__MODULE__ = "sᴛɪᴄᴋᴇʀ ᴛᴏ ɪᴍɢ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴄᴏɴᴠᴇʀᴛᴇʀ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴛᴏɪᴍɢ</code> [ʀᴇᴘʟʏ sᴛɪᴋᴇʀ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴɢᴜʙᴀʜ sᴛɪᴋᴇʀ ᴍᴇɴᴊᴀᴅɪ ꜰᴏᴛᴏ ꜰᴏʀᴍᴀᴛ ᴊᴘɢ.</blockquote>
"""

@PY.UBOT("toimg")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    
    if not message.reply_to_message or not message.reply_to_message.sticker:
        return await message.reply_text(f"<blockquote><b>{ggl} ᴍᴏʜᴏɴ ʙᴀʟᴀs ᴋᴇ sᴛɪᴋᴇʀ ʏᴀɴɢ ɪɴɢɪɴ ᴅɪᴋᴏɴᴠᴇʀsɪ.</b></blockquote>")
    
    status = await message.reply_text(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇɴɢᴏɴᴠᴇʀsɪ ᴋᴇ ꜰᴏᴛᴏ...</b></blockquote>")
    
    try:
        path = await message.reply_to_message.download()
        output = f"{path}.jpg"
        
        # Menggunakan perintah sistem untuk convert cepat
        os.system(f"ffmpeg -i {path} {output} -y")
        
        await client.send_photo(
            message.chat.id, 
            output, 
            caption=f"<blockquote><b>{brhsl} ʙᴇʀʜᴀsɪʟ ᴅɪᴜʙᴀʜ ᴍᴇɴᴊᴀᴅɪ ꜰᴏᴛᴏ!</b></blockquote>"
        )
        await status.delete()
        
    except Exception as e:
        await status.edit(f"<blockquote><b>{ggl} ᴇʀʀᴏʀ:</b> <code>{str(e)}</code></blockquote>")
    
    finally:
        if os.path.exists(path):
            os.remove(path)
        if os.path.exists(output):
            os.remove(output)
            