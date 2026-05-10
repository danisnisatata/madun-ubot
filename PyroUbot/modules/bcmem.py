import asyncio
from PyroUbot import *

__MODULE__ = "ʙʀᴏᴀᴅᴄᴀsᴛ ᴍᴇᴍʙᴇʀ"
__HELP__ = """
<blockquote><b>ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʙʀᴏᴀᴅᴄᴀsᴛ</b>

ᴘᴇʀɪɴᴛᴀʜ:
<code>{0}ʙᴄᴍᴇᴍ</code> [ʀᴇᴘʟʏ ᴘᴇsᴀɴ/ᴍᴇᴅɪᴀ] → ʙʀᴏᴀᴅᴄᴀsᴛ ᴘᴇsᴀɴ ᴋᴇ sᴇᴍᴜᴀ ᴍᴇᴍʙᴇʀ ᴠɪᴀ ᴘᴍ.
<code>{0}sᴛᴏᴘʙᴄ</code> → ᴘᴇɴɢʜᴇɴᴛɪᴀɴ ᴘᴀᴋsᴀ ᴘʀᴏsᴇs ʙʀᴏᴀᴅᴄᴀsᴛ.</blockquote>
"""

# Dictionary untuk menyimpan task agar bisa dihentikan kapan saja
BC_RUNNING_TASKS = {}

@PY.UBOT("bcmem")
@PY.TOP_CMD
async def _(client, message):
    user_id = client.me.id
    
    if not message.reply_to_message:
        return await message.reply_text("<blockquote><b>❌ ɢᴀɢᴀʟ</b>\nʙᴀʟᴀs ᴋᴇ ᴘᴇsᴀɴ ᴀᴛᴀᴜ ᴍᴇᴅɪᴀ ʏᴀɴɢ ᴍᴀᴜ ᴅɪsᴇʙᴀʀ!</blockquote>")

    # Jika sudah ada BC yang jalan, jangan double proses
    if user_id in BC_RUNNING_TASKS:
        return await message.reply_text("<blockquote><b>⚠️ ᴘᴇʀɪɴɢᴀᴛᴀɴ</b>\nʙʀᴏᴀᴅᴄᴀsᴛ ᴍᴀsɪʜ ʙᴇʀᴊᴀʟᴀɴ. ɢᴜɴᴀᴋᴀɴ <code>.stopbc</code> ᴛᴇʀʟᴇʙɪʜ ᴅᴀʜᴜʟᴜ.</blockquote>")

    status_msg = await message.reply_text("<blockquote><b>📢 ᴍᴇᴍᴜʟᴀɪ ᴍᴀss-ᴍᴇssᴀɢᴇ ᴠɪᴀ ᴘᴍ...</b>\n<i>ᴘʀᴏsᴇs ᴀᴋᴀɴ ᴛᴇᴛᴇᴘ ᴊᴀʟᴀɴ ᴍᴇsᴋɪ ᴀᴘʟɪᴋᴀsɪ ᴅɪᴛᴜᴛᴜᴘ.</i></blockquote>")

    async def start_broadcast(client, message, status_msg):
        success = 0
        failed = 0
        try:
            # Ambil semua member dulu ke dalam list biar proses fetch chat members gak putus di tengah
            members = []
            async for member in client.get_chat_members(message.chat.id):
                if not member.user.is_bot and not member.user.is_self:
                    members.append(member.user.id)
            
            for target_id in members:
                # Cek jika task dibatalkan melalui .stopbc
                if user_id not in BC_RUNNING_TASKS:
                    break
                    
                try:
                    await message.reply_to_message.copy(target_id)
                    success += 1
                    # Delay 1.5 detik: Pas buat keamanan biar gak kena FloodWait tapi tetep kenceng
                    await asyncio.sleep(1.5) 
                except Exception:
                    failed += 1
                    continue
            
            await bot.send_message(
                user_id,
                f"<blockquote><b>✅ ʙʀᴏᴀᴅᴄᴀsᴛ sᴇʟᴇsᴀɪ</b>\n\n"
                f"<b>• ᴛᴀʀɢᴇᴛ:</b> <code>{success} ᴍᴇᴍʙᴇʀ</code>\n"
                f"<b>• ɢᴀɢᴀʟ:</b> <code>{failed} ᴍᴇᴍʙᴇʀ</code>\n\n"
                f"<i>ᴘʀᴏsᴇs ʙᴇʀʜᴀsɪʟ ᴅɪᴊᴀʟᴀɴᴋᴀɴ sᴇᴘᴇɴᴜʜɴʏᴀ.</i></blockquote>"
            )
        except Exception as e:
            await bot.send_message(user_id, f"<blockquote><b>❌ ʙʀᴏᴀᴅᴄᴀsᴛ ᴛᴇʀʜᴇɴᴛɪ:</b> {str(e)}</blockquote>")
        finally:
            BC_RUNNING_TASKS.pop(user_id, None)

    # INI KUNCINYA: Menjalankan proses di background task mandiri
    task = asyncio.create_task(start_broadcast(client, message, status_msg))
    BC_RUNNING_TASKS[user_id] = task

@PY.UBOT("stopbc")
@PY.TOP_CMD
async def _(client, message):
    user_id = client.me.id
    if user_id in BC_RUNNING_TASKS:
        # Hapus dari dictionary dulu agar loop di dalam task berhenti
        BC_RUNNING_TASKS[user_id].cancel()
        BC_RUNNING_TASKS.pop(user_id, None)
        await message.reply_text("<blockquote><b>🛑 ʙʀᴏᴀᴅᴄᴀsᴛ ʙᴇʀʜᴀsɪʟ ᴅɪʜᴇɴᴛɪᴋᴀɴ ᴘᴀᴋsᴀ!</b></blockquote>")
    else:
        await message.reply_text("<blockquote><b>ℹ️ ᴛɪᴅᴀᴋ ᴀᴅᴀ ʙʀᴏᴀᴅᴄᴀsᴛ ʏᴀɴɢ sᴇᴅᴀɴɢ ʙᴇʀᴊᴀʟᴀɴ.</b></blockquote>")
        