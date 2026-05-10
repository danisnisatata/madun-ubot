import requests
from PyroUbot import *

__MODULE__ = "sʜɪᴏ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sʜɪᴏ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}sʜɪᴏ</code> [sʜɪᴏ] [ᴛɢʟ] [ʙʟɴ] [ᴛʜɴ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇʟɪʜᴀᴛ ʀᴀᴍᴀʟᴀɴ ɴᴀsɪʙ ʙᴇʀᴅᴀsᴀʀᴋᴀɴ sʜɪᴏ ᴅᴀɴ ᴛᴀɴɢɢᴀʟ ʟᴀʜɪʀ.</blockquote>
"""

@PY.UBOT("shio")
@PY.TOP_CMD
async def get_shio(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)
    
    args = message.text.split()
    if len(args) < 5:
        return await message.reply_text(
            f"<blockquote><b>{ggl} ꜰᴏʀᴍᴀᴛ sᴀʟᴀʜ!</b>\nᚗ ᴄᴏɴᴛᴏʜ: <code>.sʜɪᴏ ɴᴀɢᴀ 22 03 2000</code></blockquote>"
        )

    shio, tanggal, bulan, tahun = args[1], args[2], args[3], args[4]
    status_msg = await message.reply_text(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇᴍʙᴀᴄᴀ ᴛᴀᴋᴅɪʀ...</b></blockquote>")
    
    API_URL = f"https://api.botcahx.eu.org/api/primbon/shio?shio={shio}&tanggal={tanggal}&bulan={bulan}&tahun={tahun}&apikey=@iqbalnew77"

    try:
        response = requests.get(API_URL).json()

        if not response.get("status") or not response["result"].get("status"):
            return await status_msg.edit(f"<blockquote><b>{ggl} ᴅᴀᴛᴀ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ ᴀᴛᴀᴜ API ʟɪᴍɪᴛ.</b></blockquote>")

        result = response["result"]["message"]
        nama = result["nama"]
        arti = result["arti"]

        reply_text = (
            f"<blockquote><b>{brhsl} ʀᴀᴍᴀʟᴀɴ sʜɪᴏ ᴘʀᴇᴍɪᴜᴍ</b>\n"
            f"━━━━━━━━━━━━━━━━━━\n"
            f"<b>ᚗ sʜɪᴏ :</b> <code>{nama}</code>\n"
            f"<b>ᚗ ᴛᴀɴɢɢᴀʟ :</b> <code>{tanggal}-{bulan}-{tahun}</code>\n"
            f"━━━━━━━━━━━━━━━━━━\n"
            f"<b>⌭ ᴀʀᴛɪ & ɴᴀsɪʙ :</b>\n"
            f"<i>{arti}</i>\n"
            f"━━━━━━━━━━━━━━━━━━</blockquote>"
        )

        await status_msg.edit(reply_text)

    except Exception as e:
        await status_msg.edit(f"<blockquote><b>{ggl} ᴇʀʀᴏʀ:</b> <code>{str(e)}</code></blockquote>")
        