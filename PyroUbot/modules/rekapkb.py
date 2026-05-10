import re
from PyroUbot import *

__MODULE__ = "ʀᴇᴋᴀᴘ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʀᴇᴋᴀᴘ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ʀᴇᴋᴀᴘ</code> [ʀᴇᴘʟʏ ᴘᴇsᴀɴ]
ᚗ <code>{0}ᴡɪɴ</code> [ꜰᴇᴇ] [ʀᴇᴘʟʏ ᴘᴇsᴀɴ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇᴍʙᴀɴᴛᴜ ᴍᴇɴɢʜɪᴛᴜɴɢ sᴇʟɪsɪʜ sᴀʟᴅᴏ ᴅᴀɴ ᴋᴀʟᴋᴜʟᴀsɪ ᴡɪɴ sᴇᴛᴇʟᴀʜ ᴅɪᴘᴏᴛᴏɴɢ ꜰᴇᴇ.</blockquote>
"""

def rekap_data(text):
    kecil, besar = [], []
    kecil_total, besar_total = 0, 0
    for match in re.finditer(r"(\w+)\s*:\s*(\d+)", text):
        nama, nominal = match.groups()
        nominal = int(nominal)
        if nama.lower() in ["k", "kecil"]:
            kecil.append(nominal)
            kecil_total += nominal
        elif nama.lower() in ["b", "besar"]:
            besar.append(nominal)
            besar_total += nominal
    return {"kecil": kecil, "besar": besar, "k_total": kecil_total, "b_total": besar_total}

def format_number(num):
    return f"{num:,}".replace(",", ".")

@PY.UBOT("rekap")
@PY.TOP_CMD
async def rekap_handler(client, message):
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)
    
    if not message.reply_to_message or not message.reply_to_message.text:
        return await message.reply_text(f"<blockquote><b>{ggl} ᴍᴏʜᴏɴ ʙᴀʟᴀs ᴋᴇ ᴘᴇsᴀɴ ʏᴀɴɢ ʙᴇʀɪsɪ ᴅᴀᴛᴀ!</b></blockquote>")

    data = rekap_data(message.reply_to_message.text)
    k_total, b_total = data["k_total"], data["b_total"]
    selisih = abs(k_total - b_total)
    
    status_selisih = "sᴇɪᴍʙᴀɴɢ 🎉"
    if k_total > b_total:
        status_selisih = f"ᴋᴇᴄɪʟ ᴜɴɢɢᴜʟ {format_number(selisih)} ᴋ"
    elif b_total > k_total:
        status_selisih = f"ʙᴇsᴀʀ ᴜɴɢɢᴜʟ {format_number(selisih)} ᴋ"

    res = (
        f"<blockquote><b>{brhsl} ʀᴇᴋᴀᴘ sᴀʟᴅᴏ ᴘʀᴇᴍɪᴜᴍ</b>\n\n"
        f"<b>ᚗ ᴋᴇᴄɪʟ :</b> <code>[{', '.join(map(format_number, data['kecil']))}]</code>\n"
        f"<b>ᚗ ᴛᴏᴛᴀʟ ᴋ :</b> <code>{format_number(k_total)}</code>\n\n"
        f"<b>ᚗ ʙᴇsᴀʀ :</b> <code>[{', '.join(map(format_number, data['besar']))}]</code>\n"
        f"<b>ᚗ ᴛᴏᴛᴀʟ ʙ :</b> <code>{format_number(b_total)}</code>\n\n"
        f"<b>⌭ sᴇʟɪsɪʜ :</b> <code>{status_selisih}</code>\n"
        f"<b>⌭ ᴛᴏᴛᴀʟ ᴀʟʟ :</b> <code>{format_number(k_total + b_total)} ᴋ</code></blockquote>"
    )
    await message.reply_text(res)

@PY.UBOT("win")
@PY.TOP_CMD
async def win_handler(client, message):
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)
    
    args = get_arg(message)
    if not args or not args.isdigit():
        return await message.reply_text(f"<blockquote><b>{ggl} ꜰᴏʀᴍᴀᴛ: <code>.ᴡɪɴ 5</code> (ᴜɴᴛᴜᴋ ꜰᴇᴇ 5%)</b></blockquote>")

    if not message.reply_to_message or not message.reply_to_message.text:
        return await message.reply_text(f"<blockquote><b>{ggl} ʙᴀʟᴀs ᴋᴇ ᴘᴇsᴀɴ ᴅᴀᴛᴀ sᴀʟᴅᴏ!</b></blockquote>")

    fee = int(args)
    data = rekap_data(message.reply_to_message.text)
    
    def calc(list_data):
        return [f"{format_number(x)} // {format_number(round(x - (x * fee / 100)))}" for x in list_data]

    res = (
        f"<blockquote><b>{brhsl} ʜᴀsɪʟ ᴡɪɴ (ꜰᴇᴇ {fee}%)</b>\n\n"
        f"<b>ᚗ ᴋᴇᴄɪʟ :</b>\n<code>" + "\n".join(calc(data['kecil'])) + "</code>\n\n"
        f"<b>ᚗ ʙᴇsᴀʀ :</b>\n<code>" + "\n".join(calc(data['besar'])) + "</code>\n\n"
        f"<b>⌭ sᴛᴀᴛᴜs :</b> sᴇʟᴇsᴀɪ ᴅɪʜɪᴛᴜɴɢ</blockquote>"
    )
    await message.reply_text(res)
    