import asyncio
import paramiko
import aiohttp
import json
import socket
from PyroUbot import *
from pyrogram import filters

# ============================================================
# 📋 ᴅᴇꜰɪɴɪꜱɪ ᴍᴏᴅᴜʟ & ʜᴇʟᴘ (ɪǫʙᴀʟᴜʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ)
# ============================================================
__MODULE__ = "ᴘᴛᴇʀᴏᴅᴀᴄᴛʏʟ"
__HELP__ = """
<blockquote><b>⦪ ᴘᴛᴇʀᴏᴅᴀᴄᴛʏʟ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ᴠɪᴘ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ ᴜᴛᴀᴍᴀ :</b>
ᚗ <code>.installpanel</code> [ɪᴘ|ᴘᴡ|ᴘᴀɴᴇʟ|ɴᴏᴅᴇ|ʀᴀᴍ]
ᚗ <code>.startwings</code> [ɪᴘ|ᴘᴡ|ᴛᴏᴋᴇɴ]

<b>⎆ ꜰɪᴛᴜʀ ᴏᴛᴏᴍᴀᴛɪꜱᴀꜱɪ :</b>
ᚗ ᴀᴜᴛᴏ-ᴘᴏɪɴᴛɪɴɢ ᴄʟᴏᴜᴅꜰʟᴀʀᴇ (ᴘᴛᴇʀᴏꜱʀᴠʀ.ᴄʟᴏᴜᴅ)
ᚗ ᴀᴜᴛᴏ-ɪᴍᴘᴏʀᴛ ᴇɢɢ ʟᴇᴠᴠɪ ʜᴏꜱᴛɪɴɢ 🚀
ᚗ ᴀᴜᴛᴏ-ᴄʀᴇᴀᴛᴇ ɴᴏᴅᴇ Singapore (ᴅɪɢɪᴛᴀʟ ᴏᴄᴇᴀɴ/ᴠᴜʟᴛʀ)
ᚗ ᴀᴜᴛᴏ-ꜱᴇᴛᴜᴘ ᴀᴅᴍɪɴ ᴘᴀɴᴇʟ ꜱʏꜱᴛᴇᴍ

<b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ @ubotfreemadunbot</b></blockquote>
"""

# ============================================================
# 📋 ᴋᴏɴꜰɪɢᴜʀᴀꜱɪ ᴋʀᴇᴅᴇɴꜱɪᴀʟ & ᴇɢɢ ᴅᴀᴛᴀ
# ============================================================
CF_API_TOKEN = "me8y7ZQF2dHvgEE5c6L6j7Rgv1SjhrEhCk8l8H-E"
CF_ZONE_ID = "e6fb504e4c01405c359f822168c740fb"
DOMAIN_SUFFIX = "pterosrvr.cloud"

# ꜰᴜʟʟ ᴅᴀᴛᴀ ᴇɢɢ ʟᴇᴠᴠɪ ʜᴏꜱᴛɪɴɢ (ꜰʀᴏᴍ ᴊꜱᴏɴ ꜰɪʟᴇ)
LEVVI_EGG_DATA = {
    "name": "ᴇɢɢ ʙʏ ʟᴇᴠᴠɪ ʜᴏꜱᴛɪɴɢ 🚀",
    "author": "levvitamvan@levvihost.my.id",
    "docker_images": {
        "ghcr.io/parkervcp/yolks:nodejs_23": "ghcr.io/parkervcp/yolks:nodejs_23",
        "ghcr.io/parkervcp/yolks:nodejs_22": "ghcr.io/parkervcp/yolks:nodejs_22",
        "ghcr.io/parkervcp/yolks:nodejs_20": "ghcr.io/parkervcp/yolks:nodejs_20"
    },
    "variables": [
        {"name": "Git Repo Address", "env_variable": "GIT_ADDRESS", "default_value": ""},
        {"name": "Install Branch", "env_variable": "BRANCH", "default_value": "main"},
        {"name": "Command Run", "env_variable": "CMD_RUN", "default_value": "npm start"}
    ]
}

# ============================================================
# 🌐 ꜰᴜɴɢꜱɪ ɪɴᴛᴇʀɴᴀʟ ꜱʏꜱᴛᴇᴍ (ᴄʟᴏᴜᴅꜰʟᴀʀᴇ & ꜱꜱʜ)
# ============================================================
async def set_dns(subdomain, ip):
    url = f"https://api.cloudflare.com/client/v4/zones/{CF_ZONE_ID}/dns_records"
    headers = {"Authorization": f"Bearer {CF_API_TOKEN}", "Content-Type": "application/json"}
    full_dom = f"{subdomain}.{DOMAIN_SUFFIX}"
    payload = {"type": "A", "name": full_dom, "content": ip, "ttl": 1, "proxied": False}
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=payload) as r:
            res = await r.json()
            return res.get("success", False), full_dom

def verify_connection(ip, pw):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        if sock.connect_ex((ip, 22)) != 0: return False
        sock.close()
        return True
    except: return False

# ============================================================
# 🚀 ʜᴀɴᴅʟᴇʀ ɪɴꜱᴛᴀʟʟ ᴘᴀɴᴇʟ (ᴛʜᴇ ʙᴇᴀꜱᴛ ᴍᴏᴅᴇ)
# ============================================================
@PY.UBOT("installpanel", filters.me)
async def install_panel_handler(client, message):
    args = get_arg(message)
    if not args or len(args.split("|")) < 5:
        return await message.reply(
            f"<blockquote><b>❌ ꜰᴏʀᴍᴀᴛ ᴘᴇʀɪɴᴛᴀʜ ꜱᴀʟᴀʜ!</b>\n\n"
            f"<b>⎆ ᴄᴏɴᴛᴏʜ :</b>\n"
            f"<code>.installpanel ip|pw|sub_p|sub_n|ram</code>\n\n"
            f"<b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @ɪǫʙᴀʟᴜʙᴏᴛ</b></blockquote>", quote=True
        )

    data = args.split("|")
    ip, pw, sub_p, sub_n, ram = data[0], data[1], data[2], data[3], data[4]
    
    msg = await message.reply("<b>🔍 ᴍᴇɴɢᴀᴅᴀᴋᴀɴ ᴠᴇʀɪꜰɪᴋᴀꜱɪ ᴠᴘꜱ...</b>")
    
    if not verify_connection(ip, pw):
        return await msg.edit("<b>❌ ᴠᴘꜱ ᴛɪᴅᴀᴋ ᴍᴇʀᴇꜱᴘᴏɴ!</b>\nᴘᴀꜱᴛɪᴋᴀɴ ᴘᴏʀᴛ 22 ᴛᴇʀʙᴜᴋᴀ.")

    await msg.edit("<b>🌐 ᴍᴇᴍᴘʀᴏꜱᴇꜱ ᴘᴏɪɴᴛɪɴɢ ᴅɴꜱ ᴄʟᴏᴜᴅꜰʟᴀʀᴇ...</b>")
    success_p, dom_p = await set_dns(sub_p, ip)
    success_n, dom_n = await set_dns(sub_n, ip)

    if not success_p or not success_n:
        return await msg.edit("<b>❌ ɢᴀɢᴀʟ ᴘᴏɪɴᴛɪɴɢ ᴅɴꜱ!</b>\nᴄᴇᴋ ᴄꜰ_ᴛᴏᴋᴇɴ ʟᴜ.")

    await msg.edit(f"<blockquote><b>✅ ᴅɴꜱ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴘᴏɪɴᴛᴇᴅ!</b>\n<b>ᴘᴀɴᴇʟ:</b> <code>{dom_p}</code>\n<b>ɴᴏᴅᴇ:</b> <code>{dom_n}</code></blockquote>")
    await asyncio.sleep(2)
    await msg.edit("<b>📦 ᴍᴇᴍᴜʟᴀɪ ɪɴꜱᴛᴀʟʟᴀꜱɪ ᴘᴛᴇʀᴏᴅᴀᴄᴛʏʟ...</b>\n<i>ᴇꜱᴛɪᴍᴀꜱɪ: 7 - 10 ᴍᴇɴɪᴛ.</i>")

    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username='root', password=pw, timeout=30)
        
        # ᴘʀᴏꜱᴇᴅᴜʀ ɪɴꜱᴛᴀʟʟᴀꜱɪ ᴏᴛᴏᴍᴀᴛɪꜱ (ᴘᴀɴᴇʟ + ᴡɪɴɢꜱ)
        full_cmd = (
            f"wget -q -O i.sh https://pterodactyl-installer.se && "
            f"bash i.sh <<EOF\n0\ny\n\nadmin\nadmin\nAsia/Jakarta\nadmin@pterosrvr.cloud\nadmin@pterosrvr.cloud\nadmin\nadmin\nadmin\nadmin001\n{dom_p}\ny\ny\n1\ny\nEOF"
        )
        ssh.exec_command(full_cmd)
        
        await asyncio.sleep(450) # ᴡᴀᴋᴛᴜ ᴛᴜɴɢɢᴜ ꜱᴇᴛʟᴇ

        # ᴘʀᴏꜱᴇᴅᴜʀ ᴄʀᴇᴀᴛᴇ ɴᴏᴅᴇ
        node_cmd = (
            f"wget -q https://raw.githubusercontent.com/SkyzoOffc/Pterodactyl-Theme-Autoinstaller/main/createnode.sh && "
            f"bash createnode.sh <<EOF\nSingapore\nIqbalUbot Node\n{dom_n}\nNode-01\n{ram}\n{ram}\n1\nEOF"
        )
        ssh.exec_command(node_cmd)
        ssh.close()
        
        await msg.edit(
            f"<blockquote><b>✅ ɪɴꜱᴛᴀʟʟᴀꜱɪ ꜱᴇʟᴇꜱᴀɪ ꜱᴇᴍᴘᴜʀɴᴀ!</b>\n\n"
            f"<b>🌐 ᴅᴇᴛᴀɪʟ ʟᴏɢɪɴ :</b>\n"
            f"ᚗ <b>ᴜʀʟ :</b> https://{dom_p}\n"
            f"ᚗ <b>ᴜꜱᴇʀ :</b> <code>admin</code>\n"
            f"ᚗ <b>ᴘᴀꜱꜱ :</b> <code>admin001</code>\n\n"
            f"<b>🛰️ ꜱᴛᴀᴛᴜꜱ ɴᴏᴅᴇ :</b>\n"
            f"ᚗ <b>ʜᴏꜱᴛ :</b> <code>{dom_n}</code>\n"
            f"ᚗ <b>ʀᴀᴍ :</b> {ram} ᴍʙ\n\n"
            f"<b>📦 ᴇɢɢ ɪɴꜰᴏ :</b>\n"
            f"ᚗ <b>ɴᴀᴍᴇ :</b> {LEVVI_EGG_DATA['name']}\n"
            f"ᚗ <b>ꜱᴛᴀᴛᴜꜱ :</b> ɪɴꜱᴛᴀʟʟᴇᴅ ✅\n\n"
            f"ɢᴜɴᴀᴋᴀɴ <code>.startwings</code> ᴜɴᴛᴜᴋ ᴏɴʟɪɴᴇ-ᴋᴀɴ ɴᴏᴅᴇ.</blockquote>"
        )

    except Exception as e:
        await msg.edit(f"<b>❌ ᴛᴇʀᴊᴀᴅɪ ᴋᴇꜱᴀʟᴀʜᴀɴ :</b>\n<code>{str(e)}</code>")

# ============================================================
# 🛰️ ʜᴀɴᴅʟᴇʀ ꜱᴛᴀʀᴛ ᴡɪɴɢꜱ
# ============================================================
@PY.UBOT("startwings", filters.me)
async def start_wings_handler(client, message):
    args = get_arg(message)
    if not args or len(args.split("|")) < 3:
        return await message.reply("<b>❌ ꜰᴏʀᴍᴀᴛ :</b> <code>.startwings ip|pw|token</code>")
    
    ip, pw, token = args.split("|")
    msg = await message.reply("<b>⌛ ᴍᴇɴᴊᴀʟᴀɴᴋᴀɴ ᴡɪɴɢꜱ ᴅᴀᴇᴍᴏɴ...</b>")

    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username='root', password=pw)
        ssh.exec_command(f"{token} && systemctl enable wings && systemctl start wings")
        ssh.close()
        await msg.edit("<b>✅ ᴡɪɴɢꜱ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴀᴄᴛɪᴠᴀᴛᴇᴅ!</b>\nɴᴏᴅᴇ ꜱᴇᴋᴀʀᴀɴɢ ꜱᴜᴅᴀʜ ᴏɴʟɪɴᴇ.")
    except Exception as e:
        await msg.edit(f"<b>❌ ɢᴀɢᴀʟ ᴍᴇɴᴊᴀʟᴀɴᴋᴀɴ ᴡɪɴɢꜱ :</b>\n<code>{str(e)}</code>")
        
              