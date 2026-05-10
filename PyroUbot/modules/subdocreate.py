import requests
import json
from pyrogram import *
from pyrogram import Client, filters
from PyroUbot import *

__MODULE__ = "ᴄʀᴇᴀᴛᴇ ᴅᴏᴍᴀɪɴ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴜʙᴅᴏᴍᴀɪɴ ᴄʀᴇᴀᴛᴏʀ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}sᴜʙᴅᴏᴄʀᴇᴀᴛᴇ</code> [ᴅᴏᴍᴀɪɴ] [sᴜʙ] [ɪᴘ]
ᚗ <code>{0}ᴅᴏᴍᴀɪɴʟɪsᴛ</code>

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ʀᴇᴄᴏʀᴅ ᴀ sᴜʙᴅᴏᴍᴀɪɴ ᴋᴇ ᴄʟᴏᴜᴅꜰʟᴀʀᴇ sᴇᴄᴀʀᴀ ᴏᴛᴏᴍᴀᴛɪs.</blockquote>
"""

# Konfigurasi Cloudflare Terbaru
CLOUDFLARE_API_TOKEN = "me8y7ZQF2dHvgEE5c6L6j7Rgv1SjhrEhCk8l8H-E"
DOMAIN_LIST = {
    "pterosrvr.cloud": "e6fb504e4c01405c359f822168c740fb",
    "digitalatelier.tech": "1932711fb1d4d86b1f53b00d1b275f8a",
    "mydigital-store.me": "11c1abb8f727bf4d7342f1cade2b3cd7"
}

def create_subdomain(zone_id, subdomain, target_ip):
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"
    headers = {
        "Authorization": f"Bearer {CLOUDFLARE_API_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "type": "A",
        "name": subdomain,
        "content": target_ip,
        "ttl": 1,
        "proxied": False
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

@PY.UBOT("subdocreate")
@PY.TOP_CMD
async def subdomain_create(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    
    args = message.text.split(maxsplit=3)
    if len(args) < 4:
        return await message.reply_text(
            "<blockquote><b>❌ ꜰᴏʀᴍᴀᴛ sᴀʟᴀʜ!\nɢᴜɴᴀᴋᴀɴ: <code>.sᴜʙᴅᴏᴄʀᴇᴀᴛᴇ</code> [ᴅᴏᴍᴀɪɴ] [sᴜʙ] [ɪᴘ]</b></blockquote>"
        )

    domain = args[1].strip()
    subdomain = args[2].strip()
    target_ip = args[3].strip()

    if domain not in DOMAIN_LIST:
        return await message.reply_text(f"<blockquote><b>{ggl} ᴅᴏᴍᴀɪɴ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ ᴅᴀʟᴀᴍ ʟɪsᴛ.</b></blockquote>")

    zone_id = DOMAIN_LIST[domain]
    full_subdomain = f"{subdomain}.{domain}"

    status_msg = await message.reply_text(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ sᴜʙᴅᴏᴍᴀɪɴ...</b></blockquote>")

    result = create_subdomain(zone_id, full_subdomain, target_ip)

    if result.get("success"):
        await status_msg.edit(
            f"<blockquote><b>{brhsl} sᴜʙᴅᴏᴍᴀɪɴ ʙᴇʀʜᴀsɪʟ ᴅɪʙᴜᴀᴛ</b>\n\n"
            f"<b>ᚗ ᴛᴀᴜᴛᴀɴ :</b> <code>{full_subdomain}</code>\n"
            f"<b>ᚗ ᴀʟᴀᴍᴀᴛ ɪᴘ :</b> <code>{target_ip}</code></blockquote>"
        )
    else:
        error_msg = result.get("errors", [{"message": "Unknown Error"}])[0]["message"]
        await status_msg.edit(f"<blockquote><b>{ggl} ɢᴀɢᴀʟ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ sᴜʙᴅᴏᴍᴀɪɴ</b>\n<b>⚠️ ᴇʀʀᴏʀ:</b> <code>{error_msg}</code></blockquote>")

@PY.UBOT("domainlist|listdomain")
@PY.TOP_CMD
async def list_domains(client, message):
    brhsl = await EMO.BERHASIL(client)
    domain_list_text = f"<blockquote><b>{brhsl} ᴅᴀꜰᴛᴀʀ ᴅᴏᴍᴀɪɴ ᴛᴇʀsᴇᴅɪᴀ:</b>\n\n"
    for domain in DOMAIN_LIST.keys():
        domain_list_text += f"<b>ᚗ</b> <code>{domain}</code>\n"
    domain_list_text += "</blockquote>"
    
    await message.reply_text(domain_list_text)
    
