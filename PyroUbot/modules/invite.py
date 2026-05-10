import asyncio
from PyroUbot import *

__MODULE__ = "ɪɴᴠɪᴛᴇ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ɪɴᴠɪᴛᴇ ɢᴀᴄᴏʀ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ɪɴᴠɪᴛᴇ</code> [ᴜsᴇʀɴᴀᴍᴇ/ɪᴅ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴɢᴜɴᴅᴀɴɢ ᴘᴇɴɢɢᴜɴᴀ ᴋᴇ ᴅᴀʟᴀᴍ ɢʀᴜᴘ ɪɴɪ.</blockquote>
"""

@PY.UBOT("invite")
@PY.TOP_CMD
@PY.GROUP
async def invite_handler(client, message):
    # --- EMOJI & STATUS ---
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    ktrng = await EMO.BL_KETERANGAN(client)
    
    # Ambil argumen
    args = get_arg(message)
    if not args:
        return await message.reply_text(
            f"<blockquote><b>{ktrng} ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ᴜsᴇʀɴᴀᴍᴇ!</b></blockquote>"
        )

    mg = await message.reply(f"<blockquote><b>{prs} ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ᴘᴇɴɢɢᴜɴᴀ...</b></blockquote>")
    
    # Split daftar username/ID
    user_list = args.split()
    
    try:
        # Pake gaya lama yang lu suka
        await client.add_chat_members(message.chat.id, user_list)
        
        await mg.edit(
            f"<blockquote><b>{brhsl} ʙᴇʀʜᴀsɪʟ ᴅɪᴛᴀᴍʙᴀʜᴋᴀɴ!</b>\n\n"
            f"<b>ᚗ ᴛᴏᴛᴀʟ :</b> <code>{len(user_list)}</code> ᴘᴇɴɢɢᴜɴᴀ\n"
            f"<b>ᚗ ɢʀᴜᴘ :</b> <code>{message.chat.title}</code></blockquote>"
        )
    except Exception as e:
        # Biar lu tau kenapa dia gak masuk
        error_msg = str(e)
        if "USER_PRIVACY_RESTRICTED" in error_msg:
            reason = "ᴘʀɪᴠᴀsɪ ᴜsᴇʀ (ᴍʏ ᴄᴏɴᴛᴀᴄᴛs)"
        elif "USER_NOT_MUTUAL_CONTACT" in error_msg:
            reason = "ʙᴜᴋᴀɴ ᴋᴏɴᴛᴀᴋ ᴛɪᴍʙᴀʟ ʙᴀʟɪᴋ"
        elif "PEER_ID_INVALID" in error_msg:
            reason = "ᴜsᴇʀɴᴀᴍᴇ/ɪᴅ ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ"
        else:
            reason = error_msg

        await mg.edit(
            f"<blockquote><b>{ggl} ɢᴀɢᴀʟ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ!</b>\n"
            f"<b>ᚗ ᴀʟᴀsᴀɴ :</b> <code>{reason}</code></blockquote>"
        )
        