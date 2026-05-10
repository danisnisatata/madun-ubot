import httpx
from pyrogram import *
from pyrogram.types import *
from PyroUbot import *

__MODULE__ = "ᴀᴅᴢᴀɴ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀᴅᴢᴀɴ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴀᴅᴢᴀɴ</code> [ɴᴀᴍᴀ ᴋᴏᴛᴀ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴᴀᴍᴘɪʟᴋᴀɴ ᴊᴀᴅᴡᴀʟ sʜᴀʟᴀᴛ ʟᴇɴɢᴋᴀᴘ ʙᴇʀᴅᴀsᴀʀᴋᴀɴ ᴡɪʟᴀʏᴀʜ ᴋᴏᴛᴀ ʏᴀɴɢ ᴅɪᴄᴀʀɪ.</blockquote>
"""

async def get_adzan_data(lok):
    url = f"http://muslimsalat.com/{lok}.json?key=bd099c5825cbedb9aa934e255a81a5fc"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
        return None

@PY.UBOT("adzan")
@PY.TOP_CMD
async def adzan_handler(client, message):
    prs_emo = await EMO.PROSES(client)
    brhsl_emo = await EMO.BERHASIL(client)
    ggl_emo = await EMO.GAGAL(client)
    
    args = get_arg(message)
    if not args:
        return await message.reply_text(f"<blockquote><b>{ggl_emo} ᴍᴏʜᴏɴ sᴇʀᴛᴀᴋᴀɴ ɴᴀᴍᴀ ᴋᴏᴛᴀ!</b></blockquote>")
    
    status_msg = await message.reply_text(f"<blockquote><b>{prs_emo} ᴍᴇɴɢᴀᴍʙɪʟ ᴊᴀᴅᴡᴀʟ sʜᴀʟᴀᴛ...</b></blockquote>")
    
    try:
        result = await get_adzan_data(args)
        if not result or "items" not in result:
            return await status_msg.edit(f"<blockquote><b>{ggl_emo} ᴋᴏᴛᴀ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ!</b></blockquote>")
        
        item = result['items'][0]
        lokasi = f"{result['query']}, {result['country']}"
        
        res_text = (
            f"<blockquote><b>🕌 ᴊᴀᴅᴡᴀʟ sʜᴀʟᴀᴛ ᴘʀᴇᴍɪᴜᴍ</b>\n\n"
            f"<b>ᚗ ᴡɪʟᴀʏᴀʜ :</b> <code>{lokasi}</code>\n"
            f"<b>ᚗ ᴛᴀɴɢɢᴀʟ :</b> <code>{item['date_for']}</code>\n\n"
            f"<b>ᚗ sᴜʙᴜʜ :</b> <code>{item['fajr']}</code>\n"
            f"<b>ᚗ ᴛᴇʀʙɪᴛ :</b> <code>{item['shurooq']}</code>\n"
            f"<b>ᚗ ᴅᴢᴜʜᴜʀ :</b> <code>{item['dhuhr']}</code>\n"
            f"<b>ᚗ ᴀsʜᴀʀ :</b> <code>{item['asr']}</code>\n"
            f"<b>ᚗ ᴍᴀɢʜʀɪʙ :</b> <code>{item['maghrib']}</code>\n"
            f"<b>ᚗ ɪsʏᴀ :</b> <code>{item['isha']}</code>\n\n"
            f"<b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>"
        )
        await status_msg.edit(res_text)
        
    except Exception as e:
        await status_msg.edit(f"<blockquote><b>{ggl_emo} ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ:</b>\n<code>{str(e)}</code></blockquote>")

# Versi Assistant Bot
@PY.BOT("adzan")
async def adzan_bot_handler(client, message):
    args = get_arg(message)
    if not args:
        return await message.reply_text("<b>ᚗ ᴍᴏʜᴏɴ sᴇʀᴛᴀᴋᴀɴ ɴᴀᴍᴀ ᴋᴏᴛᴀ!</b>")
    
    result = await get_adzan_data(args)
    if result and "items" in result:
        item = result['items'][0]
        res_text = (
            f"<blockquote><b>🕌 ᴊᴀᴅᴡᴀʟ sʜᴀʟᴀᴛ</b>\n\n"
            f"<b>ᚗ ᴡɪʟᴀʏᴀʜ :</b> <code>{result['query']}</code>\n"
            f"<b>ᚗ sᴜʙᴜʜ :</b> <code>{item['fajr']}</code>\n"
            f"<b>ᚗ ᴅᴢᴜʜᴜʀ :</b> <code>{item['dhuhr']}</code>\n"
            f"<b>ᚗ ᴀsʜᴀʀ :</b> <code>{item['asr']}</code>\n"
            f"<b>ᚗ ᴍᴀɢʜʀɪʙ :</b> <code>{item['maghrib']}</code>\n"
            f"<b>ᚗ ɪsʏᴀ :</b> <code>{item['isha']}</code></blockquote>"
        )
        await message.reply_text(res_text)
        