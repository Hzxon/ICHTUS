import pygame
import random
import math

# --- SETUP AWAL ---
pygame.init()

# ukuran layar
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pop Balon")

clock = pygame.time.Clock()

# warna
WHITE = (255, 255, 255)
BLUE = (135, 206, 235)   # langit
RED = (220, 50, 50)

font = pygame.font.SysFont(None, 32)
big_font = pygame.font.SysFont(None, 48)

# --- BALON ---
balloon_radius = 25

def reset_balloon():
    x = random.randint(balloon_radius, WIDTH - balloon_radius)
    y = HEIGHT + balloon_radius   # mulai dari bawah layar
    speed = random.randint(2, 5)
    return x, y, speed

balloon_x, balloon_y, balloon_speed = reset_balloon()

# --- SKOR & WAKTU ---
score = 0
total_time = 30  # detik
start_time = pygame.time.get_ticks()
game_over = False

def draw_text(text, x, y, font_obj=font, color=WHITE):
    img = font_obj.render(text, True, color)
    screen.blit(img, (x, y))

# --- LOOP GAME ---
running = True
while running:
    # 1. Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # klik mouse untuk pop balon
        if not game_over and event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            dx = mouse_x - balloon_x
            dy = mouse_y - balloon_y
            distance = math.sqrt(dx * dx + dy * dy)

            if distance <= balloon_radius:
                # balon meletus
                score += 1
                balloon_x, balloon_y, balloon_speed = reset_balloon()

        # restart game jika sudah game over
        if game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                score = 0
                start_time = pygame.time.get_ticks()
                balloon_x, balloon_y, balloon_speed = reset_balloon()
                game_over = False

    # 2. Update logika game
    if not game_over:
        # gerak balon ke atas
        balloon_y -= balloon_speed

        # kalau balon keluar di atas → spawn lagi dari bawah
        if balloon_y + balloon_radius < 0:
            balloon_x, balloon_y, balloon_speed = reset_balloon()

        # hitung sisa waktu
        elapsed_ms = pygame.time.get_ticks() - start_time
        remaining_time = total_time - elapsed_ms // 1000

        if remaining_time <= 0:
            remaining_time = 0
            game_over = True

    else:
        remaining_time = 0

    # 3. Gambar ke layar
    screen.fill(BLUE)  # background langit

    # gambar balon (kalau belum game over)
    if not game_over:
        pygame.draw.circle(screen, RED, (balloon_x, balloon_y), balloon_radius)
        # tali balon
        pygame.draw.line(screen, WHITE, (balloon_x, balloon_y + balloon_radius),
                         (balloon_x, balloon_y + balloon_radius + 30), 2)

    # skor dan waktu
    draw_text(f"Score: {score}", 10, 10)
    draw_text(f"Time: {remaining_time}", 10, 40)

    # jika game over, tampilkan pesan besar
    if game_over:
        draw_text("Waktu Habis!", WIDTH//2 - 110, HEIGHT//2 - 40, big_font)
        draw_text(f"Score akhir: {score}", WIDTH//2 - 120, HEIGHT//2, big_font)
        draw_text("Tekan R untuk bermain lagi", WIDTH//2 - 170, HEIGHT//2 + 40, font)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
