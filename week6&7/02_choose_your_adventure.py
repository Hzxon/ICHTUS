# adventure.py
# Jalankan: python adventure.py

print("=== PETUALANGAN DI HUTAN ===")
print("Kamu melihat dua jalan: kiri atau kanan.")

pilih1 = input("Pilih (kiri/kanan): ").strip().lower()

if pilih1 == "kiri":
    print("Kamu bertemu sungai deras.")
    pilih2 = input("Mau (seberang/tunggu)?: ").strip().lower()
    if pilih2 == "seberang":
        print("Kamu hampir hanyut, tapi menemukan perahu. SELAMAT! 🛶")
    else:
        print("Kamu menunggu, datang jembatan. Kamu pulang dengan aman. 😊")
elif pilih1 == "kanan":
    print("Kamu melihat gua gelap.")
    pilih2 = input("Mau (masuk/pulang)?: ").strip().lower()
    if pilih2 == "masuk":
        print("Di dalam ada harta karun kecil. YEAY! 💎")
    else:
        print("Kamu memilih aman. Tidak apa-apa, keselamatan nomor 1! ✅")
else:
    print("Kamu ragu-ragu, hari keburu malam. Petualangan ditunda.")