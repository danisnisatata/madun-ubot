import os
import requests
import asyncio
from PyroUbot import *
from pyrogram.enums import ChatAction

__MODULE__ = "ᴏᴘᴇɴᴀɪ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴏᴘᴇɴᴀɪ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴀɪ</code> [ᴘᴇʀᴛᴀɴʏᴀᴀɴ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴛᴀɴʏᴀ ᴀᴘᴀ sᴀᴊᴀ ᴋᴇ ᴀɪ (ᴄʜᴀᴛɢᴘᴛ) sᴇᴄᴀʀᴀ ᴏᴛᴏᴍᴀᴛɪs.</blockquote>
"""

@PY.UBOT("ai")
async def chat_gpt_handler(client, message):
    prs_emo = await EMO.PROSES(client)
    ggl_emo = await EMO.GAGAL(client)
    
    args = get_arg(message)
    if not args:
        return await message.reply_text(
            f"<blockquote><b>{ggl_emo} ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ᴘᴇʀᴛᴀɴʏᴀᴀɴ!</b>\nᚗ ᴄᴏɴᴛᴏʜ: <code>.ᴀɪ ᴀᴘᴀ ɪᴛᴜ ᴜsᴇʀʙᴏᴛ?</code></blockquote>"
        )

    # Efek ngetik biar keren
    await client.send_chat_action(message.chat.id, ChatAction.TYPING)
    status_msg = await message.reply_text(f"<blockquote><b>{prs_emo} sᴇᴅᴀɴɢ ᴍᴇɴᴄᴀʀɪ ᴊᴀᴡᴀʙᴀɴ...</b></blockquote>")

    # Menggunakan loop.run_in_executor agar requests tidak blocking
    def get_ai_response():
        api_key = os.getenv("API_KEY") or "@iqbalnew77" # Fallback apikey lu
        url = f'https://api.botcahx.eu.org/api/search/gpt?text={args}&apikey={api_key}'
        try:
            response = requests.get(url, timeout=30)
            return response.json()
        except:
            return None

    loop = asyncio.get_event_loop()
    res_json = await loop.run_in_executor(None, get_ai_response)

    if res_json and res_json.get("status"):
        answer = res_json.get("message")
        await status_msg.edit(
            f"<blockquote><b>🤖 ᴀɪ ʀᴇsᴘᴏɴsᴇ:</b>\n\n{answer}\n\n<b>ᚗ ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>"
        )
    else:
        await status_msg.edit(f"<blockquote><b>{ggl_emo} ɢᴀɢᴀʟ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ʀᴇsᴘᴏɴ ᴅᴀʀɪ sᴇʀᴠᴇʀ!</b></blockquote>")
        