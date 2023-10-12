import random
from tkinter import font
import pygame

# Инизиализация pygame
pygame.init()

# Установить размеры экрана и поверхности
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Feed the bird")

# Установить FPS и часов
FPS = 60
clock = pygame.time.Clock()

# Цвета
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# Игровые переменные
TOP_MARGIN = 64
BOTTOM_MARGIN = 32
BLACK = (0, 0, 0)
BEAN_ACCELERATION = 0.5

BUFFER_BEAN_DIST = -100

PLAYER_SPEED = 5
INIT_BEAN_SPEED = 8

bean_speed = INIT_BEAN_SPEED
score = 0
lives = 3

# загрузить шрифт
font = pygame.font.Font('VT323-Regular.ttf', 32)

# установить текст
score_text = font.render("Score: " + str(score), True, YELLOW)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

lives_text = font.render("Lives: " + str(lives), True, YELLOW)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 10, 10)

# текст GameOver
game_over_text = font.render("GAMEOVER", True, WHITE)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

continue_text = font.render("Press any key to play again", True, WHITE)
continue_text_rect = continue_text.get_rect()
continue_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + game_over_rect.height)

# Загрузить картинки
player_image = pygame.image.load("images/bird.png")
player_rect = player_image.get_rect()
player_rect.x = 32
player_rect.centery = WINDOW_HEIGHT // 2

bean_image = pygame.image.load("images/bean.png")
bean_rect = bean_image.get_rect()
bean_rect.x = WINDOW_WIDTH - BUFFER_BEAN_DIST
bean_rect.y = random.randint(TOP_MARGIN, WINDOW_HEIGHT - BOTTOM_MARGIN)

# загрузить звуки и музыку
bean_sound = pygame.mixer.Sound("sounds/pickupCoin.wav")
bean_sound.set_volume(.1)

miss_sound = pygame.mixer.Sound("sounds/miss_sound.wav")
miss_sound.set_volume(.1)

pygame.mixer.music.load("sounds/POL-magical-sun-short.wav")
pygame.mixer.music.set_volume(.05)
pygame.mixer.music.play(-1, 0, 1000)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Перемещение птичкой при нажатии клавиш вверх/вниз
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_rect.top > TOP_MARGIN:
        player_rect.y -= PLAYER_SPEED
    elif keys[pygame.K_DOWN] and player_rect.bottom < WINDOW_HEIGHT:
        player_rect.y += PLAYER_SPEED

    # Перемещение зернышка
    if bean_rect.x < 0:
        lives -= 1
        bean_rect.x = WINDOW_WIDTH - BUFFER_BEAN_DIST
        bean_rect.y = random.randint(TOP_MARGIN, WINDOW_HEIGHT - BOTTOM_MARGIN)
        miss_sound.play()
    else:
        bean_rect.x -= bean_speed
    
    # Проверить столкновение птички и зернышка
    if player_rect.colliderect(bean_rect):
        score += 1

        # проиграт звук
        bean_sound.play()
        
        # ускорить зернышко
        bean_speed += BEAN_ACCELERATION

        
        bean_rect.x = WINDOW_WIDTH - BUFFER_BEAN_DIST
        bean_rect.y = random.randint(TOP_MARGIN, WINDOW_HEIGHT - BOTTOM_MARGIN)

    # Проверить завершение (если Lives <= 0)
    if lives == 0:
        # отобразить текст GameOver
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_text_rect)
        # обновить экран
        pygame.display.update()

        pygame.mixer.music.stop()

        is_paused = True
        # в цикле проверить, что игрок хочет играть по новой нажав на любую клавишу
        while is_paused:
            for event in pygame.event.get():
                #    если игрок нажал клавишу, то сбросить игру в начальное состояние
                if event.type == pygame.KEYDOWN:
                    score = 0
                    lives = 3
                    player_rect.y = WINDOW_HEIGHT//2
                    bean_speed = INIT_BEAN_SPEED
                    is_paused = False
                    pygame.mixer.music.play(-1, 0, 1000)
                #    если игрок нажмет esc, то выйти из игры
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

    # Обновить HUD
    score_text = font.render("Score: " + str(score), True, YELLOW)
    lives_text = font.render("Lives: " + str(lives), True, YELLOW)

    # закрасить окошко  
    display_surface.fill(BLACK)

    # отобразить HUD
    display_surface.blit(score_text, score_rect)
    display_surface.blit(lives_text, lives_rect)

    # отобразить спрайты
    display_surface.blit(player_image, player_rect)
    display_surface.blit(bean_image, bean_rect)

    # обновить экран
    pygame.display.update() # вместо flip()

    clock.tick(FPS)

# Остановить игру
pygame.quit()