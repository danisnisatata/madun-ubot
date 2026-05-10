import asyncio
import os
import random
from io import BytesIO

import cv2
from PIL import Image
from pyrogram import *
from pyrogram.enums import ParseMode
from pyrogram.errors import StickersetInvalid, YouBlockedUser
from pyrogram.raw.functions.messages import DeleteHistory, GetStickerSet
from pyrogram.raw.types import InputStickerSetShortName
from pyrogram.types import *
from PyroUbot import *

nomber_stiker = "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 28 27 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67".split()

__MODULE__ = "ꜱᴛɪᴄᴋᴇʀ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴛɪᴄᴋᴇʀ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ǫ</code> : ᴜʙᴀʜ ᴛᴇᴋs ᴊᴀᴅɪ sᴛɪᴄᴋᴇʀ ǫᴜᴏᴛᴇ.
ᚗ <code>{0}ᴋᴀɴɢ</code> : ᴛᴀᴍʙᴀʜ sᴛɪᴄᴋᴇʀ ᴋᴇ sᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋ ʟᴜ.
ᚗ <code>{0}ᴛɪɴʏ</code> : ᴜʙᴀʜ sᴛɪᴄᴋᴇʀ ᴍᴇɴᴊᴀᴅɪ ᴋᴇᴄɪʟ.
ᚗ <code>{0}ᴍᴍꜰ</code> : ᴜʙᴀʜ ꜰᴏᴛᴏ/sᴛɪᴄᴋᴇʀ ᴊᴀᴅɪ sᴛɪᴄᴋᴇʀ ᴍᴇᴍᴇ.

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴏᴅᴜʟ ᴋʀᴇᴀᴛɪꜰ ᴜɴᴛᴜᴋ ᴍᴇɴɢᴇʟᴏʟᴀ ᴅᴀɴ ᴍᴇᴍʙᴜᴀᴛ sᴛɪᴄᴋᴇʀ sᴇᴄᴀʀᴀ ɪɴsᴛᴀɴ.</blockquote>
"""

@PY.UBOT("mmf")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    if not message.reply_to_message:
        return await message.reply(f"<blockquote><b>{ggl} ʙᴀʟᴀs ᴋᴇ ᴘᴇsᴀɴ ꜰᴏᴛᴏ ᴀᴛᴀᴜ sᴛɪᴄᴋᴇʀ!</b></blockquote>")
    reply_message = message.reply_to_message
    if not reply_message.media:
        return await message.reply(f"<blockquote><b>{ggl} ʙᴀʟᴀs ᴋᴇ ᴘᴇsᴀɴ ꜰᴏᴛᴏ ᴀᴛᴀᴜ sᴛɪᴄᴋᴇʀ.</b></blockquote>")
    file = await client.download_media(reply_message)
    Tm = await message.reply(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs...</b></blockquote>")
    text = get_arg(message)
    if len(text) < 1:
        return await Tm.edit(f"<blockquote><b>{ggl} ʜᴀʀᴀᴘ ᴋᴇᴛɪᴋ: mmf - [ᴛᴇᴋs]</b></blockquote>")
    meme = await add_text_img(file, text)
    await asyncio.gather(
        Tm.delete(),
        client.send_sticker(
            message.chat.id,
            sticker=meme,
            reply_to_message_id=message.id,
        ),
    )
    os.remove(meme)
    os.remove(file)

@PY.UBOT("q")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    info = await message.reply(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs...</b></blockquote>", quote=True)
    await client.unblock_user("@QuotLyBot")
    if message.reply_to_message:
        if len(message.command) < 2:
            msg = [message.reply_to_message]
        else:
            try:
                count = int(message.command[1])
            except Exception as error:
                await info.edit(f"<blockquote><b>{ggl} ᴇʀʀᴏʀ:</b> <code>{error}</code></blockquote>")
            msg = [
                i
                for i in await client.get_messages(
                    chat_id=message.chat.id,
                    message_ids=range(
                        message.reply_to_message.id, message.reply_to_message.id + count
                    ),
                    replies=-1,
                )
            ]
        try:
            for x in msg:
                await x.forward("@QuotLyBot")
        except Exception:
            pass
        await asyncio.sleep(9)
        await info.delete()
        async for quotly in client.get_chat_history("@QuotLyBot", limit=1):
            if not quotly.sticker:
                await message.reply(
                    f"<blockquote><b>{ggl} @QuotLyBot ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇʀᴇsᴘᴏɴ.</b></blockquote>", quote=True
                )
            else:
                sticker = await client.download_media(quotly)
                await message.reply_sticker(sticker, quote=True)
                os.remove(sticker)
    else:
        if len(message.command) < 2:
            return await info.edit(f"<blockquote><b>{ggl} ʀᴇᴘʟʏ ᴋᴇ ᴛᴇᴋs/ᴍᴇᴅɪᴀ.</b></blockquote>")
        else:
            msg = await client.send_message(
                "@QuotLyBot", f"/qcolor {message.command[1]}"
            )
            await asyncio.sleep(1)
            get = await client.get_messages("@QuotLyBot", msg.id + 1)
            await info.edit(
                f"<blockquote><b>{brhsl} ᴡᴀʀɴᴀ ǫᴜᴏᴛᴇ ᴅɪsᴇᴛᴇʟ ᴋᴇ:</b> <code>{get.text.split(':')[1]}</code></blockquote>"
            )
    user_info = await client.resolve_peer("@QuotLyBot")
    return await client.invoke(DeleteHistory(peer=user_info, max_id=0, revoke=True))

@PY.UBOT("tiny")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    reply = message.reply_to_message
    if not (reply and (reply.media)):
        return await message.reply(f"<blockquote><b>{ggl} sɪʟᴀᴋᴀɴ ʙᴀʟᴀs ᴋᴇ sᴛɪᴄᴋᴇʀ!</b></blockquote>")
    Tm = await message.reply(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ᴛɪɴʏ...</b></blockquote>")
    ik = await client.download_media(reply)
    im1 = Image.open("storage/TM_BLACK.png")
    if ik.endswith(".tgs"):
        await client.download_media(reply, "Tm.tgs")
        await bash("lottie_convert.py man.tgs json.json")
        with open("json.json", "r") as f:
            jsn = f.read()
        jsn = jsn.replace("512", "2000")
        with open("json.json", "w") as f:
            f.write(jsn)
        await bash("lottie_convert.py json.json Tm.tgs")
        file = "man.tgs"
        os.remove("json.json")
    elif ik.endswith((".gif", ".mp4")):
        iik = cv2.VideoCapture(ik)
        busy, frame = iik.read()
        cv2.imwrite("i.png", frame)
        fil = "i.png"
        im = Image.open(fil)
        z, d = im.size
        if z == d:
            xxx, yyy = 200, 200
        else:
            t = z + d
            a = z / t
            b = d / t
            aa = (a * 100) - 50
            bb = (b * 100) - 50
            xxx = 200 + 5 * aa
            yyy = 200 + 5 * bb
        k = im.resize((int(xxx), int(yyy)))
        k.save("k.png", format="PNG", optimize=True)
        im2 = Image.open("k.png")
        back_im = im1.copy()
        back_im.paste(im2, (150, 0))
        back_im.save("o.webp", "WEBP", quality=95)
        file = "o.webp"
        os.remove(fil)
        os.remove("k.png")
    else:
        im = Image.open(ik)
        z, d = im.size
        if z == d:
            xxx, yyy = 200, 200
        else:
            t = z + d
            a = z / t
            b = d / t
            aa = (a * 100) - 50
            bb = (b * 100) - 50
            xxx = 200 + 5 * aa
            yyy = 200 + 5 * bb
        k = im.resize((int(xxx), int(yyy)))
        k.save("k.png", format="PNG", optimize=True)
        im2 = Image.open("k.png")
        back_im = im1.copy()
        back_im.paste(im2, (150, 0))
        back_im.save("o.webp", "WEBP", quality=95)
        file = "o.webp"
        os.remove("k.png")
    await asyncio.gather(
        Tm.delete(),
        client.send_sticker(
            message.chat.id,
            sticker=file,
            reply_to_message_id=message.id,
        ),
    )
    if os.path.exists(file): os.remove(file)
    if os.path.exists(ik): os.remove(ik)

@PY.UBOT("kang")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    await client.unblock_user("stickers")
    user = message.from_user
    replied = message.reply_to_message
    Tm = await message.reply(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs sᴛɪᴄᴋᴇʀ...</b></blockquote>")
    media_ = None
    emoji_ = None
    is_anim = False
    is_video = False
    resize = False
    ff_vid = False
    if replied and replied.media:
        if replied.photo: resize = True
        elif replied.document and "image" in replied.document.mime_type: resize = True
        elif replied.document and "tgsticker" in replied.document.mime_type: is_anim = True
        elif replied.document and "video" in replied.document.mime_type:
            resize = True
            is_video = True
            ff_vid = True
        elif replied.animation or replied.video:
            resize = True
            is_video = True
            ff_vid = True
        elif replied.sticker:
            if not replied.sticker.file_name:
                return await Tm.edit(f"<blockquote><b>{ggl} sᴛɪᴄᴋᴇʀ ᴛɪᴅᴀᴋ ᴍᴇᴍɪʟɪᴋɪ ɴᴀᴍᴀ!</b></blockquote>")
            emoji_ = replied.sticker.emoji
            is_anim = replied.sticker.is_animated
            is_video = replied.sticker.is_video
            if not (replied.sticker.file_name.endswith(".tgs") or replied.sticker.file_name.endswith(".webm")):
                resize = True
                ff_vid = True
        else:
            return await Tm.edit(f"<blockquote><b>{ggl} ꜰɪʟᴇ ᴛɪᴅᴀᴋ ᴅɪᴅᴜᴋᴜɴɢ.</b></blockquote>")
        media_ = await client.download_media(replied, file_name="PyroUbot/plugins/")
    else:
        return await Tm.edit(f"<blockquote><b>{ggl} sɪʟᴀᴋᴀɴ ʀᴇᴘʟʏ ᴋᴇ ᴍᴇᴅɪᴀ ꜰᴏᴛᴏ/ɢɪꜰ/sᴛɪᴄᴋᴇʀ!</b></blockquote>")

    if media_:
        args = get_arg(message)
        pack = 1
        if len(args) == 2: emoji_, pack = args
        elif len(args) == 1:
            if args[0].isnumeric(): pack = int(args[0])
            else: emoji_ = args[0]
        
        if not emoji_: emoji_ = "✨"
        u_name = user.username or user.first_name or user.id
        packname = f"Sticker_u{user.id}_v{pack}"
        packnick = f"{u_name} ᴘᴀᴄᴋ Vol.{pack}"
        cmd = "/newpack"
        if resize: media_ = await resize_media(media_, is_video, ff_vid)
        if is_anim:
            packname += "_animated"; packnick += " (Animated)"; cmd = "/newanimated"
        if is_video:
            packname += "_video"; packnick += " (Video)"; cmd = "/newvideo"

        exist = False
        while True:
            try:
                exist = await client.invoke(GetStickerSet(stickerset=InputStickerSetShortName(short_name=packname), hash=0))
            except StickersetInvalid:
                exist = False; break
            limit = 50 if (is_video or is_anim) else 120
            if exist.set.count >= limit:
                pack += 1
                packname = f"a{user.id}_by_userge_{pack}"
                packnick = f"{u_name} ᴘᴀᴄᴋ Vol.{pack}"
                if is_anim: packname += "_anim"; packnick += " (Animated)"
                if is_video: packname += "_video"; packnick += " (Video)"
                await Tm.edit(f"<blockquote><b>{brhsl} ᴍᴇᴍʙᴜᴀᴛ sᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋ ɴᴏᴍᴏʀ {pack}...</b></blockquote>")
                continue
            break

        if exist is not False:
            await client.send_message("stickers", "/addsticker")
            await asyncio.sleep(2)
            await client.send_message("stickers", packname)
            await asyncio.sleep(2)
            await client.send_document("stickers", media_)
            await asyncio.sleep(2)
            await client.send_message("stickers", emoji_)
            await asyncio.sleep(2)
            await client.send_message("stickers", "/done")
        else:
            await Tm.edit(f"<blockquote><b>{prs} ᴍᴇᴍʙᴜᴀᴛ sᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋ ʙᴀʀᴜ...</b></blockquote>")
            await client.send_message("stickers", cmd)
            await asyncio.sleep(2)
            await client.send_message("stickers", packnick)
            await asyncio.sleep(2)
            await client.send_document("stickers", media_)
            await asyncio.sleep(2)
            await client.send_message("stickers", emoji_)
            await asyncio.sleep(2)
            await client.send_message("stickers", "/publish")
            await asyncio.sleep(2)
            if is_anim: await client.send_message("stickers", f"<{packnick}>")
            await client.send_message("stickers", "/skip")
            await asyncio.sleep(2)
            await client.send_message("stickers", packname)
            await asyncio.sleep(2)

        await Tm.edit(f"<blockquote><b>{brhsl} sᴛɪᴄᴋᴇʀ ʙᴇʀʜᴀsɪʟ ᴅɪᴛᴀᴍʙᴀʜᴋᴀɴ!</b>\nᚗ <a href='https://t.me/addstickers/{packname}'>ᴋʟɪᴋ ᴅɪ sɪɴɪ</a> ᴜɴᴛᴜᴋ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ sᴛɪᴄᴋᴇʀ.</blockquote>")
        if os.path.exists(str(media_)): os.remove(media_)
        await client.delete_messages("stickers", client.me.id)

async def get_response(message, client):
    return [x async for x in client.get_chat_history("stickers", limit=1)][0].text
    
    