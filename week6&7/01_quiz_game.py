# quiz_game.py
# Jalankan: python quiz_game.py

pertanyaan = [
    {
        "soal": "1) Ibu kota Indonesia?",
        "opsi": {"a": "Bandung", "b": "Jakarta", "c": "Surabaya"},
        "jawab": "b"
    },
    {
        "soal": "2) 7 + 5 = ?",
        "opsi": {"a": "10", "b": "11", "c": "12"},
        "jawab": "c"
    },
    {
        "soal": "3) Warna bendera Indonesia?",
        "opsi": {"a": "Merah-Putih", "b": "Biru-Kuning", "c": "Hijau-Hitam"},
        "jawab": "a"
    }
]

print("=== QUIZ SEDERHANA ===")
skor = 0

for q in pertanyaan:
    print("\n" + q["soal"])
    for key, val in q["opsi"].items():
        print(f"   {key}) {val}")
    ans = input("Jawabanmu (a/b/c): ").strip().lower()
    if ans == q["jawab"]:
        print("Benar! +10 poin")
        skor += 10
    else:
        print("Kurang tepat.")

print(f"\nSelesai! Skor kamu: {skor} / {len(pertanyaan)*10}")