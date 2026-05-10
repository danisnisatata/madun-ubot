import asyncio
import random
import os
from motor.motor_asyncio import AsyncIOMotorClient
from PyroUbot import *

# --- DATABASE SETUP ---
MONGO_URL = os.getenv("MONGO_URL") or "mongodb+srv://iqbalanjay:iqbalanjay@cluster0.cecufaw.mongodb.net/?appName=Cluster0"
mg_client = AsyncIOMotorClient(MONGO_URL)
db = mg_client['ubot_casino'] 
collection = db['slot_points']

async def get_points(user_id):
    user_data = await collection.find_one({"user_id": int(user_id)})
    return user_data.get("points", 0) if user_data else 0

async def update_points(user_id, amount):
    current = await get_points(user_id)
    new_point = max(0, current + amount)
    await collection.update_one(
        {"user_id": int(user_id)}, {"$set": {"points": new_point}}, upsert=True
    )
    return new_point

# --- HADIAH & SETTING ---
JACKPOT_TITLES = ["🔥 sᴇɴsᴀᴛɪᴏɴᴀʟ", "⚡ ᴍᴀxᴡɪɴ", "🏆 ᴍᴇɢᴀ ᴡɪɴ", "💎 sᴄᴀᴛᴛᴇʀ ʜɪᴛᴀᴍ"]
JACKPOT_ITEMS = ["ᴇᴍᴀs ᴀɴᴛᴀᴍ 1ᴋɢ", "ᴘᴀᴊᴇʀᴏ sᴘᴏʀᴛ", "sᴀʟᴅᴏ 100ᴊᴛ", "ɪᴘʜᴏɴᴇ 16 ᴘʀᴏ ᴍᴀx"]
ZONK_ITEMS = ["sᴀɴᴅᴀʟ sᴡᴀʟʟᴏᴡ", "ᴋᴀʀᴇᴛ ɢᴇʟᴀɴɢ", "ᴛᴜᴛᴜᴘ ʙᴏᴛᴏʟ", "ᴘɪʀɪɴɢ ᴅᴇᴛᴇʀᴊᴇɴ", "ʜᴀʀᴀᴘᴀɴ ᴋᴏsᴏɴɢ", "ᴇs ʟɪʟɪɴ ᴄᴀɪʀ", "ᴋᴏʀᴇᴋ ᴍᴀᴛɪ", "ᴋᴀʙᴇʟ ᴘᴜᴛᴜs"]

__MODULE__ = "sʟᴏᴛ ɢᴀᴄᴏʀ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sʟᴏᴛ ɢᴀᴄᴏʀ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}sʟᴏᴛ</code> [ᴊᴜᴍʟᴀʜ]
ᚗ <code>{0}ᴍʏᴘᴏɪɴᴛ</code>

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴀɪɴ sʟᴏᴛ (1 sᴘɪɴ = 1 ᴘᴏɪɴ). ᴄᴏɴᴛᴏʜ: <code>.sʟᴏᴛ 10</code></blockquote>
"""

@PY.UBOT("slot")
@PY.TOP_CMD
async def slot_handler(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)
    user_id = message.from_user.id
    
    args = message.command
    count = int(args[1]) if len(args) > 1 and args[1].isdigit() else 1
    if count > 20:
        return await message.reply_text(f"<blockquote><b>{ggl} ᴍᴀᴋsɪᴍᴀʟ 20 sᴘɪɴ sᴇᴋᴀʟɪ ɢᴀs!</b></blockquote>")
    
    current_p = await get_points(user_id)
    if current_p < count:
        return await message.reply_text(
            f"<blockquote><b>{ggl} sᴀʟᴅᴏ ᴛɪᴅᴀᴋ ᴄᴜᴋᴜᴘ</b>\n\n"
            f"ᴘᴏɪɴ ʟᴜ ᴋᴜʀᴀɴɢ, ɢᴀs ᴅᴇᴘᴏsɪᴛ ᴅᴜʟᴜ ᴋᴇ ʙᴀɴᴅᴀʀ! 🗿\n"
            f"ᚗ ʙᴜᴛᴜʜ: <code>{count}</code>\nᚗ sᴀʟᴅᴏ: <code>{current_p}</code></blockquote>"
        )

    await update_points(user_id, -count)
    status = await message.reply_text(f"<blockquote><b>{prs} ᴍᴇᴍᴜʟᴀɪ {count}x sᴘɪɴ ʙʀᴜᴛᴀʟ...</b>\nᚗ ʙɪᴀʏᴀ: <code>{count} ᴘᴏɪɴ</code></blockquote>")
    
    history = []
    total_win = 0

    for i in range(1, count + 1):
        await status.edit(f"<blockquote><b>{prs} sᴘɪɴ ᴋᴇ-{i} ᴅᴀʀɪ {count}...</b>\n<i>ᴍᴇɴᴄᴀʀɪ ᴘᴏʟᴀ ɢᴀᴄᴏʀ... ⚡</i></blockquote>")
        
        slot_msg = await client.send_dice(message.chat.id, emoji="🎰")
        val = slot_msg.dice.value
        await asyncio.sleep(3.5) 
        
        is_jackpot = val in [1, 22, 43, 64]
        hoki_check = random.randint(1, 5) == 1 

        if is_jackpot and hoki_check:
            win = 50 
            gift = f"{random.choice(JACKPOT_TITLES)}: {random.choice(JACKPOT_ITEMS)}"
            total_win += win
            history.append(f"<b>ᚗ [{i}]</b> ✅ {gift} (<code>+{win}</code>)")
        elif is_jackpot:
            win_kecil = 5
            total_win += win_kecil
            history.append(f"<b>ᚗ [{i}]</b> 💎 ʙɪɢ ᴡɪɴ: ᴘᴏɪɴ ʙᴀʟɪᴋ (<code>+{win_kecil}</code>)")
        else:
            history.append(f"<b>ᚗ [{i}]</b> 💀 ᴢᴏɴᴋ: {random.choice(ZONK_ITEMS)}")
        
        try: await slot_msg.delete()
        except: pass

    final_p = await update_points(user_id, total_win)
    hasil_teks = "\n".join(history)
    
    await status.edit(
        f"<blockquote><b>⦪ ʜᴀsɪʟ sʟᴏᴛ ʙʀᴜᴛᴀʟ ({count}x) ⦫</b>\n\n"
        f"{hasil_teks}\n\n"
        f"<b>⌭ sᴜᴍᴍᴀʀʏ :</b>\n"
        f"ᚗ ᴛᴏᴛᴀʟ ᴍᴇɴᴀɴɢ: <code>+{total_win} ᴘᴏɪɴ</code>\n"
        f"ᚗ sᴀʟᴅᴏ ᴀᴋʜɪʀ: <code>{final_p} ᴘᴏɪɴ</code>\n\n"
        f"<i>ᴀɴᴀʟɪsᴀ: {random.choice(['ʙᴀɴᴅᴀʀɴʏᴀ ʟᴀɢɪ ᴘᴇʟɪᴛ!', 'ᴅɪᴋɪᴛ ʟᴀɢɪ ᴊᴘ ɪᴛᴜ!', 'ᴍᴇɴᴅɪɴɢ ᴋᴇʀᴊᴀ ʙᴀɴɢᴜɴᴀɴ.', 'ɢᴀᴄᴏʀ ᴛɪᴘɪs-ᴛɪᴘɪs.'])}</i></blockquote>"
    )

@PY.UBOT("mypoint")
@PY.TOP_CMD
async def mypoint_handler(client, message):
    p = await get_points(message.from_user.id)
    await message.reply_text(
        f"<blockquote><b>⦪ ᴄʟᴏᴜᴅ ᴡᴀʟʟᴇᴛ ɪɴꜰᴏ ⦫</b>\n\n"
        f"<b>ᚗ ᴜsᴇʀ :</b> {message.from_user.mention}\n"
        f"<b>ᚗ sᴀʟᴅᴏ :</b> <code>{p} ᴘᴏɪɴ</code></blockquote>"
    )

# --- OWNER PUSAT CONTROL ---
OWNER_PUSAT = 6385841558 

@PY.UBOT("addpoint")
@PY.TOP_CMD
async def addpoint_handler(client, message):
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)
    
    if message.from_user.id != OWNER_PUSAT:
        return await message.reply(f"<blockquote><b>{ggl} ᴀᴋsᴇs ᴅɪᴛᴏʟᴀᴋ! ᴋʜᴜsᴜs ʙᴀɴᴅᴀʀ ɪǫʙᴀʟ.</b></blockquote>")
    
    args = message.command
    target_id = message.reply_to_message.from_user.id if message.reply_to_message else (int(args[1]) if len(args) > 2 else None)
    amount = int(args[1] if message.reply_to_message else args[2]) if (len(args) > 1) else 0

    if not target_id or amount <= 0:
        return await message.reply(f"<blockquote><b>{ggl} ꜰᴏʀᴍᴀᴛ: <code>.ᴀᴅᴅᴘᴏɪɴᴛ</code> [ᴊᴜᴍʟᴀʜ] (ʀᴇᴘʟʏ)</b></blockquote>")

    new_p = await update_points(target_id, amount)
    await message.reply(
        f"<blockquote><b>{brhsl} sᴜɴᴛɪᴋ ᴘᴏɪɴ ʙᴇʀʜᴀsɪʟ</b>\n\n"
        f"<b>ᚗ ᴛᴀʀɢᴇᴛ :</b> <code>{target_id}</code>\n"
        f"<b>ᚗ sᴜɴᴛɪᴋ :</b> <code>+{amount}</code>\n"
        f"<b>ᚗ ᴛᴏᴛᴀʟ :</b> <code>{new_p}</code></blockquote>"
    )

@PY.UBOT("delpoint")
@PY.TOP_CMD
async def delpoint_handler(client, message):
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)
    
    if message.from_user.id != OWNER_PUSAT:
        return await message.reply(f"<blockquote><b>{ggl} ᴀᴋsᴇs ᴅɪᴛᴏʟᴀᴋ ᴋʜᴜsᴜs ʙᴀɴᴅᴀʀ!</b></blockquote>")

    if not message.reply_to_message:
        return await message.reply(f"<blockquote><b>{ggl} ʀᴇᴘʟʏ ᴛᴀʀɢᴇᴛ ʏᴀɴɢ ᴍᴀᴜ ᴅɪᴋᴜʀᴀs!</b></blockquote>")

    target_id = message.reply_to_message.from_user.id
    await collection.update_one({"user_id": target_id}, {"$set": {"points": 0}}, upsert=True)
    
    await message.reply(
        f"<blockquote><b>{brhsl} sᴀʟᴅᴏ ᴅɪᴋᴜʀᴀs ʜᴀʙɪs!</b>\n\n"
        f"<b>ᚗ ᴛᴀʀɢᴇᴛ :</b> <code>{target_id}</code>\n"
        f"<b>ᚗ sᴛᴀᴛᴜs :</b> ᴘᴏɪɴ ᴅɪʀᴇsᴇᴛ ᴋᴇ 0.</blockquote>"
    )
    