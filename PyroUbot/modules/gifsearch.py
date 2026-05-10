import random
import asyncio
from PyroUbot import *

__MODULE__ = "ɢɪꜰsᴇᴀʀᴄʜ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɢɪꜰsᴇᴀʀᴄʜ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ɢɪꜰ</code> [ǫᴜᴇʀʏ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴᴄᴀʀɪ ᴅᴀɴ ᴍᴇɴɢɪʀɪᴍ ɢɪꜰ/ᴀɴɪᴍᴀsɪ ʀᴀɴᴅᴏᴍ ᴅᴀʀɪ ɢᴏᴏɢʟᴇ sᴇᴀʀᴄʜ.</blockquote>
"""

@PY.UBOT("gif")
@PY.TOP_CMD
async def gif_handler(client, message):
    prs_emo = await EMO.PROSES(client)
    brhsl_emo = await EMO.BERHASIL(client)
    ggl_emo = await EMO.GAGAL(client)
    
    args = get_arg(message)
    if not args:
        return await message.reply_text(
            f"<blockquote><b>{ggl_emo} ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ǫᴜᴇʀʏ!</b>\nᚗ ᴄᴏɴᴛᴏʜ: <code>.ɢɪꜰ ʟᴜᴄᴜ</code></blockquote>"
        )

    status_msg = await message.reply_text(f"<blockquote><b>{prs_emo} sᴇᴅᴀɴɢ ᴍᴇɴᴄᴀʀɪ ɢɪꜰ...</b></blockquote>")

    try:
        # Menggunakan inline bot bawaan Telegram untuk mencari GIF
        inline_results = await client.get_inline_bot_results("gif", args)
        
        if not inline_results.results:
            return await status_msg.edit(f"<blockquote><b>{ggl_emo} ɢɪꜰ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ!</b></blockquote>")

        # Pilih hasil secara random dari daftar yang ada
        random_result = random.choice(inline_results.results)
        
        # Kirim hasil inline ke chat diri sendiri dulu untuk mendapatkan file_id
        saved_result = await client.send_inline_bot_result(
            "me", 
            inline_results.query_id, 
            random_result.id
        )
        
        # Ambil kembali pesan tadi untuk mendapatkan objek animation
        msg_id = saved_result.updates[1].message.id
        gif_msg = await client.get_messages("me", msg_id)
        
        if gif_msg.animation:
            await client.send_animation(
                message.chat.id,
                gif_msg.animation.file_id,
                caption=f"<blockquote><b>{brhsl_emo} ɢɪꜰ sᴇᴀʀᴄʜ sᴇʟᴇsᴀɪ!</b>\n\n<b>ᚗ ǫᴜᴇʀʏ :</b> <code>{args}</code>\n<b>ᚗ ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>",
                reply_to_message_id=message.id
            )
            await status_msg.delete()
        else:
            await status_msg.edit(f"<blockquote><b>{ggl_emo} ɢᴀɢᴀʟ ᴍᴇɴɢᴀᴍʙɪʟ ꜰɪʟᴇ ᴀɴɪᴍᴀsɪ.</b></blockquote>")

        # Hapus pesan sampah di Saved Messages
        await gif_msg.delete()

    except Exception as e:
        await status_msg.edit(f"<blockquote><b>{ggl_emo} ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ:</b>\n<code>{str(e)}</code></blockquote>")
        