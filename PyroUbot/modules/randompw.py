import secrets
import string
from PyroUbot import *

__MODULE__ = "ʀᴀɴᴅᴏᴍ ᴘᴡ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʀᴀɴᴅᴏᴍ ᴘᴡ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴘᴀss</code> [ᴘᴀɴᴊᴀɴɢ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴɢʜᴀsɪʟᴋᴀɴ ᴘᴀssᴡᴏʀᴅ ᴀᴄᴀᴋ ʏᴀɴɢ ᴋᴜᴀᴛ ᴅᴀɴ ᴀᴍᴀɴ.
ᚗ ᴘᴀɴᴊᴀɴɢ ᴍɪɴɪᴍᴀʟ 6 ᴅᴀɴ ᴍᴀᴋsɪᴍᴀʟ 64 ᴋᴀʀᴀᴋᴛᴇʀ.</blockquote>
"""

@PY.UBOT("pass")
@PY.TOP_CMD
async def password_generator_handler(client, message):
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)
    
    length = 12
    args = get_arg(message)

    if args and args.isdigit():
        length = int(args)

    if length < 6 or length > 64:
        return await message.reply_text(
            f"<blockquote><b>{ggl} ᴘᴀɴᴊᴀɴɢ ᴘᴀssᴡᴏʀᴅ ʜᴀʀᴜs ᴅɪ ᴀɴᴛᴀʀᴀ 6 sᴀᴍᴘᴀɪ 64 ᴋᴀʀᴀᴋᴛᴇʀ!</b></blockquote>"
        )

    # Kombinasi karakter: Huruf besar, kecil, angka, dan simbol
    chars = string.ascii_letters + string.digits + "!@#$%^&*()_+-="
    password = "".join(secrets.choice(chars) for _ in range(length))

    res_text = (
        f"<blockquote><b>{brhsl} ᴘᴀssᴡᴏʀᴅ ʀᴀɴᴅᴏᴍ ʙᴇʀʜᴀsɪʟ ᴅɪʙᴜᴀᴛ</b>\n\n"
        f"<b>ᚗ ᴘᴀssᴡᴏʀᴅ :</b> <code>{password}</code>\n"
        f"<b>ᚗ ᴘᴀɴᴊᴀɴɢ :</b> <code>{length} ᴋᴀʀᴀᴋᴛᴇʀ</code>\n\n"
        f"<b>⌭ sᴛᴀᴛᴜs :</b> sᴀɴɢᴀᴛ ᴋᴜᴀᴛ ᴅᴀɴ ᴀᴍᴀɴ</blockquote>"
    )
    
    await message.reply_text(res_text)
    