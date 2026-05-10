import os
import aiohttp
from PyroUbot import *

__MODULE__ = "sᴘᴏᴛɪғʏ ᴘʀᴏ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴘᴏᴛɪғʏ ᴘʀᴏ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}sᴘᴏᴛɪꜰʏ</code> [ᴊᴜᴅᴜʟ ʟᴀɢᴜ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴᴄᴀʀɪ ᴅᴀɴ ᴍᴇɴɢᴜɴᴅᴜʜ ʟᴀɢᴜ ᴅᴀʀɪ sᴘᴏᴛɪꜰʏ ᴍᴇɴᴊᴀᴅɪ ꜰᴏʀᴍᴀᴛ ᴍᴘ3.</blockquote>
"""

APIKEY = "@iqbalnew77"

@PY.UBOT("spotify")
@PY.TOP_CMD
async def spotify_dl(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)

    args = get_arg(message)
    if not args:
        return await message.reply_text(
            f"<blockquote><b>{ggl} ʜᴀʀᴀᴘ ᴍᴀsᴜᴋᴋᴀɴ ᴊᴜᴅᴜʟ ʟᴀɢᴜ!\nᴄᴏɴᴛᴏʜ: <code>.sᴘᴏᴛɪꜰʏ</code> ʟᴀᴛʜɪ</b></blockquote>"
        )

    query = args
    status = await message.reply_text(
        f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇɴᴄᴀʀɪ ʟᴀɢᴜ...</b></blockquote>"
    )

    async with aiohttp.ClientSession() as session:
        try:
            # SEARCH PHASE
            search_url = f"https://api.botcahx.eu.org/api/search/spotify?query={query}&apikey={APIKEY}"
            async with session.get(search_url) as r:
                search = await r.json()

            if not search.get("status"):
                return await status.edit(f"<blockquote><b>{ggl} ʟᴀɢᴜ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ.</b></blockquote>")

            result = search.get("result") or search.get("data")
            if isinstance(result, dict):
                data = result.get("data") or result.get("tracks") or []
            else:
                data = result

            if not data:
                return await status.edit(f"<blockquote><b>{ggl} ᴅᴀᴛᴀ ʟᴀɢᴜ ᴋᴏsᴏɴɢ.</b></blockquote>")

            track = data[0]
            track_url = track.get("url")

            if not track_url:
                return await status.edit(f"<blockquote><b>{ggl} ᴛᴀᴜᴛᴀɴ sᴘᴏᴛɪꜰʏ ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ.</b></blockquote>")

            await status.edit(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇɴɢᴜɴᴅᴜʜ ᴀᴜᴅɪᴏ...</b></blockquote>")

            # DOWNLOAD PHASE
            dl_url = f"https://api.botcahx.eu.org/api/download/spotify?url={track_url}&apikey={APIKEY}"
            async with session.get(dl_url) as r:
                dl = await r.json()

            if not dl.get("status"):
                return await status.edit(f"<blockquote><b>{ggl} ɢᴀɢᴀʟ ᴍᴇɴɢᴏɴᴠᴇʀsɪ ʟᴀɢᴜ.</b></blockquote>")

            result_dl = dl.get("result") or dl.get("data") or {}
            res = result_dl.get("data") if isinstance(result_dl, dict) else result_dl

            title = res.get("title") or "ᴜɴᴋɴᴏᴡɴ ᴛɪᴛʟᴇ"
            artist_data = res.get("artist")
            if isinstance(artist_data, dict):
                artist = artist_data.get("name", "ᴜɴᴋɴᴏᴡɴ ᴀʀᴛɪsᴛ")
            else:
                artist = str(artist_data) if artist_data else "ᴜɴᴋɴᴏᴡɴ ᴀʀᴛɪsᴛ"

            duration = res.get("duration") or "-"
            audio_url = res.get("url") or res.get("download")

            if not audio_url:
                return await status.edit(f"<blockquote><b>{ggl} ʟɪɴᴋ ᴜɴᴅᴜʜᴀɴ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ.</b></blockquote>")

            file_name = f"{title} - {artist}.mp3".replace("/", "-").replace("\\", "-")

            async with session.get(audio_url) as audio:
                if audio.status != 200:
                    return await status.edit(f"<blockquote><b>{ggl} sᴇʀᴠᴇʀ ᴍᴇɴᴏʟᴀᴋ ᴘᴇʀᴍɪɴᴛᴀᴀɴ.</b></blockquote>")
                with open(file_name, "wb") as f:
                    f.write(await audio.read())

            # SENDING PHASE
            await client.send_audio(
                message.chat.id,
                audio=file_name,
                caption=(
                    f"<blockquote><b>⦪ sᴘᴏᴛɪꜰʏ ᴅᴏᴡɴʟᴏᴀᴅᴇʀ ⦫</b>\n\n"
                    f"ᚗ ᴊᴜᴅᴜʟ : <code>{title}</code>\n"
                    f"ᚗ ᴀʀᴛɪs : <code>{artist}</code>\n"
                    f"ᚗ ᴅᴜʀᴀsɪ : <code>{duration}</code>\n\n"
                    f"<b>{brhsl} ʙᴇʀʜᴀsɪʟ ᴅɪᴜɴᴅᴜʜ</b></blockquote>"
                ),
                reply_to_message_id=message.id
            )

            await status.delete()
            if os.path.exists(file_name):
                os.remove(file_name)

        except Exception as e:
            await status.edit(f"<blockquote><b>{ggl} ᴇʀʀᴏʀ:</b> <code>{str(e)}</code></blockquote>")
            