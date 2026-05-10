import random
import string
from PyroUbot import *

__MODULE__ = "ʀᴀɴᴅᴏᴍ ᴘʀᴏ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʀᴀɴᴅᴏᴍ ᴘʀᴏ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ʀᴀɴᴅɴᴜᴍ</code> [ᴍɪɴ] [ᴍᴀx]
ᚗ <code>{0}ʀᴀɴᴅᴘɪᴄᴋ</code> [ᴀ|ʙ|ᴄ]
ᚗ <code>{0}ʀᴀɴᴅᴘᴀss</code> [ᴘᴀɴᴊᴀɴɢ]
ᚗ <code>{0}ʀᴀɴᴅʙᴏᴏʟ</code>
ᚗ <code>{0}ʀᴀɴᴅʜᴇx</code>

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ɢᴇɴᴇʀᴀᴛᴏʀ ᴀᴄᴀᴋ ᴜɴᴛᴜᴋ ᴀɴɢᴋᴀ, ᴘɪʟɪʜᴀɴ, ᴘᴀssᴡᴏʀᴅ, ᴅᴀɴ ᴡᴀʀɴᴀ.</blockquote>
"""

@PY.UBOT("randnum")
async def rand_number(client, message):
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)
    args = get_arg(message)
    if not args or len(message.command) < 3:
        return await message.reply_text(f"<blockquote><b>{ggl} ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ᴀɴɢᴋᴀ!</b>\nᚗ ᴄᴏɴᴛᴏʜ: <code>.ʀᴀɴᴅɴᴜᴍ 1 100</code></blockquote>")
    try:
        a, b = int(message.command[1]), int(message.command[2])
        res = random.randint(a, b)
        await message.reply_text(f"<blockquote><b>{brhsl} ʀᴀɴᴅᴏᴍ ɴᴜᴍʙᴇʀ</b>\n\n<b>ᚗ ʜᴀsɪʟ :</b> <code>{res}</code>\n<b>ᚗ ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>")
    except:
        await message.reply_text(f"<blockquote><b>{ggl} ɪɴᴘᴜᴛ ʜᴀʀᴜs ʙᴇʀᴜᴘᴀ ᴀɴɢᴋᴀ!</b></blockquote>")

@PY.UBOT("randpick")
async def rand_pick(client, message):
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)
    args = get_arg(message)
    if not args:
        return await message.reply_text(f"<blockquote><b>{ggl} ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ᴘɪʟɪʜᴀɴ!</b>\nᚗ ᴄᴏɴᴛᴏʜ: <code>.ʀᴀɴᴅᴘɪᴄᴋ ᴋᴏᴘɪ|ᴛᴇʜ|sᴜsᴜ</code></blockquote>")
    items = args.split("|")
    pick = random.choice(items)
    await message.reply_text(f"<blockquote><b>{brhsl} ʀᴀɴᴅᴏᴍ ᴘɪᴄᴋ</b>\n\n<b>ᚗ ᴛᴇʀᴘɪʟɪʜ :</b> <code>{pick}</code>\n<b>ᚗ ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>")

@PY.UBOT("randpass")
async def rand_password(client, message):
    brhsl = await EMO.BERHASIL(client)
    length = int(message.command[1]) if len(message.command) > 1 else 12
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    pwd = "".join(random.choice(chars) for _ in range(length))
    await message.reply_text(f"<blockquote><b>{brhsl} ʀᴀɴᴅᴏᴍ ᴘᴀssᴡᴏʀᴅ</b>\n\n<b>ᚗ ᴘᴀssᴡᴏʀᴅ :</b> <code>{pwd}</code>\n<b>ᚗ ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>")

@PY.UBOT("randbool")
async def rand_bool(client, message):
    brhsl = await EMO.BERHASIL(client)
    res = random.choice(['ʏᴀ', 'ᴛɪᴅᴀᴋ'])
    await message.reply_text(f"<blockquote><b>{brhsl} ʀᴀɴᴅᴏᴍ ᴊᴀᴡᴀʙᴀɴ</b>\n\n<b>ᚗ ʜᴀsɪʟ :</b> <code>{res}</code>\n<b>ᚗ ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>")

@PY.UBOT("randhex")
async def rand_hex(client, message):
    brhsl = await EMO.BERHASIL(client)
    color = "#" + "".join(random.choice("0123456789ABCDEF") for _ in range(6))
    await message.reply_text(f"<blockquote><b>{brhsl} ʀᴀɴᴅᴏᴍ ʜᴇx ᴄᴏʟᴏʀ</b>\n\n<b>ᚗ ᴡᴀʀɴᴀ :</b> <code>{color}</code>\n<b>ᚗ ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>")
    