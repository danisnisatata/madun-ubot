import asyncio
from PyroUbot import *
from pyrogram.enums import ChatType, ChatMemberStatus

__MODULE__ = "ɢᴄᴀsᴛ ɴᴇᴡ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɢᴄᴀsᴛ ɴᴇᴡ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ʙᴄ</code> [ᴛʏᴘᴇ] (ʀᴇᴘʟʏ ᴘᴇsᴀɴ)

<b>⌭ ᴘɪʟɪʜᴀɴ ᴛʏᴘᴇ :</b>
ᚗ <code>ɢᴄ</code> : ᴋɪʀɪᴍ ᴋᴇ sᴇᴍᴜᴀ ɢʀᴜᴘ
ᚗ <code>ᴀᴅᴍ</code> : ᴋɪʀɪᴍ ᴋᴇ ɢʀᴜᴘ ᴅɪ ᴍᴀɴᴀ ʟᴜ ᴀᴅᴍɪɴ
ᚗ <code>ᴘᴠ</code> : ᴋɪʀɪᴍ ᴋᴇ sᴇᴍᴜᴀ ᴄʜᴀᴛ ᴘʀɪʙᴀᴅɪ</blockquote>
"""

def get_message(message):
    return (
        message.reply_to_message
        if message.reply_to_message
        else ""
        if len(message.command) < 2
        else " ".join(message.command[1:])
    )

@PY.UBOT("bc")
@PY.TOP_CMD
async def gcast_handler(c, m):
    prs = await EMO.PROSES(c)
    brhsl = await EMO.BERHASIL(c)
    ggl = await EMO.GAGAL(c)
    
    if len(m.command) < 2:
        return await m.reply(f"<blockquote><b>{ggl} ᴍᴏʜᴏɴ ɢᴜɴᴀᴋᴀɴ ꜰᴏʀᴍᴀᴛ:</b>\n<code>.ʙᴄ [ɢᴄ|ᴀᴅᴍ|ᴘᴠ]</code> (ʀᴇᴘʟʏ ᴘᴇsᴀɴ)</blockquote>")

    send = get_message(m)
    if not send:
        return await m.reply(f"<blockquote><b>{ggl} ᴍᴏʜᴏɴ ʙᴀʟᴀs ᴋᴇ ᴘᴇsᴀɴ ʏᴀɴɢ ɪɴɢɪɴ ᴅɪsᴇʙᴀʀ!</b></blockquote>")

    blacklist = await get_chat(c.me.id)
    done = 0
    target_type = m.command[1].lower()
    
    Haku = await m.reply(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ʙʀᴏᴀᴅᴄᴀsᴛ...</b></blockquote>")

    try:
        async for dialog in c.get_dialogs():
            # Broadcast ke Grup
            if target_type == "gc":
                if dialog.chat.type in (ChatType.SUPERGROUP, ChatType.GROUP):
                    if dialog.chat.id not in blacklist:
                        try:
                            await send.copy(dialog.chat.id)
                            done += 1
                            await asyncio.sleep(0.1)
                        except: pass

            # Broadcast ke Private Chat
            elif target_type == "pv":
                if dialog.chat.type == ChatType.PRIVATE:
                    if dialog.chat.id not in blacklist:
                        try:
                            await send.copy(dialog.chat.id)
                            done += 1
                            await asyncio.sleep(0.1)
                        except: pass

            # Broadcast Khusus Grup di mana lu Admin/Owner
            elif target_type == "adm":
                if dialog.chat.type in (ChatType.SUPERGROUP, ChatType.GROUP):
                    try:
                        member = await c.get_chat_member(dialog.chat.id, "me")
                        if member.status in (ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER):
                            await send.copy(dialog.chat.id)
                            done += 1
                            await asyncio.sleep(0.1)
                    except: pass

        await Haku.edit(
            f"<blockquote><b>{brhsl} ʙʀᴏᴀᴅᴄᴀsᴛ sᴇʟᴇsᴀɪ!</b>\n\n"
            f"<b>ᚗ ᴛᴇʀᴋɪʀɪᴍ :</b> <code>{done}</code> ᴄʜᴀᴛ\n"
            f"<b>ᚗ ᴛʏᴘᴇ :</b> <code>{target_type.upper()}</code>\n\n"
            f"<b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>"
        )

    except Exception as e:
        await Haku.edit(f"<blockquote><b>{ggl} ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ:</b>\n<code>{str(e)}</code></blockquote>")
        