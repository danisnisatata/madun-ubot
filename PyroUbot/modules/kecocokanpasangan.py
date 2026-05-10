import asyncio
import requests
from PyroUbot import *

__MODULE__ = "ᴘᴀsᴀɴɢᴀɴ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴘᴀsᴀɴɢᴀɴ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴘᴀsᴀɴɢᴀɴ</code> [ɴᴀᴍᴀ1], [ɴᴀᴍᴀ2]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇʀᴀᴍᴀʟ ᴋᴇᴄᴏᴄᴏᴋᴀɴ ᴘᴀsᴀɴɢᴀɴ ʙᴇʀᴅᴀsᴀʀᴋᴀɴ ᴘʀɪᴍʙᴏɴ ɴᴀᴍᴀ.</blockquote>
"""

@PY.UBOT("pasangan")
async def cek_kecocokan(client, message):
    prs_emo = await EMO.PROSES(client)
    brhsl_emo = await EMO.BERHASIL(client)
    ggl_emo = await EMO.GAGAL(client)
    
    args = get_arg(message)
    if not args or "," not in args:
        return await message.reply_text(
            f"<blockquote><b>{ggl_emo} ᴍᴏʜᴏɴ ɢᴜɴᴀᴋᴀɴ ꜰᴏʀᴍᴀᴛ:</b>\nᚗ <code>.ᴘᴀsᴀɴɢᴀɴ ɴᴀᴍᴀ1, ɴᴀᴍᴀ2</code></blockquote>"
        )

    nama1, nama2 = map(str.strip, args.split(",", 1))
    status_msg = await message.reply_text(f"<blockquote><b>{prs_emo} sᴇᴅᴀɴɢ ᴍᴇʀᴀᴍᴀʟ ᴋᴇᴄᴏᴄᴏᴋᴀɴ...</b></blockquote>")

    def fetch_primbon():
        try:
            url = f"https://api.siputzx.my.id/api/primbon/kecocokan_nama_pasangan?nama1={nama1}&nama2={nama2}"
            response = requests.get(url, timeout=20)
            return response.json()
        except:
            return None

    loop = asyncio.get_event_loop()
    data = await loop.run_in_executor(None, fetch_primbon)

    if data and data.get("status"):
        hasil = data["data"]
        teks = f"""
<blockquote><b><emoji id=6026321200597176575>🃏</emoji> ᴋᴇᴄᴏᴄᴏᴋᴀɴ ᴘᴀsᴀɴɢᴀɴ <emoji id=6026321200597176575>🃏</emoji></b>

<b>ᚗ ɴᴀᴍᴀ ᴀɴᴅᴀ :</b> <code>{hasil['nama_anda']}</code>
<b>ᚗ ᴘᴀsᴀɴɢᴀɴ :</b> <code>{hasil['nama_pasangan']}</code>

<b><emoji id=5217466996337165348>👍</emoji> sɪsɪ ᴘᴏsɪᴛɪꜰ :</b>
<i>{hasil['sisi_positif']}</i>

<b><emoji id=5436223772510142944>👎</emoji> sɪsɪ ɴᴇɢᴀᴛɪꜰ :</b>
<i>{hasil['sisi_negatif']}</i>

<b><emoji id=5238039443008408242>💌</emoji> ᴄᴀᴛᴀᴛᴀɴ :</b>
<u>{hasil['catatan']}</u>

<b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>"""
        
        try:
            await message.reply_photo(hasil["gambar"], caption=teks)
            await status_msg.delete()
        except:
            await status_msg.edit(teks)
    else:
        await status_msg.edit(f"<blockquote><b>{ggl_emo} ɢᴀɢᴀʟ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ᴅᴀᴛᴀ ʀᴀᴍᴀʟᴀɴ!</b></blockquote>")
        