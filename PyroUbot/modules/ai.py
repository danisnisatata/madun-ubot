import httpx
from pyrogram.enums import ChatAction
from PyroUbot import *

__MODULE__ = "ᴀɪ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀɪ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴀɪ</code> [ᴘᴇʀᴛᴀɴʏᴀᴀɴ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴀsɪsᴛᴇɴ ᴄᴇʀᴅᴀs ʙᴇʀʙᴀsɪs ᴏᴘᴇɴᴀɪ ᴜɴᴛᴜᴋ ᴍᴇɴᴊᴀᴡᴀʙ sᴇɢᴀʟᴀ ᴘᴇʀᴛᴀɴʏᴀᴀɴ ᴀɴᴅᴀ.</blockquote>
"""

@PY.UBOT("ai")
@PY.TOP_CMD
async def chat_gpt_handler(client, message):
    prs_emo = await EMO.PROSES(client)
    ggl_emo = await EMO.GAGAL(client)
    
    args = get_arg(message)
    if not args:
        return await message.reply_text(
            f"<blockquote><b>{ggl_emo} ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ᴘᴇʀᴛᴀɴʏᴀᴀɴ!</b>\nᚗ ᴄᴏɴᴛᴏʜ: <code>.ᴀɪ ᴀᴘᴀ ɪᴛᴜ ᴘʏᴛʜᴏɴ?</code></blockquote>"
        )

    status_msg = await message.reply_text(f"<blockquote><b>{prs_emo} sᴇᴅᴀɴɢ ʙᴇʀᴘɪᴋɪʀ...</b></blockquote>")
    await client.send_chat_action(message.chat.id, ChatAction.TYPING)

    api_url = f"https://api.botcahx.eu.org/api/search/openai-chat?text={args}&apikey=bEcJ8rQU"

    try:
        async with httpx.AsyncClient() as session:
            response = await session.get(api_url, timeout=30)
            if response.status_code != 200:
                return await status_msg.edit(f"<blockquote><b>{ggl_emo} sᴇʀᴠᴇʀ ᴀɪ sᴇᴅᴀɴɢ sɪʙᴜᴋ, ᴄᴏʙᴀ ʟᴀɢɪ ɴᴀɴᴛɪ.</b></blockquote>")
            
            data = response.json()
            if "message" in data:
                res_text = (
                    f"<blockquote>{data['message']}</blockquote>\n"
                    f"<b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ"
                )
                await status_msg.edit(res_text)
            else:
                await status_msg.edit(f"<blockquote><b>{ggl_emo} ɢᴀɢᴀʟ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ʀᴇsᴘᴏɴ ᴅᴀʀɪ ᴀɪ.</b></blockquote>")
                
    except Exception as e:
        await status_msg.edit(f"<blockquote><b>{ggl_emo} ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ:</b>\n<code>{str(e)}</code></blockquote>")

@PY.BOT("ai")
async def chat_gpt_bot(client, message):
    args = get_arg(message)
    if not args:
        return await message.reply_text("<b>ᚗ ɢᴜɴᴀᴋᴀɴ ꜰᴏʀᴍᴀᴛ: /ᴀɪ [ᴘᴇʀᴛᴀɴʏᴀᴀɴ]</b>")
    
    status_msg = await message.reply_text("<code>🔍 sᴇᴅᴀɴɢ ᴍᴇɴᴄᴀʀɪ ᴊᴀᴡᴀʙᴀɴ...</code>")
    api_url = f"https://api.botcahx.eu.org/api/search/openai-chat?text={args}&apikey=bEcJ8rQU"
    
    try:
        async with httpx.AsyncClient() as session:
            response = await session.get(api_url, timeout=30)
            data = response.json()
            if "message" in data:
                await status_msg.edit(f"<blockquote>{data['message']}</blockquote>")
            else:
                await status_msg.edit("<b>ᚗ ɢᴀɢᴀʟ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ᴊᴀᴡᴀʙᴀɴ.</b>")
    except:
        await status_msg.edit("<b>ᚗ ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ sɪsᴛᴇᴍ.</b>")
        