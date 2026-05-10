import httpx
from pyrogram.enums import ChatAction
from PyroUbot import *

__MODULE__ = "ᴀɴsᴀʀɪ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀɴsᴀʀɪ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴀɴsᴀʀɪ</code> [ᴘᴇʀᴛᴀɴʏᴀᴀɴ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴀsɪsᴛᴇɴ ᴀɪ ɪsʟᴀᴍɪ ᴜɴᴛᴜᴋ ʙᴇʀᴛᴀɴʏᴀ sᴇᴘᴜᴛᴀʀ ᴀʏᴀᴛ ᴀʟ-ǫᴜʀ'ᴀɴ, ʜᴀᴅɪᴛs, ᴅᴀɴ ʜᴜᴋᴜᴍ ɪsʟᴀᴍ ʟᴀɪɴɴʏᴀ.</blockquote>
"""

@PY.UBOT("ansari")
@PY.TOP_CMD
async def ansari_handler(client, message):
    prs_emo = await EMO.PROSES(client)
    ggl_emo = await EMO.GAGAL(client)
    
    args = get_arg(message)
    if not args:
        return await message.reply_text(
            f"<blockquote><b>{ggl_emo} ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ᴘᴇʀᴛᴀɴʏᴀᴀɴ!</b>\nᚗ ᴄᴏɴᴛᴏʜ: <code>.ᴀɴsᴀʀɪ ᴀᴘᴀ ɪᴛᴜ ᴛᴀᴜʜɪᴅ?</code></blockquote>"
        )

    status_msg = await message.reply_text(f"<blockquote><b>😇 sᴇᴅᴀɴɢ ᴍᴇɴᴄᴀʀɪ ʀᴇꜰᴇʀᴇɴsɪ...</b></blockquote>")
    await client.send_chat_action(message.chat.id, ChatAction.TYPING)

    api_url = f"https://fastrestapis.fasturl.cloud/aillm/islamic?ask={args}"

    try:
        async with httpx.AsyncClient() as session:
            response = await session.get(api_url, timeout=60) # Timeout lebih lama untuk AI
            if response.status_code != 200:
                return await status_msg.edit(f"<blockquote><b>{ggl_emo} sᴇʀᴠᴇʀ ᴀɴsᴀʀɪ sᴇᴅᴀɴɢ sɪʙᴜᴋ, ᴄᴏʙᴀ ʟᴀɢɪ ɴᴀɴᴛɪ.</b></blockquote>")
            
            data = response.json()
            if "result" in data:
                res_text = (
                    f"<blockquote>{data['result']}</blockquote>\n"
                    f"<b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ"
                )
                await status_msg.edit(res_text)
            else:
                await status_msg.edit(f"<blockquote><b>{ggl_emo} ɢᴀɢᴀʟ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ᴊᴀᴡᴀʙᴀɴ ᴅᴀʀɪ ᴀɴsᴀʀɪ.</b></blockquote>")
                
    except Exception as e:
        await status_msg.edit(f"<blockquote><b>{ggl_emo} ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ:</b>\n<code>{str(e)}</code></blockquote>")
        