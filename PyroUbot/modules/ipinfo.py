import asyncio
import socket
import subprocess
from PyroUbot import *

__MODULE__ = "ɴᴇᴛᴛᴏᴏʟs"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɴᴇᴛᴛᴏᴏʟs ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ɪᴘ</code> [ᴅᴏᴍᴀɪɴ]
ᚗ <code>{0}ᴘɪɴɢ</code> [ʜᴏsᴛ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴɢᴇᴄᴇᴋ ᴀʟᴀᴍᴀᴛ ɪᴘ ᴅᴏᴍᴀɪɴ ᴅᴀɴ ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴛᴇs ᴋᴏɴᴇᴋsɪ ᴘɪɴɢ.</blockquote>
"""

@PY.UBOT("ip")
async def ip_resolve_handler(client, message):
    prs_emo = await EMO.PROSES(client)
    brhsl_emo = await EMO.BERHASIL(client)
    ggl_emo = await EMO.GAGAL(client)
    
    args = get_arg(message)
    if not args:
        return await message.reply_text(
            f"<blockquote><b>{ggl_emo} ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ᴅᴏᴍᴀɪɴ!</b>\nᚗ ᴄᴏɴᴛᴏʜ: <code>.ɪᴘ ɢᴏᴏɢʟᴇ.ᴄᴏᴍ</code></blockquote>"
        )

    status_msg = await message.reply_text(f"<blockquote><b>{prs_emo} sᴇᴅᴀɴɢ ᴍᴇɴᴄᴀʀɪ ᴀʟᴀᴍᴀᴛ ɪᴘ...</b></blockquote>")

    def resolve_ip():
        try:
            return socket.gethostbyname(args)
        except:
            return None

    loop = asyncio.get_event_loop()
    ip_addr = await loop.run_in_executor(None, resolve_ip)

    if ip_addr:
        await status_msg.edit(
            f"<blockquote><b>🌐 ɪᴘ ᴅᴏᴍᴀɪɴ ʀᴇsᴏʟᴠᴇʀ</b>\n\n"
            f"<b>ᚗ ᴅᴏᴍᴀɪɴ :</b> <code>{args}</code>\n"
            f"<b>ᚗ ᴀʟᴀᴍᴀᴛ ɪᴘ :</b> <code>{ip_addr}</code>\n\n"
            f"<b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>"
        )
    else:
        await status_msg.edit(f"<blockquote><b>{ggl_emo} ɢᴀɢᴀʟ ᴍᴇɴɢᴀᴍʙɪʟ ɪᴘ ᴅᴀʀɪ ᴅᴏᴍᴀɪɴ ᴛᴇʀsᴇʙᴜᴛ!</b></blockquote>")

@PY.UBOT("ping")
async def ping_handler(client, message):
    prs_emo = await EMO.PROSES(client)
    brhsl_emo = await EMO.BERHASIL(client)
    ggl_emo = await EMO.GAGAL(client)
    
    args = get_arg(message)
    if not args:
        return await message.reply_text(
            f"<blockquote><b>{ggl_emo} ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ʜᴏsᴛ!</b>\nᚗ ᴄᴏɴᴛᴏʜ: <code>.ᴘɪɴɢ 8.8.8.8</code></blockquote>"
        )

    status_msg = await message.reply_text(f"<blockquote><b>{prs_emo} sᴇᴅᴀɴɢ ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴘɪɴɢ ᴋᴇ {args}...</b></blockquote>")

    def run_ping():
        try:
            # Menggunakan ping -c 3 (3 kali kirim paket)
            return subprocess.check_output(
                ["ping", "-c", "3", args],
                stderr=subprocess.STDOUT,
                universal_newlines=True,
                timeout=10
            )
        except:
            return None

    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, run_ping)

    if result:
        await status_msg.edit(
            f"<blockquote><b>📡 ᴘɪɴɢ ʀᴇsᴜʟᴛ ꜰᴏʀ {args}</b>\n\n"
            f"<code>{result}</code>\n"
            f"<b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>"
        )
    else:
        await status_msg.edit(f"<blockquote><b>{ggl_emo} ʜᴏsᴛ ᴛɪᴅᴀᴋ ᴍᴇʀᴇsᴘᴏɴ ᴀᴛᴀᴜ ᴅɪʙʟᴏᴋɪʀ!</b></blockquote>")
        