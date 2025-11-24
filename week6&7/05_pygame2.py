# catch_the_object.py
# Jalankan: python catch_the_object.py

import pygame, random
pygame.init()

LEBAR, TINGGI = 480, 640
layar = pygame.display.set_mode((LEBAR, TINGGI))
pygame.display.set_caption("Catch the Object")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 28)

# pemain: “keranjang” di bawah
pemain = pygame.Rect(LEBAR//2 - 40, TINGGI - 60, 80, 20)
speed_player = 7

# objek jatuh (apel)
objek_list = []  # list of dicts: {"rect": Rect, "speed": int}
drop_speed_min, drop_speed_max = 3, 7
spawn_timer, spawn_delay = 0, 35  # frame

skor = 0
nyawa = 3

jalan = True
game_over = False

def reset_game():
    global objek_list, skor, nyawa, game_over, spawn_timer
    objek_list.clear()
    skor = 0
    nyawa = 3
    game_over = False
    spawn_timer = 0
    pemain.centerx = LEBAR//2

def gambar_ui():
    teks = font.render(f"Skor: {skor}   Nyawa: {nyawa}", True, (255, 255, 255))
    layar.blit(teks, (10, 10))

reset_game()

while jalan:
    # === Event handling ===
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jalan = False
        if game_over and event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            reset_game()

    # === Input gerak pemain (kiri/kanan) ===
    if not game_over:
        tombol = pygame.key.get_pressed()
        if tombol[pygame.K_LEFT]:  pemain.x -= speed_player
        if tombol[pygame.K_RIGHT]: pemain.x += speed_player
        pemain.x = max(0, min(pemain.x, LEBAR - pemain.width))
        
    #maya_pert

    # === Spawn objek jatuh ===
    if not game_over:
        spawn_timer += 1
        if spawn_timer >= spawn_delay:
            spawn_timer = 0
            ukuran = random.randint(20, 30)
            x = random.randint(0, LEBAR - ukuran)
            rect = pygame.Rect(x, -ukuran, ukuran, ukuran)
            objek_list.append({
                "rect": rect,
                "speed": random.randint(drop_speed_min, drop_speed_max),
            })

    # === Update objek jatuh ===
    if not game_over:
        baru = []
        for o in objek_list:
            rect = o["rect"]
            rect.y += o["speed"]
            # Cek tabrakan
            if rect.colliderect(pemain):
                skor += 1
            elif rect.top > TINGGI:
                nyawa -= 1
                if nyawa <= 0:
                    game_over = True
                else:
                    pass  # objek hilang karena terlewat
            else:
                baru.append(o)  # tetap ada di layar
        objek_list = baru

    # === Gambar ===
    layar.fill((25, 35, 60))
    # pemain (keranjang)
    pygame.draw.rect(layar, (240, 200, 50), pemain, border_radius=6)
    # objek jatuh (apel kotak)
    for o in objek_list:
        pygame.draw.rect(layar, (200, 50, 50), o["rect"], border_radius=6)

    gambar_ui()

    if game_over:
        t1 = font.render("GAME OVER — tekan R untuk main lagi", True, (255, 255, 255))
        layar.blit(t1, (LEBAR//2 - t1.get_width()//2, TINGGI//2 - 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()