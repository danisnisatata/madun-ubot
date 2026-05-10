import asyncio
import requests
from PyroUbot import *

__MODULE__ = "ʟᴜᴍɪɴᴀɪ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʟᴜᴍɪɴᴀɪ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ʟᴜᴍɪɴ</code> [ᴘᴇʀᴛᴀɴʏᴀᴀɴ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴛᴀɴʏᴀ ᴊᴀᴡᴀʙ ᴅᴇɴɢᴀɴ ᴀɪ ʟᴜᴍɪɴ sᴇᴄᴀʀᴀ ᴏᴛᴏᴍᴀᴛɪs.</blockquote>
"""

@PY.UBOT("lumin")
async def lumin_ai_handler(client, message):
    prs_emo = await EMO.PROSES(client)
    ggl_emo = await EMO.GAGAL(client)
    
    args = get_arg(message)
    if not args:
        return await message.reply_text(
            f"<emoji id=5019523782004441717>❌</emoji> <b>ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ᴘᴇʀᴛᴀɴʏᴀᴀɴ!</b>\nᚗ ᴄᴏɴᴛᴏʜ: <code>.ʟᴜᴍɪɴ ʜᴀʟᴏ</code>"
        )

    # Status awal pake ID Emoji Premium lu
    status_msg = await message.reply_text(f"<emoji id=5319230516929502602>🔍</emoji> <b>sᴇᴅᴀɴɢ ᴍᴇɴᴊᴀᴡᴀʙ...</b>")

    def fetch_ai():
        try:
            url = f'https://api.diioffc.web.id/api/ai/luminai?query={args}'
            return requests.get(url, timeout=20).json()
        except:
            return None

    loop = asyncio.get_event_loop()
    data = await loop.run_in_executor(None, fetch_ai)

    if data and "result" in data and "message" in data["result"]:
        answer = data["result"]["message"]
        res = f"""
<blockquote><b>🤖 ʟᴜᴍɪɴ ᴀɪ ʀᴇsᴘᴏɴsᴇ:</b>

{answer}

<b>ᚗ ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>"""
        await status_msg.edit(res)
    else:
        await status_msg.edit(f"<blockquote><b>{ggl_emo} ɢᴀɢᴀʟ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ʀᴇsᴘᴏɴ ᴅᴀʀɪ sᴇʀᴠᴇʀ ʟᴜᴍɪɴᴀɪ!</b></blockquote>")
        