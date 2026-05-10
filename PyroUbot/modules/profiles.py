import asyncio
import random
from os import remove
from asyncio import gather
from pyrogram.raw.functions.messages import DeleteHistory
from pyrogram.enums import ChatType
from PyroUbot import *

__MODULE__ = "ᴘʀᴏꜰɪʟᴇꜱ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴘʀᴏꜰɪʟᴇꜱ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ɪɴꜰᴏ</code> [ʀᴇᴘʟʏ/ᴜsᴇʀ]
ᚗ <code>{0}sɢ</code> [ʀᴇᴘʟʏ/ᴜsᴇʀ]
ᚗ <code>{0}ɪᴅ</code> [ʀᴇᴘʟʏ/ᴜsᴇʀ]
ᚗ <code>{0}sᴇᴛɴᴀᴍᴇ</code> [ᴛᴇᴋs]
ᚗ <code>{0}sᴇᴛʙɪᴏ</code> [ᴛᴇᴋs]
ᚗ <code>{0}ʙʟᴏᴄᴋ</code> | <code>ᴜɴʙʟᴏᴄᴋ</code>

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴɢᴇʟᴏʟᴀ ɪɴꜰᴏʀᴍᴀsɪ ᴘʀᴏꜰɪʟ ᴅᴀɴ ᴍᴇʟɪʜᴀᴛ ᴅᴀᴛᴀ ᴘᴇɴɢɢᴜɴᴀ ᴀᴛᴀᴜ ɢʀᴜᴘ sᴇᴄᴀʀᴀ ᴅᴇᴛᴀɪʟ.</blockquote>
"""

@PY.UBOT("sg")
@PY.TOP_CMD
async def sg_handler(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)
    
    get_user = await extract_user(message)
    status_msg = await message.reply(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇᴍᴇʀɪᴋsᴀ ʜɪsᴛᴏʀɪ...</b></blockquote>")
    
    if not get_user:
        return await status_msg.edit(f"<blockquote><b>{ggl} ᴜsᴇʀ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ.</b></blockquote>")
    
    try:
        user_id = (await client.get_users(get_user)).id
    except:
        return await status_msg.edit(f"<blockquote><b>{ggl} ɪᴅ ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ.</b></blockquote>")

    bot = ["@Sangmata_bot", "@SangMata_beta_bot"]
    getbot = random.choice(bot)
    await client.unblock_user(getbot)
    txt = await client.send_message(getbot, user_id)
    await asyncio.sleep(4)
    
    await txt.delete()
    await status_msg.delete()
    
    async for name in client.search_messages(getbot, limit=2):
        if name.text:
            await message.reply(f"<blockquote><b>{brhsl} ʜɪsᴛᴏʀɪ ɴᴀᴍᴀ:</b>\n\n{name.text}</blockquote>", quote=True)
    
    user_info = await client.resolve_peer(getbot)
    return await client.invoke(DeleteHistory(peer=user_info, max_id=0, revoke=True))

@PY.UBOT("info")
@PY.TOP_CMD
async def info_handler(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    
    user_id = await extract_user(message)
    status_msg = await message.reply(f"<blockquote><b>{prs} ᴍᴇɴɢᴀᴍʙɪʟ ᴅᴀᴛᴀ...</b></blockquote>")
    
    if not user_id:
        return await status_msg.edit(f"<blockquote><b>{ggl} ʙᴇʀɪᴋᴀɴ ᴜsᴇʀɴᴀᴍᴇ ᴀᴛᴀᴜ ʀᴇᴘʟʏ ᴜsᴇʀ.</b></blockquote>")
    
    try:
        user = await client.get_users(user_id)
        chat = await client.get_chat(user.id)
        bio = chat.bio if chat.bio else "-"
        common = await client.get_common_chats(user.id)
        
        out_str = (
            f"<blockquote><b>{brhsl} ᴜsᴇʀ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ</b>\n\n"
            f"<b>ᚗ ɪᴅ :</b> <code>{user.id}</code>\n"
            f"<b>ᚗ ɴᴀᴍᴀ :</b> <code>{user.first_name} {user.last_name or ''}</code>\n"
            f"<b>ᚗ ᴜsᴇʀɴᴀᴍᴇ :</b> @{user.username if user.username else '-'}\n"
            f"<b>ᚗ ᴅᴄ ɪᴅ :</b> <code>{user.dc_id or '-'}</code>\n"
            f"<b>ᚗ ᴘʀᴇᴍɪᴜᴍ :</b> <code>{user.is_premium}</code>\n"
            f"<b>ᚗ ʙɪᴏ :</b> <code>{bio}</code>\n\n"
            f"<b>⌭ ɢʀᴜᴘ ʏᴀɴɢ sᴀᴍᴀ :</b> <code>{len(common)}</code>\n"
            f"<b>ᚗ ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>"
        )
        
        if user.photo:
            photo = await client.download_media(user.photo.big_file_id)
            await gather(
                status_msg.delete(),
                client.send_photo(message.chat.id, photo, caption=out_str, reply_to_message_id=message.id)
            )
            remove(photo)
        else:
            await status_msg.edit(out_str)
    except Exception as e:
        await status_msg.edit(f"<blockquote><b>{ggl} ᴇʀʀᴏʀ:</b> <code>{str(e)}</code></blockquote>")

@PY.UBOT("id")
@PY.TOP_CMD
async def id_handler(client, message):
    brhsl = await EMO.BERHASIL(client)
    
    text = f"<blockquote><b>{brhsl} ɪᴅ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ</b>\n\n"
    text += f"<b>ᚗ ᴍᴇssᴀɢᴇ ɪᴅ :</b> <code>{message.id}</code>\n"
    text += f"<b>ᚗ ᴄʜᴀᴛ ɪᴅ :</b> <code>{message.chat.id}</code>\n"
    
    if message.from_user:
        text += f"<b>ᚗ ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n"
        
    if message.reply_to_message:
        rep = message.reply_to_message
        rep_id = rep.from_user.id if rep.from_user else rep.sender_chat.id
        text += f"<b>ᚗ ʀᴇᴘʟɪᴇᴅ ɪᴅ :</b> <code>{rep_id}</code>\n"
        text += f"<b>ᚗ ʀᴇᴘʟɪᴇᴅ ᴍsɢ :</b> <code>{rep.id}</code>\n"
    
    text += "</blockquote>"
    await message.reply(text)

@PY.UBOT("setbio")
@PY.TOP_CMD
async def setbio_handler(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    
    args = get_arg(message)
    if not args:
        return await message.reply(f"<blockquote><b>{ggl} ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ᴛᴇᴋs ʙɪᴏ!</b></blockquote>")
        
    status_msg = await message.reply(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs...</b></blockquote>")
    try:
        await client.update_profile(bio=args)
        await status_msg.edit(f"<blockquote><b>{brhsl} ʙɪᴏ ʙᴇʀʜᴀsɪʟ ᴅɪᴜʙᴀʜ ᴍᴇɴᴊᴀᴅɪ:</b>\n<code>{args}</code></blockquote>")
    except Exception as e:
        await status_msg.edit(f"<blockquote><b>{ggl} ᴇʀʀᴏʀ:</b> <code>{str(e)}</code></blockquote>")

@PY.UBOT("setname")
@PY.TOP_CMD
async def setname_handler(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    
    args = get_arg(message)
    if not args:
        return await message.reply(f"<blockquote><b>{ggl} ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ɴᴀᴍᴀ!</b></blockquote>")
        
    status_msg = await message.reply(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs...</b></blockquote>")
    try:
        await client.update_profile(first_name=args)
        await status_msg.edit(f"<blockquote><b>{brhsl} ɴᴀᴍᴀ ʙᴇʀʜᴀsɪʟ ᴅɪᴜʙᴀʜ ᴍᴇɴᴊᴀᴅɪ:</b>\n<code>{args}</code></blockquote>")
    except Exception as e:
        await status_msg.edit(f"<blockquote><b>{ggl} ᴇʀʀᴏʀ:</b> <code>{str(e)}</code></blockquote>")

@PY.UBOT("block")
@PY.TOP_CMD
async def block_handler(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    user_id = await extract_user(message)
    
    if not user_id: return await message.reply(f"<blockquote><b>{ggl} ʀᴇᴘʟʏ ᴜsᴇʀ ʏᴀɴɢ ɪɴɢɪɴ ᴅɪʙʟᴏᴋɪʀ.</b></blockquote>")
    
    await client.block_user(user_id)
    await message.reply(f"<blockquote><b>{brhsl} ᴘᴇɴɢɢᴜɴᴀ ʙᴇʀʜᴀsɪʟ ᴅɪʙʟᴏᴋɪʀ.</b></blockquote>")

@PY.UBOT("unblock")
@PY.TOP_CMD
async def unblock_handler(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    user_id = await extract_user(message)
    
    if not user_id: return await message.reply(f"<blockquote><b>{ggl} ʀᴇᴘʟʏ ᴜsᴇʀ ʏᴀɴɢ ɪɴɢɪɴ ᴅɪʙʟᴏᴋɪʀ.</b></blockquote>")
    
    await client.unblock_user(user_id)
    await message.reply(f"<blockquote><b>{brhsl} ᴘᴇɴɢɢᴜɴᴀ ʙᴇʀʜᴀsɪʟ ᴅɪʙᴇʙᴀsᴋᴀɴ.</b></blockquote>")
    