import random
import string
import requests
from datetime import datetime, timedelta
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bs4 import BeautifulSoup
from PyroUbot import *

__MODULE__ = "ᴛᴇᴍᴘ ᴍᴀɪʟ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴛᴇᴍᴘ ᴍᴀɪʟ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴛᴇᴍᴘᴍᴀɪʟ</code> → ᴍᴇᴍʙᴜᴀᴛ ᴇᴍᴀɪʟ sᴇᴍᴇɴᴛᴀʀᴀ.
ᚗ <code>{0}ᴄᴇᴋᴍᴀɪʟ</code> → ᴍᴇɴɢᴇᴄᴇᴋ ɪɴʙᴏx ᴇᴍᴀɪʟ.
ᚗ <code>{0}ʀᴇsᴇᴛᴍᴀɪʟ</code> → ᴍᴇɴɢɢᴀɴᴛɪ ᴀʟᴀᴍᴀᴛ ᴇᴍᴀɪʟ.

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴇᴍᴀɪʟ sᴇᴍᴇɴᴛᴀʀᴀ ʙᴇʀʟᴀᴋᴜ sᴇʟᴀᴍᴀ 30 ᴍᴇɴɪᴛ.</blockquote>
"""

sessions_mail = {}
DOMAINS = ["1secmail.com", "1secmail.net", "1secmail.org"]

def generate_email():
    name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    domain = random.choice(DOMAINS)
    return name, domain

def fetch_messages(login, domain):
    url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={login}&domain={domain}"
    return requests.get(url, timeout=15).json()

def read_message(login, domain, msg_id):
    url = f"https://www.1secmail.com/api/v1/?action=readMessage&login={login}&domain={domain}&id={msg_id}"
    return requests.get(url, timeout=15).json()

@PY.UBOT("tempmail")
@PY.TOP_CMD
async def tempmail(client: Client, message):
    user_id = message.from_user.id
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)

    # Clean expired sessions
    expired = [uid for uid, data in sessions_mail.items() 
               if datetime.utcnow() - data["created_at"] > timedelta(minutes=30)]
    for uid in expired: del sessions_mail[uid]

    if user_id in sessions_mail:
        email = sessions_mail[user_id]["email"]
        return await message.reply_text(
            f"<blockquote><b>{brhsl} ᴛᴇᴍᴘᴍᴀɪʟ ᴀᴋᴛɪꜰ</b>\n\n"
            f"<b>📩 ᴇᴍᴀɪʟ:</b> <code>{email}</code>\n"
            f"<b>⏳ ʙᴇʀʟᴀᴋᴜ:</b> ±30 ᴍᴇɴɪᴛ\n\n"
            f"ᚗ ᴄᴇᴋ ɪɴʙᴏx: <code>.ᴄᴇᴋᴍᴀɪʟ</code>\n"
            f"ᚗ ɢᴀɴᴛɪ ᴇᴍᴀɪʟ: <code>.ʀᴇsᴇᴛᴍᴀɪʟ</code></blockquote>"
        )

    login, domain = generate_email()
    email = f"{login}@{domain}"
    sessions_mail[user_id] = {
        "login": login, "domain": domain, "email": email, "created_at": datetime.utcnow()
    }

    await message.reply_text(
        f"<blockquote><b>{brhsl} ᴛᴇᴍᴘᴍᴀɪʟ ʙᴇʀʜᴀsɪʟ ᴅɪʙᴜᴀᴛ</b>\n\n"
        f"<b>📩 ᴇᴍᴀɪʟ:</b> <code>{email}</code>\n"
        f"<b>⏳ ʙᴇʀʟᴀᴋᴜ:</b> ±30 ᴍᴇɴɪᴛ\n\n"
        f"ᚗ ᴄᴇᴋ ɪɴʙᴏx: <code>.ᴄᴇᴋᴍᴀɪʟ</code>\n"
        f"ᚗ ɢᴀɴᴛɪ ᴇᴍᴀɪʟ: <code>.ʀᴇsᴇᴛᴍᴀɪʟ</code></blockquote>"
    )

@PY.UBOT("cekmail")
@PY.TOP_CMD
async def cekmail(client: Client, message):
    user_id = message.from_user.id
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)

    if user_id not in sessions_mail:
        return await message.reply_text(f"<blockquote><b>{ggl} ᴀɴᴅᴀ ʙᴇʟᴜᴍ ᴍᴇᴍɪʟɪᴋɪ ᴛᴇᴍᴘᴍᴀɪʟ.</b></blockquote>")

    data = sessions_mail[user_id]
    status_msg = await message.reply_text(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇɴɢᴇᴄᴇᴋ ɪɴʙᴏx...</b></blockquote>")
    msgs = fetch_messages(data["login"], data["domain"])

    if not msgs:
        return await status_msg.edit(f"<blockquote><b>📭 ɪɴʙᴏx <code>{data['email']}</code> ᴍᴀsɪʜ ᴋᴏsᴏɴɢ.</b></blockquote>")

    hasil = []
    for msg in msgs:
        detail = read_message(data["login"], data["domain"], msg["id"])
        soup = BeautifulSoup(detail.get('htmlBody') or detail.get('textBody') or '-', 'html.parser')
        clean_text = soup.get_text()
        hasil.append(
            f"<blockquote><b>📬 ᴇᴍᴀɪʟ ᴍᴀsᴜᴋ</b>\n"
            f"<b>👤 ᴅᴀʀɪ:</b> <code>{detail.get('from')}</code>\n"
            f"<b>📚 sᴜʙᴊᴇᴋ:</b> <code>{detail.get('subject')}</code>\n\n"
            f"<b>📜 ɪsɪ:</b>\n<code>{clean_text[:500]}</code></blockquote>"
        )

    await status_msg.delete()
    await message.reply("\n".join(hasil), disable_web_page_preview=True)

@PY.UBOT("resetmail")
@PY.TOP_CMD
async def resetmail(client: Client, message):
    user_id = message.from_user.id
    sessions_mail.pop(user_id, None)
    await tempmail(client, message)
    