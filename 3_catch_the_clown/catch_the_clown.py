import pygame, random

# Инициализация pygame
pygame.init()

# Установить размеры окна игры и заголовок
WINDOW_WIDTH = 945
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Catch the clown")

# Установить FPS и часы
FPS = 60
clock = pygame.time.Clock()

# Загрузить картинки
bg_image = pygame.image.load("images/background.png")
bg_rect = bg_image.get_rect()
bg_rect.topleft = (0, 0)

clown_image = pygame.image.load("images/clown.png")
clown_rect = clown_image.get_rect()
clown_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

# Начальные значения переменных клоуна
CLOWN_INIT_SPEED = 3
PLAYER_STARTING_LIVES = 3
CLOWN_ACCELERATION = 0.5

clown_speed = CLOWN_INIT_SPEED
clown_dx = random.choice([-1, 1])
clown_dy = random.choice([-1, 1])

score = 0
lives = PLAYER_STARTING_LIVES

# Установить цвета
BLUE = (1, 176, 210)
YELLOW = (246, 231, 20)

# Загрузить шрифт
font = pygame.font.Font("Franxurter.ttf", 32)

# Установить текст
score_text = font.render(f"Score: {score}", True, YELLOW)
score_rect = score_text.get_rect()
score_rect.topright = (WINDOW_WIDTH - 50, 10)

lives_text = font.render(f"Lives: {lives}", True, BLUE)
lives_rect = lives_text.get_rect()
lives_rect.topleft = (50, 10)

game_over_text = font.render("GAMEOVER", True, BLUE, YELLOW)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

continue_text = font.render("Click anyware to play again", True, YELLOW, BLUE)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 64)

# загрузить звуки и музыку
click_sound = pygame.mixer.Sound("sounds/click_sound.wav")
miss_sound = pygame.mixer.Sound("sounds/miss_sound.wav")
pygame.mixer.music.load("music/background_music.wav")
pygame.mixer.music.set_volume(0.5)

# проиграть музыку
pygame.mixer.music.play(-1, 0, 1000)

# Главный игоровой цикл
running = True
while running:
    #   Обработать событие закрытия окна, если пользователь хочет выйти
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Если есть клик
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]

            #   Если кликнули по клоуну
            if clown_rect.collidepoint(mouse_x, mouse_y):
                click_sound.play()
                score += 1
                #       Увеличить скорость клоуна
                clown_speed += CLOWN_ACCELERATION
                #       Выбрать новое случайное направление
                previous_dx = clown_dx
                previous_dy = clown_dy

                while previous_dx == clown_dx and previous_dy == clown_dy:
                    clown_dx = random.choice([-1, 1])
                    clown_dy = random.choice([-1, 1])
            else:
                # промахнулись
                miss_sound.play()
                lives -= 1

    # проверить завершение игры
    if lives == 0:
        #   Вывести текст Game over и Click anyware
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        pygame.display.update()

        #   Остановить музыку
        pygame.mixer.music.stop()
        is_paused = True
        #   Запустить цикл с паузой
        while is_paused:
            for event in pygame.event.get():
                #       Если игрок кликнул в любом месте окна
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #   сбросить все игровые переменные
                    score = 0
                    lives = PLAYER_STARTING_LIVES

                    clown_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)
                    clown_speed = CLOWN_INIT_SPEED
                    clown_speed = CLOWN_INIT_SPEED
                    clown_dx = random.choice([-1, 1])
                    clown_dy = random.choice([-1, 1])
                    pygame.mixer.music.play(-1, 0, 1000)
                    is_paused = False

                #       Если игрок хочет выйти
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False


    # обновление HUD
    score_text = font.render(f"Score: {score}", True, YELLOW)
    lives_text = font.render(f"lives: {lives}", True, BLUE)

    # переместить клоуна
    clown_rect.x += clown_dx * clown_speed
    clown_rect.y += clown_dy * clown_speed

    # отразить клоуна от границ окна
    if clown_rect.left <= 0 or clown_rect.right >= WINDOW_WIDTH:
        clown_dx *= -1
    if clown_rect.top <= 0 or clown_rect.bottom >= WINDOW_HEIGHT:
        clown_dy *= -1

    # нарисовать фон
    display_surface.blit(bg_image, bg_rect)

    # нарисовать HUD
    display_surface.blit(score_text, score_rect)
    display_surface.blit(lives_text, lives_rect)
    
    # нарисовать клоуна
    display_surface.blit(clown_image, clown_rect)

    #   Выполнить обновление экрана и часов
    pygame.display.update()
    clock.tick(FPS)

# Выйти из игры
pygame.quit()

