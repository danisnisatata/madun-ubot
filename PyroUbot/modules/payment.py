# ============================================================
# 💳 MODUL PAYMENT MANUAL (SEPERTI FILE LAMA)
# ============================================================
# FITUR: KONFIRMASI PEMBAYARAN, LOG KE CHANNEL, NOTIF ADMIN
# ============================================================

import asyncio
from datetime import datetime
from dateutil.relativedelta import relativedelta
from pytz import timezone
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from PyroUbot import *

# ============================================================
# 📋 KONFIGURASI
# ============================================================

# List untuk menyimpan user yang sedang dalam proses konfirmasi
# (SINKRON DENGAN FILE add_ubot.py)
try:
    from add_ubot import CONFIRM_PAYMENT
except:
    CONFIRM_PAYMENT = []

# ID Channel untuk log transaksi - GANTI DENGAN ID CHANNEL ANDA!
ID_CHANNEL_LOG = -1003709287352  # <--- GANTI DENGAN ID CHANNEL ANDA!

# ============================================================
# 💰 DATABASE HARGA (SMART MATH)
# ============================================================

HARGA_ROLE = {
    "member": {"1": 1000, "0": 2000},
    "seles": {"1": 3000, "0": 5000},
    "admin": {"1": 7000, "0": 10000},
    "owner": {"1": 13000, "0": 15000},
    "tk": {"1": 17000, "0": 20000},
    "ceo": {"1": 22000, "0": 25000},
    "founder": {"1": 32000, "0": 35000}
}

HIERARKI_ROLE = {
    "member": 1, "seles": 2, "admin": 3, "owner": 4, 
    "tk": 5, "ceo": 6, "founder": 7
}

LIST_ROLE_DATABASE = [
    "PREM_USERS", "SELER_USERS", "ADMIN_USERS", "OWNER_USERS", 
    "KHASJIR_USERS", "CIOGWMAH_USERS", "ALLROLE_USERS"
]

# ============================================================
# 💳 HANDLER KONFIRMASI PEMBAYARAN
# ============================================================

@PY.CALLBACK("confirm")
async def ProsesKonfirmasiBayar(client, callback_query):
    """
    HANDLER UNTUK KONFIRMASI PEMBAYARAN (VERSI MANUAL).
    MENGGUNAKAN SISTEM SEPERTI DI FILE j167fk.py
    """
    try:
        # 1. AMBIL DATA DARI CALLBACK
        data = callback_query.data.split()
        role = data[1]
        durasi = data[2]
        user_id = callback_query.from_user.id
        full_name = f"<b>{callback_query.from_user.first_name} {callback_query.from_user.last_name or ''}</b>"
        BotID = client.me.id

        # 2. HITUNG HARGA DENGAN SMART MATH
        HargaTarget = HARGA_ROLE.get(role, {}).get(durasi, 0)
        Potongan = 0

        # CEK POTONGAN BERDASARKAN ROLE YANG SUDAH DIMILIKI
        if await get_vars(BotID, "ALLROLE_USERS", user_id): 
            Potongan = HARGA_ROLE["founder"][durasi]
        elif await get_vars(BotID, "CIOGWMAH_USERS", user_id): 
            Potongan = HARGA_ROLE["ceo"][durasi]
        elif await get_vars(BotID, "KHASJIR_USERS", user_id): 
            Potongan = HARGA_ROLE["tk"][durasi]
        elif await get_vars(BotID, "OWNER_USERS", user_id): 
            Potongan = HARGA_ROLE["owner"][durasi]
        elif await get_vars(BotID, "ADMIN_USERS", user_id): 
            Potongan = HARGA_ROLE["admin"][durasi]
        elif await get_vars(BotID, "SELER_USERS", user_id): 
            Potongan = HARGA_ROLE["seles"][durasi]
        elif await get_vars(BotID, "PREM_USERS", user_id): 
            Potongan = HARGA_ROLE["member"][durasi]

        NominalBayar = max(0, HargaTarget - Potongan)

        if NominalBayar == 0:
            return await callback_query.answer(
                "⚠️ ANDA SUDAH MEMILIKI AKSES INI ATAU YANG LEBIH TINGGI!", 
                show_alert=True
            )

        teks_durasi = "1 BULAN" if durasi == "1" else "PERMANEN"

        # 3. TAMBAHKAN USER KE LIST CONFIRM_PAYMENT
        if user_id in CONFIRM_PAYMENT:
            CONFIRM_PAYMENT.remove(user_id)
        CONFIRM_PAYMENT.append(user_id)

        await callback_query.message.delete()

        # 4. KIRIM INSTRUKSI PEMBAYARAN DENGAN QRIS STATIS
        await bot.send_photo(
            user_id,
            photo="https://ibb.co.com/20CFtTx5",  # QRIS STATIS
            caption=f"""
<blockquote><b>💳 INSTRUKSI PEMBAYARAN
━━━━━━━━━━━━━━━━━━━━

🎟️ ROLE : {role.upper()}
⏳ DURASI : {teks_durasi}
💰 HARGA : Rp {NominalBayar:,}
💳 NO DANA : <code>082216997138</code>

📌 CARA PEMBAYARAN:
1️⃣ Transfer ke nomor DANA di atas
2️⃣ Screenshot bukti transfer
3️⃣ Kirim screenshot ke sini

⏱️ Batas waktu: 5 menit</b></blockquote>
""",
        )

        try:
            # 5. MENUNGGU KIRIMAN DARI USER (TIMEOUT 5 MENIT)
            pesan = await bot.listen(user_id, timeout=300)
        except asyncio.TimeoutError:
            if user_id in CONFIRM_PAYMENT:
                CONFIRM_PAYMENT.remove(user_id)
            return await bot.send_message(
                user_id, 
                "<b>❌ PEMBATALAN OTOMATIS (TIMEOUT)\n\nSilakan /start ulang.</b>"
            )

        if user_id in CONFIRM_PAYMENT:
            # 6. CEK APAKAH YANG DIKIRIM ADALAH FOTO
            if not pesan.photo:
                CONFIRM_PAYMENT.remove(user_id)
                buttons = [[InlineKeyboardButton(
                    "✅ KONFIRMASI ULANG", 
                    callback_data=f"confirm {role} {durasi}"
                )]]
                return await bot.send_message(
                    user_id, 
                    "<b>❌ HARAP KIRIMKAN BUKTI DALAM BENTUK FOTO (SCREENSHOT)!\n\nKlik tombol di bawah untuk mencoba lagi.</b>",
                    reply_markup=InlineKeyboardMarkup(buttons)
                )

            # 7. JIKA KIRIM FOTO BENAR, TERUSKAN KE ADMIN
            else:
                buttons_admin = [
                    [InlineKeyboardButton("✅ TERIMA", callback_data=f"success {user_id} {role} {durasi}")],
                    [InlineKeyboardButton("❌ TOLAK", callback_data=f"failed {user_id}")]
                ]

                await pesan.copy(
                    OWNER_ID,
                    caption=f"""
<blockquote><b>🔔 LAPORAN PEMBAYARAN BARU

👤 USER: {full_name}
🆔 ID: <code>{user_id}</code>
💎 ROLE: {role.upper()}
⏳ DURASI: {teks_durasi}
💰 NOMINAL: Rp {NominalBayar:,}</b></blockquote>
""",
                    reply_markup=InlineKeyboardMarkup(buttons_admin),
                )

                CONFIRM_PAYMENT.remove(user_id)
                return await bot.send_message(
                    user_id, 
                    f"<blockquote><b>✅ BUKTI DITERIMA!\n\n🏦 PEMBAYARAN SEDANG DICEK ADMIN.\nMOHON TUNGGU KONFIRMASI.</b></blockquote>"
                )
    except Exception as e:
        await callback_query.answer(f"❌ ERROR: {e}", show_alert=True)


# ============================================================
# ✅ HANDLER UNTUK ADMIN (TERIMA / TOLAK)
# ============================================================

@PY.CALLBACK("^(success|failed|home)")
async def HandleAdminActions(client, callback_query):
    """
    HANDLER UNTUK ADMIN: TERIMA / TOLAK PEMBAYARAN
    DAN OTOMATIS LOG KE CHANNEL
    """
    query = callback_query.data.split()
    user_target = int(query[1])
    get_user = await bot.get_users(user_target)
    admin_id = callback_query.from_user.id

    # PASTIKAN YANG KLIK ADALAH ADMIN
    if admin_id != OWNER_ID:
        return await callback_query.answer("❌ HANYA ADMIN!", show_alert=True)

    # ✅ ADMIN KLIK TERIMA
    if query[0] == "success":
        role = query[2]
        durasi = query[3]  # "1" = 1 Bulan, "0" = Permanen
        BotID = client.me.id

        # HITUNG ULANG HARGA UNTUK LOG
        HargaTarget = HARGA_ROLE.get(role, {}).get(durasi, 0)
        
        # HITUNG POTONGAN (UNTUK LOG)
        Potongan = 0
        if await get_vars(BotID, "ALLROLE_USERS", user_target): 
            Potongan = HARGA_ROLE["founder"][durasi]
        elif await get_vars(BotID, "CIOGWMAH_USERS", user_target): 
            Potongan = HARGA_ROLE["ceo"][durasi]
        elif await get_vars(BotID, "KHASJIR_USERS", user_target): 
            Potongan = HARGA_ROLE["tk"][durasi]
        elif await get_vars(BotID, "OWNER_USERS", user_target): 
            Potongan = HARGA_ROLE["owner"][durasi]
        elif await get_vars(BotID, "ADMIN_USERS", user_target): 
            Potongan = HARGA_ROLE["admin"][durasi]
        elif await get_vars(BotID, "SELER_USERS", user_target): 
            Potongan = HARGA_ROLE["seles"][durasi]
        elif await get_vars(BotID, "PREM_USERS", user_target): 
            Potongan = HARGA_ROLE["member"][durasi]

        NominalDibayar = HargaTarget - Potongan
        teks_durasi = "1 BULAN" if durasi == "1" else "PERMANEN"

        # 1. DATABASE ROLE LIST SESUAI HIERARKI
        target_rank = HIERARKI_ROLE.get(role, 1)

        # BOM DATABASE (OTOMATIS ADD SEMUA ROLE DI BAWAHNYA)
        for i in range(target_rank):
            await add_to_vars(client.me.id, LIST_ROLE_DATABASE[i], get_user.id)

        # 2. ATUR MASA EXPIRED
        now = datetime.now(timezone("Asia/Jakarta"))
        if durasi == "1":
            expired = now + relativedelta(months=1)
            await set_expired_date(get_user.id, expired)
            msg_exp = "1 BULAN"
        else:
            expired = now + relativedelta(years=100)
            await set_expired_date(get_user.id, expired)
            msg_exp = "PERMANEN"

        # 3. FORMAT WAKTU UNTUK LOG
        waktu_sekarang = now.strftime("%A, %d %B %Y %H:%M WIB")
        # GANTI NAMA HARI KE BAHASA INDONESIA
        hari_indonesia = {
            'Monday': 'Senin', 'Tuesday': 'Selasa', 'Wednesday': 'Rabu',
            'Thursday': 'Kamis', 'Friday': 'Jumat', 'Saturday': 'Sabtu',
            'Sunday': 'Minggu'
        }
        for eng, ind in hari_indonesia.items():
            waktu_sekarang = waktu_sekarang.replace(eng, ind)

        # 4. KIRIM LOG KE CHANNEL (DENGAN FOTO)
        teks_log_channel = f"""
<blockquote><b>📜 STRUK PEMBELIAN PRODUK
━━━━━━━━━━━━━━━━━━━━━━━

🪪 IDENTITAS PEMBELI
├👤 NAMA : {get_user.first_name} {get_user.last_name or ''}
╰🆔 ID : <code>{get_user.id}</code>

🎀 DATA PRODUK
├🛒 PRODUK : {role.upper()} ({teks_durasi})
├💰 HARGA : Rp {NominalDibayar:,}
╰⏰ WAKTU : {waktu_sekarang}

━━━━━━━━━━━━━━━━━━━━━━━
📨 TERIMAKASIH SUDAH BELANJA</b></blockquote>
"""

        try:
            # KIRIM KE CHANNEL LOG
            await bot.send_photo(
                chat_id=ID_CHANNEL_LOG,
                photo="https://ibb.co.com/20CFtTx5",  # FOTO BACKGROUND
                caption=teks_log_channel,
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton("🤖 KE BOT", url="https://t.me/ubotfreemadunbot")
                ]])
            )
        except Exception as e:
            print(f"GAGAL KIRIM KE CHANNEL: {e}")

        # 5. LINK GRUP (kecuali member 1 bulan)
        is_member_sebulan = (role == "member" and durasi == "1")
        link_grup = (
            "\n\n<b>🔗 LINK GRUP KHUSUS:\nhttps://t.me/+ubotlelen</b>\n"
            "<b>💬 JOIN DAN TAG ADMIN UNTUK KLAIM ROLE!</b>"
        )

        # 6. KIRIM NOTIF KE USER
        caption_user = (
            f"<blockquote><b>✅ PEMBAYARAN DITERIMA!\n\n"
            f"💎 ROLE: {role.upper()}\n"
            f"🗓️ DURASI: {msg_exp}\n\n"
            f"SEKARANG ANDA BISA MEMBUAT USERBOT!</b>"
        )

        if not is_member_sebulan:
            caption_user += link_grup

        caption_user += "</blockquote>"

        await bot.send_message(
            get_user.id,
            caption_user,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("🤖 BUAT USERBOT", callback_data="add_ubot")
            ]]),
        )

        # 7. UPDATE PESAN DI ADMIN
        return await callback_query.edit_message_caption(
            caption=f"<blockquote><b>✅ {get_user.first_name} BERHASIL DIJADIKAN {role.upper()} ({msg_exp})</b></blockquote>",
        )

    # ❌ ADMIN KLIK TOLAK
    if query[0] == "failed":
        await bot.send_message(
            get_user.id, 
            "<b>❌ PEMBAYARAN DITOLAK!\n\nBukti tidak valid. Silakan bayar ulang.</b>"
        )
        return await callback_query.edit_message_caption(
            caption=f"<b>❌ {get_user.first_name} DITOLAK.</b>"
        )

    # 🏠 KEMBALI KE HOME
    if query[0] == "home":
        if get_user.id in CONFIRM_PAYMENT:
            CONFIRM_PAYMENT.remove(get_user.id)
        
        # GUNAKAN FUNGSI DARI MODULE LAIN
        try:
            from add_ubot import StartUtama
            buttons_home = BTN.START(callback_query)
            return await callback_query.edit_message_text(
                MSG.START(callback_query), 
                reply_markup=InlineKeyboardMarkup(buttons_home)
            )
        except:
            # FALLBACK
            return await callback_query.edit_message_text(
                "<b>🏠 HOME</b>",
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton("🔃 MULAI", callback_data="bahan")
                ]])
            )

# ============================================================
# 🏁 END OF MODULE
# ============================================================