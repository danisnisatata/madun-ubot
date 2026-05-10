import asyncio
from pyrogram.enums import ChatType, ChatMemberStatus
from PyroUbot import *

__MODULE__ = "ᴊᴏɪɴʟᴇᴀᴠᴇ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴊᴏɪɴʟᴇᴀᴠᴇ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴋɪᴄᴋᴍᴇ</code>
⊷ ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ ɢʀᴜᴘ ʏᴀɴɢ sᴇᴅᴀɴɢ ᴅɪʙᴜᴋᴀ
ᚗ <code>{0}ᴊᴏɪɴ</code> [ʟɪɴᴋ/ᴜsᴇʀɴᴀᴍᴇ]
⊷ ʙᴇʀɢᴀʙᴜɴɢ ᴋᴇ ɢʀᴜᴘ/ᴄʜᴀɴɴᴇʟ
ᚗ <code>{0}ʟᴇᴀᴠᴇᴀʟʟɢᴄ</code>
⊷ ᴋᴇʟᴜᴀʀ sᴇᴍᴜᴀ ɢʀᴜᴘ (ᴋᴇᴄᴜᴀʟɪ ᴀᴅᴍɪɴ)
ᚗ <code>{0}ʟᴇᴀᴠᴇᴀʟʟᴄʜ</code>
⊷ ᴋᴇʟᴜᴀʀ sᴇᴍᴜᴀ ᴄʜᴀɴɴᴇʟ (ᴋᴇᴄᴜᴀʟɪ ᴀᴅᴍɪɴ)
ᚗ <code>{0}ʟᴇᴀᴠᴇᴀʟʟᴍᴜᴛᴇ</code>
⊷ ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ ɢʀᴜᴘ ʏᴀɴɢ ᴍᴇᴍʙᴀᴛᴀsɪ ʟᴜ</blockquote>
"""

@PY.UBOT("kickme")
@PY.TOP_CMD
@PY.GROUP
async def kickme_handler(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    
    status_msg = await message.reply(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs...</b></blockquote>")
    
    if message.chat.id in BLACKLIST_CHAT:
        return await status_msg.edit(f"<blockquote><b>{ggl} ᴘᴇʀɪɴᴛᴀʜ ɪɴɪ ᴅɪʟᴀʀᴀɴɢ ᴅɪ ɢʀᴜᴘ ɪɴɪ!</b></blockquote>")
    
    try:
        await status_msg.edit(f"<blockquote><b>{brhsl} {client.me.first_name} ᴛᴇʟᴀʜ ᴍᴇɴɪɴɢɢᴀʟᴋᴀɴ ɢʀᴜᴘ, ʙʏᴇ!</b></blockquote>")
        await client.leave_chat(message.chat.id)
    except Exception as e:
        await status_msg.edit(f"<blockquote><b>{ggl} ᴇʀʀᴏʀ:</b>\n<code>{str(e)}</code></blockquote>")

@PY.UBOT("join")
@PY.TOP_CMD
async def join_handler(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    
    args = get_arg(message)
    if not args:
        return await message.reply(f"<blockquote><b>{ggl} ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ʟɪɴᴋ ᴀᴛᴀᴜ ᴜsᴇʀɴᴀᴍᴇ!</b></blockquote>")
    
    status_msg = await message.reply(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs...</b></blockquote>")
    try:
        await client.join_chat(args)
        await status_msg.edit(f"<blockquote><b>{brhsl} ʙᴇʀʜᴀsɪʟ ʙᴇʀɢᴀʙᴜɴɢ ᴋᴇ:</b>\n<code>{args}</code></blockquote>")
    except Exception as e:
        await status_msg.edit(f"<blockquote><b>{ggl} ᴇʀʀᴏʀ:</b>\n<code>{str(e)}</code></blockquote>")

@PY.UBOT("leaveallgc")
@PY.TOP_CMD
async def leaveallgc_handler(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    
    status_msg = await message.reply(f"<blockquote><b>{prs} ɢʟᴏʙᴀʟ ʟᴇᴀᴠᴇ sᴇᴅᴀɴɢ ʙᴇʀᴊᴀʟᴀɴ...</b></blockquote>")
    done, err = 0, 0
    
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP):
            if dialog.chat.id in BLACKLIST_CHAT: continue
            try:
                member = await client.get_chat_member(dialog.chat.id, "me")
                if member.status not in (ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER):
                    await client.leave_chat(dialog.chat.id)
                    done += 1
                    await asyncio.sleep(0.1)
            except:
                err += 1
                
    await status_msg.edit(
        f"<blockquote><b>{brhsl} ɢʟᴏʙᴀʟ ʟᴇᴀᴠᴇ sᴇʟᴇsᴀɪ!</b>\n\n"
        f"<b>ᚗ ʙᴇʀʜᴀsɪʟ :</b> <code>{done}</code> ɢʀᴜᴘ\n"
        f"<b>ᚗ ɢᴀɢᴀʟ :</b> <code>{err}</code> ɢʀᴜᴘ\n\n"
        f"<b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>"
    )

@PY.UBOT("leaveallch")
@PY.TOP_CMD
async def leaveallch_handler(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    
    status_msg = await message.reply(f"<blockquote><b>{prs} ɢʟᴏʙᴀʟ ʟᴇᴀᴠᴇ ᴄʜᴀɴɴᴇʟ sᴇᴅᴀɴɢ ʙᴇʀᴊᴀʟᴀɴ...</b></blockquote>")
    done, err = 0, 0
    
    async for dialog in client.get_dialogs():
        if dialog.chat.type == ChatType.CHANNEL:
            try:
                member = await client.get_chat_member(dialog.chat.id, "me")
                if member.status not in (ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER):
                    await client.leave_chat(dialog.chat.id)
                    done += 1
                    await asyncio.sleep(0.1)
            except:
                err += 1
                
    await status_msg.edit(
        f"<blockquote><b>{brhsl} ʟᴇᴀᴠᴇ ᴄʜᴀɴɴᴇʟ sᴇʟᴇsᴀɪ!</b>\n\n"
        f"<b>ᚗ ʙᴇʀʜᴀsɪʟ :</b> <code>{done}</code> ᴄʜᴀɴɴᴇʟ\n"
        f"<b>ᚗ ɢᴀɢᴀʟ :</b> <code>{err}</code> ᴄʜᴀɴɴᴇʟ\n\n"
        f"<b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>"
    )

@PY.UBOT("leaveallmute")
@PY.TOP_CMD
async def leaveallmute_handler(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    
    status_msg = await message.reply(f"<blockquote><b>{prs} ᴍᴇᴍᴘʀᴏsᴇs ʟᴇᴀᴠᴇ ᴍᴜᴛᴇ...</b></blockquote>")
    done = 0
    
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (ChatType.SUPERGROUP, ChatType.GROUP):
            try:
                member = await client.get_chat_member(dialog.chat.id, "me")
                if member.status == ChatMemberStatus.RESTRICTED:
                    await client.leave_chat(dialog.chat.id)
                    done += 1
                    await asyncio.sleep(0.1)
            except:
                pass
                
    await status_msg.edit(
        f"<blockquote><b>{brhsl} ʙᴇʀʜᴀsɪʟ ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ {done} ɢʀᴜᴘ ʏᴀɴɢ ᴛᴇʟᴀʜ ᴍᴇᴍʙᴀᴛᴀsɪ ʟᴜ!</b>\n\n"
        f"<b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>"
    )
    