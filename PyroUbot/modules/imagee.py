import asyncio
import os
import cv2
from PyroUbot import *

__MODULE__ = "ɪᴍᴀɢᴇ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɪᴍᴀɢᴇ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴍɪʀʀᴏʀ</code>
⊷ ᴍᴇᴍʙᴜᴀᴛ ᴇꜰᴇᴋ ᴄᴇʀᴍɪɴ ᴘᴀᴅᴀ ɢᴀᴍʙᴀʀ.
ᚗ <code>{0}ɴᴇɢᴀᴛɪᴠᴇ</code>
⊷ ᴍᴇɴɢᴜʙᴀʜ ᴡᴀʀɴᴀ ɢᴀᴍʙᴀʀ ᴍᴇɴᴊᴀᴅɪ ɴᴇɢᴀᴛɪꜰ.

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ʙᴀʟᴀs ᴋᴇ ꜰᴏᴛᴏ ᴀᴛᴀᴜ sᴛɪᴋᴇʀ ᴜɴᴛᴜᴋ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ꜰɪᴛᴜʀ ɪɴɪ.</blockquote>
"""

@PY.UBOT("negative")
async def negative_cmd(client, message):
    prs_emo = await EMO.PROSES(client)
    brhsl_emo = await EMO.BERHASIL(client)
    ggl_emo = await EMO.GAGAL(client)
    
    ureply = message.reply_to_message
    if not ureply:
        return await message.reply_text(f"<blockquote><b>{ggl_emo} ʙᴀʟᴀs ᴋᴇ ɢᴀᴍʙᴀʀ ᴀᴛᴀᴜ sᴛɪᴋᴇʀ!</b></blockquote>")
        
    status_msg = await message.reply_text(f"<blockquote><b>{prs_emo} ᴍᴇᴍᴘʀᴏsᴇs ᴇꜰᴇᴋ ɴᴇɢᴀᴛɪᴠᴇ...</b></blockquote>")
    
    dl_path = await client.download_media(ureply, "./downloads/")
    output_png = "negative_res.png"
    output_jpg = "negative_res.jpg"

    def process_negative():
        try:
            img = cv2.imread(dl_path)
            if img is None: # Handle jika format tidak didukung cv2 langsung
                cap = cv2.VideoCapture(dl_path)
                _, frame = cap.read()
                img = frame
            
            res = cv2.bitwise_not(img)
            cv2.imwrite(output_jpg, res)
            return True
        except:
            return False

    loop = asyncio.get_event_loop()
    success = await loop.run_in_executor(None, process_negative)

    if success:
        await client.send_photo(
            message.chat.id,
            output_jpg,
            caption=f"<blockquote><b>{brhsl_emo} ᴇꜰᴇᴋ ɴᴇɢᴀᴛɪᴠᴇ sᴇʟᴇsᴀɪ!</b>\n\n<b>ᚗ ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>",
            reply_to_message_id=message.id,
        )
        await status_msg.delete()
    else:
        await status_msg.edit(f"<blockquote><b>{ggl_emo} ɢᴀɢᴀʟ ᴍᴇᴍᴘʀᴏsᴇs ɢᴀᴍʙᴀʀ!</b></blockquote>")

    if os.path.exists(dl_path): os.remove(dl_path)
    if os.path.exists(output_jpg): os.remove(output_jpg)


@PY.UBOT("mirror")
async def mirror_cmd(client, message):
    prs_emo = await EMO.PROSES(client)
    brhsl_emo = await EMO.BERHASIL(client)
    ggl_emo = await EMO.GAGAL(client)
    
    ureply = message.reply_to_message
    if not ureply:
        return await message.reply_text(f"<blockquote><b>{ggl_emo} ʙᴀʟᴀs ᴋᴇ ɢᴀᴍʙᴀʀ ᴀᴛᴀᴜ sᴛɪᴋᴇʀ!</b></blockquote>")

    status_msg = await message.reply_text(f"<blockquote><b>{prs_emo} ᴍᴇᴍᴘʀᴏsᴇs ᴇꜰᴇᴋ ᴍɪʀʀᴏʀ...</b></blockquote>")
    
    dl_path = await client.download_media(ureply, "./downloads/")
    output_jpg = "mirror_res.jpg"

    def process_mirror():
        try:
            img = cv2.imread(dl_path)
            if img is None:
                cap = cv2.VideoCapture(dl_path)
                _, frame = cap.read()
                img = frame
            
            flipped = cv2.flip(img, 1)
            combined = cv2.hconcat([img, flipped])
            cv2.imwrite(output_jpg, combined)
            return True
        except:
            return False

    loop = asyncio.get_event_loop()
    success = await loop.run_in_executor(None, process_mirror)

    if success:
        await client.send_photo(
            message.chat.id,
            output_jpg,
            caption=f"<blockquote><b>{brhsl_emo} ᴇꜰᴇᴋ ᴍɪʀʀᴏʀ sᴇʟᴇsᴀɪ!</b>\n\n<b>ᚗ ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>",
            reply_to_message_id=message.id,
        )
        await status_msg.delete()
    else:
        await status_msg.edit(f"<blockquote><b>{ggl_emo} ɢᴀɢᴀʟ ᴍᴇᴍᴘʀᴏsᴇs ɢᴀᴍʙᴀʀ!</b></blockquote>")

    if os.path.exists(dl_path): os.remove(dl_path)
    if os.path.exists(output_jpg): os.remove(output_jpg)
    