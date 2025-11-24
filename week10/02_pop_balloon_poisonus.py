import pygame
import random
import math

pygame.init()

WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pop Balon - Balon Jahat")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLUE = (135, 206, 235)
RED = (220, 50, 50)
BLACK = (0, 0, 0)

font = pygame.font.SysFont(None, 32)
big_font = pygame.font.SysFont(None, 48)

balloon_radius = 25

def reset_balloon():
    x = random.randint(balloon_radius, WIDTH - balloon_radius)
    y = HEIGHT + balloon_radius
    speed = random.randint(2, 5)
    return x, y, speed

good_x, good_y, good_speed = reset_balloon()
evil_x, evil_y, evil_speed = reset_balloon()

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
            mx, my = event.pos

            dx_g = mx - good_x
            dy_g = my - good_y
            dist_g = math.sqrt(dx_g * dx_g + dy_g * dy_g)

            dx_e = mx - evil_x
            dy_e = my - evil_y
            dist_e = math.sqrt(dx_e * dx_e + dy_e * dy_e)

            if dist_g <= balloon_radius:
                score += 1
                good_x, good_y, good_speed = reset_balloon()
            elif dist_e <= balloon_radius:
                score = max(0, score - 1)
                evil_x, evil_y, evil_speed = reset_balloon()

        if game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                score = 0
                start_time = pygame.time.get_ticks()
                good_x, good_y, good_speed = reset_balloon()
                evil_x, evil_y, evil_speed = reset_balloon()
                game_over = False

    if not game_over:
        good_y -= good_speed
        evil_y -= evil_speed

        if good_y + balloon_radius < 0:
            good_x, good_y, good_speed = reset_balloon()
        if evil_y + balloon_radius < 0:
            evil_x, evil_y, evil_speed = reset_balloon()

        elapsed_ms = pygame.time.get_ticks() - start_time
        remaining_time = total_time - elapsed_ms // 1000

        if remaining_time <= 0:
            remaining_time = 0
            game_over = True
    else:
        remaining_time = 0

    screen.fill(BLUE)

    if not game_over:
        # balon baik (merah)
        pygame.draw.circle(screen, RED, (good_x, good_y), balloon_radius)
        pygame.draw.line(screen, WHITE,
                         (good_x, good_y + balloon_radius),
                         (good_x, good_y + balloon_radius + 30), 2)
        # balon jahat (hitam)
        pygame.draw.circle(screen, BLACK, (evil_x, evil_y), balloon_radius)
        pygame.draw.line(screen, WHITE,
                         (evil_x, evil_y + balloon_radius),
                         (evil_x, evil_y + balloon_radius + 30), 2)

    draw_text(f"Score: {score}", 10, 10)
    draw_text(f"Time: {remaining_time}", 10, 40)

    if game_over:
        draw_text("Waktu Habis!", WIDTH//2 - 110, HEIGHT//2 - 40, big_font)
        draw_text(f"Score akhir: {score}", WIDTH//2 - 120, HEIGHT//2, big_font)
        draw_text("Tekan R untuk bermain lagi", WIDTH//2 - 170, HEIGHT//2 + 40)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
