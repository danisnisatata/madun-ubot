import asyncio
import random
from PyroUbot.modules import truth_and_dare_string as tod
from PyroUbot import *

__MODULE__ = "ᴛʀᴜᴛʜ & ᴅᴀʀᴇ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴛʀᴜᴛʜ & ᴅᴀʀᴇ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴛʀᴜᴛʜ</code> → ᴍᴇɴᴊᴀᴡᴀʙ ᴊᴜᴊᴜʀ.
ᚗ <code>{0}ᴅᴀʀᴇ</code> → ᴍᴇɴᴇʀɪᴍᴀ ᴛᴀɴᴛᴀɴɢᴀɴ.
ᚗ <code>{0}ᴀᴘᴀᴋᴀʜ</code> [ᴘᴇʀᴛᴀɴʏᴀᴀɴ]
ᚗ <code>{0}ᴋᴇɴᴀᴘᴀ</code> [ᴘᴇʀᴛᴀɴʏᴀᴀɴ]
ᚗ <code>{0}ʙᴀɢᴀɪᴍᴀɴᴀ</code> [ᴘᴇʀᴛᴀɴʏᴀᴀɴ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ɢᴀᴍᴇ sᴇʀᴜ ᴜɴᴛᴜᴋ ᴍᴇɴᴀɴʏᴀᴋᴀɴ ᴋᴇʙᴇɴᴀʀᴀɴ ᴀᴛᴀᴜ ᴛᴀɴᴛᴀɴɢᴀɴ.</blockquote>
"""

@PY.UBOT("apakah")
@PY.TOP_CMD
async def apakah(client, message):
    split_text = message.text.split(None, 1)
    if len(split_text) < 2:
        return await message.reply("<blockquote><b>❌ ᴍᴏʜᴏɴ ʙᴇʀɪᴋᴀɴ sᴀʏᴀ ᴘᴇʀᴛᴀɴʏᴀᴀɴ!</b></blockquote>")
    await message.reply(f"<blockquote><b>{random.choice(tod.AP)}</b></blockquote>")

@PY.UBOT("kenapa")
@PY.TOP_CMD
async def kenapa(client, message):
    split_text = message.text.split(None, 1)
    if len(split_text) < 2:
        return await message.reply("<blockquote><b>❌ ᴍᴏʜᴏɴ ʙᴇʀɪᴋᴀɴ sᴀʏᴀ ᴘᴇʀᴛᴀɴʏᴀᴀɴ!</b></blockquote>")
    await message.reply(f"<blockquote><b>{random.choice(tod.KN)}</b></blockquote>")

@PY.UBOT("bagaimana")
@PY.TOP_CMD
async def bagaimana(client, message):
    split_text = message.text.split(None, 1)
    if len(split_text) < 2:
        return await message.reply("<blockquote><b>❌ ᴍᴏʜᴏɴ ʙᴇʀɪᴋᴀɴ sᴀʏᴀ ᴘᴇʀᴛᴀɴʏᴀᴀɴ!</b></blockquote>")
    await message.reply(f"<blockquote><b>{random.choice(tod.BG)}</b></blockquote>")

@PY.UBOT("dare")
@PY.TOP_CMD
async def dare(client, message):
    try:        
        await message.edit(f"<blockquote><b>{random.choice(tod.DARE)}</b></blockquote>")
    except Exception:
        pass

@PY.UBOT("truth")
@PY.TOP_CMD
async def truth(client, message):
    try:
        await message.edit(f"<blockquote><b>{random.choice(tod.TRUTH)}</b></blockquote>")
    except Exception:
        pass
        