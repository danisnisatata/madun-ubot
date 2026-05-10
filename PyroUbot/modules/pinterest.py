import aiohttp
from PyroUbot import *

__MODULE__ = "ᴘɪɴᴛᴇʀᴇsᴛ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴘɪɴᴛᴇʀᴇsᴛ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴘɪɴ</code> [ʟɪɴᴋ ᴘɪɴᴛᴇʀᴇsᴛ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴɢᴜɴᴅᴜʜ ꜰᴏᴛᴏ ᴀᴛᴀᴜ ᴠɪᴅᴇᴏ ᴅᴀʀɪ ᴘɪɴᴛᴇʀᴇsᴛ sᴇᴄᴀʀᴀ ᴏᴛᴏᴍᴀᴛɪs.</blockquote>
"""

@PY.UBOT("pin")
async def pinterest_handler(client, message):
    # EMO tetap ambil dari database ubot lu
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)
    
    args = get_arg(message)
    if not args:
        return await message.reply_text(
            f"<blockquote><b>{ggl} ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ʟɪɴᴋ!</b>\nᚗ ᴄᴏɴᴛᴏʜ: <code>.ᴘɪɴ [ʟɪɴᴋ ᴘɪɴᴛᴇʀᴇsᴛ]</code></blockquote>"
        )

    status_msg = await message.reply_text(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ᴅᴏᴡɴʟᴏᴀᴅ...</b></blockquote>")

    async with aiohttp.ClientSession() as session:
        try:
            api_url = f"https://api.botcahx.eu.org/api/dowloader/pinterest?url={args}&apikey=@iqbalnew77"
            async with session.get(api_url) as resp:
                data = await resp.json()

            if not data.get("status") or "result" not in data:
                return await status_msg.edit(f"<blockquote><b>{ggl} ɢᴀɢᴀʟ ᴍᴇɴɢᴜɴᴅᴜʜ!</b>\nᚗ ʟɪɴᴋ ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ ᴀᴛᴀᴜ ᴀᴘɪ ʟɪᴍɪᴛ.</blockquote>")

            res = data["result"]
            media_url = res.get("url")
            is_video = res.get("type") == "video"
            
            caption = (
                f"<blockquote><b>{brhsl} ᴘɪɴᴛᴇʀᴇsᴛ ᴅᴏᴡɴʟᴏᴀᴅᴇʀ</b>\n\n"
                f"<b>ᚗ ᴛʏᴘᴇ :</b> <code>{'ᴠɪᴅᴇᴏ' if is_video else 'ꜰᴏᴛᴏ'}</code>\n"
                f"<b>ᚗ ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>"
            )

            if is_video:
                await client.send_video(message.chat.id, media_url, caption=caption)
            else:
                await client.send_photo(message.chat.id, media_url, caption=caption)
            
            await status_msg.delete()
            
        except Exception as e:
            await status_msg.edit(f"<blockquote><b>{ggl} ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ:</b>\n<code>{str(e)}</code></blockquote>")
            