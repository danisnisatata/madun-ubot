import asyncio
import requests
from PyroUbot import *
from pyrogram.enums import ChatAction

__MODULE__ = "ᴋᴏᴅᴇ ᴘᴏs"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴋᴏᴅᴇ ᴘᴏs ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴋᴅᴘs</code> [ɴᴀᴍᴀ ᴅᴇsᴀ/ᴅᴀᴇʀᴀʜ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴᴄᴀʀɪ ɪɴꜰᴏʀᴍᴀsɪ ᴋᴏᴅᴇ ᴘᴏs sᴜᴀᴛᴜ ᴅᴀᴇʀᴀʜ sᴇᴄᴀʀᴀ ᴏᴛᴏᴍᴀᴛɪs.</blockquote>
"""

@PY.UBOT("kdps")
async def kodepos_handler(client, message):
    prs_emo = await EMO.PROSES(client)
    ggl_emo = await EMO.GAGAL(client)
    
    args = get_arg(message)
    if not args:
        return await message.reply_text(
            f"<emoji id=5019523782004441717>❌</emoji> <b>ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ɴᴀᴍᴀ ᴅᴇsᴀ!</b>\nᚗ ᴄᴏɴᴛᴏʜ: <code>.ᴋᴅᴘs ᴍᴀʀɢᴀʜᴀʏᴜ</code>"
        )

    # Action ngetik & status proses (Pakai ID emoji premium lu)
    await client.send_chat_action(message.chat.id, ChatAction.TYPING)
    status_msg = await message.reply_text(f"<emoji id=5319230516929502602>🔍</emoji> <b>sᴇᴅᴀɴɢ ᴍᴇɴᴄᴀʀɪ...</b>")

    def fetch_kodepos():
        try:
            url = f'https://api.botcahx.eu.org/api/search/kodepos?query={args}&apikey=@iqbalnew77'
            response = requests.get(url, timeout=20)
            return response.json()
        except:
            return None

    loop = asyncio.get_event_loop()
    res_json = await loop.run_in_executor(None, fetch_kodepos)

    if res_json and "result" in res_json:
        data = res_json["result"]
        # Jika data berupa list, kita rapihin tampilannya
        if isinstance(data, list):
            res_text = ""
            for item in data:
                res_text += f"ᚗ <code>{item}</code>\n"
        else:
            res_text = data

        await status_msg.edit(
            f"<blockquote><b>📍 ɪɴꜰᴏʀᴍᴀsɪ ᴋᴏᴅᴇ ᴘᴏs:</b>\n\n{res_text}\n\n<b>ᚗ ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>"
        )
    else:
        await status_msg.edit(f"<blockquote><b>{ggl_emo} ᴋᴏᴅᴇ ᴘᴏs ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ ᴀᴛᴀᴜ API ᴇʀʀᴏʀ!</b></blockquote>")
        