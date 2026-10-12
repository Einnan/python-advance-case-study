# Studi Kasus 3 — Sistem Keamanan Akun & Audit Log Login

## Masalah
Memvalidasi format kredensial dan mencatat setiap percobaan login, baik berhasil maupun ditolak.

## Konsep Python
- **RegEx (`re`)**: username minimal lima karakter alfanumerik; password minimal delapan karakter dan memiliki angka.
- **Class `User` dan `@property`**: setter memvalidasi nilai sebelum menyimpannya.
- **Decorator dan closure**: `audit_log` membungkus fungsi `login`, menangkap hasil dan alasan penolakan, serta mencatat timestamp.

## Cara Menjalankan
```bash
python main.py
```

Akun simulasi yang berhasil: username `Mahasiswa01`, password `Belajar123`. Kredensial ini hanya untuk demonstrasi lokal, bukan untuk akun nyata.

Screenshot hasil terminal disimpan sebagai `output.png`.
