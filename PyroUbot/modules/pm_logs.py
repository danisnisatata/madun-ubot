import asyncio
import wget
from gc import get_objects
from pykeyboard import InlineKeyboard
from pyrogram.types import (InlineKeyboardButton, InlineQueryResultArticle,
                            InlineQueryResultPhoto, InlineQueryResultVideo,
                            InputTextMessageContent, InlineKeyboardMarkup)
from PyroUbot import *

# Default Premium Text
PM_TEXT = """
<blockquote><b>🙋🏻‍♂️ ʜᴀʟᴏ {mention} ᴀᴅᴀ ʏᴀɴɢ ʙɪsᴀ ᴅɪʙᴀɴᴛᴜ?</b>

sᴀʏᴀ ᴀᴅᴀʟᴀʜ ᴘᴍ-sᴇᴄᴜʀɪᴛʏ ᴅɪsɪɴɪ.
sɪʟᴀᴋᴀɴ ᴛᴜɴɢɢᴜ ᴍᴀᴊɪᴋᴀɴ sᴀʏᴀ ᴍᴇᴍʙᴀʟᴀs ᴘᴇsᴀɴ ᴀɴᴅᴀ.
ᴊᴀɴɢᴀɴ sᴘᴀᴍ ᴀᴛᴀᴜ ᴀɴᴅᴀ ᴀᴋᴀɴ ᴅɪʙʟᴏᴋɪʀ ᴏᴛᴏᴍᴀᴛɪs!

<b>⚠ ᴘᴇʀɪɴɢᴀᴛᴀɴ :</b> <code>{warn}</code> ʜᴀᴛɪ-ʜᴀᴛɪ</blockquote>
"""

__MODULE__ = "ᴘᴍᴘᴇʀᴍɪᴛ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴘᴍᴘᴇʀᴍɪᴛ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴘᴍᴘᴇʀᴍɪᴛ</code> [ᴏɴ/ᴏꜰꜰ]
ᚗ <code>{0}ᴏᴋ</code> | <code>.ᴛᴇʀɪᴍᴀ</code>
ᚗ <code>{0}ɴᴏ</code> | <code>.ᴛᴏʟᴀᴋ</code>
ᚗ <code>{0}sᴇᴛᴘᴍ</code> [ʟɪᴍɪᴛ/ᴛᴇxᴛ/ᴘɪᴄ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴɢᴀᴛᴜʀ ᴘᴇʀɪᴊɪɴᴀɴ ᴘᴇsᴀɴ ᴘʀɪʙᴀᴅɪ ᴜɴᴛᴜᴋ ᴍᴇɴɢʜɪɴᴅᴀʀɪ sᴘᴀᴍᴍᴇʀ.
ᚗ ᴛᴜᴛᴏʀɪᴀʟ ʙᴜᴛᴛᴏɴ : <a href='https://t.me/Priaindiareal/1558'>ᴄʟɪᴄᴋ ᴋɪɴɢᴢ</a></blockquote>
"""

FLOOD = {}
MSG_ID = {}

@PY.NO_CMD_UBOT("PMPERMIT", ubot)
async def pmpermit_handler(client, message):
    DEVS = [6385841558]
    user = message.from_user
    if not user or user.id in DEVS or user.id == client.me.id:
        return
    
    pm_on = await get_vars(client.me.id, "PMPERMIT")
    if pm_on:
        if user.id in MSG_ID:
            try: await client.delete_messages(message.chat.id, MSG_ID.get(user.id))
            except: pass
            
        check = await get_pm_id(client.me.id)
        if user.id not in check:
            FLOOD[user.id] = FLOOD.get(user.id, 0) + 1
            pm_limit = await get_vars(client.me.id, "PM_LIMIT") or "5"
            
            if FLOOD[user.id] > int(pm_limit):
                del FLOOD[user.id]
                await message.reply("<blockquote><b>❌ sᴜᴅᴀʜ ᴅɪɪɴɢᴀᴛᴋᴀɴ ᴊᴀɴɢᴀɴ sᴘᴀᴍ, sᴇᴋᴀʀᴀɴɢ ᴀɴᴅᴀ ᴅɪʙʟᴏᴋɪʀ!</b></blockquote>")
                return await client.block_user(user.id)

            pm_msg = await get_vars(client.me.id, "PM_TEXT") or PM_TEXT
            rpk = f"[{user.first_name}](tg://user?id={user.id})"
            peringatan = f"{FLOOD[user.id]} / {pm_limit}"

            if "~>" in pm_msg:
                x = await client.get_inline_bot_results(bot.me.username, f"pm_pr {id(message)} {FLOOD[user.id]}")
                msg = await client.send_inline_bot_result(message.chat.id, x.query_id, x.results[0].id, reply_to_message_id=message.id)
                MSG_ID[user.id] = int(msg.updates[0].id)
            else:
                pm_pic = await get_vars(client.me.id, "PM_PIC")
                if pm_pic:
                    try:
                        msg = await message.reply_photo(pm_pic, caption=pm_msg.format(mention=rpk, warn=peringatan))
                    except:
                        msg = await message.reply(pm_msg.format(mention=rpk, warn=peringatan))
                else:
                    msg = await message.reply(pm_msg.format(mention=rpk, warn=peringatan))
                MSG_ID[user.id] = msg.id

@PY.UBOT("setpm")
@PY.TOP_CMD
async def setpm_handler(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    if len(message.command) < 3:
        return await message.reply(f"<blockquote><b>{ggl} ɢᴜɴᴀᴋᴀɴ: .sᴇᴛᴘᴍ [ʟɪᴍɪᴛ/ᴛᴇxᴛ/ᴘɪᴄ] [ᴠᴀʟᴜᴇ]</b></blockquote>")
    
    query = {"limit": "PM_LIMIT", "text": "PM_TEXT", "pic": "PM_PIC"}
    key = message.command[1].lower()
    if key not in query:
        return await message.reply(f"<blockquote><b>{ggl} ǫᴜᴇʀʏ ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ!</b></blockquote>")
    
    val = message.text.split(None, 2)[2]
    if val.lower() == "none": val = False
    
    await set_vars(client.me.id, query[key], val)
    await message.reply(f"<blockquote><b>{brhsl} ᴘᴍᴘᴇʀᴍɪᴛ {key} ʙᴇʀʜᴀsɪʟ ᴅɪsᴇᴛᴛɪɴɢ.</b></blockquote>")

@PY.UBOT("pmpermit")
@PY.TOP_CMD
async def pm_toggle_handler(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    if len(message.command) < 2:
        return await message.reply(f"<blockquote><b>{ggl} ɢᴜɴᴀᴋᴀɴ: .ᴘᴍᴘᴇʀᴍɪᴛ [ᴏɴ/ᴏꜰꜰ]</b></blockquote>")

    cmd = message.command[1].lower()
    if cmd not in ["on", "off"]:
        return await message.reply(f"<blockquote><b>{ggl} ᴏᴘsɪ ʜᴀɴʏᴀ ᴏɴ/ᴏꜰꜰ!</b></blockquote>")

    status = (cmd == "on")
    await set_vars(client.me.id, "PMPERMIT", status)
    await message.reply(f"<blockquote><b>{brhsl} ᴘᴍᴘᴇʀᴍɪᴛ ʙᴇʀʜᴀsɪʟ ᴅɪ{'ᴀᴋᴛɪꜰᴋᴀɴ' if status else 'ɴᴏɴᴀᴋᴛɪꜰᴋᴀɴ'}.</b></blockquote>")

@PY.UBOT("ok|terima")
@PY.TOP_CMD
@PY.PRIVATE
async def ok_handler(client, message):
    brhsl = await EMO.BERHASIL(client)
    user = message.chat
    rpk = f"[{user.first_name}](tg://user?id={user.id})"
    vars = await get_pm_id(client.me.id)
    if user.id not in vars:
        await add_pm_id(client.me.id, user.id)
        return await message.reply(f"<blockquote><b>{brhsl} ʙᴀɪᴋʟᴀʜ, {rpk} ᴛᴇʟᴀʜ ᴅɪᴛᴇʀɪᴍᴀ.</b></blockquote>")
    return await message.reply(f"<blockquote><b>{brhsl} {rpk} sᴜᴅᴀʜ ᴀᴅᴀ ᴅɪ ᴅᴀꜰᴛᴀʀ ɪᴢɪɴ.</b></blockquote>")

@PY.UBOT("no|tolak")
@PY.TOP_CMD
@PY.PRIVATE
async def no_handler(client, message):
    ggl = await EMO.GAGAL(client)
    user = message.chat
    rpk = f"[{user.first_name}](tg://user?id={user.id})"
    vars = await get_pm_id(client.me.id)
    if user.id not in vars:
        await message.reply(f"<blockquote><b>{ggl} ᴍᴀᴀꜰ {rpk}, ᴀɴᴅᴀ ᴅɪʙʟᴏᴋɪʀ ᴋᴀʀᴇɴᴀ sᴘᴀᴍ!</b></blockquote>")
        return await client.block_user(user.id)
    else:
        await remove_pm_id(client.me.id, user.id)
        return await message.reply(f"<blockquote><b>{ggl} ɪᴢɪɴ ᴘᴍ ᴜɴᴛᴜᴋ {rpk} ᴛᴇʟᴀʜ ᴅɪᴄᴀʙᴜᴛ.</b></blockquote>")

@PY.UBOT("logs")
@PY.TOP_CMD
async def logs_handler(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    if len(message.command) < 2:
        return await message.reply(f"<blockquote><b>{ggl} ɢᴜɴᴀᴋᴀɴ: .ʟᴏɢs [ᴏɴ/ᴏꜰꜰ]</b></blockquote>")

    cmd = message.command[1].lower()
    status = (cmd == "on")
    await set_vars(client.me.id, "ON_LOGS", status)
    await message.reply(f"<blockquote><b>{brhsl} ʟᴏɢs ʙᴇʀʜᴀsɪʟ ᴅɪsᴇᴛᴛɪɴɢ ᴋᴇ: {cmd.upper()}</b></blockquote>")
    