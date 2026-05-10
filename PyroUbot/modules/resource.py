import psutil
from PyroUbot import *

__MODULE__ = "ʀᴇsᴏᴜʀᴄᴇ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʀᴇsᴏᴜʀᴄᴇ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ʀᴇsᴏᴜʀᴄᴇ</code>

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇʟɪʜᴀᴛ ᴅᴇᴛᴀɪʟ ᴘᴇɴɢɢᴜɴᴀᴀɴ ᴄᴘᴜ, ʀᴀᴍ, ᴅᴀɴ sᴡᴀᴘ ᴘᴀᴅᴀ sᴇʀᴠᴇʀ ᴠᴘs ʟᴜ.</blockquote>
"""

@PY.UBOT("resource")
async def resource_handler(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    
    status_msg = await message.reply(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇɴɢᴀᴍʙɪʟ ᴅᴀᴛᴀ sɪsᴛᴇᴍ...</b></blockquote>")
    
    cpu = psutil.cpu_percent(percpu=True)
    ram = psutil.virtual_memory()
    swap = psutil.swap_memory()

    res_text = f"<blockquote><b>{brhsl} ᴅᴇᴛᴀɪʟ sᴜᴍʙᴇʀ ᴅᴀᴛᴀ sɪsᴛᴇᴍ</b>\n\n"
    
    # Menampilkan penggunaan per core CPU
    for i, usage in enumerate(cpu):
        res_text += f"<b>ᚗ ᴄᴘᴜ ᴄᴏʀᴇ {i+1} :</b> <code>{usage}%</code>\n"
    
    res_text += f"\n<b>ᚗ ʀᴀᴍ ᴛᴇʀsᴇᴅɪᴀ :</b> <code>{ram.available // 1024**2} ᴍʙ</code>"
    res_text += f"\n<b>ᚗ sᴡᴀᴘ ᴛᴇʀᴘᴀᴋᴀɪ :</b> <code>{swap.used // 1024**2} ᴍʙ</code>"
    res_text += "\n\n<b>⌭ sᴛᴀᴛᴜs :</b> sɪsᴛᴇᴍ ʙᴇʀᴊᴀʟᴀɴ ɴᴏʀᴍᴀʟ</blockquote>"

    await status_msg.edit(res_text)
    