<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
        @keyframes slideIn {
            from { transform: translateX(-50px); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }
        .madun {
            font-size: 48px;
            font-weight: bold;
            background: linear-gradient(45deg, #ff0000, #00ff00, #0000ff);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            animation: pulse 1s infinite;
        }
        .fade { animation: fadeIn 1s ease-in; }
        .slide { animation: slideIn 0.8s ease-out; }
        .box {
            border: 2px solid #00ff00;
            padding: 20px;
            margin: 20px 0;
            border-radius: 10px;
            animation: fadeIn 1.5s;
        }
    </style>
</head>
<body>

<div class="fade">
    <h1 class="madun">⚡ MADUN UBOT ⚡</h1>
    <p><i>Bot Pembuat Userbot Telegram | GRATIS & PERMANEN</i></p>
</div>

<div class="slide box">
    <h2>📌 FITUR UNGGULAN</h2>
    <ul>
        <li>✅ Buat Userbot <b>GRATIS</b></li>
        <li>✅ <b>PERMANEN</b> - Tidak Ada Expired</li>
        <li>✅ Wajib Join Channel @newmadun</li>
        <li>✅ Notifikasi Owner & Channel</li>
        <li>✅ Multi Userbot Support</li>
        <li>✅ OTP Wajib Pakai Spasi</li>
        <li>✅ Auto Restart Userbot</li>
    </ul>
</div>

<div class="slide box">
    <h2>📝 CARA PENGGUNAAN</h2>
    <ol>
        <li>Start bot: <code>/start</code></li>
        <li>Klik tombol <b>BUAT USERBOT GRATIS</b></li>
        <li>Masukkan nomor Telegram (contoh: +628123456789)</li>
        <li>Masukkan OTP <b>WAJIB PAKAI SPASI</b> (contoh: 1 2 3 4 5)</li>
        <li>Masukkan password 2FA (jika ada)</li>
        <li>Userbot siap digunakan!</li>
    </ol>
</div>

<div class="slide box">
    <h2>🔧 PERINTAH OWNER</h2>
    <table border="1" cellpadding="10">
        <tr><th>Perintah</th><th>Fungsi</th></tr>
        <tr><td><code>cb_restart</code></td><td>Restart bot utama</td></tr>
        <tr><td><code>cb_gitpull</code></td><td>Update dari GitHub</td></tr>
        <tr><td><code>cek_ubot</code></td><td>Lihat semua userbot</td></tr>
        <tr><td><code>del_ubot</code></td><td>Hapus userbot</td></tr>
    </table>
</div>

<div class="slide box">
    <h2>📦 DEPLOY SENDIRI</h2>
    <pre><code>
git clone https://github.com/danisnisatata/madun-ubot.git
cd madun-ubot/PyroUbot
pip3 install -r requirements.txt
pip3 install uvloop==0.17.0 pymongo dnspython pytz
python3 -m PyroUbot
    </code></pre>
</div>

<div class="slide box">
    <h2>👤 KONTAK</h2>
    <ul>
        <li>Owner: <b>@kingmadun</b></li>
        <li>Channel: <b>@newmadun</b></li>
        <li>Bot Utama: <b>@ubotfreemadunbot</b></li>
    </ul>
</div>

<div class="fade">
    <p align="center"><b>MADUN UBOT | GRATIS SELAMANYA</b></p>
</div>

</body>
</html>
