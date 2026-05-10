import random
from PyroUbot import *

__MODULE__ = "ǫᴜɪᴄᴋǫᴜɪᴢ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ǫᴜɪᴄᴋǫᴜɪᴢ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ǫᴜɪᴢ</code>
⊷ ᴍᴇᴍᴜʟᴀɪ ᴋᴜɪs ᴛᴇʙᴀᴋ ᴄᴇᴘᴀᴛ.
ᚗ <code>{0}ǫᴜɪᴢsᴋᴏʀ</code>
⊷ ᴍᴇʟɪʜᴀᴛ ᴘᴀᴘᴀɴ sᴋᴏʀ ᴛᴇʀᴛɪɴɢɢɪ.

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴊᴀᴡᴀʙ ʟᴀɴɢsᴜɴɢ ᴅɪ ᴄʜᴀᴛ ᴛᴀɴᴘᴀ ᴀᴡᴀʟᴀɴ ᴘʀᴇꜰɪx ᴜɴᴛᴜᴋ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ᴘᴏɪɴ!</blockquote>
"""

QUIZ_DATA = [
    {"q": "ɪʙᴜᴋᴏᴛᴀ ɪɴᴅᴏɴᴇsɪᴀ?", "a": "jakarta"},
    {"q": "ᴘʀᴇsɪᴅᴇɴ ᴘᴇʀᴛᴀᴍᴀ ɪɴᴅᴏɴᴇsɪᴀ?", "a": "soekarno"},
    {"q": "𝟸 + 𝟻 = ?", "a": "7"},
    {"q": "ʙᴀʜᴀsᴀ ᴘᴇᴍʀᴏɢʀᴀᴍᴀɴ ʟᴏɢᴏ ᴜʟᴀʀ?", "a": "python"},
    {"q": "ᴀᴘʟɪᴋᴀsɪ ᴄʜᴀᴛ ᴡᴀʀɴᴀ ʙɪʀᴜ?", "a": "telegram"},
    {"q": "ɢᴜɴᴜɴɢ ᴛᴇʀᴛɪɢɢɪ ᴅɪ ᴅᴜɴɪᴀ?", "a": "everest"},
    {"q": "ʟᴀᴜᴛ ᴛᴇʀʟᴜᴀs ᴅɪ ᴅᴜɴɪᴀ?", "a": "pasifik"},
    {"q": "ʜᴇᴡᴀɴ ᴛᴇʀᴄᴇᴘᴀᴛ ᴅɪ ᴅᴀʀᴀᴛ?", "a": "cheetah"},
]

ACTIVE_GAME = {}
PLAYER_SCORE = {}

@PY.UBOT("quiz")
@PY.TOP_CMD
async def start_quiz_handler(client, message):
    prs = await EMO.PROSES(client)
    chat_id = message.chat.id
    
    soal = random.choice(QUIZ_DATA)
    ACTIVE_GAME[chat_id] = soal

    res = (
        f"<blockquote><b>🎯 ǫᴜɪᴄᴋ ǫᴜɪᴢ ᴘʀᴇᴍɪᴜᴍ</b>\n\n"
        f"<b>❓ ᴘᴇʀᴛᴀɴʏᴀᴀɴ :</b>\n"
        f"<code>{soal['q']}</code>\n\n"
        f"<b>{prs} ᴊᴀᴡᴀʙ ʟᴀɴɢsᴜɴɢ ᴅɪ ᴄʜᴀᴛ!</b>\n\n"
        f"<b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>"
    )
    await message.reply_text(res)

@PY.UBOT("quizskor")
@PY.TOP_CMD
async def score_quiz_handler(client, message):
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)
    
    if not PLAYER_SCORE:
        return await message.reply_text(f"<blockquote><b>{ggl} ʙᴇʟᴜᴍ ᴀᴅᴀ sᴋᴏʀ ᴛᴇʀᴄᴀᴛᴀᴛ.</b></blockquote>")

    # Sort skor tertinggi
    sorted_scores = sorted(PLAYER_SCORE.items(), key=lambda x: x[1], reverse=True)
    
    res = f"<blockquote><b>{brhsl} ᴘᴀᴘᴀɴ sᴋᴏʀ ǫᴜɪᴄᴋ ǫᴜɪᴢ</b>\n\n"
    for i, (uid, sc) in enumerate(sorted_scores[:10], 1):
        res += f"<b>{i}.</b> ɪᴅ: <code>{uid}</code> ⤶ <b>{sc} ᴘᴏɪɴ</b>\n"
    
    res += f"\n<b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>"
    await message.reply_text(res)

# 🛠️ FIX: Gunakan @PY.UBOT dengan filters mentah agar tidak error 'client is not defined'
@PY.UBOT(filters.group & ~filters.bot & ~filters.me)
async def auto_check_quiz(client, message):
    chat_id = message.chat.id
    if chat_id not in ACTIVE_GAME:
        return

    # Pastikan pesan ada teksnya
    if not message.text:
        return

    jawaban_user = message.text.lower().strip()
    jawaban_benar = ACTIVE_GAME[chat_id]["a"].lower()

    if jawaban_user == jawaban_benar:
        brhsl = await EMO.BERHASIL(client)
        user = message.from_user
        uid = user.id

        PLAYER_SCORE[uid] = PLAYER_SCORE.get(uid, 0) + 1
        del ACTIVE_GAME[chat_id]

        res = (
            f"<blockquote><b>{brhsl} ᴊᴀᴡᴀʙᴀɴ ʙᴇɴᴀʀ!</b>\n\n"
            f"<b>ᚗ ᴘᴇᴍᴇɴᴀɴɢ :</b> {user.mention}\n"
            f"<b>ᚗ ᴛᴏᴛᴀʟ sᴋᴏʀ :</b> <code>{PLAYER_SCORE[uid]} ᴘᴏɪɴ</code>\n\n"
            f"<b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>"
        )
        await message.reply_text(res)
        