import asyncio
import requests
from PyroUbot import *
from pyrogram.enums import ChatAction

__MODULE__ = "ʟᴀᴛᴜᴋᴀᴍ ᴀɪ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʟᴀᴛᴜᴋᴀᴍ ᴀɪ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ʟᴀᴛᴜᴋᴀᴍ</code> [ᴘᴇʀᴛᴀɴʏᴀᴀɴ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ɴɢᴏʙʀᴏʟ sᴀᴍᴀ ᴀɪ ʟᴀᴛᴜᴋᴀᴍ ʏᴀɴɢ ᴀɢᴀᴋ ᴛᴏxɪᴄ ᴅᴀɴ ᴋᴏᴄᴀᴋ.</blockquote>
"""

@PY.UBOT("latukam")
async def latukam_ai_handler(client, message):
    prs_emo = await EMO.PROSES(client)
    ggl_emo = await EMO.GAGAL(client)
    
    args = get_arg(message)
    if not args:
        return await message.reply_text(
            f"<emoji id=5019523782004441717>❌</emoji> <b>ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ᴘᴇʀᴛᴀɴʏᴀᴀɴ!</b>\nᚗ ᴄᴏɴᴛᴏʜ: <code>.ʟᴀᴛᴜᴋᴀᴍ sɪᴀᴘᴀ ʟᴜ?</code>"
        )

    # Kirim action ngetik & status proses (Pakai ID emoji premium lu)
    await client.send_chat_action(message.chat.id, ChatAction.TYPING)
    status_msg = await message.reply_text(f"<emoji id=6260400955498435049>🌎</emoji> <b>ʟᴀᴛᴜᴋᴀᴍ sᴇᴅᴀɴɢ ᴍɪᴋɪʀ...</b>")

    def fetch_latukam():
        try:
            url = f'https://api.siputzx.my.id/api/ai/latukam?content={args}'
            response = requests.get(url, timeout=20)
            return response.json()
        except:
            return None

    loop = asyncio.get_event_loop()
    res_json = await loop.run_in_executor(None, fetch_latukam)

    if res_json and "data" in res_json:
        answer = res_json["data"]
        await status_msg.edit(
            f"<blockquote><b>🤖 ʟᴀᴛᴜᴋᴀᴍ ʀᴇsᴘᴏɴsᴇ:</b>\n\n{answer}\n\n<b>ᚗ ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>"
        )
    else:
        await status_msg.edit(f"<blockquote><b>{ggl_emo} ɢᴀɢᴀʟ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ʀᴇsᴘᴏɴ ᴅᴀʀɪ sᴇʀᴠᴇʀ ʟᴀᴛᴜᴋᴀᴍ!</b></blockquote>")
        