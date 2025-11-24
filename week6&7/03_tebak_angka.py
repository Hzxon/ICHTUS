# tebak_angka.py
# Jalankan: python tebak_angka.py

import random

NYAWA_AWAL = 5

def main():
    print("=== TEBAK ANGKA 1..50 ===")
    target = random.randint(1, 50)
    nyawa = NYAWA_AWAL
    skor = 0
    percobaan = 0
    while nyawa > 0:
        try:
            tebak = int(input("Tebakanmu (1-50): "))
        except ValueError:
            print("Masukkan angka ya.")
            continue

        percobaan += 1
        if tebak == target:
            bonus = nyawa * 10
            skor += 50 + bonus
            print(f"BENAR! 🎉 Angkanya {target}. Bonus {bonus} poin.")
            break
        elif tebak < target:
            nyawa -= 1
            print("Terlalu kecil. Nyawa:", nyawa)
        else:
            nyawa -= 1
            print("Terlalu besar. Nyawa:", nyawa)

    if nyawa == 0:
        print(f"GAME OVER. Angkanya {target}.")
    print(f"Skor akhir: {skor} (percobaan: {percobaan})")

if __name__ == "__main__":
    main()