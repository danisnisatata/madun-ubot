import requests
import asyncio
from PyroUbot import *

__MODULE__ = "sᴇɴᴅ ᴘʀᴏxʏ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴇɴᴅ ᴘʀᴏxʏ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴘʀᴏxʏ</code>

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴɢɪʀɪᴍᴋᴀɴ ᴅᴀꜰᴛᴀʀ ᴘʀᴏxʏ ʜᴛᴛᴘ ᴛᴇʀʙᴀʀᴜ ʏᴀɴɢ ᴅɪᴘᴇʀʙᴀʀᴜɪ sᴇᴛɪᴀᴘ sᴀᴀᴛ.</blockquote>
"""

# URL sumber proxy
PROXY_URL = "https://api.proxyscrape.com/?request=displayproxies&proxytype=http"

# List untuk menyimpan data proxy
latest_proxies = []

async def update_proxies():
    global latest_proxies
    while True:
        try:
            # Menggunakan requests dalam loop async (disarankan aiohttp untuk produksi)
            response = requests.get(PROXY_URL, timeout=10)
            if response.status_code == 200:
                latest_proxies = response.text.strip().split("\n")
        except Exception:
            pass
        await asyncio.sleep(180)  # Update setiap 3 menit

@PY.UBOT("proxy")
@PY.TOP_CMD
async def send_proxy_command(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)

    if not latest_proxies:
        return await message.reply_text(f"<blockquote><b>{ggl} ᴘʀᴏxʏ ʙᴇʟᴜᴍ ᴛᴇʀsᴇᴅɪᴀ ᴀᴛᴀᴜ ɢᴀɢᴀʟ ᴜᴘᴅᴀᴛᴇ.</b></blockquote>")

    # Ambil 50-100 proxy biar gak kepanjangan di chat
    proxy_list = "\n".join(latest_proxies[:50])
    
    result_text = (
        f"<blockquote><b>{brhsl} ᴅᴀꜰᴛᴀʀ ᴘʀᴏxʏ ᴛᴇʀʙᴀʀᴜ</b>\n\n"
        f"<code>{proxy_list}</code>\n\n"
        f"<b>⌭ sᴛᴀᴛᴜs :</b> ᴜᴘᴅᴀᴛᴇ ᴏᴛᴏᴍᴀᴛɪs ᴛɪᴀᴘ 3 ᴍᴇɴɪᴛ</blockquote>"
    )
    await message.reply_text(result_text)

# Memastikan task berjalan saat modul dimuat
loop = asyncio.get_event_loop()
loop.create_task(update_proxies())
