import asyncio
from pyrogram.errors import FloodWait
from PyroUbot import *

spam_taksdb = {}
is_spamming = False

__MODULE__ = "sᴘᴀᴍ ᴅʙ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴘᴀᴍ ᴅʙ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}sᴘᴀᴍᴅʙ</code> [ᴅᴇʟᴀʏ] [ʀᴇᴘʟʏ]
ᚗ <code>{0}sᴛsᴘᴀᴍ</code>
ᚗ <code>{0}sᴘᴀᴍʟɪsᴛ</code>
ᚗ <code>{0}ᴀᴅᴅsᴘᴀᴍ</code>
ᚗ <code>{0}ᴅᴇʟsᴘᴀᴍ</code>

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴᴊᴀʟᴀɴᴋᴀɴ ᴘᴇɴɢɪʀɪᴍᴀɴ ᴘᴇsᴀɴ ᴏᴛᴏᴍᴀᴛɪs ᴋᴇ ᴅᴀꜰᴛᴀʀ ɢʀᴜᴘ ʏᴀɴɢ ᴀᴅᴀ ᴅɪ ᴅᴀᴛᴀʙᴀsᴇ.</blockquote>
"""

@PY.UBOT("spamdb")
@PY.TOP_CMD
async def spamdb_cmd(c, m):
    global is_spamming
    ggl = await EMO.GAGAL(c)
    prs = await EMO.PROSES(c)

    if not m.reply_to_message:
        return await m.reply(f"<blockquote><b>{ggl} sɪʟᴀᴋᴀɴ ʙᴀʟᴀs ᴋᴇ ᴘᴇsᴀɴ!</b></blockquote>")
    
    args = get_arg(m)
    if not args:
        return await m.reply(f"<blockquote><b>{ggl} ʜᴀʀᴀᴘ ᴍᴀsᴜᴋᴋᴀɴ ᴡᴀᴋᴛᴜ ᴅᴇʟᴀʏ!</b></blockquote>")
        
    try:
        interval = int(args)
    except ValueError:
        return await m.reply(f"<blockquote><b>{ggl} ᴅᴇʟᴀʏ ʜᴀʀᴜs ʙᴇʀᴜᴘᴀ ᴀɴɢᴋᴀ.</b></blockquote>")

    if interval < 10:
        return await m.reply(f"<blockquote><b>{ggl} ᴍɪɴɪᴍᴀʟ ᴅᴇʟᴀʏ ᴀᴅᴀʟᴀʜ 10 ᴅᴇᴛɪᴋ.</b></blockquote>")

    chat_ids = monggo.ambil_spdb(c.me.id)
    if not chat_ids:
        return await m.reply(f"<blockquote><b>{ggl} ᴅᴀᴛᴀʙᴀsᴇ ᴋᴏsᴏɴɢ, ᴀᴅᴅsᴘᴀᴍ ᴅᴜʟᴜ ʙᴏs.</b></blockquote>")

    scheduled_message = m.reply_to_message
    is_spamming = True
    
    await m.reply(f"<blockquote><b>{prs} sᴛᴀʀᴛɪɴɢ sᴘᴀᴍ ᴛᴏ ᴅᴀᴛᴀʙᴀsᴇ...</b></blockquote>")

    for chat_id in chat_ids:
        if not is_spamming:
            break

        async def send_scheduled_message(target_id):
            try:
                while True:
                    await asyncio.sleep(interval)
                    await scheduled_message.copy(target_id)
            except FloodWait as e:
                await asyncio.sleep(e.value)
            except Exception:
                if target_id in spam_taksdb:
                    task = spam_taksdb[target_id]
                    task.cancel()
                    del spam_taksdb[target_id]

        task = asyncio.create_task(send_scheduled_message(chat_id))
        spam_taksdb[chat_id] = task

@PY.UBOT("stspam")
@PY.TOP_CMD
async def stspam_cmd(c, m):
    global is_spamming
    ggl = await EMO.GAGAL(c)
    brhsl = await EMO.BERHASIL(c)

    if not spam_taksdb:
        return await m.reply_text(f"<blockquote><b>{ggl} ᴛɪᴅᴀᴋ ᴀᴅᴀ sᴘᴀᴍ ʏᴀɴɢ ʙᴇʀᴊᴀʟᴀɴ.</b></blockquote>")
        
    for chat_id in list(spam_taksdb.keys()):
        task = spam_taksdb[chat_id]
        task.cancel()
        del spam_taksdb[chat_id]
        
    is_spamming = False
    await m.reply(f"<blockquote><b>{brhsl} sᴘᴀᴍ ᴅᴀᴛᴀʙᴀsᴇ ʙᴇʀʜᴀsɪʟ ᴅɪʜᴇɴᴛɪᴋᴀɴ.</b></blockquote>")

@PY.UBOT("spamlist")
@PY.TOP_CMD
async def spamlist_cmd(c, m):
    ggl = await EMO.GAGAL(c)
    teks = "<blockquote><b>⦪ ᴅᴀꜰᴛᴀʀ ᴅᴀᴛᴀʙᴀsᴇ sᴘᴀᴍ ⦫</b>\n\n"
    lists = monggo.ambil_spdb(c.me.id)
    
    if not lists:
        return await m.reply(f"<blockquote><b>{ggl} ᴅᴀᴛᴀʙᴀsᴇ ᴋᴏsᴏɴɢ.</b></blockquote>")
        
    for count, chat_id in enumerate(lists, 1):
        teks += f"ᚗ {count}. <code>{chat_id}</code>\n"
    
    teks += "</blockquote>"
    await m.reply(teks)

@PY.UBOT("addspam|delspam")
@PY.TOP_CMD
async def manage_spam_cmd(c, m):
    brhsl = await EMO.BERHASIL(c)
    prs = await EMO.PROSES(c)
    user_id = c.me.id
    chat_id = m.command[1] if len(m.command) > 1 else m.chat.id
    
    mmk = await m.reply(f"<blockquote><b>{prs} ᴘʀᴏᴄᴇssɪɴɢ...</b></blockquote>")
    
    if m.command[0] == "addspam":
        monggo.tambah_spdb(user_id, chat_id)
        return await mmk.edit(f"<blockquote><b>{brhsl} ɪᴅ <code>{chat_id}</code> ʙᴇʀʜᴀsɪʟ ᴅɪᴛᴀᴍʙᴀʜᴋᴀɴ.</b></blockquote>")
    elif m.command[0] == "delspam":
        monggo.kureng_spdb(user_id, chat_id)
        return await mmk.edit(f"<blockquote><b>{brhsl} ɪᴅ <code>{chat_id}</code> ʙᴇʀʜᴀsɪʟ ᴅɪʜᴀᴘᴜs.</b></blockquote>")
        