import asyncio
from pyrogram.enums import *
from pyrogram.errors import FloodWait
from pyrogram.types import *
from PyroUbot import *

__MODULE__ = "sᴜᴅᴏ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴜᴅᴏ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴀᴅᴅsᴜᴅᴏ</code> [ʀᴇᴘʟʏ/ᴜsᴇʀɴᴀᴍᴇ]
ᚗ <code>{0}ᴅᴇʟsᴜᴅᴏ</code> [ʀᴇᴘʟʏ/ᴜsᴇʀɴᴀᴍᴇ]
ᚗ <code>{0}ʟɪsᴛsᴜᴅᴏ</code>

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴɢᴀᴛᴜʀ ᴀᴋsᴇs sᴜᴅᴏ ᴀɢᴀʀ ᴜsᴇʀ ʟᴀɪɴ ʙɪsᴀ ᴍᴇɴᴊᴀʟᴀɴᴋᴀɴ ꜰɪᴛᴜʀ ᴜsᴇʀʙᴏᴛ ʟᴜ.</blockquote>
"""

@PY.UBOT("addsudo")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    
    msg = await message.reply(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs...</b></blockquote>")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(f"<blockquote><b>{ggl} sɪʟᴀᴋᴀɴ ʙᴀʟᴀs ᴘᴇsᴀɴ ᴀᴛᴀᴜ ᴍᴀsᴜᴋᴋᴀɴ ᴜsᴇʀɴᴀᴍᴇ/ɪᴅ.</b></blockquote>")

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(f"<blockquote><b>{ggl} ᴇʀʀᴏʀ:</b> <code>{error}</code></blockquote>")

    sudo_users = await get_list_from_vars(client.me.id, "SUDOERS")
    if user.id in sudo_users:
        return await msg.edit(f"<blockquote><b>{ggl} {user.first_name} sᴜᴅᴀʜ ᴍᴇɴᴊᴀᴅɪ ᴘᴇɴɢɢᴜɴᴀ sᴜᴅᴏ.</b></blockquote>")

    try:
        await add_to_vars(client.me.id, "SUDOERS", user.id)
        return await msg.edit(f"<blockquote><b>{brhsl} {user.first_name} ʙᴇʀʜᴀsɪʟ ᴅɪᴛᴀᴍʙᴀʜᴋᴀɴ sᴇʙᴀɢᴀɪ sᴜᴅᴏ.</b></blockquote>")
    except Exception as error:
        return await msg.edit(f"<blockquote><b>{ggl} ᴇʀʀᴏʀ:</b> <code>{error}</code></blockquote>")

@PY.UBOT("delsudo|unsudo")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    msg = await message.reply(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs...</b></blockquote>")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(f"<blockquote><b>{ggl} sɪʟᴀᴋᴀɴ ʙᴀʟᴀs ᴘᴇsᴀɴ ᴀᴛᴀᴜ ᴍᴀsᴜᴋᴋᴀɴ ᴜsᴇʀɴᴀᴍᴇ/ɪᴅ.</b></blockquote>")

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(f"<blockquote><b>{ggl} ᴇʀʀᴏʀ:</b> <code>{error}</code></blockquote>")

    sudo_users = await get_list_from_vars(client.me.id, "SUDOERS")
    if user.id not in sudo_users:
        return await msg.edit(f"<blockquote><b>{ggl} {user.first_name} ʙᴜᴋᴀɴ ʙᴀɢɪᴀɴ ᴅᴀʀɪ ᴘᴇɴɢɢᴜɴᴀ sᴜᴅᴏ.</b></blockquote>")

    try:
        await remove_from_vars(client.me.id, "SUDOERS", user.id)
        return await msg.edit(f"<blockquote><b>{brhsl} {user.first_name} ʙᴇʀʜᴀsɪʟ ᴅɪʜᴀᴘᴜs ᴅᴀʀɪ ᴅᴀꜰᴛᴀʀ sᴜᴅᴏ.</b></blockquote>")
    except Exception as error:
        return await msg.edit(f"<blockquote><b>{ggl} ᴇʀʀᴏʀ:</b> <code>{error}</code></blockquote>")

@PY.UBOT("sudolist|listsudo")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    msg = await message.reply(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs...</b></blockquote>")
    sudo_users = await get_list_from_vars(client.me.id, "SUDOERS")

    if not sudo_users:
        return await msg.edit(f"<blockquote><b>{ggl} ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴘᴇɴɢɢᴜɴᴀ sᴜᴅᴏ ᴅɪᴛᴇᴍᴜᴋᴀɴ.</b></blockquote>")

    sudo_list = []
    for user_id in sudo_users:
        try:
            user = await client.get_users(int(user_id))
            sudo_list.append(f"<b>ᚗ</b> <a href='tg://user?id={user.id}'>{user.first_name}</a> | <code>{user.id}</code>")
        except:
            continue

    response = f"<blockquote><b>{brhsl} ᴅᴀꜰᴛᴀʀ ᴘᴇɴɢɢᴜɴᴀ sᴜᴅᴏ:</b>\n" + "\n".join(sudo_list) + "</blockquote>"
    return await msg.edit(response)
    