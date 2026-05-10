import asyncio
from pyrogram.types import ChatPermissions
from PyroUbot import *

__MODULE__ = "ɢʟᴏʙᴀʟ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɢʟᴏʙᴀʟ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ɢʙᴀɴ</code> [ʀᴇᴘʟʏ/ᴜsᴇʀ]
⊷ ʙᴀɴ ᴘᴇɴɢɢᴜɴᴀ ᴅᴀʀɪ sᴇᴍᴜᴀ ɢʀᴜᴘ ᴄʜᴀᴛ.
ᚗ <code>{0}ᴜɴɢʙᴀɴ</code> [ʀᴇᴘʟʏ/ᴜsᴇʀ]
⊷ ᴄᴀʙᴜᴛ ʙᴀɴ ɢʟᴏʙᴀʟ ᴘᴇɴɢɢᴜɴᴀ.
ᚗ <code>{0}ɢᴍᴜᴛᴇ</code> [ʀᴇᴘʟʏ/ᴜsᴇʀ]
⊷ ᴍᴜᴛᴇ ᴘᴇɴɢɢᴜɴᴀ ᴅɪ sᴇᴍᴜᴀ ɢʀᴜᴘ ʏᴀɴɢ ᴀɴᴅᴀ ᴀᴅᴍɪɴ.
ᚗ <code>{0}ᴜɴɢᴍᴜᴛᴇ</code> [ʀᴇᴘʟʏ/ᴜsᴇʀ]
⊷ ᴄᴀʙᴜᴛ ᴍᴜᴛᴇ ɢʟᴏʙᴀʟ ᴘᴇɴɢɢᴜɴᴀ.

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ꜰɪᴛᴜʀ ɪɴɪ ʜᴀɴʏᴀ ʙᴇᴋᴇʀᴊᴀ ᴘᴀᴅᴀ ɢʀᴜᴘ ᴅɪᴍᴀɴᴀ ᴀɴᴅᴀ ᴀᴅᴀʟᴀʜ ᴀᴅᴍɪɴ.</blockquote>
"""

@PY.UBOT("gban")
@PY.TOP_CMD
async def gban_handler(client, message):
    prs_emo = await EMO.PROSES(client)
    brhsl_emo = await EMO.BERHASIL(client)
    ggl_emo = await EMO.GAGAL(client)
    
    user_id = await extract_user(message)
    if not user_id:
        return await message.reply_text(f"<blockquote><b>{ggl_emo} ᴘᴇɴɢɢᴜɴᴀ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ!</b></blockquote>")

    status_msg = await message.reply_text(f"<blockquote><b>{prs_emo} ᴍᴇᴍᴘʀᴏsᴇs ɢʟᴏʙᴀʟ ʙᴀɴ...</b></blockquote>")
    
    try:
        user = await client.get_users(user_id)
    except Exception as e:
        return await status_msg.edit(f"<blockquote><b>{ggl_emo} ᴇʀʀᴏʀ:</b> <code>{str(e)}</code></blockquote>")

    if user.id == OWNER_ID:
        return await status_msg.edit(f"<blockquote><b>{ggl_emo} ᴀɴᴅᴀ ᴛɪᴅᴀᴋ ʙɪsᴀ ɢʙᴀɴ ᴅᴇᴠᴇʟᴏᴘᴇʀ sᴇɴᴅɪʀɪ!</b></blockquote>")

    done = 0
    failed = 0
    global_id = await get_data_id(client, "global")
    
    for dialog in global_id:
        try:
            await client.ban_chat_member(dialog, user.id)
            done += 1
        except:
            failed += 1
        await asyncio.sleep(0.1)

    res_text = f"""
<blockquote><b>{brhsl_emo} ɢʟᴏʙᴀʟ ʙᴀɴ sᴇʟᴇsᴀɪ</b>

<b>ᚗ sᴛᴀᴛᴜs :</b> <code>ʙᴀɴɴᴇᴅ</code>
<b>ᚗ ʙᴇʀʜᴀsɪʟ :</b> <code>{done} ᴄʜᴀᴛ</code>
<b>ᚗ ɢᴀɢᴀʟ :</b> <code>{failed} ᴄʜᴀᴛ</code>
<b>ᚗ ᴛᴀʀɢᴇᴛ :</b> <a href='tg://user?id={user.id}'>{user.first_name}</a>

<b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>"""
    await message.reply_text(res_text)
    await status_msg.delete()

@PY.UBOT("ungban")
@PY.TOP_CMD
async def ungban_handler(client, message):
    prs_emo = await EMO.PROSES(client)
    brhsl_emo = await EMO.BERHASIL(client)
    ggl_emo = await EMO.GAGAL(client)
    
    user_id = await extract_user(message)
    if not user_id:
        return await message.reply_text(f"<blockquote><b>{ggl_emo} ᴘᴇɴɢɢᴜɴᴀ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ!</b></blockquote>")

    status_msg = await message.reply_text(f"<blockquote><b>{prs_emo} ᴍᴇᴍᴘʀᴏsᴇs ɢʟᴏʙᴀʟ ᴜɴʙᴀɴ...</b></blockquote>")
    
    try:
        user = await client.get_users(user_id)
    except Exception as e:
        return await status_msg.edit(f"<blockquote><b>{ggl_emo} ᴇʀʀᴏʀ:</b> <code>{str(e)}</code></blockquote>")

    done = 0
    failed = 0
    global_id = await get_data_id(client, "global")
    
    for dialog in global_id:
        try:
            await client.unban_chat_member(dialog, user.id)
            done += 1
        except:
            failed += 1
        await asyncio.sleep(0.1)

    res_text = f"""
<blockquote><b>{brhsl_emo} ɢʟᴏʙᴀʟ ᴜɴʙᴀɴ sᴇʟᴇsᴀɪ</b>

<b>ᚗ sᴛᴀᴛᴜs :</b> <code>ᴜɴʙᴀɴɴᴇᴅ</code>
<b>ᚗ ʙᴇʀʜᴀsɪʟ :</b> <code>{done} ᴄʜᴀᴛ</code>
<b>ᚗ ɢᴀɢᴀʟ :</b> <code>{failed} ᴄʜᴀᴛ</code>
<b>ᚗ ᴛᴀʀɢᴇᴛ :</b> <a href='tg://user?id={user.id}'>{user.first_name}</a>

<b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>"""
    await message.reply_text(res_text)
    await status_msg.delete()

@PY.UBOT("gmute")
@PY.TOP_CMD
async def gmute_handler(client, message):
    prs_emo = await EMO.PROSES(client)
    brhsl_emo = await EMO.BERHASIL(client)
    ggl_emo = await EMO.GAGAL(client)
    
    user_id = await extract_user(message)
    if not user_id:
        return await message.reply_text(f"<blockquote><b>{ggl_emo} ᴘᴇɴɢɢᴜɴᴀ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ!</b></blockquote>")

    status_msg = await message.reply_text(f"<blockquote><b>{prs_emo} ᴍᴇᴍᴘʀᴏsᴇs ɢʟᴏʙᴀʟ ᴍᴜᴛᴇ...</b></blockquote>")
    
    try:
        user = await client.get_users(user_id)
    except Exception as e:
        return await status_msg.edit(f"<blockquote><b>{ggl_emo} ᴇʀʀᴏʀ:</b> <code>{str(e)}</code></blockquote>")

    if user.id == OWNER_ID:
        return await status_msg.edit(f"<blockquote><b>{ggl_emo} ᴀɴᴅᴀ ᴛɪᴅᴀᴋ ʙɪsᴀ ɢᴍᴜᴛᴇ ᴅᴇᴠᴇʟᴏᴘᴇʀ sᴇɴᴅɪʀɪ!</b></blockquote>")

    done = 0
    failed = 0
    global_id = await get_data_id(client, "group")
    
    for dialog in global_id:
        try:
            await client.restrict_chat_member(dialog, user.id, ChatPermissions(can_send_messages=False))
            done += 1
        except:
            failed += 1
        await asyncio.sleep(0.1)

    res_text = f"""
<blockquote><b>{brhsl_emo} ɢʟᴏʙᴀʟ ᴍᴜᴛᴇ sᴇʟᴇsᴀɪ</b>

<b>ᚗ sᴛᴀᴛᴜs :</b> <code>ᴍᴜᴛᴇᴅ</code>
<b>ᚗ ʙᴇʀʜᴀsɪʟ :</b> <code>{done} ᴄʜᴀᴛ</code>
<b>ᚗ ɢᴀɢᴀʟ :</b> <code>{failed} ᴄʜᴀᴛ</code>
<b>ᚗ ᴛᴀʀɢᴇᴛ :</b> <a href='tg://user?id={user.id}'>{user.first_name}</a>

<b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>"""
    await message.reply_text(res_text)
    await status_msg.delete()

@PY.UBOT("ungmute")
@PY.TOP_CMD
async def ungmute_handler(client, message):
    prs_emo = await EMO.PROSES(client)
    brhsl_emo = await EMO.BERHASIL(client)
    ggl_emo = await EMO.GAGAL(client)
    
    user_id = await extract_user(message)
    if not user_id:
        return await message.reply_text(f"<blockquote><b>{ggl_emo} ᴘᴇɴɢɢᴜɴᴀ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ!</b></blockquote>")

    status_msg = await message.reply_text(f"<blockquote><b>{prs_emo} ᴍᴇᴍᴘʀᴏsᴇs ɢʟᴏʙᴀʟ ᴜɴᴍᴜᴛᴇ...</b></blockquote>")
    
    try:
        user = await client.get_users(user_id)
    except Exception as e:
        return await status_msg.edit(f"<blockquote><b>{ggl_emo} ᴇʀʀᴏʀ:</b> <code>{str(e)}</code></blockquote>")

    done = 0
    failed = 0
    global_id = await get_data_id(client, "global")
    
    for dialog in global_id:
        try:
            await client.restrict_chat_member(dialog, user.id, ChatPermissions(can_send_messages=True))
            done += 1
        except:
            failed += 1
        await asyncio.sleep(0.1)

    res_text = f"""
<blockquote><b>{brhsl_emo} ɢʟᴏʙᴀʟ ᴜɴᴍᴜᴛᴇ sᴇʟᴇsᴀɪ</b>

<b>ᚗ sᴛᴀᴛᴜs :</b> <code>ᴜɴᴍᴜᴛᴇᴅ</code>
<b>ᚗ ʙᴇʀʜᴀsɪʟ :</b> <code>{done} ᴄʜᴀᴛ</code>
<b>ᚗ ɢᴀɢᴀʟ :</b> <code>{failed} ᴄʜᴀᴛ</code>
<b>ᚗ ᴛᴀʀɢᴇᴛ :</b> <a href='tg://user?id={user.id}'>{user.first_name}</a>

<b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>"""
    await message.reply_text(res_text)
    await status_msg.delete()
    