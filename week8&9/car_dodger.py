import pygame
import random

# Inisialisasi pygame
pygame.init()

# Ukuran layar
LEBAR = 500
TINGGI = 600

# Warna (R, G, B)
PUTIH = (255, 255, 255)
HITAM = (0, 0, 0)
MERAH = (200, 50, 50)
BIRU = (50, 100, 200)
ABU = (160, 160, 160)

# Membuat layar
layar = pygame.display.set_mode((LEBAR, TINGGI))
pygame.display.set_caption("Hindari Mobil")

# Clock untuk atur FPS
clock = pygame.time.Clock()
FPS = 60

# Data pemain (mobil kita)
lebar_mobil = 40
tinggi_mobil = 70
pemain_x = LEBAR // 2 - lebar_mobil // 2
pemain_y = TINGGI - tinggi_mobil - 20
kecepatan_pemain = 5

# List mobil musuh
musuh_list = []
jarak_muncul = 40  # semakin kecil semakin sering muncul
timer_muncul = 0

# Skor (lama bertahan)
skor = 0
font = pygame.font.SysFont(None, 28)

# Status game
game_over = False

def buat_musuh():
    """Buat 1 mobil musuh di posisi acak di atas."""
    x = random.randint(40, LEBAR - 40 - lebar_mobil)
    y = -tinggi_mobil
    kecepatan = random.randint(3, 7)
    rect_musuh = pygame.Rect(x, y, lebar_mobil, tinggi_mobil)
    return {"rect": rect_musuh, "speed": kecepatan}

def reset_game():
    """Kembalikan nilai awal saat game over dan tekan R."""
    global musuh_list, skor, pemain_x, pemain_y, game_over
    musuh_list = []
    skor = 0
    pemain_x = LEBAR // 2 - lebar_mobil // 2
    pemain_y = TINGGI - tinggi_mobil - 20
    game_over = False

# Loop utama game
running = True
while running:
    clock.tick(FPS)

    # 1. Tangkap event (tutup jendela dsb.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Tekan tombol saat game over
    keys = pygame.key.get_pressed()
    if game_over:
        if keys[pygame.K_r]:
            reset_game()

    if not game_over:
        # 2. Gerakkan pemain
        if keys[pygame.K_LEFT]:
            pemain_x -= kecepatan_pemain
        if keys[pygame.K_RIGHT]:
            pemain_x += kecepatan_pemain

        # Batasi mobil agar tidak keluar layar
        if pemain_x < 20:
            pemain_x = 20
        if pemain_x > LEBAR - lebar_mobil - 20:
            pemain_x = LEBAR - lebar_mobil - 20

        # 3. Tambahkan musuh baru
        timer_muncul += 1
        if timer_muncul >= jarak_muncul:
            musuh_list.append(buat_musuh())
            timer_muncul = 0

        # 4. Gerakkan musuh dan cek tabrakan
        pemain_rect = pygame.Rect(pemain_x, pemain_y, lebar_mobil, tinggi_mobil)
        for musuh in musuh_list:
            musuh["rect"].y += musuh["speed"]

            # Cek tabrakan
            if pemain_rect.colliderect(musuh["rect"]):
                game_over = True

        # Hapus musuh yang sudah lewat bawah
        musuh_list = [m for m in musuh_list if m["rect"].y < TINGGI + 100]

        # 5. Tambah skor
        skor += 1

    # 6. Gambar semua ke layar
    layar.fill(ABU)

    # Gambar jalan
    pygame.draw.rect(layar, (100, 100, 100), (20, 0, LEBAR - 40, TINGGI))
    # Garis putih tengah
    for y in range(0, TINGGI, 40):
        pygame.draw.rect(layar, PUTIH, (LEBAR // 2 - 5, y, 10, 20))

    # Gambar mobil pemain
    pygame.draw.rect(layar, BIRU, (pemain_x, pemain_y, lebar_mobil, tinggi_mobil))

    # Gambar musuh
    for musuh in musuh_list:
        pygame.draw.rect(layar, MERAH, musuh["rect"])

    # Tulis skor
    teks_skor = font.render(f"Skor: {skor}", True, HITAM)
    layar.blit(teks_skor, (10, 10))

    if game_over:
        teks_go = font.render("TABRAKAN! Tekan R untuk main lagi", True, HITAM)
        layar.blit(teks_go, (60, TINGGI // 2))

    # 7. Update layar
    pygame.display.flip()

# Keluar pygame
pygame.quit()
