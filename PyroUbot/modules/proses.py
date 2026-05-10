import asyncio
from PyroUbot import *

__MODULE__ = "ᴘʀᴏꜱᴇꜱ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴘʀᴏꜱᴇꜱ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴘʀᴏsᴇs</code> [ɴᴀᴍᴇ ɪᴛᴇᴍ],[ᴛᴇsᴛɪ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇᴍʙᴜᴀᴛ ɴᴏᴛɪꜰɪᴋᴀsɪ ʙᴀʜᴡᴀ ᴘᴇsᴀɴᴀɴ sᴇᴅᴀɴɢ ᴅɪᴘʀᴏsᴇs sᴇᴄᴀʀᴀ ᴘʀᴏꜰᴇsɪᴏɴᴀʟ.</blockquote>
"""

@PY.UBOT("proses")
@PY.TOP_CMD
async def proses_handler(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)

    status_msg = await message.reply_text(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ᴛʀᴀɴsᴀᴋsɪ...</b></blockquote>")
    await asyncio.sleep(2) # Delay biar kerasa lagi kerja

    try:
        args = get_arg(message)
        if not args or "," not in args:
            return await status_msg.edit(
                f"<blockquote><b>{ggl} ꜰᴏʀᴍᴀᴛ sᴀʟᴀʜ!</b>\nᚗ ɢᴜɴᴀᴋᴀɴ: <code>.ᴘʀᴏsᴇs ɴᴀᴍᴀ ʙᴀʀᴀɴɢ,ʟɪɴᴋ ᴛᴇsᴛɪ</code></blockquote>"
            )

        parts = args.split(",", 1)
        name_item = parts[0].strip()
        testi = parts[1].strip()

        response = (
            f"<blockquote><b>{brhsl} ᴘᴇsᴀɴᴀɴ ᴅɪᴘʀᴏsᴇs</b>\n\n"
            f"<b>ᚗ ʙᴀʀᴀɴɢ :</b> <code>{name_item}</code>\n"
            f"<b>ᚗ ᴛᴇsᴛɪᴍᴏɴɪ :</b> <a href='{testi}'>ᴋʟɪᴋ ᴅɪsɪɴɪ</a>\n\n"
            f"<b>⌭ ɴᴏᴛᴇ :</b>\nsᴇᴅᴀɴɢ ᴅɪᴋᴇʀᴊᴀᴋᴀɴ, ᴍᴏʜᴏɴ ᴛɪᴅᴀᴋ sᴘᴀᴍ ᴏᴡɴᴇʀ ᴀɢᴀʀ ᴘʀᴏsᴇs ʟᴇʙɪʜ ᴄᴇᴘᴀᴛ. ᴛᴇʀɪᴍᴀ ᴋᴀsɪʜ!</blockquote>\n"
            f"<blockquote><b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ : ɪǫʙᴀʟᴜʙᴏᴛᴠɪᴘ_</b></blockquote>"
        )
        
        await status_msg.edit(response, disable_web_page_preview=True)

    except Exception as e:
        await status_msg.edit(f"<blockquote><b>{ggl} ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ:</b>\n<code>{str(e)}</code></blockquote>")
        