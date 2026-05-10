import random
import asyncio
from PyroUbot import *

__MODULE__ = "ʙᴏᴍ-ᴀɴɢᴋᴀ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʙᴏᴍ-ᴀɴɢᴋᴀ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ʙᴏᴍ</code>
ᚗ <code>{0}ᴘᴏᴛᴏɴɢ</code> [ᴀɴɢᴋᴀ 𝟷-𝟷𝟶]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴊɪɴᴀᴋᴋᴀɴ ʙᴏᴍ ᴅᴇɴɢᴀɴ ᴍᴇᴍɪʟɪʜ ᴋᴀʙᴇʟ (ᴀɴɢᴋᴀ) ʏᴀɴɢ ᴀᴍᴀɴ!</blockquote>
"""

@PY.UBOT("bom")
async def bom_handler(client, message):
    emo = "<emoji id=5318780365889215011>💣</emoji>" if client.me.is_premium else "💣"
    
    # Tanam bom di angka acak 1-10
    target_bom = random.randint(1, 10)
    await set_vars(client.me.id, "BOM_TARGET", target_bom)
    await set_vars(client.me.id, "BOM_STATUS", True)
    
    await message.edit(f"""
<blockquote><b>{emo} ʙᴏᴍ ᴛᴇʟᴀʜ ᴅɪᴛᴀɴᴀᴍ!</b>

ᚗ <b>ᴛɪᴘᴇ :</b> <code>ᴛɪᴍᴇ ʙᴏᴍʙ ᴠ.𝟷</code>
ᚗ <b>ᴋᴀʙᴇʟ :</b> <code>𝟷 sᴀᴍᴘᴀɪ 𝟷𝟶</code>

<b>ᴘɪʟɪʜ sᴀᴛᴜ ᴋᴀʙᴇʟ ᴜɴᴛᴜᴋ ᴅɪᴘᴏᴛᴏɴɢ :</b>
ᚗ <code>.ᴘᴏᴛᴏɴɢ [ᴀɴɢᴋᴀ]</code>
<b>sᴀʟᴀʜ ᴘᴏᴛᴏɴɢ = ᴍᴇʟᴇᴅᴀᴋ!</b></blockquote>""")

@PY.UBOT("potong")
async def potong_handler(client, message):
    is_active = await get_vars(client.me.id, "BOM_STATUS")
    if not is_active:
        return await message.reply("<blockquote><b>ɢᴀᴋ ᴀᴅᴀ ʙᴏᴍ ʏᴀɴɢ ᴀᴋᴛɪꜰ ᴄᴏ!</b></blockquote>")

    try:
        pilihan = int(get_arg(message))
    except:
        return await message.reply("<blockquote><b>ᴍᴀsᴜᴋᴋᴀɴ ᴀɴɢᴋᴀ 𝟷-𝟷𝟶 ᴄᴏ!</b></blockquote>")

    target = await get_vars(client.me.id, "BOM_TARGET")

    if pilihan == target:
        emo_boom = "<emoji id=5319114705571552553>💥</emoji>" if client.me.is_premium else "💥"
        await message.reply(f"""
<blockquote><b>{emo_boom} ᴅᴜᴀᴀᴀᴀᴀᴀʀʀʀʀ!!!</b>

{message.from_user.mention} <b>sᴀʟᴀʜ ᴘᴏᴛᴏɴɢ ᴋᴀʙᴇʟ!</b>
<b>ʙᴏᴍ ᴍᴇʟᴇᴅᴀᴋ ᴅɪ ᴀɴɢᴋᴀ :</b> <code>{target}</code></blockquote>""")
        await set_vars(client.me.id, "BOM_STATUS", False)
    else:
        await message.reply(f"<blockquote><b>✂️ ᴋᴀʙᴇʟ {pilihan} ᴀᴍᴀɴ! sɪʟᴀʜᴋᴀɴ ʟᴀɴᴊᴜᴛ...</b></blockquote>")
        