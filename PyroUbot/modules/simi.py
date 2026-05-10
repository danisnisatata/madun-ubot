import requests
from PyroUbot import *
from pyrogram.enums import ChatAction

__MODULE__ = "sɪᴍɪ ᴀɪ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sɪᴍɪ ᴀɪ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}sɪᴍɪ</code> [ᴘᴇʀᴛᴀɴʏᴀᴀɴ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴɢᴏʙʀᴏʟ sᴀɴᴛᴀɪ sᴀᴍᴀ sɪᴍɪ, ᴛᴀᴘɪ ʜᴀᴛɪ-ʜᴀᴛɪ ᴅɪᴀ ᴀɢᴀᴋ ᴛᴏxɪᴄ.</blockquote>
"""

@PY.UBOT("simi")
@PY.TOP_CMD
async def simi_chat(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    
    args = get_arg(message)
    if not args:
        return await message.reply_text(
            f"<blockquote><b>{ggl} ʜᴀʀᴀᴘ ᴍᴀsᴜᴋᴋᴀɴ ᴘᴇsᴀɴ!\nᴄᴏɴᴛᴏʜ: <code>.sɪᴍɪ</code> ʜᴀʟᴏ ᴀsᴜ</b></blockquote>"
        )

    await client.send_chat_action(message.chat.id, ChatAction.TYPING)
    status_msg = await message.reply_text(f"<blockquote><b>{prs} sɪᴍɪ sᴇᴅᴀɴɢ ᴍᴇɴɢᴇᴛɪᴋ...</b></blockquote>")

    try:
        url = f"https://api.botcahx.eu.org/api/search/simsimi?query={args}&apikey=@iqbalnew77"
        response = requests.get(url).json()

        if response.get("status") and "result" in response:
            result_text = response["result"]
            await status_msg.edit(f"<blockquote>{result_text}</blockquote>")
        else:
            await status_msg.edit(f"<blockquote><b>{ggl} sɪᴍɪ ʟᴀɢɪ sᴀʀɪᴀᴡᴀɴ, ɢᴀᴋ ʙɪsᴀ ᴊᴀᴡᴀʙ.</b></blockquote>")
            
    except Exception as e:
        await status_msg.edit(f"<blockquote><b>{ggl} ᴇʀʀᴏʀ:</b> <code>{str(e)}</code></blockquote>")
        