import asyncio
from PyroUbot import *

__MODULE__ = "ʀᴇᴀᴄᴛɪᴏɴ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʀᴇᴀᴄᴛɪᴏɴ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ʀᴇᴀᴄᴛ</code> [ᴜsᴇʀ/ᴄʜᴀᴛ] [ᴇᴍᴏᴊɪ]
ᚗ <code>{0}sᴛᴏᴘʀᴇᴀᴄᴛ</code>

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇᴍʙᴇʀɪᴋᴀɴ ʀᴇᴀᴄᴛɪᴏɴ ᴇᴍᴏᴊɪ ᴘᴀᴅᴀ sᴇᴍᴜᴀ ᴘᴇsᴀɴ ᴅɪ ᴅᴀʟᴀᴍ ᴄʜᴀᴛ ᴛᴀʀɢᴇᴛ.</blockquote>
"""

# Global list untuk melacak proses yang berjalan
reaction_progress = []

@PY.UBOT("react")
@PY.TOP_CMD
async def react_handler(client, message):
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    
    global reaction_progress
    
    if len(message.command) < 3:
        return await message.reply_text(
            f"<blockquote><b>{ggl} ꜰᴏʀᴍᴀᴛ sᴀʟᴀʜ!</b>\nᚗ ɢᴜɴᴀᴋᴀɴ: <code>.ʀᴇᴀᴄᴛ @ᴜsᴇʀɴᴀᴍᴇ 🔥</code></blockquote>"
        )

    chat_target = message.command[1]
    emoji_target = message.command[2]
    
    # Tambahkan ID user ke list progress
    if client.me.id not in reaction_progress:
        reaction_progress.append(client.me.id)
    
    status_msg = await message.reply_text(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇᴍʙᴇʀɪᴋᴀɴ ʀᴇᴀᴄᴛɪᴏɴ ᴅɪ {chat_target}...</b></blockquote>")
    
    try:
        async for msg in client.get_chat_history(chat_target):
            # Cek apakah user memberhentikan proses
            if client.me.id not in reaction_progress:
                break
            
            try:
                await client.send_reaction(chat_id=msg.chat.id, message_id=msg.id, emoji=emoji_target)
                await asyncio.sleep(0.3) # Delay halus biar gak kena flood
            except Exception:
                continue
        
        await status_msg.edit(f"<blockquote><b>{brhsl} ʀᴇᴀᴄᴛɪᴏɴ sᴇʟᴇsᴀɪ ᴅɪʙᴇʀɪᴋᴀɴ!</b></blockquote>")
        
    except Exception as e:
        await status_msg.edit(f"<blockquote><b>{ggl} ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ:</b>\n<code>{str(e)}</code></blockquote>")
    
    finally:
        if client.me.id in reaction_progress:
            reaction_progress.remove(client.me.id)


@PY.UBOT("stopreact")
@PY.TOP_CMD
async def stop_react_handler(client, message):
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)
    
    global reaction_progress
    if client.me.id in reaction_progress:
        reaction_progress.remove(client.me.id)
        await message.reply_text(f"<blockquote><b>{brhsl} ᴘʀᴏsᴇs ʀᴇᴀᴄᴛɪᴏɴ ʙᴇʀʜᴀsɪʟ ᴅɪʙᴇʀʜᴇɴᴛɪᴋᴀɴ!</b></blockquote>")
    else:
        await message.reply_text(f"<blockquote><b>{ggl} ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴘʀᴏsᴇs ʀᴇᴀᴄᴛɪᴏɴ ʏᴀɴɢ ʙᴇʀᴊᴀʟᴀɴ.</b></blockquote>")
        