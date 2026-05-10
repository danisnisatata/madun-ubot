import asyncio
from PyroUbot import *

__MODULE__ = "ᴘᴜʀɢᴇ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴘᴜʀɢᴇ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴘᴜʀɢᴇ</code> [ʀᴇᴘʟʏ ᴘᴇsᴀɴ]
ᚗ <code>{0}ᴅᴇʟ</code> [ʀᴇᴘʟʏ ᴘᴇsᴀɴ]
ᚗ <code>{0}ᴘᴜʀɢᴇᴍᴇ</code> [ᴊᴜᴍʟᴀʜ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇᴍʙᴇʀsɪʜᴋᴀɴ ᴘᴇsᴀɴ sᴇᴄᴀʀᴀ ᴍᴀssᴀʟ ᴀᴛᴀᴜ ᴍᴇɴɢʜᴀᴘᴜs ᴘᴇsᴀɴ sᴘᴇsɪꜰɪᴋ ᴅᴇɴɢᴀɴ ᴄᴇᴘᴀᴛ.</blockquote>
"""

@PY.UBOT("del")
@PY.TOP_CMD
async def delete_handler(client, message):
    if message.reply_to_message:
        await message.delete()
        await message.reply_to_message.delete()
    else:
        await message.delete()

@PY.UBOT("purgeme")
@PY.TOP_CMD
async def purgeme_handler(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    
    args = get_arg(message)
    if not args or not args.isnumeric():
        return await message.reply_text(f"<blockquote><b>{ggl} ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ᴊᴜᴍʟᴀʜ ᴘᴇsᴀɴ!</b></blockquote>")
    
    n = int(args)
    if n < 1:
        return await message.reply_text(f"<blockquote><b>{ggl} ᴊᴜᴍʟᴀʜ ᴍɪɴɪᴍᴀʟ ᴀᴅᴀʟᴀʜ 1.</b></blockquote>")
        
    chat_id = message.chat.id
    message_ids = [
        m.id
        async for m in client.search_messages(
            chat_id,
            from_user="me",
            limit=n,
        )
    ]
    
    if not message_ids:
        return await message.reply_text(f"<blockquote><b>{ggl} ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴘᴇsᴀɴ ᴀɴᴅᴀ ʏᴀɴɢ ᴅɪᴛᴇᴍᴜᴋᴀɴ.</b></blockquote>")
    
    await client.delete_messages(chat_id, message_ids, revoke=True)
    status_msg = await message.reply_text(f"<blockquote><b>{brhsl} {len(message_ids)} ᴘᴇsᴀɴ ᴀɴᴅᴀ ᴛᴇʟᴀʜ ᴅɪʜᴀᴘᴜs.</b></blockquote>")
    await asyncio.sleep(2)
    await status_msg.delete()

@PY.UBOT("purge")
@PY.TOP_CMD
async def purge_handler(client, message):
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)
    
    if not message.reply_to_message:
        return await message.reply_text(f"<blockquote><b>{ggl} ᴍᴏʜᴏɴ ʙᴀʟᴀs ᴋᴇ ᴘᴇsᴀɴ ᴀᴡᴀʟ ᴘᴜʀɢᴇ!</b></blockquote>")
    
    chat_id = message.chat.id
    message_ids = []
    
    # Kumpulkan ID pesan dari reply sampai pesan perintah
    for m_id in range(message.reply_to_message.id, message.id):
        message_ids.append(m_id)
        if len(message_ids) == 100:
            await client.delete_messages(chat_id, message_ids, revoke=True)
            message_ids = []
            
    if message_ids:
        await client.delete_messages(chat_id, message_ids, revoke=True)
    
    await message.delete()
    status_msg = await client.send_message(chat_id, f"<blockquote><b>{brhsl} ᴘᴜʀɢᴇ sᴇʟᴇsᴀɪ ᴅɪʟᴀᴋᴜᴋᴀɴ!</b></blockquote>")
    await asyncio.sleep(2)
    await status_msg.delete()
    