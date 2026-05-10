import asyncio
import requests
from pyrogram.enums import ChatAction
from PyroUbot import *

__MODULE__ = "ɢᴜʀᴜ ᴀɪ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɢᴜʀᴜ ᴀɪ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ɢᴜʀᴜᴀɪ</code> [ᴘᴇʀᴛᴀɴʏᴀᴀɴ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴀssɪsᴛᴀɴᴛ ᴘɪɴᴛᴀʀ ᴜɴᴛᴜᴋ ᴍᴇɴᴊᴀᴡᴀʙ sᴇɢᴀʟᴀ ᴘᴇʀᴛᴀɴʏᴀᴀɴ ᴅᴀɴ ᴍᴇᴍʙᴀɴᴛᴜ ᴛᴜɢᴀs ᴀɴᴅᴀ.</blockquote>
"""

@PY.UBOT("guruai")
@PY.TOP_CMD
async def chat_guru_handler(client, message):
    prs_emo = await EMO.PROSES(client)
    brhsl_emo = await EMO.BERHASIL(client)
    ggl_emo = await EMO.GAGAL(client)
    
    args = get_arg(message)
    if not args:
        return await message.reply_text(
            f"<blockquote><b>{ggl_emo} ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ᴘᴇʀᴛᴀɴʏᴀᴀɴ!</b>\nᚗ ᴄᴏɴᴛᴏʜ: <code>.ɢᴜʀᴜᴀɪ ᴀᴘᴀ ɪᴛᴜ ᴘʏᴛʜᴏɴ?</code></blockquote>"
        )

    # Menampilkan status sedang mengetik
    await client.send_chat_action(message.chat.id, ChatAction.TYPING)
    status_msg = await message.reply_text(f"<blockquote><b>{prs_emo} ᴏᴋᴇ ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ ᴍᴜʀɪᴅ-ᴍᴜʀɪᴅ...</b></blockquote>")

    def ask_guru():
        try:
            url = f'https://fastrestapis.fasturl.cloud/aillm/degreeguru?ask={args}'
            response = requests.get(url, timeout=30)
            return response.json()
        except:
            return None

    loop = asyncio.get_event_loop()
    data = await loop.run_in_executor(None, ask_guru)

    if data and "result" in data:
        jawaban = data["result"]
        res_text = f"""
<blockquote><b>🎓 ᴊᴀᴡᴀʙᴀɴ sᴀɴɢ ɢᴜʀᴜ</b>
{jawaban}
<b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>"""
        await status_msg.edit(res_text)
    else:
        await status_msg.edit(f"<blockquote><b>{ggl_emo} ᴍᴀᴀꜰ ᴍᴜʀɪᴅᴋᴜ, sᴇʀᴠᴇʀ ɢᴜʀᴜ sᴇᴅᴀɴɢ ɢᴀɴɢɢᴜᴀɴ!</b></blockquote>")
        