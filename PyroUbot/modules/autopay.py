import asyncio
import aiohttp
from io import BytesIO
from datetime import datetime
from PyroUbot import *
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# ============================================================
# 📋 ᴋᴏɴꜰɪɢᴜʀᴀꜱɪ ᴀʙꜱᴏʟᴜᴛᴇ MADUN
# ============================================================
PakasirApiData = {
    "ApiKey": "lVu8n7Y4Ryuakn9vpwqyF2OvXnlbrwez",
    "ProjectSlug": "ubotjuna"
}
MDR_FEE = 0.007

__MODULE__ = "ᴀᴜᴛᴏᴘᴀʏ"
__HELP__ = """
<blockquote><b>⦪ MADUN ᴍᴜʟᴛɪ-ʙʟᴏᴄᴋ ᴘᴀʏ ⦫</b></blockquote>
<blockquote><b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b> <code>.pay</code> [ᴊᴜᴍʟᴀʜ]</blockquote>
<blockquote><b>⎆ ꜰɪᴛᴜʀ :</b> ᴀɴɪᴍᴀꜱɪ ᴠɪᴘ & ᴍᴜʟᴛɪ-ǫᴜᴏᴛᴇ</blockquote>
"""

# ============================================================
# 🛡️ ꜰᴜɴɢꜱɪ ɪɴᴛɪ ᴘᴀᴋᴀꜱɪʀ Qʀɪꜱ (ꜰᴜʟʟ ꜰɪx ʙʏᴛᴇꜱɪᴏ)
# ============================================================
async def BuatQrisPakasir(JumlahBayar, IdPesanan):
    UrlPakasir = "https://app.pakasir.com/api/transactioncreate/qris"
    PayloadData = {
        "project": PakasirApiData["ProjectSlug"],
        "api_key": PakasirApiData["ApiKey"],
        "order_id": str(IdPesanan),
        "amount": JumlahBayar
    }
    async with aiohttp.ClientSession() as SesiBot:
        try:
            async with SesiBot.post(UrlPakasir, json=PayloadData) as ResponApi:
                DataJson = await ResponApi.json()
                DetailBayar = DataJson.get("payment") or DataJson
                KodeBayar = DataJson.get("code") or DetailBayar.get("code")
                StringQris = DetailBayar.get("payment_number") or DataJson.get("qris_string") or DetailBayar.get("qris_string")
                
                LinkGambarQr = None
                if KodeBayar:
                    LinkGambarQr = f"https://app.pakasir.com/qris/{KodeBayar}.png"
                elif StringQris:
                    LinkGambarQr = f"https://quickchart.io/qr?text={StringQris}&size=500&format=png"
                
                if not LinkGambarQr: return None
                async with SesiBot.get(LinkGambarQr) as ResponGambar:
                    if ResponGambar.status == 200:
                        KontenGambar = await ResponGambar.read()
                        FotoQris = BytesIO(KontenGambar)
                        FotoQris.name = "qris_pembayaran.png"
                        return FotoQris
        except: return None
    return None

# ============================================================
# 🚀 ʜᴀɴᴅʟᴇʀ .ᴘᴀʏ ᴘʀᴇᴍɪᴜᴍ
# ============================================================
@PY.UBOT("pay", filters.me)
async def PayHandler(client, message):
    args = get_arg(message)
    if not args or not args.isdigit():
        return await message.reply("<blockquote><b>❌ ꜰᴏʀᴍᴀᴛ ꜱᴀʟᴀʜ!</b></blockquote>\n<blockquote>ᚗ ᴄᴏɴᴛᴏʜ: <code>.pay 10000</code></blockquote>")

    nominal = int(args)
    total_bayar = nominal + int(nominal * MDR_FEE)
    user_id = message.from_user.id
    order_id = f"IQB-{user_id}-{datetime.now().strftime('%H%M%S')}"

    # --- ᴀɴɪᴍᴀꜱɪ ᴘʀᴇᴍɪᴜᴍ ʙᴇʀʙᴏʙᴏᴛ ---
    msg = await message.reply("<blockquote><b>⚙️ ᴍᴇɴʏɪᴀᴘᴋᴀɴ ɪɴᴠᴏɪᴄᴇ ᴠɪᴘ...</b></blockquote>\n<blockquote>▒▒▒▒▒▒▒▒▒▒ 0%</blockquote>")
    await asyncio.sleep(0.3)
    await msg.edit("<blockquote><b>🔐 ᴍᴇɴɢᴇɴᴋʀɪᴘꜱɪ ᴅᴀᴛᴀ ᴛʀᴀɴꜱᴀᴋꜱɪ...</b></blockquote>\n<blockquote>██████▒▒▒▒ 60%</blockquote>")

    foto_qris = await BuatQrisPakasir(total_bayar, order_id)
    if not foto_qris:
        return await msg.edit("<blockquote><b>❌ ɢᴀᴛᴇᴡᴀʏ ᴇʀʀᴏʀ:</b></blockquote>\n<blockquote>ᚗ ɢᴀɢᴀʟ ɢᴇɴᴇʀᴀᴛᴇ Qʀɪꜱ!</blockquote>")

    await msg.edit("<blockquote><b>🌐 ᴍᴇɴɢʜᴜʙᴜɴɢᴋᴀɴ ᴋᴇ ɢᴀᴛᴇᴡᴀʏ...</b></blockquote>\n<blockquote>██████████ 100%</blockquote>")
    await asyncio.sleep(0.2)

    # --- ᴛᴀᴍᴘɪʟᴀɴ ᴍᴜʟᴛɪ-ʙʟᴏᴄᴋǫᴜᴏᴛᴇ ᴘᴀʟɪɴɢ ᴍᴇᴡᴀʜ ---
    caption = (
        f"<blockquote><b>⦪ MADUN ꜱᴇᴄᴜʀᴇ ᴘᴀʏᴍᴇɴᴛ ⦫</b></blockquote>\n"
        f"<blockquote>ᚗ <b>ɪᴅ ᴏʀᴅᴇʀ:</b> <code>{order_id}</code></blockquote>\n"
        f"<blockquote>ᚗ <b>ɴᴏᴍɪɴᴀʟ:</b> ʀᴘ {nominal:,}</blockquote>\n"
        f"<blockquote>ᚗ <b>ᴛᴏᴛᴀʟ ʙᴀʏᴀʀ:</b> <b>ʀᴘ {total_bayar:,}</b></blockquote>\n"
        f"<blockquote>ᚗ ꜱᴄᴀɴ Qʀɪꜱ ᴅɪ ᴀᴛᴀꜱ ᴜɴᴛᴜᴋ ʙᴀʏᴀʀ ᴏᴛᴏᴍᴀᴛɪꜱ.</blockquote>"
    )
    
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("✅ ᴄᴇᴋ ꜱᴛᴀᴛᴜꜱ ʙᴀʏᴀʀ", callback_data=f"v_cek {order_id} {nominal}")],
        [InlineKeyboardButton("🚫 ʙᴀᴛᴀʟᴋᴀɴ ᴘᴇᴍʙᴀʏᴀʀᴀɴ", callback_data=f"v_cancel {order_id}")]
    ])
    
    await msg.delete()
    await client.send_photo(message.chat.id, photo=foto_qris, caption=caption, reply_markup=buttons)

@Client.on_callback_query(filters.regex("^(v_cek|v_cancel)"))
async def CallbackHandler(client, callback_query):
    data = callback_query.data.split()
    action, order_id = data[0], data[1]
    
    if action == "v_cek":
        nom = data[2]
        url_check = "https://app.pakasir.com/api/transactiondetail"
        params = {"project": PakasirApiData["ProjectSlug"], "api_key": PakasirApiData["ApiKey"], "order_id": order_id}
        async with aiohttp.ClientSession() as session:
            async with session.get(url_check, params=params) as r:
                res = await r.json()
                detail = res.get("transaction") or res.get("data") or {}
                if str(detail.get("status", "")).upper() in ["PAID", "SUCCESS", "BERHASIL"]:
                    text_lunas = (
                        f"<blockquote><b>⦪ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ʟᴜɴᴀꜱ ✅ ⦫</b></blockquote>\n"
                        f"<blockquote>ᚗ <b>ɪᴅ ᴏʀᴅᴇʀ:</b> <code>{order_id}</code></blockquote>\n"
                        f"<blockquote>ᚗ <b>ɴᴏᴍɪɴᴀʟ:</b> ʀᴘ {int(nom):,}+</blockquote>\n"
                        f"<blockquote>ᚗ ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ ꜱᴜᴅᴀʜ ᴏʀᴅᴇʀ ᴅɪ MADUN!</blockquote>"
                    )
                    await callback_query.edit_message_caption(caption=text_lunas)
                else:
                    await callback_query.answer("⚠️ ᴅᴀɴᴀ ʙᴇʟᴜᴍ ᴍᴀꜱᴜᴋ ʙᴏꜱ!", show_alert=True)

    elif action == "v_cancel":
        text_batal = (
            f"<blockquote><b>❌ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴅɪʙᴀᴛᴀʟᴋᴀɴ</b></blockquote>\n"
            f"<blockquote>ᚗ <b>ɪᴅ ᴏʀᴅᴇʀ:</b> <code>{order_id}</code></blockquote>\n"
            f"<blockquote>ᚗ ᴛʀᴀɴꜱᴀᴋꜱɪ ᴛᴇʟᴀʜ ᴅɪʜᴀᴘᴜꜱ ᴅᴀʀɪ ꜱɪꜱᴛᴇᴍ.</blockquote>"
        )
        await callback_query.edit_message_caption(caption=text_batal)
        await callback_query.answer("🗑️ ᴏʀᴅᴇʀ ʙᴇʀʜᴀꜱɪʟ ᴅɪʜᴀᴘᴜꜱ!", show_alert=True)
         