import pygame
import random
import math

pygame.init()

WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.setCaption = pygame.display.set_caption("Pop Balon - Balon Emas")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLUE = (135, 206, 235)
RED = (220, 50, 50)
YELLOW = (255, 215, 0)

font = pygame.font.SysFont(None, 32)
big_font = pygame.font.SysFont(None, 48)

balloon_radius = 25

def reset_balloon():
    x = random.randint(balloon_radius, WIDTH - balloon_radius)
    y = HEIGHT + balloon_radius
    speed = random.randint(2, 5)
    # 1 dari 5 balon jadi balon emas
    is_special = (random.randint(1, 5) == 1)
    return x, y, speed, is_special

balloon_x, balloon_y, balloon_speed, is_special = reset_balloon()

score = 0
total_time = 30
start_time = pygame.time.get_ticks()
game_over = False

def draw_text(text, x, y, font_obj=font, color=WHITE):
    img = font_obj.render(text, True, color)
    screen.blit(img, (x, y))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if (not game_over) and event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            dx = mouse_x - balloon_x
            dy = mouse_y - balloon_y
            distance = math.sqrt(dx * dx + dy * dy)

            if distance <= balloon_radius:
                if is_special:
                    score += 3
                else:
                    score += 1
                balloon_x, balloon_y, balloon_speed, is_special = reset_balloon()

        if game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                score = 0
                start_time = pygame.time.get_ticks()
                balloon_x, balloon_y, balloon_speed, is_special = reset_balloon()
                game_over = False

    if not game_over:
        balloon_y -= balloon_speed

        if balloon_y + balloon_radius < 0:
            balloon_x, balloon_y, balloon_speed, is_special = reset_balloon()

        elapsed_ms = pygame.time.get_ticks() - start_time
        remaining_time = total_time - elapsed_ms // 1000

        if remaining_time <= 0:
            remaining_time = 0
            game_over = True
    else:
        remaining_time = 0

    screen.fill(BLUE)

    if not game_over:
        color = YELLOW if is_special else RED
        pygame.draw.circle(screen, color, (balloon_x, balloon_y), balloon_radius)
        pygame.draw.line(screen, WHITE,
                         (balloon_x, balloon_y + balloon_radius),
                         (balloon_x, balloon_y + balloon_radius + 30), 2)

    draw_text(f"Score: {score}", 10, 10)
    draw_text(f"Time: {remaining_time}", 10, 40)

    if game_over:
        draw_text("Waktu Habis!", WIDTH//2 - 110, HEIGHT//2 - 40, big_font)
        draw_text(f"Score akhir: {score}", WIDTH//2 - 120, HEIGHT//2, big_font)
        draw_text("Tekan R untuk bermain lagi", WIDTH//2 - 170, HEIGHT//2 + 40)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
