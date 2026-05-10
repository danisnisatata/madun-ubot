import asyncio
import random
from PyroUbot import *

__MODULE__ = "ᴍᴀꜰɪᴀ-ǫᴜɪᴢ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴍᴀꜰɪᴀ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴍᴀꜰɪᴀ</code>
ᚗ <code>{0}ᴠᴏᴛᴇ</code> [ᴛᴀɢ/ʀᴇᴘʟʏ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ɢᴀᴍᴇ ᴍᴇɴᴄᴀʀɪ sɪᴀᴘᴀ ᴍᴀꜰɪᴀ ᴅɪ ᴀɴᴛᴀʀᴀ ᴍᴇᴍʙᴇʀ.
ᚗ ᴍᴀꜰɪᴀ ᴅɪᴘɪʟɪʜ sᴇᴄᴀʀᴀ ʀᴀʜᴀsɪᴀ ᴏʟᴇʜ ᴜʙᴏᴛ!</blockquote>
"""

@PY.UBOT("mafia")
async def mafia_handler(client, message):
    emo = "<emoji id=5328212170568434856>🕵️</emoji>" if client.me.is_premium else "🕵️"
    
    # Ambil list member yang online/aktif di grup (limit 15 biar gak spam)
    members = []
    async for m in client.get_chat_members(message.chat.id, limit=30):
        if not m.user.is_bot and not m.user.is_deleted:
            members.append(m.user)
    
    if len(members) < 3:
        return await message.reply("<blockquote><b>ᴍᴇᴍʙᴇʀ ʏᴀɴɢ ᴀᴋᴛɪꜰ ᴋᴇᴅɪᴋɪᴛᴀɴ ᴄᴏ, ᴍɪɴɪᴍᴀʟ 𝟹 ᴏʀᴀɴɢ!</b></blockquote>")

    mafia_target = random.choice(members)
    await set_vars(client.me.id, "MAFIA_ID", mafia_target.id)
    await set_vars(client.me.id, "MAFIA_STATUS", True)

    await message.edit(f"""
<blockquote><b>{emo} ᴍᴀꜰɪᴀ ɢᴀᴍᴇ ᴅɪᴍᴜʟᴀɪ!</b>

ᚗ <b>ᴍɪsɪ :</b> ᴄᴀʀɪ sɪᴀᴘᴀ ᴍᴀꜰɪᴀɴʏᴀ!
ᚗ <b>ᴅᴜʀᴀsɪ :</b> <code>60 ᴅᴇᴛɪᴋ ᴅɪsᴋᴜsɪ</code>

<b>sɪʟᴀʜᴋᴀɴ sᴀʟɪɴɢ ᴛᴜᴅᴜʜ! ᴋᴇᴛɪᴋ :</b>
ᚗ <code>.ᴠᴏᴛᴇ [ᴛᴀɢ/ʀᴇᴘʟʏ]</code> ᴜɴᴛᴜᴋ ᴍᴇᴍɪʟɪʜ sᴜsᴘᴇᴄᴛ.</blockquote>""")

    await asyncio.sleep(60)

    # Closing Game
    is_active = await get_vars(client.me.id, "MAFIA_STATUS")
    if is_active:
        await message.reply(f"""
<blockquote><b>{emo} ᴡᴀᴋᴛᴜ ʜᴀʙɪs!</b>

ᚗ <b>ᴍᴀꜰɪᴀ sᴇʙᴇɴᴀʀɴʏᴀ :</b> {mafia_target.mention}
ᚗ <b>ʜᴀsɪʟ :</b> ᴍᴀꜰɪᴀ ʙᴇʀʜᴀsɪʟ ᴋᴀʙᴜʀ! 🎩</blockquote>""")
        await set_vars(client.me.id, "MAFIA_STATUS", False)

@PY.UBOT("vote")
async def vote_handler(client, message):
    is_active = await get_vars(client.me.id, "MAFIA_STATUS")
    if not is_active: return

    reply = message.reply_to_message
    if not reply:
        return await message.reply("<blockquote><b>ʀᴇᴘʟʏ ᴏʀᴀɴɢ ʏᴀɴɢ ʟᴏ ᴛᴜᴅᴜʜ ᴄᴏ!</b></blockquote>")

    mafia_id = await get_vars(client.me.id, "MAFIA_ID")
    
    if reply.from_user.id == mafia_id:
        await message.reply(f"""
<blockquote><b>🎯 ᴛᴇᴘᴀᴛ sᴀsᴀʀᴀɴ!</b>

{reply.from_user.mention} <b>ᴀᴅᴀʟᴀʜ ᴍᴀꜰɪᴀɴʏᴀ!</b>
<b>ᴠɪʟʟᴀɢᴇʀs ᴡɪɴ!</b> 🎉</blockquote>""")
        await set_vars(client.me.id, "MAFIA_STATUS", False)
    else:
        await message.reply(f"<blockquote><b>❌ sᴀʟᴀʜ! {reply.from_user.first_name} ᴄᴜᴍᴀ ᴡᴀʀɢᴀ sɪᴘɪʟ ʙɪᴀsᴀ. ᴊᴀɴɢᴀɴ sᴀʟᴀʜ ᴛᴜᴅᴜʜ ᴄᴏ!</b></blockquote>")
        