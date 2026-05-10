from pyrogram.raw.functions.contacts import AddContact
from pyrogram.errors import RPCError
from PyroUbot import *

__MODULE__ = "ᴋᴏɴᴛᴀᴋ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴋᴏɴᴛᴀᴋ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}sᴀᴠᴇᴋᴏɴ</code> [ʀᴇᴘʟʏ/ᴜsᴇʀ] [ɴᴀᴍᴀ]
ᚗ <code>{0}ᴅᴇʟᴋᴏɴ</code> [ʀᴇᴘʟʏ/ᴜsᴇʀ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴʏɪᴍᴘᴀɴ ᴀᴛᴀᴜ ᴍᴇɴɢʜᴀᴘᴜs ᴋᴏɴᴛᴀᴋ ᴅᴀʀɪ ᴅᴀꜰᴛᴀʀ ᴛᴇʟᴇɢʀᴀᴍ ʟᴜ sᴇᴄᴀʀᴀ ᴏᴛᴏᴍᴀᴛɪs.</blockquote>
"""

@PY.UBOT("savekon")
@PY.TOP_CMD
async def save_contact_handler(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)
    
    user_id = None
    custom_name = ""

    reply = message.reply_to_message
    args = get_arg(message)

    if reply:
        user_id = reply.from_user.id
        custom_name = args if args else reply.from_user.first_name
    else:
        if len(message.command) < 3:
            return await message.reply_text(f"<blockquote><b>{ggl} ɢᴜɴᴀᴋᴀɴ ꜰᴏʀᴍᴀᴛ: <code>.sᴀᴠᴇᴋᴏɴ</code> [ɪᴅ/ᴜsᴇʀ] [ɴᴀᴍᴀ]</b></blockquote>")
        
        user_id_or_username = message.command[1]
        custom_name = " ".join(message.command[2:])
        try:
            user = await client.get_users(user_id_or_username)
            user_id = user.id
        except Exception as e:
            return await message.reply_text(f"<blockquote><b>{ggl} ᴇʀʀᴏʀ:</b> <code>{str(e)}</code></blockquote>")

    if not user_id:
        return await message.reply_text(f"<blockquote><b>{ggl} ᴘᴇɴɢɢᴜɴᴀ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ.</b></blockquote>")

    status_msg = await message.reply_text(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇɴʏɪᴍᴘᴀɴ ᴋᴏɴᴛᴀᴋ...</b></blockquote>")
    peer = await client.resolve_peer(user_id)

    try:
        await client.invoke(
            AddContact(
                id=peer,
                first_name=custom_name,
                last_name="",
                phone="",
                add_phone_privacy_exception=True
            )
        )
        await status_msg.edit(
            f"<blockquote><b>{brhsl} sɪᴍᴘᴀɴ ᴋᴏɴᴛᴀᴋ ʙᴇʀʜᴀsɪʟ</b>\n\n"
            f"<b>ᚗ ɴᴀᴍᴀ :</b> <code>{custom_name}</code>\n"
            f"<b>ᚗ ᴜsᴇʀ ɪᴅ :</b> <code>{user_id}</code></blockquote>"
        )
    except RPCError as e:
        await status_msg.edit(f"<blockquote><b>{ggl} ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ:</b> <code>{str(e)}</code></blockquote>")

@PY.UBOT("delkon")
@PY.TOP_CMD
async def delete_contact_handler(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)
    
    user_id = None
    reply = message.reply_to_message

    if reply:
        user_id = reply.from_user.id
    else:
        args = get_arg(message)
        if not args:
            return await message.reply_text(f"<blockquote><b>{ggl} ʀᴇᴘʟʏ ᴀᴛᴀᴜ ᴍᴀsᴜᴋᴋᴀɴ ID/ᴜsᴇʀɴᴀᴍᴇ!</b></blockquote>")
        try:
            user = await client.get_users(args)
            user_id = user.id
        except Exception as e:
            return await message.reply_text(f"<blockquote><b>{ggl} ᴇʀʀᴏʀ:</b> <code>{str(e)}</code></blockquote>")

    status_msg = await message.reply_text(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇɴɢʜᴀᴘᴜs ᴋᴏɴᴛᴀᴋ...</b></blockquote>")

    try:
        await client.delete_contacts([user_id])
        await status_msg.edit(
            f"<blockquote><b>{brhsl} ʜᴀᴘᴜs ᴋᴏɴᴛᴀᴋ ʙᴇʀʜᴀsɪʟ</b>\n"
            f"<b>ᚗ ᴜsᴇʀ ɪᴅ :</b> <code>{user_id}</code></blockquote>"
        )
    except Exception as e:
        await status_msg.edit(f"<blockquote><b>{ggl} ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ:</b> <code>{str(e)}</code></blockquote>")
        