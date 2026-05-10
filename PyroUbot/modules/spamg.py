import asyncio
from pyrogram.enums import ChatType
from pyrogram.errors import FloodWait
from .. import *
from PyroUbot import *

__MODULE__ = "sᴘᴀᴍ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴘᴀᴍ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}sᴘᴀᴍ</code> [ᴊᴜᴍʟᴀʜ] [ᴛᴇᴋs/ʀᴇᴘʟʏ]
ᚗ <code>{0}sᴇᴛᴅᴇʟᴀʏ</code> [ᴅᴇᴛɪᴋ]
ᚗ <code>{0}sᴛᴏᴘsᴘᴀᴍ</code>

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴘᴇɴɢɪʀɪᴍᴀɴ ᴘᴇsᴀɴ ʙᴇʀᴜʟᴀɴɢ sᴇᴄᴀʀᴀ ᴏᴛᴏᴍᴀᴛɪs.</blockquote>
"""

spam_progress = []

async def SpamMsg(client, message, send):
    delay = await get_vars(client.me.id, "SPAM") or 0
    await asyncio.sleep(int(delay))
    try:
        if message.reply_to_message:
            await send.copy(message.chat.id)
        else:
            await client.send_message(message.chat.id, send)
    except FloodWait as e:
        await asyncio.sleep(e.value)
    except Exception:
        pass

@PY.UBOT("spam")
@PY.TOP_CMD
async def spam_handler(client, message):
    global spam_progress
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    
    count, msg = extract_type_and_msg(message)
    
    try:
        count = int(count)
    except (ValueError, TypeError):
        return await message.reply(f"<blockquote><b>{ggl} ɢᴜɴᴀᴋᴀɴ ꜰᴏʀᴍᴀᴛ: <code>.sᴘᴀᴍ</code> [ᴊᴜᴍʟᴀʜ] [ᴛᴇᴋs]</b></blockquote>")

    if not msg:
        return await message.reply(f"<blockquote><b>{ggl} ʜᴀʀᴀᴘ ᴍᴀsᴜᴋᴋᴀɴ ᴘᴇsᴀɴ ᴀᴛᴀᴜ ʙᴀʟᴀs ᴋᴇ sᴇsᴜᴀᴛᴜ!</b></blockquote>")
    
    spam_progress.append(client.me.id)
    r = await message.reply(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇɴᴊᴀʟᴀɴᴋᴀɴ sᴘᴀᴍ...</b></blockquote>")

    for _ in range(count):
        if client.me.id not in spam_progress:
            return await r.edit(f"<blockquote><b>{sks} ᴘʀᴏsᴇs sᴘᴀᴍ ʙᴇʀʜᴀsɪʟ ᴅɪʜᴇɴᴛɪᴋᴀɴ!</b></blockquote>")
        await SpamMsg(client, message, msg)

    if client.me.id in spam_progress:
        spam_progress.remove(client.me.id)
        
    await r.edit(f"<blockquote><b>{sks} sᴘᴀᴍ ᴛᴇʟᴀʜ sᴇʟᴇsᴀɪ!</b></blockquote>")

@PY.UBOT("setdelay")
@PY.TOP_CMD
async def setdelay_handler(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    
    args = get_arg(message)
    if not args:
        return await message.reply(f"<blockquote><b>{ggl} ᴍᴀsᴜᴋᴋᴀɴ ᴊᴜᴍʟᴀʜ ᴅᴇᴛɪᴋ!</b></blockquote>")

    try:
        count = int(args)
    except ValueError:
        return await message.reply(f"<blockquote><b>{ggl} ᴅᴇʟᴀʏ ʜᴀʀᴜs ʙᴇʀᴜᴘᴀ ᴀɴɢᴋᴀ!</b></blockquote>")

    await set_vars(client.me.id, "SPAM", count)
    return await message.reply(f"<blockquote><b>{sks} sᴘᴀᴍ ᴅᴇʟᴀʏ ʙᴇʀʜᴀsɪʟ ᴅɪsᴇᴛᴛɪɴɢ ᴋᴇ <code>{count}</code> ᴅᴇᴛɪᴋ.</b></blockquote>")

@PY.UBOT("stopspam")
@PY.TOP_CMD
async def stopspam_handler(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    
    if client.me.id in spam_progress:
        spam_progress.remove(client.me.id)
        await message.reply(f"<blockquote><b>{sks} sᴘᴀᴍ ᴛᴇʟᴀʜ ᴅɪʜᴇɴᴛɪᴋᴀɴ!</b></blockquote>")
    else:
        await message.reply(f"<blockquote><b>{ggl} ᴛɪᴅᴀᴋ ᴀᴅᴀ sᴘᴀᴍ ʏᴀɴɢ ʙᴇʀᴊᴀʟᴀɴ.</b></blockquote>")
        