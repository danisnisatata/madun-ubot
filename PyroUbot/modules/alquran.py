import aiohttp
from PyroUbot import *

API_URL = "https://api.quran.gading.dev"

async def fetch_ayat(surah: int, ayat: int):
    url = f"{API_URL}/surah/{surah}/{ayat}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, timeout=15) as res:
            if res.status != 200:
                raise Exception("ᴀʏᴀᴛ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ")
            data = await res.json()
            ayat_data = data["data"]
            return (
                ayat_data["surah"]["name"]["transliteration"]["id"],
                ayat_data["text"]["arab"],
                ayat_data["text"]["transliteration"]["en"],
                ayat_data["translation"]["id"],
                ayat_data["audio"]["primary"]
            )

__MODULE__ = "ᴀʟǫᴜʀᴀɴ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀʟǫᴜʀᴀɴ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴀʟǫᴜʀᴀɴ</code> [ɴᴏ_sᴜʀᴀʜ] [ɴᴏ_ᴀʏᴀᴛ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴᴀᴍᴘɪʟᴋᴀɴ ᴀʏᴀᴛ ᴀʟ-ǫᴜʀ'ᴀɴ ʙᴇsᴇʀᴛᴀ ᴀʀᴛɪ ᴅᴀɴ ᴀᴜᴅɪᴏ ᴍᴜʀᴏᴛᴛᴀʟ.

<b>ᚗ ᴄᴏɴᴛᴏʜ :</b> <code>{0}ᴀʟǫᴜʀᴀɴ 1 2</code></blockquote>
"""

@PY.UBOT("alquran")
@PY.TOP_CMD
async def alquran_handler(client, message):
    prs_emo = await EMO.PROSES(client)
    brhsl_emo = await EMO.BERHASIL(client)
    ggl_emo = await EMO.GAGAL(client)
    
    args = message.command[1:]
    if len(args) < 2 or not all(arg.isdigit() for arg in args):
        return await message.reply_text(
            f"<blockquote><b>{ggl_emo} ꜰᴏʀᴍᴀᴛ sᴀʟᴀʜ!</b>\nᚗ ᴄᴏɴᴛᴏʜ: <code>.ᴀʟǫᴜʀᴀɴ 1 7</code></blockquote>"
        )

    status_msg = await message.reply_text(f"<blockquote><b>{prs_emo} ᴍᴇɴɢᴀᴍʙɪʟ ᴀʏᴀᴛ...</b></blockquote>")
    
    surah_no = int(args[0])
    ayat_no = int(args[1])

    try:
        surah_name, arab, latin, arti, audio = await fetch_ayat(surah_no, ayat_no)

        res_text = (
            f"<blockquote><b>📖 {surah_name} : {ayat_no}</b></blockquote>\n\n"
            f"<code>{arab}</code>\n\n"
            f"<blockquote><b>ᚗ ʟᴀᴛɪɴ :</b>\n<i>{latin}</i>\n\n"
            f"<b>ᚗ ᴀʀᴛɪɴʏᴀ :</b>\n{arti}</blockquote>\n"
            f"<b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ"
        )

        await status_msg.edit(res_text)

        await client.send_audio(
            message.chat.id,
            audio=audio,
            caption=f"<blockquote><b>🔊 ᴍᴜʀᴏᴛᴛᴀʟ {surah_name} : {ayat_no}</b>\n\n<b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>",
            title=f"{surah_name} : {ayat_no}",
            performer="ɪǫʙᴀʟ ᴜʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ",
            reply_to_message_id=message.id
        )

    except Exception as e:
        await status_msg.edit(f"<blockquote><b>{ggl_emo} ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ:</b>\n<code>{str(e)}</code></blockquote>")
        