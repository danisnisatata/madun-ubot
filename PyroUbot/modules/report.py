import asyncio
from datetime import datetime
from pyrogram import raw
from pyrogram.errors import FloodWait, RPCError
from PyroUbot import *

__MODULE__ = "ᴀᴜᴛᴏ ʀᴇᴘᴏʀᴛ"
__HELP__ = """
<blockquote><b>⦪ ᴜʟᴛɪᴍᴀᴛᴇ sᴛᴇᴀʟᴛʜ ʀᴇᴘᴏʀᴛ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ʀᴇᴘᴏʀᴛ</code> [ʀᴇᴘʟʏ/ᴜsᴇʀ] [ᴀʟᴀsᴀɴ]

<b>⌭ ᴀʟᴀsᴀɴ :</b>
ᚗ <code>sᴄᴀᴍ</code>, <code>sᴘᴀᴍ</code>, <code>ᴠɪᴏʟᴇɴᴄᴇ</code>, <code>ᴄᴏᴘʏʀɪɢʜᴛ</code>, <code>ᴄʜɪʟᴅ</code>.

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇʟᴀᴘᴏʀᴋᴀɴ ᴛᴀʀɢᴇᴛ sᴇᴄᴀʀᴀ ᴍᴀsɪꜰ ᴅᴀɴ sɪʟᴇɴᴛ ᴛᴀɴᴘᴀ ᴊᴇᴊᴀᴋ sɪsᴛᴇᴍ ʙᴏᴛ ᴅᴇɴɢᴀɴ ᴛᴇᴋs ᴀᴅᴜᴀɴ sᴘᴇsɪꜰɪᴋ.</blockquote>
"""

@PY.UBOT("report")
@PY.TOP_CMD
async def report_handler(client, message):
    # Proteksi Visual & Loading
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)
    load = getattr(EMO, "LOADING", lambda x: "⏳")(client)
    if asyncio.iscoroutine(load):
        load = await load

    # DATABASE TEKS ADUAN SPESIFIK (1000% PROFESSIONAL)
    report_configs = {
        "scam": {
            "raw": raw.types.InputReportReasonFake(),
            "text": "This account asked me to send money for a service/product and did not deliver after payment. I believe this account is scamming users. Please review the chat history for evidence."
        },
        "spam": {
            "raw": raw.types.InputReportReasonSpam(),
            "text": "This user is flooding groups and private chats with unsolicited links and promotional content. This is disruptive and violates community standards."
        },
        "violence": {
            "raw": raw.types.InputReportReasonViolence(),
            "text": "This account is promoting violence and making direct threats. This behavior poses a risk to the community safety."
        },
        "copyright": {
            "raw": raw.types.InputReportReasonCopyright(),
            "text": "This account is distributing copyrighted content without any legal rights or authorization. Please remove the infringing materials."
        },
        "child": {
            "raw": raw.types.InputReportReasonChildAbuse(),
            "text": "This account is sharing illegal and harmful content involving minors. This requires immediate urgent attention from the moderation team."
        },
        "other": {
            "raw": raw.types.InputReportReasonOther(),
            "text": "This account is violating the Terms of Service with suspicious activity. Please investigate further."
        }
    }

    user_id = None
    reason_input = "other"
    msg_ids = []

    # Validasi Target & Bukti Pesan
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        msg_ids = [message.reply_to_message.id]
        args = get_arg(message)
        if args:
            reason_input = args.split()[0].lower()
    else:
        args = message.command
        if len(args) < 2:
            return await message.reply_text(f"<blockquote><b>{ggl} ᴍᴏʜᴏɴ ʀᴇᴘʟʏ ᴀᴛᴀᴜ ᴍᴀsᴜᴋᴋᴀɴ ᴜsᴇʀɴᴀᴍᴇ!</b></blockquote>")
        user_id = args[1]
        if len(args) > 2:
            reason_input = args[2].lower()

    # Ambil Config
    config = report_configs.get(reason_input, report_configs["other"])
    selected_reason = config["raw"]
    final_report_text = config["text"]
    
    try:
        user = await client.get_users(user_id)
        peer_to_report = await client.resolve_peer(user.id)
    except Exception as e:
        return await message.reply_text(f"<blockquote><b>{ggl} ɢᴀɢᴀʟ ʀᴇsᴏʟᴠᴇ:</b> <code>{str(e)}</code></blockquote>")

    all_ubots = ubot._ubot
    total_ubots = len(all_ubots)
    success_count = 0
    fail_count = 0
    start_time = datetime.now() # Fix: Datetime calculation
    
    status_msg = await message.reply_text(f"<blockquote><b>{prs} ɪɴɪᴛɪᴀᴛɪɴɢ ᴍᴜʟᴛɪ-ᴇᴠɪᴅᴇɴᴄᴇ sᴛʀɪᴋᴇ ᴏɴ {user.first_name}...</b></blockquote>")

    # PROSES GLOBAL SILENT (UBOT LAIN TIDAK AKAN CHAT)
    for index, bot in enumerate(all_ubots, start=1):
        try:
            # 1. Report Profil via API (Silent)
            await bot.invoke(
                raw.functions.account.ReportPeer(
                    peer=peer_to_report,
                    reason=selected_reason,
                    message=final_report_text
                )
            )
            # 2. Report Pesan via API (Silent)
            if msg_ids:
                await bot.invoke(
                    raw.functions.messages.Report(
                        peer=peer_to_report,
                        id=msg_ids,
                        reason=selected_reason,
                        message=f"Verified evidence for {reason_input} violation."
                    )
                )
            # 3. Silent Block Masal
            await bot.block_user(user.id)
            success_count += 1
        except FloodWait as e:
            await asyncio.sleep(e.value)
            success_count += 1
        except:
            fail_count += 1

        # Animasi Progress Bar
        if index % 5 == 0 or index == total_ubots:
            duration = (datetime.now() - start_time).seconds
            persen = int((index / total_ubots) * 100)
            bar = "■" * (persen // 10) + "□" * (10 - (persen // 10))
            await status_msg.edit(
                f"<blockquote><b>{load} ᴍᴇʟᴀᴘᴏʀᴋᴀɴ ({reason_input.upper()})...</b>\n\n"
                f"<b>ᚗ ᴘʀᴏɢʀᴇss :</b> <code>[{bar}] {persen}%</code>\n"
                f"<b>ᚗ sᴜᴄᴄᴇss :</b> <code>{success_count}</code> | <b>ꜰᴀɪʟ :</b> <code>{fail_count}</code>\n"
                f"<b>ᚗ ʀᴜɴᴛɪᴍᴇ :</b> <code>{duration}s</code></blockquote>"
            )
        await asyncio.sleep(0.15)

    # KIRIM CHAT FORMAL KE NOTOSCAM (HANYA AKUN PEMANGGIL/OWNER)
    if reason_input in ["scam", "fake", "spam"]:
        try:
            # Mengirimkan laporan dengan teks spesifik ke bot resmi Telegram
            notoscam_msg = f"/report {user.id}\n\n{final_report_text}"
            await client.send_message("NoToScam", notoscam_msg)
        except:
            pass

    # Laporan Akhir
    await status_msg.edit(
        f"<blockquote><b>{brhsl} sᴛᴇᴀʟᴛʜ sᴛʀɪᴋᴇ sᴇʟᴇsᴀɪ!</b>\n\n"
        f"<b>ᚗ ᴛᴀʀɢᴇᴛ :</b> {user.mention}\n"
        f"<b>ᚗ ᴀʟᴀsᴀɴ :</b> <code>{reason_input.upper()}</code>\n"
        f"<b>ᚗ sᴜᴄᴄᴇss :</b> <code>{success_count} ʀᴇᴘᴏʀᴛs</code>\n\n"
        f"<b>⌭ sᴛᴀᴛᴜs :</b> ʟᴀᴘᴏʀᴀɴ ᴍᴀsɪꜰ ᴛᴇʟᴀʜ ᴅɪᴘʀᴏsᴇs sᴇᴄᴀʀᴀ sɪʟᴇɴᴛ.</blockquote>"
    )
    