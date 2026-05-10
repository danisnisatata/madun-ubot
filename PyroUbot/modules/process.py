import psutil
from pyrogram import enums
from pyrogram.types import Message
from PyroUbot import *

__MODULE__ = "ᴘʀᴏᴄᴇꜱꜱ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴘʀᴏᴄᴇꜱꜱ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴘs</code>

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴᴀᴍᴘɪʟᴋᴀɴ 5 ᴘʀᴏsᴇs ᴛᴇʀʙᴇʀᴀᴛ ʏᴀɴɢ sᴇᴅᴀɴɢ ʙᴇʀᴊᴀʟᴀɴ ᴅɪ ᴠᴘs/sᴇʀᴠᴇʀ.</blockquote>
"""

@PY.UBOT("ps")
@PY.TOP_CMD
async def process_monitor_handler(client, message: Message):
    brhsl = await EMO.BERHASIL(client)
    
    # Ambil semua proses yang sedang berjalan
    procs = []
    for p in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            procs.append(p.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    # Urutkan berdasarkan penggunaan CPU tertinggi (ambil top 5)
    top_procs = sorted(procs, key=lambda x: x['cpu_percent'], reverse=True)[:5]

    res_text = f"<blockquote><b>{brhsl} ᴛᴏᴘ ᴘʀᴏᴄᴇss ᴍᴏɴɪᴛᴏʀ</b>\n"
    
    for p in top_procs:
        res_text += (
            f"\n<b>ᚗ ᴘʀᴏᴄᴇss :</b> <code>{p['name']}</code>"
            f"\n<b>⊷ ᴄᴘᴜ :</b> <code>{p['cpu_percent']}%</code> | <b>ʀᴀᴍ :</b> <code>{p['memory_percent']:.1f}%</code>\n"
        )
    
    res_text += "\n<b>⌭ sᴛᴀᴛᴜs :</b> sʏsᴛᴇᴍ ɴᴏʀᴍᴀʟ</blockquote>"

    await message.reply(res_text, parse_mode=enums.ParseMode.HTML)
    