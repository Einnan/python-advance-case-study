# Studi Kasus 2: Streaming Data Sensor IoT Hemat Memori

def baca_sensor():
    """Menghasilkan suhu satu per satu, bukan menyimpan semuanya dalam list."""
    for nomor in range(10):
        yield round(18.5 + nomor * 2.1, 1)


def kategori_suhu(suhu):
    if suhu < 20:
        return "Dingin"
    elif suhu <= 30:
        return "Normal"
    return "Panas"


print("=" * 48)
print("       MONITORING SUHU SENSOR IoT")
print("=" * 48)

iterator_sensor = iter(baca_sensor())
for nomor in range(1, 11):
    suhu = next(iterator_sensor)
    status = kategori_suhu(suhu)
    print(f"Pembacaan ke-{nomor:02d} | Suhu: {suhu:4.1f}°C | Status: {status}")

print("\nSelesai: 10 data diproses bertahap menggunakan generator.")
