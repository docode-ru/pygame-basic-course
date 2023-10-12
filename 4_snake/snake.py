import pygame, random

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("~SNAKE~")

FPS = 10
clock = pygame.time.Clock()

# Игровые переменные
SNAKE_HEAD_SIZE = 20

head_x = WINDOW_WIDTH // 2
head_y = WINDOW_HEIGHT // 2

snake_dx = 0
snake_dy = 0

score = 0

# Цвета
DARK_GRAY = (60, 60, 60)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (10, 100, 0)
WHITE = (255, 255, 255)

# Шрифт
font = pygame.font.SysFont("Pixeboy-z8XGD.ttf", 40)
small_font = pygame.font.SysFont("Pixeboy-z8XGD.ttf", 30)

# Текст
score_text = font.render(f"Score: {score}", True, WHITE)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

game_over_text = font.render("GAMEOVER", True, RED)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

continue_text = small_font.render("Press any key on keyboard", True, RED)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 42)

# Звуки
pick_up_sound = pygame.mixer.Sound("sounds/pickup.wav")
pick_up_sound.set_volume(0.5)

# Спрайты (нарисуем при помощи простой функции rect указывая размер и координаты)
# Для прямоугольника надо указать: top-left x, top-left y, width, height
apple_coord = (500, 500, SNAKE_HEAD_SIZE, SNAKE_HEAD_SIZE)
apple_rect = pygame.draw.rect(display_surface, RED, apple_coord)

head_coord = (head_x, head_y, SNAKE_HEAD_SIZE, SNAKE_HEAD_SIZE)
head_rect = pygame.draw.rect(display_surface, GREEN, head_coord)

body_coords = []    # координаты частей тела змейки

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # передвижение змейки
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_dx = -1
                snake_dy = 0
            if event.key == pygame.K_RIGHT:
                snake_dx = 1
                snake_dy = 0
            if event.key == pygame.K_UP:
                snake_dx = 0
                snake_dy = -1
            if event.key == pygame.K_DOWN:
                snake_dx = 0
                snake_dy = 1

    # Проверить GameOver
    if head_rect.left < 0 or head_rect.right > WINDOW_WIDTH or head_rect.top < 0 or head_rect.bottom > WINDOW_HEIGHT or head_coord in body_coords:
        # Вывести текст GameOver
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)

        pygame.display.update()
        # Сделать паузу, пока игроку не нажмет любую клавишу
        is_paused = True
        while is_paused:
            # Если игрок хочет играть по новой
            for event in pygame.event.get():
                # Сбросить игру
                if event.type == pygame.KEYDOWN:
                    head_x = WINDOW_WIDTH // 2
                    head_y = WINDOW_HEIGHT // 2
                    snake_dx = 0
                    snake_dy = 0
                    head_coord = (head_x, head_y, SNAKE_HEAD_SIZE, SNAKE_HEAD_SIZE)
                    body_coords = []
                    score = 0
                    is_paused = False
                # если хочет выйти
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

    # проверить столкновение с яблоком
    if head_rect.colliderect(apple_rect):
        score += 1
        pick_up_sound.play()
        
        cols = WINDOW_WIDTH // SNAKE_HEAD_SIZE
        rows = WINDOW_HEIGHT // SNAKE_HEAD_SIZE

        apple_x = random.randint(0, cols-1)
        apple_y = random.randint(0, rows-1)
        apple_coord = (apple_x * SNAKE_HEAD_SIZE, apple_y * SNAKE_HEAD_SIZE, SNAKE_HEAD_SIZE, SNAKE_HEAD_SIZE)

        body_coords.append(head_coord)
    
    

    # Обновить HUD
    score_text = font.render(f"Score: {score}", True, WHITE)

    # Заливка фона
    display_surface.fill(DARK_GRAY)

    # Добавить координату головы змейки по первому индексу 
    # и сдвинуть все координаты частей змейки на одну позицию
    body_coords.insert(0, head_coord)
    body_coords.pop()

    head_x += snake_dx * SNAKE_HEAD_SIZE
    head_y += snake_dy * SNAKE_HEAD_SIZE

    head_coord = (head_x, head_y, SNAKE_HEAD_SIZE, SNAKE_HEAD_SIZE)

    # HUD
    display_surface.blit(score_text, score_rect)

    # отображение спрайтов
    for body_part in body_coords:
        pygame.draw.rect(display_surface, DARK_GREEN, body_part)

    apple_rect = pygame.draw.rect(display_surface, RED, apple_coord)
    head_rect = pygame.draw.rect(display_surface, GREEN, head_coord)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()

