import asyncio
import requests
from bs4 import BeautifulSoup
from PyroUbot import *

__MODULE__ = "ʜᴇʀᴏ ᴍʟ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʜᴇʀᴏ ᴍʟ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ʜᴇʀᴏᴍʟ</code> [ɴᴀᴍᴀ_ʜᴇʀᴏ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴɢᴀᴍʙɪʟ ɪɴꜰᴏʀᴍᴀsɪ ᴅᴇᴛᴀɪʟ, ʀᴏʟᴇ, ᴅᴀɴ sᴛᴀᴛs ʜᴇʀᴏ ᴍᴏʙɪʟᴇ ʟᴇɢᴇɴᴅs.</blockquote>
"""

def get_hero_info(hero_name):
    # Format nama hero (contoh: "Alucard" atau "Gusion")
    formatted_name = hero_name.replace(" ", "_").title()
    url = f"https://mobile-legends.fandom.com/wiki/{formatted_name}"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.find("h1", {"class": "page-header__title"}).text.strip()
    hero_info = soup.find("aside", {"class": "portable-infobox"})
    
    # Ambil link gambar dengan resolusi tinggi jika ada
    image_url = hero_info.find("img")["src"] if hero_info.find("img") else None

    details = {}
    for row in hero_info.find_all("div", {"class": "pi-item"}):
        label = row.find("h3")
        value = row.find("div")
        if label and value:
            details[label.text.strip()] = value.text.strip()

    # Format caption ala Iqbal Ubot Premium
    caption = f"<blockquote><b>📊 ɪɴꜰᴏʀᴍᴀsɪ ʜᴇʀᴏ: {title.upper()}</b>\n\n"
    for key, value in details.items():
        # Hanya ambil info penting biar gak kepanjangan
        if key in ["Role", "Specialty", "Lane", "Price", "Release Date"]:
            caption += f"<b>ᚗ {key} :</b> <code>{value}</code>\n"
    
    caption += f"\n<b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>"

    return image_url, caption

@PY.UBOT("heroml")
@PY.TOP_CMD
async def hero_name_handler(client, message):
    prs_emo = await EMO.PROSES(client)
    ggl_emo = await EMO.GAGAL(client)
    
    args = get_arg(message)
    if not args:
        return await message.reply_text(
            f"<blockquote><b>{ggl_emo} ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ɴᴀᴍᴀ ʜᴇʀᴏ!</b>\nᚗ ᴄᴏɴᴛᴏʜ: <code>.ʜᴇʀᴏᴍʟ ᴀʟᴜᴄᴀʀᴅ</code></blockquote>"
        )

    status_msg = await message.reply_text(f"<blockquote><b>{prs_emo} sᴇᴅᴀɴɢ ᴍᴇɴᴄᴀʀɪ ᴅᴀᴛᴀ ʜᴇʀᴏ...</b></blockquote>")

    loop = asyncio.get_event_loop()
    try:
        # Menjalankan fungsi scraping di executor agar tidak blocking
        image_url, caption = await loop.run_in_executor(None, get_hero_info, args)
        
        if image_url:
            await client.send_photo(
                message.chat.id, 
                image_url, 
                caption=caption,
                reply_to_message_id=message.id
            )
            await status_msg.delete()
        else:
            await status_msg.edit(f"<blockquote><b>{ggl_emo} ɢᴀᴍʙᴀʀ ʜᴇʀᴏ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ!</b></blockquote>")
            
    except Exception as e:
        await status_msg.edit(f"<blockquote><b>{ggl_emo} ʜᴇʀᴏ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ ᴀᴛᴀᴜ ᴇʀʀᴏʀ:</b>\n<code>{str(e)}</code></blockquote>")
        