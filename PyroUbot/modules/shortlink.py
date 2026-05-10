import requests
from PyroUbot import *
from pyrogram.enums import ChatAction

__MODULE__ = "sʜᴏʀᴛ ʟɪɴᴋ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sʜᴏʀᴛ ʟɪɴᴋ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴛɪɴʏᴜʀʟ</code> [ʟɪɴᴋ]
ᚗ <code>{0}ʙɪᴛʟʏ</code> [ʟɪɴᴋ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇᴍᴘᴇʀᴘᴇɴᴅᴇᴋ ᴛᴀᴜᴛᴀɴ ᴜʀʟ ʏᴀɴɢ ᴘᴀɴᴊᴀɴɢ ᴍᴇɴᴊᴀᴅɪ sɪɴɢᴋᴀᴛ.</blockquote>
"""

async def get_shortlink(api_type, link):
    url = f"https://api.botcahx.eu.org/api/linkshort/{api_type}?link={link}&apikey=@iqbalnew77"
    try:
        res = requests.get(url).json()
        if res.get("status"):
            return res.get("result")
        return None
    except:
        return None

@PY.UBOT("tinyurl|bitly")
@PY.TOP_CMD
async def shortlink_handler(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)
    
    cmd = message.command[0].lower()
    args = get_arg(message)
    
    if not args:
        return await message.reply_text(
            f"<blockquote><b>{ggl} ʜᴀʀᴀᴘ ᴍᴀsᴜᴋᴋᴀɴ ᴛᴀᴜᴛᴀɴ!\nᴄᴏɴᴛᴏʜ: <code>.{cmd}</code> ʜᴛᴛᴘs://ɢᴏᴏɢʟᴇ.ᴄᴏᴍ</b></blockquote>"
        )

    await client.send_chat_action(message.chat.id, ChatAction.TYPING)
    status_msg = await message.reply_text(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇᴍᴘᴇʀᴘᴇɴᴅᴇᴋ ʟɪɴᴋ...</b></blockquote>")

    result = await get_shortlink(cmd, args)
    
    if result:
        await status_msg.edit(
            f"<blockquote><b>{brhsl} sʜᴏʀᴛʟɪɴᴋ ʙᴇʀʜᴀsɪʟ</b>\n\n"
            f"ᚗ ʀᴇsᴜʟᴛ : <code>{result}</code></blockquote>"
        )
    else:
        await status_msg.edit(f"<blockquote><b>{ggl} ɢᴀɢᴀʟ ᴍᴇᴍᴘᴇʀᴘᴇɴᴅᴇᴋ ᴛᴀᴜᴛᴀɴ. ᴄᴏʙᴀ ʟᴀɢɪ ɴᴀɴᴛɪ.</b></blockquote>")
        