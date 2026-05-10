import os
import requests
from PyroUbot import *

__MODULE__ = "ᴘʟᴀʏʙᴜᴛᴛᴏɴ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴘʟᴀʏʙᴜᴛᴛᴏɴ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ʏᴛɢᴏʟᴅ</code> | <code>ʏᴛsɪʟᴠᴇʀ</code>
ᚗ <code>{0}ɪɢɢᴏʟᴅ</code> | <code>ɪɢsɪʟᴠᴇʀ</code>
ᚗ <code>{0}ꜰʙɢᴏʟᴅ</code> | <code>ꜰʙsɪʟᴠᴇʀ</code>
ᚗ <code>{0}ᴛᴡᴛɢᴏʟᴅ</code> | <code>ᴛᴡᴛsɪʟᴠᴇʀ</code>

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇᴍʙᴜᴀᴛ ɢᴀᴍʙᴀʀ ᴘʟᴀʏʙᴜᴛᴛᴏɴ ᴄᴜsᴛᴏᴍ sᴇsᴜᴀɪ ɴᴀᴍᴀ ʏᴀɴɢ ᴅɪɪɴɢɪɴᴋᴀɴ.</blockquote>
"""

# Base function untuk ambil gambar dari API
def get_playbutton(endpoint, text):
    url = f"https://api.botcahx.eu.org/api/ephoto/{endpoint}"
    params = {"text": text, "apikey": "@iqbalnew77"}
    try:
        response = requests.get(url, params=params, timeout=20)
        if response.status_code == 200 and response.headers.get("Content-Type", "").startswith("image/"):
            return response.content
    except:
        return None
    return None

async def playbutton_handler(client, message, endpoint, title):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)
    
    args = get_arg(message)
    if not args:
        return await message.reply_text(f"<blockquote><b>{ggl} ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ɴᴀᴍᴀ!</b>\nᚗ ᴄᴏɴᴛᴏʜ: <code>{message.text.split()[0]} Iqbal Ubot</code></blockquote>")

    status_msg = await message.reply_text(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ɢᴇɴᴇʀᴀᴛᴇ...</b></blockquote>")
    
    image_content = get_playbutton(endpoint, args)
    
    if image_content:
        temp_file = f"pb_{message.id}.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await client.send_photo(
            message.chat.id,
            photo=temp_file,
            caption=f"<blockquote><b>{brhsl} {title} ʙᴇʀʜᴀsɪʟ ᴅɪʙᴜᴀᴛ!</b>\n\n<b>ᚗ ɴᴀᴍᴀ :</b> <code>{args}</code>\n<b>ᚗ ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>"
        )
        await status_msg.delete()
        os.remove(temp_file)
    else:
        await status_msg.edit(f"<blockquote><b>{ggl} ᴀᴘɪᴋᴇʏ ʙᴇʀᴍᴀsᴀʟᴀʜ ᴀᴛᴀᴜ ʟɪᴍɪᴛ!</b></blockquote>")

# --- YOUTUBE ---
@PY.UBOT("ytgold")
async def ytgold_cmd(client, message):
    await playbutton_handler(client, message, "ytgoldbutton", "ʏᴏᴜᴛᴜʙᴇ ɢᴏʟᴅ")

@PY.UBOT("ytsilver")
async def ytsilver_cmd(client, message):
    await playbutton_handler(client, message, "ytsilverbutton", "ʏᴏᴜᴛᴜʙᴇ sɪʟᴠᴇʀ")

# --- INSTAGRAM ---
@PY.UBOT("iggold")
async def iggold_cmd(client, message):
    await playbutton_handler(client, message, "iggoldbutton", "ɪɴsᴛᴀɢʀᴀᴍ ɢᴏʟᴅ")

@PY.UBOT("igsilver")
async def igsilver_cmd(client, message):
    await playbutton_handler(client, message, "igsilverbutton", "ɪɴsᴛᴀɢʀᴀᴍ sɪʟᴠᴇʀ")

# --- FACEBOOK ---
@PY.UBOT("fbgold")
async def fbgold_cmd(client, message):
    await playbutton_handler(client, message, "fbgoldbutton", "ꜰᴀᴄᴇʙᴏᴏᴋ ɢᴏʟᴅ")

@PY.UBOT("fbsilver")
async def fbsilver_cmd(client, message):
    await playbutton_handler(client, message, "fbsilverbutton", "ꜰᴀᴄᴇʙᴏᴏᴋ sɪʟᴠᴇʀ")

# --- TWITTER ---
@PY.UBOT("twtgold")
async def twtgold_cmd(client, message):
    await playbutton_handler(client, message, "twtgoldbutton", "ᴛᴡɪᴛᴛᴇʀ ɢᴏʟᴅ")

@PY.UBOT("twtsilver")
async def twtsilver_cmd(client, message):
    await playbutton_handler(client, message, "twtsilverbutton", "ᴛᴡɪᴛᴛᴇʀ sɪʟᴠᴇʀ")
    