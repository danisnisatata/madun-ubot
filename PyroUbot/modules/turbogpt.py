from PyroUbot import *
import random
import requests
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from pyrogram.types import Message

__MODULE__ = "ᴛᴜʀʙᴏ ɢᴘᴛ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴛᴜʀʙᴏ ɢᴘᴛ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴛᴜʀʙᴏ</code> [ǫᴜᴇʀʏ]
ᚗ <code>{0}ᴄʟᴀᴜᴅᴇ</code> [ǫᴜᴇʀʏ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴀɪ ʏᴀɴɢ ᴍᴇɴᴊᴀᴡᴀʙ ᴘᴇʀᴛᴀɴʏᴀᴀɴ ᴍᴜ ᴅᴇɴɢᴀɴ ᴄᴇᴘᴀᴛ ᴅᴀɴ ᴀᴋᴜʀᴀᴛ.</blockquote>
"""

@PY.UBOT("turbo|claude")
@PY.TOP_CMD
async def chat_gpt(client, message):
    try:
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            return await message.reply_text(
                "<blockquote><b><emoji id=5019523782004441717>❌</emoji> ᴍᴏʜᴏɴ ɢᴜɴᴀᴋᴀɴ ꜰᴏʀᴍᴀᴛ:\nᴄᴏɴᴛᴏʜ : <code>.ᴛᴜʀʙᴏ</code> [ᴘᴇʀᴛᴀɴʏᴀᴀɴ]</b></blockquote>"
            )
        
        prs = await message.reply_text("<blockquote><b><emoji id=6226405134004389590>🔍</emoji> ᴛᴜʀʙᴏ sᴇᴅᴀɴɢ ᴍᴇɴᴊᴀᴡᴀʙ...</b></blockquote>")
        query = message.text.split(' ', 1)[1]
        
        # Request ke API
        response = requests.get(f'https://vapis.my.id/api/turbov1?q={query}')
        data = response.json()

        if data.get("status") and "result" in data:
            result_text = data["result"]                  
            await prs.edit(f"<blockquote>{result_text}</blockquote>")
        else:
            await prs.edit("<blockquote><b>❌ ɢᴀɢᴀʟ ᴍᴇɴɢᴀᴍʙɪʟ ʀᴇsᴘᴏɴ ᴅᴀʀɪ ᴀɪ.</b></blockquote>")
            
    except Exception as e:
        await message.reply_text(f"<blockquote><b>⚠️ ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ:</b>\n<code>{str(e)}</code></blockquote>")
        