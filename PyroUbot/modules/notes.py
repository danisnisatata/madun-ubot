import re
from pyrogram.types import *
from PyroUbot import *

__MODULE__ = "ɴᴏᴛᴇs"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɴᴏᴛᴇs ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴀᴅᴅɴᴏᴛᴇ</code> [ɴᴀᴍᴇ]
⊷ ᴍᴇɴʏɪᴍᴘᴀɴ ᴄᴀᴛᴀᴛᴀɴ (ʀᴇᴘʟʏ ᴋᴇ ᴛᴇᴋs/ᴍᴇᴅɪᴀ).
ᚗ <code>{0}ᴀᴅᴅᴄʙ</code> [ɴᴀᴍᴇ]
⊷ ᴍᴇɴʏɪᴍᴘᴀɴ ᴄᴀʟʟʙᴀᴄᴋ ʙᴜᴛᴛᴏɴ.
ᚗ <code>{0}ɢᴇᴛ</code> [ɴᴀᴍᴇ]
⊷ ᴍᴇɴɢᴀᴍʙɪʟ ᴄᴀᴛᴀᴛᴀɴ ʏᴀɴɢ ᴅɪsɪᴍᴘᴀɴ.
ᚗ <code>{0}ᴅᴇʟɴᴏᴛᴇ | ᴅᴇʟᴄʙ</code>
⊷ ᴍᴇɴɢʜᴀᴘᴜs ᴄᴀᴛᴀᴛᴀɴ ᴀᴛᴀᴜ ᴄᴀʟʟʙᴀᴄᴋ.
ᚗ <code>{0}ʟɪsᴛɴᴏᴛᴇ | ʟɪsᴛᴄʙ</code>
⊷ ᴍᴇʟɪʜᴀᴛ ᴅᴀꜰᴛᴀʀ sɪᴍᴘᴀɴᴀɴ.

<b>⌭ ꜰᴏʀᴍᴀᴛ ʙᴜᴛᴛᴏɴ :</b>
ᚗ <code>| ɴᴀᴍᴀ ᴛᴏᴍʙᴏʟ - ᴜʀʟ/ᴄᴀʟʟʙᴀᴄᴋ |</code>
ᚗ ɢᴜɴᴀᴋᴀɴ <code>#</code> ᴜɴᴛᴜᴋ ᴛᴏᴍʙᴏʟ ᴍᴇɴʏᴀᴍᴘɪɴɢ.

<b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> MADUN ᴜʙᴏᴛ</blockquote>
"""

@PY.UBOT("addnote|addcb")
@PY.TOP_CMD
async def add_notes_handler(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    args = get_arg(message)
    reply = message.reply_to_message
    query = "notes_cb" if message.command[0] == "addcb" else "notes"

    if not args or not reply:
        return await message.reply(
            f"<blockquote><b>{ggl} ꜰᴏʀᴍᴀᴛ sᴀʟᴀʜ!</b>\nᚗ ɢᴜɴᴀᴋᴀɴ: <code>{message.text.split()[0]} [ɴᴀᴍᴇ]</code> (ʀᴇᴘʟʏ ᴋᴇ ᴘᴇsᴀɴ)</blockquote>"
        )

    vars = await get_vars(client.me.id, args, query)
    if vars:
        return await message.reply(f"<blockquote><b>{ggl} ᴄᴀᴛᴀᴛᴀɴ <code>{args}</code> sᴜᴅᴀʜ ᴀᴅᴀ!</b></blockquote>")

    value = None
    type_mapping = {
        "text": reply.text,
        "photo": reply.photo,
        "voice": reply.voice,
        "audio": reply.audio,
        "video": reply.video,
        "animation": reply.animation,
        "sticker": reply.sticker,
    }

    for media_type, media in type_mapping.items():
        if media:
            # Copy ke pesan tersimpan (Saved Messages) sebagai storage
            send = await reply.copy(client.me.id)
            value = {
                "type": media_type,
                "message_id": send.id,
            }
            break

    if value:
        await set_vars(client.me.id, args, value, query)
        return await message.reply(f"<blockquote><b>{brhsl} ᴄᴀᴛᴀᴛᴀɴ <code>{args}</code> ʙᴇʀʜᴀsɪʟ ᴅɪsɪᴍᴘᴀɴ!</b></blockquote>")
    else:
        return await message.reply(f"<blockquote><b>{ggl} ɢᴀɢᴀʟ ᴍᴇɴʏɪᴍᴘᴀɴ ᴄᴀᴛᴀᴛᴀɴ!</b></blockquote>")

@PY.UBOT("delnote|delcb")
@PY.TOP_CMD
async def del_notes_handler(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    args = get_arg(message)

    if not args:
        return await message.reply(f"<blockquote><b>{ggl} ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ɴᴀᴍᴀ ᴄᴀᴛᴀᴛᴀɴ!</b></blockquote>")

    query = "notes_cb" if message.command[0] == "delcb" else "notes"
    vars = await get_vars(client.me.id, args, query)

    if not vars:
        return await message.reply(f"<blockquote><b>{ggl} ᴄᴀᴛᴀᴛᴀɴ <code>{args}</code> ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ!</b></blockquote>")

    await remove_vars(client.me.id, args, query)
    try:
        await client.delete_messages(client.me.id, int(vars["message_id"]))
    except:
        pass
    return await message.reply(f"<blockquote><b>{brhsl} ᴄᴀᴛᴀᴛᴀɴ <code>{args}</code> ʙᴇʀʜᴀsɪʟ ᴅɪʜᴀᴘᴜs!</b></blockquote>")

@PY.UBOT("get")
@PY.TOP_CMD
async def get_notes_handler(client, message):
    ggl = await EMO.GAGAL(client)
    msg = message.reply_to_message or message
    args = get_arg(message)

    if not args:
        return await message.reply(f"<blockquote><b>{ggl} ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ɴᴀᴍᴀ ᴄᴀᴛᴀᴛᴀɴ!</b></blockquote>")

    data = await get_vars(client.me.id, args, "notes")
    if not data:
        return await message.reply(f"<blockquote><b>{ggl} ᴄᴀᴛᴀᴛᴀɴ <code>{args}</code> ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ!</b></blockquote>")

    try:
        m = await client.get_messages(client.me.id, int(data["message_id"]))
    except:
        return await message.reply(f"<blockquote><b>{ggl} ᴘᴇsᴀɴ ᴀsʟɪ ᴅɪ sᴀᴠᴇᴅ ᴍᴇssᴀɢᴇs ᴛᴇʟᴀʜ ᴅɪʜᴀᴘᴜs!</b></blockquote>")

    if data["type"] == "text" and m.text:
        # FIX: Tambahkan pengecekan m.text agar tidak TypeError
        if matches := re.findall(r"\| ([^|]+) - ([^|]+) \|", m.text):
            try:
                x = await client.get_inline_bot_results(
                    bot.me.username, f"get_notes {client.me.id} {args}"
                )
                return await client.send_inline_bot_result(
                    message.chat.id,
                    x.query_id,
                    x.results[0].id,
                    reply_to_message_id=msg.id,
                )
            except Exception as error:
                # Jika inline gagal, kirim copy teks biasa saja
                return await m.copy(message.chat.id, reply_to_message_id=msg.id)
        else:
            return await m.copy(message.chat.id, reply_to_message_id=msg.id)
    else:
        return await m.copy(message.chat.id, reply_to_message_id=msg.id)

@PY.UBOT("listnote|listcb")
@PY.TOP_CMD
async def list_notes_handler(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    ktrng = await EMO.BL_KETERANGAN(client)
    query = "notes_cb" if message.command[0] == "listcb" else "notes"
    
    vars = await all_vars(client.me.id, query)
    if vars:
        msg = f"<blockquote><b>{brhsl} ᴅᴀꜰᴛᴀʀ ᴄᴀᴛᴀᴛᴀɴ MADUN ᴜʙᴏᴛ</b>\n\n"
        for x, data in vars.items():
            msg += f" <b>ᚗ</b> <code>{x}</code> | (<i>{data['type']}</i>)\n"
        msg += f"\n{ktrng} ᴛᴏᴛᴀʟ ᴄᴀᴛᴀᴛᴀɴ : <b>{len(vars)}</b></blockquote>"
    else:
        msg = f"<blockquote><b>{ggl} ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴄᴀᴛᴀᴛᴀɴ ᴛᴇʀsɪᴍᴘᴀɴ.</b></blockquote>"

    return await message.reply(msg, quote=True)

@PY.INLINE("^get_notes")
async def get_notes_inline(client, inline_query):
    query = inline_query.query.split()
    data = await get_vars(int(query[1]), query[2], "notes")
    item = [x for x in ubot._ubot if int(query[1]) == x.me.id]
    for me in item:
        try:
            m = await me.get_messages(int(me.me.id), int(data["message_id"]))
            if not m.text:
                continue
            buttons, text = create_inline_keyboard(m.text, f"{int(query[1])}_{query[2]}")
            return await client.answer_inline_query(
                inline_query.id,
                cache_time=0,
                results=[
                    InlineQueryResultArticle(
                        title="ɢᴇᴛ ɴᴏᴛᴇs!",
                        reply_markup=buttons,
                        input_message_content=InputTextMessageContent(text),
                    )
                ],
            )
        except:
            continue

@PY.CALLBACK("_gtnote")
async def get_notes_callback(client, callback_query):
    try:
        _, user_id, *query = callback_query.data.split()
        data_key = "notes_cb" if bool(query) else "notes"
        query_eplit = query[0] if bool(query) else user_id.split("_")[1]
        
        user_id_fixed = int(user_id.split("_")[0])
        data = await get_vars(user_id_fixed, query_eplit, data_key)
        
        item = [x for x in ubot._ubot if user_id_fixed == x.me.id]
        for me in item:
            m = await me.get_messages(int(me.me.id), int(data["message_id"]))
            if not m.text:
                continue
            buttons, text = create_inline_keyboard(
                m.text, f"{user_id_fixed}_{user_id.split('_')[1]}", bool(query)
            )
            return await callback_query.edit_message_text(text, reply_markup=buttons)
    except Exception as e:
        return await callback_query.answer(f"❌ ᴇʀʀᴏʀ: {str(e)}", show_alert=True)
        