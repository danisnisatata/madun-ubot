from PyroUbot import *
import random
import requests
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from pyrogram.types import Message

__MODULE__ = "ʏᴏᴜsᴇᴀʀᴄʜ ᴀɪ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʏᴏᴜsᴇᴀʀᴄʜ ᴀɪ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ʏᴏᴜsᴇᴀʀᴄʜ</code> [ǫᴜᴇʀʏ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴀɪ ʏᴀɴɢ ᴍᴇɴᴊᴀᴡᴀʙ ᴘᴇʀᴛᴀɴʏᴀᴀɴ ᴍᴜ ʟᴇʙɪʜ ʟᴇɴɢᴋᴀᴘ ᴅᴀɴ ᴀᴋᴜʀᴀᴛ.</blockquote>
"""

@PY.UBOT("yousearch")
@PY.TOP_CMD
async def Boysz_gpt(client, message):
    try:
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            return await message.reply_text(
                "<blockquote><b><emoji id=5019523782004441717>❌</emoji> ᴍᴏʜᴏɴ ɢᴜɴᴀᴋᴀɴ ꜰᴏʀᴍᴀᴛ:\nᴄᴏɴᴛᴏʜ : <code>.ʏᴏᴜsᴇᴀʀᴄʜ</code> [ᴘᴇʀᴛᴀɴʏᴀᴀɴ]</b></blockquote>"
            )
        
        prs = await message.reply_text("<blockquote><b><emoji id=5319230516929502602>🔍</emoji> ᴘʀᴏᴄᴇssɪɴɢ....</b></blockquote>")
        a = message.text.split(' ', 1)[1]
        
        # Request ke API
        response = requests.get(f'https://api.siputzx.my.id/api/ai/yousearch?text={a}')
        data = response.json()

        if data.get("status") and "data" in data:
            result_text = data["data"]                  
            await prs.edit(f"<blockquote>{result_text}</blockquote>")
        else:
            await prs.edit("<blockquote><b>❌ ɢᴀɢᴀʟ ᴍᴇɴɢᴀᴍʙɪʟ ʀᴇsᴘᴏɴ ᴅᴀʀɪ ᴀɪ.</b></blockquote>")
            
    except Exception as e:
        await message.reply_text(f"<blockquote><b>⚠️ ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ:</b>\n<code>{str(e)}</code></blockquote>")
        