# Studi Kasus 1: Analisis Nilai Mahasiswa

data_mahasiswa = [
    {"nama": "Aisyah", "nim": "230101", "tugas": 85, "uts": 80, "uas": 88},
    {"nama": "Budi", "nim": "230102", "tugas": 70, "uts": 65, "uas": 75},
    {"nama": "Cantika", "nim": "230103", "tugas": 90, "uts": 85, "uas": 92},
    {"nama": "Dimas", "nim": "230104", "tugas": 78, "uts": 82, "uas": 80},
    {"nama": "Eka", "nim": "230105", "tugas": 88, "uts": 91, "uas": 90}, 
]

data_nilai = [
    {
        **mhs,
        "nilai_akhir": mhs["tugas"] * 0.30 + mhs["uts"] * 0.30 + mhs["uas"] * 0.40,
    }
    for mhs in data_mahasiswa
]

mahasiswa_berprestasi = [mhs for mhs in data_nilai if mhs["nilai_akhir"] > 80]

ranking = sorted(data_nilai, key=lambda mhs: mhs["nilai_akhir"], reverse=True)

print("=" * 62)
print("             HASIL ANALISIS NILAI MAHASISWA")
print("=" * 62)
print("\nDAFTAR NILAI DAN RANKING")
for peringkat, mhs in enumerate(ranking, start=1):
    print(
        f"{peringkat}. {mhs['nama']} (NIM: {mhs['nim']}) | "
        f"Tugas: {mhs['tugas']} | UTS: {mhs['uts']} | UAS: {mhs['uas']} | "
        f"Nilai Akhir: {mhs['nilai_akhir']:.2f}"
    )

print("\nMAHASISWA BERPRESTASI (NILAI AKHIR > 80)")
for mhs in mahasiswa_berprestasi:
    print(f"- {mhs['nama']} ({mhs['nim']}): {mhs['nilai_akhir']:.2f}")

terbaik = ranking[0]
print("\nMAHASISWA TERBAIK")
print(f"Nama        : {terbaik['nama']}")
print(f"NIM         : {terbaik['nim']}")
print(f"Nilai Tugas : {terbaik['tugas']}")
print(f"Nilai UTS   : {terbaik['uts']}")
print(f"Nilai UAS   : {terbaik['uas']}")
print(f"Nilai Akhir : {terbaik['nilai_akhir']:.2f}")
