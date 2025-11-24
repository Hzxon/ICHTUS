# move_box.py
# Jalankan: python move_box.py

import pygame
pygame.init()

LEBAR, TINGGI = 800, 600
layar = pygame.display.set_mode((LEBAR, TINGGI))
pygame.display.set_caption("Gerak Kotak")
clock = pygame.time.Clock()

# pemain = kotak 50x50
pemain = pygame.Rect(LEBAR//2 - 25, TINGGI//2 - 25, 50, 50)
kecepatan = 2

jalan = True
while jalan:
    # 1) event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jalan = False

    # 2) input keyboard (tahan tombol)
    tombol = pygame.key.get_pressed()
    if tombol[pygame.K_LEFT]:  pemain.x -= kecepatan
    if tombol[pygame.K_RIGHT]: pemain.x += kecepatan
    if tombol[pygame.K_UP]:    pemain.y -= kecepatan
    if tombol[pygame.K_DOWN]:  pemain.y += kecepatan

    # 3) batas layar
    pemain.x = max(0, min(pemain.x, LEBAR - pemain.width))
    pemain.y = max(0, min(pemain.y, TINGGI - pemain.height))

    # 4) gambar
    layar.fill((30, 30, 30))                        # background
    pygame.draw.rect(layar, (200, 200, 0), pemain)  # kotak pemain
    pygame.display.flip()
 # 5) fps
clock.tick(120)

pygame.quit()