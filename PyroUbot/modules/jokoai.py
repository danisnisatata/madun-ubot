import asyncio
import requests
from PyroUbot import *
from pyrogram.enums import ChatAction

__MODULE__ = "ᴊᴏᴋᴏ ᴀɪ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴊᴏᴋᴏ ᴀɪ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴊᴏᴋᴏ</code> [ᴘᴇʀᴛᴀɴʏᴀᴀɴ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴀɪ ᴜɴɪᴋ ʏᴀɴɢ ᴍᴇɴᴊᴀᴡᴀʙ ᴅᴇɴɢᴀɴ ʙᴀʜᴀsᴀ ᴊᴀᴡᴀ.</blockquote>
"""

@PY.UBOT("joko")
async def joko_ai_handler(client, message):
    prs_emo = await EMO.PROSES(client)
    ggl_emo = await EMO.GAGAL(client)
    
    args = get_arg(message)
    if not args:
        return await message.reply_text(
            f"<emoji id=5019523782004441717>❌</emoji> <b>ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ᴘᴇʀᴛᴀɴʏᴀᴀɴ!</b>\nᚗ ᴄᴏɴᴛᴏʜ: <code>.ᴊᴏᴋᴏ ᴘɪʏᴇ ᴋᴀʙᴀʀᴇ?</code>"
        )

    # Action ngetik & status proses (Pakai ID emoji premium lu)
    await client.send_chat_action(message.chat.id, ChatAction.TYPING)
    status_msg = await message.reply_text(f"<emoji id=5319230516929502602>🔍</emoji> <b>ᴊᴏᴋᴏ sᴇᴅᴀɴɢ ᴍɪᴋɪʀ...</b>")

    def fetch_joko():
        try:
            url = f'https://api.siputzx.my.id/api/ai/joko?content={args}'
            response = requests.get(url, timeout=20)
            return response.json()
        except:
            return None

    loop = asyncio.get_event_loop()
    res_json = await loop.run_in_executor(None, fetch_joko)

    if res_json and "data" in res_json:
        answer = res_json["data"]
        await status_msg.edit(
            f"<blockquote><b>🤖 ᴊᴏᴋᴏ ᴀɪ ʀᴇsᴘᴏɴsᴇ:</b>\n\n{answer}\n\n<b>ᚗ ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>"
        )
    else:
        await status_msg.edit(f"<blockquote><b>{ggl_emo} ɢᴀɢᴀʟ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ʀᴇsᴘᴏɴ ᴅᴀʀɪ ᴊᴏᴋᴏ ᴀɪ!</b></blockquote>")
        