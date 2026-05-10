from pyrogram.errors import UsernameNotOccupied, UserNotParticipant, PeerIdInvalid
from PyroUbot import *

__MODULE__ = "ɢᴇᴛ ᴘᴘ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɢᴇᴛ ᴘᴘ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ɢᴇᴛᴘᴘ</code> [ʀᴇᴘʟʏ/ᴜsᴇʀ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴɢᴀᴍʙɪʟ ꜰᴏᴛᴏ ᴘʀᴏꜰɪʟ ᴘᴇɴɢɢᴜɴᴀ, ɢʀᴜᴘ, ᴀᴛᴀᴜ ᴄʜᴀɴɴᴇʟ.</blockquote>
"""

@PY.UBOT("getpp|getprofile")
@PY.TOP_CMD
async def get_profile_pic_handler(client, message):
    prs_emo = await EMO.PROSES(client)
    brhsl_emo = await EMO.BERHASIL(client)
    ggl_emo = await EMO.GAGAL(client)
    
    # Deteksi target secara otomatis
    target = None
    if message.reply_to_message:
        target = message.reply_to_message.from_user.id if message.reply_to_message.from_user else message.reply_to_message.sender_chat.id
    elif len(message.command) > 1:
        target = message.command[1]
    else:
        target = message.chat.id

    status_msg = await message.reply_text(f"<blockquote><b>{prs_emo} sᴇᴅᴀɴɢ ᴍᴇɴɢᴀᴍʙɪʟ ꜰᴏᴛᴏ ᴘʀᴏꜰɪʟ...</b></blockquote>")

    try:
        has_photo = False
        async for photo in client.get_chat_photos(target, limit=1):
            has_photo = True
            await client.send_photo(
                message.chat.id,
                photo=photo.file_id,
                caption=f"<blockquote><b>{brhsl_emo} ꜰᴏᴛᴏ ᴘʀᴏꜰɪʟ ʙᴇʀʜᴀsɪʟ ᴅɪᴀᴍʙɪʟ!</b>\n\n<b>ᚗ ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>",
                reply_to_message_id=message.id
            )
            await status_msg.delete()
            break

        if not has_photo:
            await status_msg.edit(f"<blockquote><b>{ggl_emo} ᴛᴀʀɢᴇᴛ ᴛɪᴅᴀᴋ ᴍᴇᴍɪʟɪᴋɪ ꜰᴏᴛᴏ ᴘʀᴏꜰɪʟ!</b></blockquote>")

    except (UsernameNotOccupied, UserNotParticipant, PeerIdInvalid):
        await status_msg.edit(f"<blockquote><b>{ggl_emo} ᴀᴋᴜɴ ᴀᴛᴀᴜ ɢʀᴜᴘ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ!</b></blockquote>")
    except Exception as e:
        await status_msg.edit(f"<blockquote><b>{ggl_emo} ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ:</b>\n<code>{str(e)}</code></blockquote>")
        