import asyncio
from pyrogram.enums import ChatMemberStatus
from PyroUbot import *

__MODULE__ = "ᴀɴᴀʟʏᴢᴇʀ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀɴᴀʟʏᴢᴇʀ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴀɴᴀʟʏᴢᴇ</code>

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴀɴᴀʟɪsɪs ᴍᴇɴᴅᴀʟᴀᴍ ᴛᴇʀʜᴀᴅᴀᴘ sᴛᴀᴛɪsᴛɪᴋ ᴀɴɢɢᴏᴛᴀ ᴅɪ ᴅᴀʟᴀᴍ ɢʀᴜᴘ ᴀᴛᴀᴜ ᴄʜᴀɴɴᴇʟ.</blockquote>
"""

@PY.UBOT("analyze")
@PY.TOP_CMD
async def analyze_handler(client, message):
    prs_emo = await EMO.PROSES(client)
    brhsl_emo = await EMO.BERHASIL(client)
    ggl_emo = await EMO.GAGAL(client)
    
    status_msg = await message.reply_text(
        f"<blockquote><b>{prs_emo} ᴍᴇᴍᴜʟᴀɪ ᴀɴᴀʟɪsɪs ᴄʜᴀᴛ...</b>\n"
        "<i>ᴍᴏʜᴏɴ ᴛᴜɴɢɢᴜ, sᴇᴅᴀɴɢ ᴍᴇᴍɪɴᴅᴀɪ sᴇʟᴜʀᴜʜ ᴀɴɢɢᴏᴛᴀ.</i></blockquote>"
    )
    
    chat_id = message.chat.id
    admins = 0
    bots = 0
    deleted = 0
    total = 0

    try:
        async for member in client.get_chat_members(chat_id):
            total += 1
            if member.user.is_deleted:
                deleted += 1
            elif member.user.is_bot:
                bots += 1
            if member.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
                admins += 1

        # Menghitung persentase akun terhapus (ghost)
        ghost_rate = (deleted / total * 100) if total > 0 else 0

        hasil = (
            f"<blockquote><b>📊 ʜᴀsɪʟ ᴀɴᴀʟɪsɪs ᴄʜᴀᴛ</b>\n\n"
            f"<b>ᚗ ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀ :</b> <code>{total}</code>\n"
            f"<b>ᚗ ᴀᴅᴍɪɴ :</b> <code>{admins}</code>\n"
            f"<b>ᚗ ʙᴏᴛ :</b> <code>{bots}</code>\n"
            f"<b>ᚗ ᴀᴋᴜɴ ᴛᴇʀʜᴀᴘᴜs :</b> <code>{deleted}</code> (<i>{ghost_rate:.1f}%</i>)\n\n"
            f"<b>💡 sᴀʀᴀɴ ɪǫʙᴀʟ :</b>\n"
            f"<i>ᴊɪᴋᴀ ᴀᴋᴜɴ ᴛᴇʀʜᴀᴘᴜs ᴍᴇɴᴄᴀᴘᴀɪ 𝟷𝟶%, sᴇɢᴇʀᴀ ɢᴜɴᴀᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ .ᴢᴏᴍʙɪᴇs ᴜɴᴛᴜᴋ ᴍᴇɴᴊᴀɢᴀ ᴋᴇᴀᴍᴀɴᴀɴ ɢʀᴜᴘ ᴀɴᴅᴀ.</i>\n\n"
            f"<b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>"
        )
        await status_msg.edit(hasil)

    except Exception as e:
        await status_msg.edit(f"<blockquote><b>{ggl_emo} ɢᴀɢᴀʟ ᴍᴇɴɢᴀɴᴀʟɪsɪs</b>\n<code>{str(e)}</code></blockquote>")
        