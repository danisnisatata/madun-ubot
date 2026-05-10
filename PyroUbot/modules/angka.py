import random
from PyroUbot import *

__MODULE__ = "ᴛᴇʙᴀᴋᴀɴɢᴋᴀ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴛᴇʙᴀᴋᴀɴɢᴋᴀ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴀɴɢᴋᴀ</code>
⊷ ᴍᴇᴍᴜʟᴀɪ ᴘᴇʀᴍᴀɪɴᴀɴ ᴛᴇʙᴀᴋ ᴀɴɢᴋᴀ (𝟷-𝟷𝟶).
ᚗ <code>{0}ᴊᴀᴡᴀʙ</code> [ᴀɴɢᴋᴀ]
⊷ ᴍᴇɴᴊᴀᴡᴀʙ ᴀɴɢᴋᴀ ʏᴀɴɢ sᴇᴅᴀɴɢ ᴅɪᴍᴀɪɴᴋᴀɴ.
ᚗ <code>{0}ᴀɴɢᴋᴀsᴋᴏʀ</code>
⊷ ᴍᴇʟɪʜᴀᴛ ᴅᴀꜰᴛᴀʀ sᴋᴏʀ ᴛᴇʀᴛɪɴɢɢɪ.</blockquote>
"""

GAME = {}
SCORE = {}

@PY.UBOT("angka")
@PY.BOT("angka")
@PY.TOP_CMD
async def angka_start_handler(client, message):
    prs_emo = await EMO.PROSES(client)
    chat_id = message.chat.id
    
    # Generate angka random 1-10
    nomor = random.randint(1, 10)
    GAME[chat_id] = nomor

    await message.reply_text(
        f"<blockquote><b>🎲 ᴛᴇʙᴀᴋ ᴀɴɢᴋᴀ ɪǫʙᴀʟ ᴜʙᴏᴛ</b>\n\n"
        f"ᴀᴋᴜ sᴜᴅᴀʜ ᴍᴇɴʏɪᴍᴘᴀɴ ᴀɴɢᴋᴀ ᴅᴀʀɪ <b>𝟷 sᴀᴍᴘᴀɪ 𝟷𝟶</b>.\n"
        f"sɪᴀᴘᴀ ᴄᴇᴘᴀᴛ ᴅɪᴀ ʏᴀɴɢ ᴅᴀᴘᴇᴛ ᴘᴏɪɴ! {prs_emo}\n\n"
        f"<b>ᚗ ᴊᴀᴡᴀʙ :</b> <code>.ᴊᴀᴡᴀʙ [ᴀɴɢᴋᴀ]</code>\n\n"
        f"<b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>"
    )

@PY.UBOT("jawab")
@PY.BOT("jawab")
@PY.TOP_CMD
async def jawab_handler(client, message):
    ggl_emo = await EMO.GAGAL(client)
    brhsl_emo = await EMO.BERHASIL(client)
    chat_id = message.chat.id

    if chat_id not in GAME:
        return await message.reply_text(f"<blockquote><b>{ggl_emo} ʙᴇʟᴜᴍ ᴀᴅᴀ ɢᴀᴍᴇ!</b>\nᚗ ᴋᴇᴛɪᴋ <code>.ᴀɴɢᴋᴀ</code> ᴜɴᴛᴜᴋ ᴍᴜʟᴀɪ.</blockquote>")

    args = get_arg(message)
    if not args or not args.isdigit():
        return await message.reply_text(f"<blockquote><b>{ggl_emo} ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ᴀɴɢᴋᴀ!</b>\nᚗ ᴄᴏɴᴛᴏʜ: <code>.ᴊᴀᴡᴀʙ 𝟻</code></blockquote>")

    tebakan = int(args)
    jawaban_benar = GAME[chat_id]

    if tebakan == jawaban_benar:
        user = message.from_user
        uid = user.id
        name = user.first_name

        # Simpan Skor (Bisa dipindah ke DB jika ingin permanen)
        if uid not in SCORE:
            SCORE[uid] = {"name": name, "poin": 0}
        
        SCORE[uid]["poin"] += 1
        del GAME[chat_id]

        await message.reply_text(
            f"<blockquote><b>{brhsl_emo} ᴊᴀᴡᴀʙᴀɴ ʙᴇɴᴀʀ!</b>\n\n"
            f"<b>ᚗ ᴀɴɢᴋᴀ :</b> <code>{jawaban_benar}</code>\n"
            f"<b>ᚗ ᴘᴇᴍᴇɴᴀɴɢ :</b> {user.mention}\n"
            f"<b>ᚗ ᴛᴏᴛᴀʟ sᴋᴏʀ :</b> <code>{SCORE[uid]['poin']}</code> ᴘᴏɪɴ\n\n"
            f"<b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>"
        )
    else:
        await message.reply_text(f"<blockquote><b>{ggl_emo} sᴀʟᴀʜ!</b>\nᴄᴏʙᴀ ʟᴀɢɪ ʏᴀ ᴍᴀɴɪs... 😜</blockquote>")

@PY.UBOT("angkaskor")
@PY.BOT("angkaskor")
@PY.TOP_CMD
async def skor_handler(client, message):
    if not SCORE:
        return await message.reply_text("<blockquote><b>📭 ʙᴇʟᴜᴍ ᴀᴅᴀ sᴋᴏʀ ᴛᴇʀᴄᴀᴛᴀᴛ.</b></blockquote>")

    # Sortir skor tertinggi
    sorted_score = sorted(SCORE.items(), key=lambda x: x[1]['poin'], reverse=True)
    
    res = "<blockquote><b>🏆 ᴘᴀᴘᴀɴ sᴋᴏʀ ᴛᴇʙᴀᴋ ᴀɴɢᴋᴀ</b>\n\n"
    for i, (uid, data) in enumerate(sorted_score[:10], 1):
        res += f"{i}. {data['name']} ⤶ <code>{data['poin']}</code> ᴘᴏɪɴ\n"
    
    res += f"\n<b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>"
    await message.reply_text(res)
    