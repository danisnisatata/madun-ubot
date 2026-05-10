import subprocess
from PyroUbot import *

__MODULE__ = "ʀᴇsᴄᴜᴇ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʀᴇsᴄᴜᴇ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ʀᴇsᴄᴜᴇ</code>

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴘᴇɴɢᴇᴄᴇᴋᴀɴ ʟᴏɢ ᴅᴀɴ ᴀᴜᴛᴏ ʀᴇsᴛᴀʀᴛ ᴊɪᴋᴀ ᴛᴇʀᴅᴇᴛᴇᴋsɪ ᴇʀʀᴏʀ ᴀᴛᴀᴜ ʟᴀɢ.</blockquote>
"""

@PY.UBOT("rescue")
@PY.TOP_CMD
async def rescue_handler(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)
    
    status_msg = await message.reply(f"<blockquote><b>{prs} ʀᴇsᴄᴜᴇ ᴍᴏᴅᴇ ᴀᴋᴛɪꜰ, ᴍᴇɴɢᴀɴᴀʟɪsᴀ ʟᴏɢ...</b></blockquote>")

    # Mengambil 20 baris terakhir dari logs.txt
    log = subprocess.getoutput("tail -n 20 logs.txt")

    if "Traceback" in log or "Error" in log:
        await status_msg.edit(f"<blockquote><b>{ggl} ᴇʀʀᴏʀ ᴛᴇʀᴅᴇᴛᴇᴋsɪ! ᴍᴇɴᴊᴀʟᴀɴᴋᴀɴ ʀᴇsᴛᴀʀᴛ ᴏᴛᴏᴍᴀᴛɪs...</b></blockquote>")
        
        # Eksekusi restart ubot
        subprocess.Popen(
            "pkill -f PyroUbot && python3 -m PyroUbot",
            shell=True
        )
    else:
        await status_msg.edit(
            f"<blockquote><b>{brhsl} ᴜʙᴏᴛ ᴀᴍᴀɴ ᴅᴀɴ ᴛᴇʀᴋᴇɴᴅᴀʟɪ</b>\n\n"
            f"<b>⌭ sᴛᴀᴛᴜs :</b> ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴇʀʀᴏʀ ᴋʀɪᴛɪs.\n"
            f"<b>ᚗ ᴀɴᴀʟɪsᴀ :</b> sɪsᴛᴇᴍ ʙᴇʀᴊᴀʟᴀɴ ɴᴏʀᴍᴀʟ.</blockquote>"
        )
        