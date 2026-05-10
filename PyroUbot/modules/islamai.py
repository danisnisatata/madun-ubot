import asyncio
import requests
from PyroUbot import *
from pyrogram.enums import ChatAction

__MODULE__ = "ɪsʟᴀᴍ ᴀɪ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɪsʟᴀᴍ ᴀɪ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ɪsʟᴀᴍᴀɪ</code> [ᴘᴇʀᴛᴀɴʏᴀᴀɴ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴀɪ ᴋʜᴜsᴜs ᴜɴᴛᴜᴋ ʙᴇʀᴛᴀɴʏᴀ sᴇᴘᴜᴛᴀʀ ᴀɢᴀᴍᴀ ɪsʟᴀᴍ.</blockquote>
"""

@PY.UBOT("islamai")
async def islam_ai_handler(client, message):
    prs_emo = await EMO.PROSES(client)
    ggl_emo = await EMO.GAGAL(client)
    
    args = get_arg(message)
    if not args:
        return await message.reply_text(
            f"<emoji id=5019523782004441717>❌</emoji> <b>ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ᴘᴇʀᴛᴀɴʏᴀᴀɴ!</b>\nᚗ ᴄᴏɴᴛᴏʜ: <code>.ɪsʟᴀᴍᴀɪ ᴀsᴀʟ ᴜsᴜʟ ᴀʟ-ǫᴜʀᴀɴ</code>"
        )

    # Action ngetik & status proses (Pakai ID emoji premium pilihan lu)
    await client.send_chat_action(message.chat.id, ChatAction.TYPING)
    status_msg = await message.reply_text(f"<emoji id=4943239162758169437>🤩</emoji> <b>sᴇᴅᴀɴɢ ᴍᴇɴᴄᴀʀɪ ᴊᴀᴡᴀʙᴀɴ...</b>")

    def fetch_islam_ai():
        try:
            url = f'https://vapis.my.id/api/islamai?q={args}'
            response = requests.get(url, timeout=30)
            return response.json()
        except:
            return None

    loop = asyncio.get_event_loop()
    res_json = await loop.run_in_executor(None, fetch_islam_ai)

    if res_json and "result" in res_json:
        answer = res_json["result"]
        await status_msg.edit(
            f"<blockquote><b>☪️ ɪsʟᴀᴍ ᴀɪ ʀᴇsᴘᴏɴsᴇ:</b>\n\n{answer}\n\n<b>ᚗ ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>"
        )
    else:
        await status_msg.edit(f"<blockquote><b>{ggl_emo} ɢᴀɢᴀʟ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ᴊᴀᴡᴀʙᴀɴ ᴅᴀʀɪ sᴇʀᴠᴇʀ ɪsʟᴀᴍ ᴀɪ!</b></blockquote>")
        