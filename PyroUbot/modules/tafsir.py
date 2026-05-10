import requests
import random
from PyroUbot import *

def get_random_tafsir(query):
    API_URL = "https://api.botcahx.eu.org/api/islamic/tafsirsurah"
    API_KEY = "@iqbalnew77"

    params = {"text": query, "apikey": API_KEY}

    try:
        response = requests.get(API_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        if data.get("status") and "result" in data:
            tafsir_list = data["result"]
            if tafsir_list:
                tafsir = random.choice(tafsir_list)
                # Format hasil dengan Smallcaps dan Premium Style
                return (
                    f"<blockquote><b>📖 sᴜʀᴀʜ: {tafsir['surah']}</b>\n\n"
                    f"{tafsir['tafsir']}\n\n"
                    f"<b>🔗 <a href='{tafsir['source']}'>sᴜᴍʙᴇʀ ᴛᴀꜰsɪʀ</a></b></blockquote>"
                )
        return "<blockquote><b>❌ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ ᴛᴀꜰsɪʀ ʏᴀɴɢ sᴇsᴜᴀɪ.</b></blockquote>"

    except requests.exceptions.Timeout:
        return "<blockquote><b>⌛ ᴡᴀᴋᴛᴜ ʜᴀʙɪs, sɪʟᴀᴋᴀɴ ᴄᴏʙᴀ ʟᴀɢɪ ɴᴀɴᴛɪ.</b></blockquote>"
    except requests.exceptions.RequestException as e:
        return f"<blockquote><b>⚠️ ᴇʀʀᴏʀ:</b> <code>{str(e)}</code></blockquote>"

@PY.UBOT("tafsir")
@PY.TOP_CMD
async def tafsir_handler(client, message):
    if len(message.command) < 2:
        return await message.reply(
            "<blockquote><b>📖 ᴘᴀɴᴅᴜᴀɴ ᴛᴀꜰsɪʀ</b>\n\n"
            "ᚗ ɢᴜɴᴀᴋᴀɴ: <code>.ᴛᴀꜰsɪʀ</code> [ᴋᴀᴛᴀ ᴋᴜɴᴄɪ]\n"
            "ᚗ ᴄᴏɴᴛᴏʜ: <code>.ᴛᴀꜰsɪʀ ᴍᴜʜᴀᴍᴍᴀᴅ</code></blockquote>"
        )

    prs = await EMO.PROSES(client)
    query = " ".join(message.command[1:])
    status_msg = await message.reply(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇɴᴄᴀʀɪ ᴛᴀꜰsɪʀ...</b></blockquote>")

    tafsir_text = get_random_tafsir(query)

    await status_msg.edit(tafsir_text, disable_web_page_preview=True)

__MODULE__ = "ᴛᴀꜰsɪʀ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴛᴀꜰsɪʀ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴛᴀꜰsɪʀ</code> [ᴋᴀᴛᴀ ᴋᴜɴᴄɪ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴᴄᴀʀɪ ᴛᴀꜰsɪʀ sᴜʀᴀʜ ʙᴇʀᴅᴀsᴀʀᴋᴀɴ ᴋᴀᴛᴀ ᴋᴜɴᴄɪ ᴀᴛᴀᴜ ɴᴀᴍᴀ sᴜʀᴀʜ.</blockquote>
"""
