
import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message
from PyroUbot.core.helpers.msg_type import ReplyCheck
from PyroUbot import *

@ubot.on_message(filters.command("unprem") & filters.me)
async def jwbsalamlngkp(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "ᴍᴀsᴜᴋᴀɴ ɪᴅ / ᴜsᴇʀɴᴀᴍᴇ ᴘᴇɴɢɢᴜɴᴀ",
            reply_to_message_id=ReplyCheck(message),
        ),
    )

__MODULE__ = "ʙʀᴏᴀᴅᴄᴀsᴛ ʙᴏᴛ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ʙʀᴏᴀᴅᴄᴀsᴛ ʙᴏᴛ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>/ʙᴄ</code> [ʀᴇᴘʟʏ ᴘᴇsᴀɴ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴɢɪʀɪᴍ ᴘᴇsᴀɴ ᴋᴇ sᴇʟᴜʀᴜʜ ᴜsᴇʀ ʙᴏᴛ ᴅᴀɴ sᴇʟᴜʀᴜʜ ᴀᴋᴜɴ ᴜsᴇʀʙᴏᴛ.</blockquote>
"""

@PY.BOT("bc")
@PY.OWNER
async def broadcast_bot(client, message):
    if not message.reply_to_message:
        return await message.reply("<b>⌭ ᴍᴏʜᴏɴ ʙᴀʟᴀs ᴘᴇsᴀɴ ʏᴀɴɢ ɪɴɢɪɴ ᴅɪʙʀᴀᴅᴄᴀsᴛ!</b>", quote=True)

    msg = await message.reply("<b>⌭ sᴇᴅᴀɴɢ ᴍᴇʟᴀᴋᴜᴋᴀɴ ʙʀᴏᴀᴅᴄᴀsᴛ ʜʏʙʀɪᴅ...</b>", quote=True)
    
    done_users = 0
    done_ubots = 0
    failed = 0

    # 1. BROADCAST KE USER DATABASE (YANG /START BOT)
    served_users = await get_served_users()
    if served_users:
        for user in served_users:
            try:
                await message.reply_to_message.forward(user['user_id'])
                done_users += 1
                await asyncio.sleep(0.1)
            except Exception:
                failed += 1

    # 2. BROADCAST KE SEMUA AKUN UBOT (YANG PASANG)
    for x in ubot._ubot:
        try:
            # Kirim ke ID masing-masing ubot
            await message.reply_to_message.forward(x.me.id)
            done_ubots += 1
            await asyncio.sleep(0.1)
        except Exception:
            failed += 1

    # JIKA KEDUANYA KOSONG
    if done_users == 0 and done_ubots == 0:
        return await msg.edit("<b>❌ ɢᴀɢᴀʟ! ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴛᴀʀɢᴇᴛ ʙʀᴏᴀᴅᴄᴀsᴛ sᴀᴍᴀ sᴇᴋᴀʟɪ.</b>")

    # 3. LAPORAN KOMPLIT
    return await msg.edit(
        f"<blockquote><b>⦪ ʙʀᴏᴀᴅᴄᴀsᴛ sᴇʟᴇsᴀɪ ⦫</b>\n\n"
        f"<b>ᚗ ᴜsᴇʀ ʙᴏᴛ :</b> <code>{done_users}</code>\n"
        f"<b>ᚗ ᴀᴋᴜɴ ᴜʙᴏᴛ :</b> <code>{done_ubots}</code>\n"
        f"<b>ᚗ ɢᴀɢᴀʟ :</b> <code>{failed}</code>\n\n"
        f"<b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ : ɪǫʙᴀʟ ᴜʙᴏᴛ</b></blockquote>"
    )