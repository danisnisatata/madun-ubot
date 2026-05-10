import asyncio
import pytz
from datetime import datetime
from pyrogram.types import (InlineKeyboardMarkup, InlineQueryResultArticle, 
                            InputTextMessageContent, InlineKeyboardButton)
from PyroUbot import *

hadir_list = []

def get_hadir_list():
    if not hadir_list:
        return "<i>ʙᴇʟᴜᴍ ᴀᴅᴀ ʏᴀɴɢ ᴀʙsᴇɴ.</i>"
    return "\n".join([f"ᚗ {user['mention']} - <code>{user['jam']}</code>" for user in hadir_list])

__MODULE__ = "ᴀʙsᴇɴ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀʙsᴇɴ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴀʙsᴇɴ</code>
⊷ ᴍᴇᴍʙᴜᴀᴛ ʟɪsᴛ ᴀʙsᴇɴsɪ ɪɴᴛᴇʀᴀᴋᴛɪꜰ.
ᚗ <code>{0}ᴅᴇʟᴀʙsᴇɴ</code>
⊷ ᴍᴇɴɢʜᴀᴘᴜs sᴇᴍᴜᴀ ᴅᴀᴛᴀ ᴀʙsᴇɴsɪ.</blockquote>
"""

@PY.UBOT("absen")
@PY.TOP_CMD
async def absen_command(c, m):
    ggl_emo = await EMO.GAGAL(c)
    prs_emo = await EMO.PROSES(c)
    
    # Reset list setiap kali perintah baru dibuat (opsional, tergantung kebutuhan)
    # hadir_list.clear() 

    try:
        # Menggunakan username bot untuk memicu inline query
        x = await c.get_inline_bot_results(c.me.username, "absen_in")
        if x.results:
            await m.reply_inline_bot_result(x.query_id, x.results[0].id)
        else:
            await m.reply(f"<blockquote><b>{ggl_emo} ɢᴀɢᴀʟ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ʜᴀsɪʟ ɪɴʟɪɴᴇ!</b></blockquote>")
    except Exception as e:
        await m.reply(f"<blockquote><b>{ggl_emo} ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ:</b>\n<code>{str(e)}</code></blockquote>")

@PY.UBOT("delabsen")
@PY.TOP_CMD
async def clear_absen_command(c, m):
    hadir_list.clear()
    sks_emo = await EMO.BERHASIL(c)
    await m.reply(f"<blockquote><b>{sks_emo} sᴇᴍᴜᴀ ᴅᴀᴛᴀ ᴀʙsᴇɴ ʙᴇʀʜᴀsɪʟ ᴅɪʜᴀᴘᴜs!</b></blockquote>")

@PY.INLINE("^absen_in")
async def absen_query(c, iq):
    tz = pytz.timezone('Asia/Jakarta')
    timestamp = datetime.now(tz).strftime("%d-%m-%Y")
    hadir_text = get_hadir_list()

    text = (
        f"<blockquote><b>📊 ʟɪsᴛ ᴀʙsᴇɴsɪ MADUN ᴜʙᴏᴛ</b>\n"
        f"<b>📅 ᴛᴀɴɢɢᴀʟ :</b> <code>{timestamp}</code>\n\n"
        f"<b>👥 ᴅᴀꜰᴛᴀʀ ʜᴀᴅɪʀ :</b>\n"
        f"{hadir_text}\n\n"
        f"<b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> MADUN ᴜʙᴏᴛ</blockquote>"
    )
    
    buttons = [[InlineKeyboardButton("ʜᴀᴅɪʀ", callback_data="absen_hadir")]]
    await c.answer_inline_query(
        iq.id,
        cache_time=0,
        results=[
            InlineQueryResultArticle(
                title="ᴀʙsᴇɴ ᴅɪ sɪɴɪ",
                input_message_content=InputTextMessageContent(text),
                reply_markup=InlineKeyboardMarkup(buttons)
            )
        ],
    )

@PY.CALLBACK("absen_hadir")
async def hadir_callback(c, cq):
    user_id = cq.from_user.id
    mention = cq.from_user.mention
    tz = pytz.timezone('Asia/Jakarta')
    timestamp = datetime.now(tz).strftime("%d-%m-%Y")
    jam = datetime.now(tz).strftime("%H:%M:%S")
    
    if any(user['user_id'] == user_id for user in hadir_list):
        await cq.answer("ᴀɴᴅᴀ sᴜᴅᴀʜ ᴀʙsᴇɴ sᴇʙᴇʟᴜᴍɴʏᴀ! 🗿", show_alert=True)
    else:
        hadir_list.append({"user_id": user_id, "mention": mention, "jam": jam})
        hadir_text = get_hadir_list()
        
        text = (
            f"<blockquote><b>📊 ʟɪsᴛ ᴀʙsᴇɴsɪ MADUN ᴜʙᴏᴛ</b>\n"
            f"<b>📅 ᴛᴀɴɢɢᴀʟ :</b> <code>{timestamp}</code>\n\n"
            f"<b>👥 ᴅᴀꜰᴛᴀʀ ʜᴀᴅɪʀ :</b>\n"
            f"{hadir_text}\n\n"
            f"<b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> MADUN ᴜʙᴏᴛ</blockquote>"
        )
        
        buttons = [[InlineKeyboardButton("ʜᴀᴅɪʀ", callback_data="absen_hadir")]]
        await cq.edit_message_text(text, reply_markup=InlineKeyboardMarkup(buttons))
        await cq.answer("ᴛᴇʀɪᴍᴀ ᴋᴀsɪʜ sᴜᴅᴀʜ ʜᴀᴅɪʀ! ✅")
        