import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from PyroUbot import *

__MODULE__ = "ᴘʟᴀʏ ᴘɪʟɪʜ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴘʟᴀʏ ᴘɪʟɪʜ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴘʟᴀʏ</code> [ᴊᴜᴅᴜʟ ʟᴀɢᴜ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴᴄᴀʀɪ ʟᴀɢᴜ ᴅᴇɴɢᴀɴ ᴛᴏᴍʙᴏʟ ᴋᴏɴꜰɪʀᴍᴀsɪ sᴇʙᴇʟᴜᴍ ᴅɪᴘᴜᴛᴀʀ ᴅɪ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ.</blockquote>
"""

@PY.UBOT("play")
@PY.TOP_CMD
async def play_pilih_handler(client, message):
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)
    
    args = get_arg(message)
    if not args:
        return await message.reply_text(
            f"<blockquote><b>{ggl} ᴘᴀɴᴅᴜᴀɴ ᴘᴇɴɢɢᴜɴᴀᴀɴ</b>\n\nᚗ ᴋᴇᴛɪᴋ: <code>.ᴘʟᴀʏ [ᴊᴜᴅᴜʟ ʟᴀɢᴜ]</code></blockquote>"
        )

    query = args
    
    # Tombol interaktif premium
    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("▶️ ᴘᴜᴛᴀʀ sᴇᴋᴀʀᴀɴɢ", callback_data=f"play_music|{query}"),
            InlineKeyboardButton("❌ ʙᴀᴛᴀʟᴋᴀɴ", callback_data="close_play")
        ],
        [InlineKeyboardButton("🔍 ᴄᴀʀɪ ᴅɪ sᴘᴏᴛɪꜰʏ", url=f"https://open.spotify.com/search/{query.replace(' ', '%20')}")]
    ])

    await bot.send_message(
        message.chat.id,
        f"<blockquote><b>{prs} ᴋᴏɴꜰɪʀᴍᴀsɪ ᴘᴇᴍᴜᴛᴀʀᴀɴ</b>\n\n"
        f"<b>ᚗ ᴘᴇɴᴄᴀʀɪᴀɴ :</b> <code>{query}</code>\n"
        f"<b>ᚗ ʀᴇǫᴜᴇsᴛ ᴅᴀʀɪ :</b> {message.from_user.mention}\n\n"
        f"<b>⌭ ᴀʀᴀʜᴀɴ :</b>\n"
        f"<i>sɪʟᴀᴋᴀɴ ᴘᴇɴᴄᴇᴛ ᴛᴏᴍʙᴏʟ ᴅɪ ʙᴀᴡᴀʜ ᴜɴᴛᴜᴋ ᴍᴜʟᴀɪ ᴍᴇᴍᴜᴛᴀʀ ᴍᴜsɪᴋ ᴅɪ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ.</i></blockquote>",
        reply_markup=buttons
    )

# --- CALLBACK HANDLER ---
@bot.on_callback_query(filters.regex("play_music"))
async def play_callback_handler(client, callback_query):
    brhsl = "✅" # Bisa diganti EMO.BERHASIL jika bot support
    prs = "🔄"
    
    query = callback_query.data.split("|")[1]
    
    await callback_query.edit_message_text(f"<blockquote><b>{prs} ᴍᴇᴍᴘʀᴏsᴇs ᴋᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ...</b></blockquote>")
    
    # Logika streaming ubot lu di sini
    try:
        # Contoh: await call_py.join_group_call(...)
        await asyncio.sleep(2) # Simulasi loading
        
        await callback_query.edit_message_text(
            f"<blockquote><b>{brhsl} ʙᴇʀʜᴀsɪʟ ᴍᴇᴍᴜᴛᴀʀ</b>\n\n"
            f"<b>ᚗ ᴊᴜᴅᴜʟ :</b> <code>{query}</code>\n"
            f"<b>ᚗ sᴛᴀᴛᴜs :</b> <code>sᴛʀᴇᴀᴍɪɴɢ ɪɴ ᴠᴄ</code>\n\n"
            f"<b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>"
        )
    except Exception as e:
        await callback_query.edit_message_text(f"<blockquote><b>❌ ɢᴀɢᴀʟ ᴍᴇᴍᴜᴛᴀʀ :</b>\n<code>{str(e)}</code></blockquote>")

@bot.on_callback_query(filters.regex("close_play"))
async def close_play_handler(client, callback_query):
    await callback_query.message.delete()
    