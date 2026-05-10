from PyroUbot import *
from pyrogram.types import EmojiStatus

__MODULE__ = "sᴇᴛᴇᴍᴏ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴇᴛᴇᴍᴏ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}sᴇᴛᴇᴍᴏ</code> [ʀᴇᴘʟʏ ᴇᴍᴏᴊɪ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴɢɢᴀɴᴛɪ ᴇᴍᴏᴊɪ sᴛᴀᴛᴜs ᴀᴋᴜɴ ʟᴜ ᴅᴇɴɢᴀɴ ᴍᴇᴍʙᴀʟᴀs ᴘᴇsᴀɴ ʏᴀɴɢ ʙᴇʀɪsɪ ᴄᴜsᴛᴏᴍ ᴇᴍᴏᴊɪ.</blockquote>
"""

@PY.UBOT("setemo")
@PY.TOP_CMD
async def set_emoji_handler(client, message):
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)
    
    target = message.reply_to_message
    if not target or not target.entities:
        return await message.reply_text(
            f"<blockquote><b>{ggl} ᴍᴏʜᴏɴ ʙᴀʟᴀs ᴋᴇ ᴘᴇsᴀɴ ʏᴀɴɢ ʙᴇʀɪsɪ ᴄᴜsᴛᴏᴍ ᴇᴍᴏᴊɪ!</b></blockquote>"
        )

    try:
        custom_emoji_id = None
        for entity in target.entities:
            if entity.custom_emoji_id:
                custom_emoji_id = entity.custom_emoji_id
                break
        
        if not custom_emoji_id:
            return await message.reply_text(f"<blockquote><b>{ggl} ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴄᴜsᴛᴏᴍ ᴇᴍᴏᴊɪ ʏᴀɴɢ ᴅɪᴛᴇᴍᴜᴋᴀɴ.</b></blockquote>")

        success = await client.set_emoji_status(EmojiStatus(custom_emoji_id=custom_emoji_id))
        
        if success:
            await message.reply_text(
                f"<blockquote><b>{brhsl} ᴇᴍᴏᴊɪ sᴛᴀᴛᴜs ʙᴇʀʜᴀsɪʟ ᴅɪɢᴀɴᴛɪ!</b>\n"
                f"ᚗ ᴇᴍᴏᴊɪ : <emoji id={custom_emoji_id}>{target.text[:1] if target.text else '⭐'}</emoji></blockquote>"
            )
                    
    except Exception as e:
        await message.reply_text(f"<blockquote><b>{ggl} ᴇʀʀᴏʀ:</b> <code>{str(e)}</code></blockquote>")
        