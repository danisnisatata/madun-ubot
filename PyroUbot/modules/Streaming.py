import os
from yt_dlp import YoutubeDL
from youtubesearchpython import VideosSearch
from pytgcalls.types import MediaStream
from PyroUbot import *

__MODULE__ = "sᴛʀᴇᴀᴍɪɴɢ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴛʀᴇᴀᴍɪɴɢ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴘʟᴀʏ</code> [ᴊᴜᴅᴜʟ/ʟɪɴᴋ/ʀᴇᴘʟʏ]
ᚗ <code>{0}ᴠᴘʟᴀʏ</code> [ᴊᴜᴅᴜʟ/ʟɪɴᴋ/ʀᴇᴘʟʏ]
ᚗ <code>{0}ᴘᴀᴜsᴇ</code>
ᚗ <code>{0}ʀᴇsᴜᴍᴇ</code>
ᚗ <code>{0}ᴇɴᴅ</code>

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇᴍᴜᴛᴀʀ ᴀᴜᴅɪᴏ ᴀᴛᴀᴜ ᴠɪᴅᴇᴏ ᴅɪ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ɢʀᴜᴘ.</blockquote>
"""

@PY.UBOT("play")
@PY.TOP_CMD
@PY.GROUP
async def play_audio(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)

    if message.reply_to_message and message.reply_to_message.audio:
        status_msg = await message.reply(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇɴɢᴜɴᴅᴜʜ ᴀᴜᴅɪᴏ...</b></blockquote>")
        audio_file = await message.reply_to_message.download(f"downloads/{message.reply_to_message.audio.file_name}")

        if not audio_file.endswith(".opus"):
            await status_msg.edit(f"<blockquote><b>{prs} ᴍᴇɴɢᴏɴᴠᴇʀsɪ ᴋᴇ ᴏᴘᴜs...</b></blockquote>")
            opus_file = audio_file.rsplit(".", 1)[0] + ".opus"
            os.system(f"ffmpeg -i '{audio_file}' -acodec libopus '{opus_file}' -y")
            os.remove(audio_file)
            audio_file = opus_file

        await client.call_py.play(message.chat.id, MediaStream(audio_file))
        return await status_msg.edit(f"<blockquote><b>{brhsl} ᴀᴜᴅɪᴏ ʙᴇʀʜᴀsɪʟ ᴅɪᴘᴜᴛᴀʀ!</b></blockquote>")

    if len(message.command) < 2:
        return await message.reply(f"<blockquote><b>{ggl} ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ᴊᴜᴅᴜʟ ᴀᴛᴀᴜ ʟɪɴᴋ!</b></blockquote>")

    query = " ".join(message.command[1:])
    url = query if "youtube.com" in query or "youtu.be" in query else None

    if not url:
        search = VideosSearch(query, limit=1).result()
        if not search["result"]:
            return await message.reply(f"<blockquote><b>{ggl} ʟᴀɢᴜ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ!</b></blockquote>")
        url = search["result"][0]["link"]

    try:
        mex = await message.reply(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇɴɢᴜɴᴅᴜʜ ᴀᴜᴅɪᴏ...</b></blockquote>")
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": "downloads/%(title)s.%(ext)s",
            "postprocessors": [{"key": "FFmpegExtractAudio", "preferredcodec": "opus", "preferredquality": "192"}],
            "cookiefile": "cookies.txt",
            "noplaylist": True,
            "merge_output_format": "opus",
        }

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_path = f"downloads/{info['title']}.opus"

        await client.call_py.play(message.chat.id, MediaStream(file_path))
        await mex.edit(f"<blockquote><b>{brhsl} sᴇᴅᴀɴɢ ᴍᴇᴍᴜᴛᴀʀ:</b>\n<code>{info['title']}</code></blockquote>")
    except Exception as e:
        await mex.edit(f"<blockquote><b>{ggl} ᴇʀʀᴏʀ:</b> <code>{str(e)}</code></blockquote>")

@PY.UBOT("vplay")
@PY.TOP_CMD
@PY.GROUP
async def play_video(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)

    if message.reply_to_message and message.reply_to_message.video:
        status_msg = await message.reply(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇɴɢᴜɴᴅᴜʜ ᴠɪᴅᴇᴏ...</b></blockquote>")
        video_file = await message.reply_to_message.download(f"downloads/{message.reply_to_message.video.file_name}")

        await client.call_py.play(message.chat.id, MediaStream(video_file))
        return await status_msg.edit(f"<blockquote><b>{brhsl} ᴠɪᴅᴇᴏ ʙᴇʀʜᴀsɪʟ ᴅɪᴘᴜᴛᴀʀ!</b></blockquote>")

    if len(message.command) < 2:
        return await message.reply(f"<blockquote><b>{ggl} ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ᴊᴜᴅᴜʟ ᴀᴛᴀᴜ ʟɪɴᴋ!</b></blockquote>")

    query = " ".join(message.command[1:])
    url = query if "youtube.com" in query or "youtu.be" in query else None

    if not url:
        search = VideosSearch(query, limit=1).result()
        if not search["result"]:
            return await message.reply(f"<blockquote><b>{ggl} ᴠɪᴅᴇᴏ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ!</b></blockquote>")
        url = search["result"][0]["link"]

    try:
        mex = await message.reply(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇɴɢᴜɴᴅᴜʜ ᴠɪᴅᴇᴏ...</b></blockquote>")
        ydl_opts = {
            "format": "bv*+ba/b",
            "outtmpl": "downloads/%(title)s.%(ext)s",
            "cookiefile": "cookies.txt",
            "noplaylist": True,
            "merge_output_format": "mp4",
        }

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_path = f"downloads/{info['title']}.mp4"

        await client.call_py.play(message.chat.id, MediaStream(file_path))
        await mex.edit(f"<blockquote><b>{brhsl} sᴇᴅᴀɴɢ ᴍᴇᴍᴜᴛᴀʀ ᴠɪᴅᴇᴏ:</b>\n<code>{info['title']}</code></blockquote>")
    except Exception as e:
        await mex.edit(f"<blockquote><b>{ggl} ᴇʀʀᴏʀ:</b> <code>{str(e)}</code></blockquote>")

@PY.UBOT("pause")
@PY.TOP_CMD
@PY.GROUP
async def pause_audio(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    try:
        await client.call_py.pause_stream(message.chat.id)
        await message.reply(f"<blockquote><b>{brhsl} sᴛʀᴇᴀᴍ ʙᴇʀʜᴀsɪʟ ᴅɪᴊᴇᴅᴀ!</b></blockquote>")
    except Exception as e:
        await message.reply(f"<blockquote><b>{ggl} ᴇʀʀᴏʀ:</b> <code>{str(e)}</code></blockquote>")

@PY.UBOT("resume")
@PY.TOP_CMD
@PY.GROUP
async def resume_audio(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    try:
        await client.call_py.resume_stream(message.chat.id)
        await message.reply(f"<blockquote><b>{brhsl} sᴛʀᴇᴀᴍ ʙᴇʀʜᴀsɪʟ ᴅɪʟᴀɴᴊᴜᴛᴋᴀɴ!</b></blockquote>")
    except Exception as e:
        await message.reply(f"<blockquote><b>{ggl} ᴇʀʀᴏʀ:</b> <code>{str(e)}</code></blockquote>")

@PY.UBOT("end")
@PY.TOP_CMD
@PY.GROUP
async def stop_audio(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    try:
        await client.call_py.leave_call(message.chat.id)
        await message.reply(f"<blockquote><b>{brhsl} sᴛʀᴇᴀᴍ ᴅɪʜᴇɴᴛɪᴋᴀɴ!</b></blockquote>")
    except Exception as e:
        await message.reply(f"<blockquote><b>{ggl} ᴇʀʀᴏʀ:</b> <code>{str(e)}</code></blockquote>")
        