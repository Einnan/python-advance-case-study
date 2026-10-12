# Studi Kasus 2 — Streaming Data Sensor IoT Hemat Memori

## Masalah
Membaca bacaan suhu sensor secara bertahap agar seluruh data tidak perlu ditampung sekaligus dalam list besar.

## Konsep Python
- **Generator function** memakai `yield` untuk mengeluarkan satu nilai setiap kali diminta.
- **Iterator pattern** memakai `iter()` dan `next()` untuk mengambil bacaan secara bertahap.
- **Efisiensi memori**: pemrosesan dilakukan per nilai; tidak membuat list hasil bacaan tambahan.

## Kategori Suhu
- Dingin: di bawah 20°C.
- Normal: 20°C sampai dengan 30°C.
- Panas: di atas 30°C.

## Cara Menjalankan
```bash
python main.py
```

Screenshot hasil terminal disimpan sebagai `output.png`.
