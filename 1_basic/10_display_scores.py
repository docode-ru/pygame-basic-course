import pygame
import random

pygame.init()

display_surface = pygame.display.set_mode((600, 400))

# Определине RGB цветов в кортежах 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SPEED = 5

score = 0

# устноавить шрифт
font = pygame.font.Font('VT323-Regular.ttf', 32)

# установить текст
score_text = font.render("Score: " + str(score), True, WHITE, BLACK)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

# загрузить картинку с птичкой
bird_image = pygame.image.load("images/bird.png")

# загрузить картинку с зерном
bean_image = pygame.image.load("images/bean.png")

# получить инофрмацию о поверхности (аналог слоя) на которой расположена картинки
bird_rect = bird_image.get_rect()
#                   bird_x, bird_y
bird_rect.center = (600/2, 400/2)


# получить инофрмацию о поверхности (аналог слоя) на которой расположена картинки
bean_rect = bean_image.get_rect()

bean_rect.center = (300/2, 200/2)


FPS = 60   # кол-во кадров за 1 секунду
# Объект Clock помогает отслеживать время в игре. 
# Так же предоставляет несколько функций, помогающих контролировать частоту кадров (FPS)
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():          # pygame.event.get() -> [ clickEvent, pressPress, Quit ]
        if event.type == pygame.QUIT:    
            running = False

    keys = pygame.key.get_pressed()
    #print(keys[pygame.K_LEFT])

    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and bird_rect.left > 0:
        bird_rect.x -= SPEED
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and bird_rect.right < 600:
        bird_rect.x += SPEED
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and bird_rect.top > 0:
        bird_rect.y -= SPEED
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and bird_rect.bottom < 400:
        bird_rect.y += SPEED
    
    # Проверить столкновение (пересечение) между виртуальными границами спрайтов
    if bird_rect.colliderect(bean_rect):
        # print("HIT")
        # случайно переместить зернышко в новую позицию
        rnd_x = random.randint(0, 600 - bean_rect.width)
        rnd_y = random.randint(0, 400 - bean_rect.height)
        # bean_rect.topleft = (rnd_x, rnd_y)
        bean_rect.x = rnd_x
        bean_rect.y = rnd_y
        score += 1

    # Обновить HUD (head up display)
    score_text = font.render("Score: " + str(score), True, WHITE, BLACK)

    # закрасить фон заданным цветом
    display_surface.fill(BLACK)
    
    # Нарисовать рамки вокруг спрайтов птички и зернышка
    pygame.draw.rect(display_surface, (255, 0, 0), bird_rect, 1)
    pygame.draw.rect(display_surface, (255, 255, 0), bean_rect, 1)

    # отобразить спрайты
    display_surface.blit(score_text, score_rect)
    display_surface.blit(bird_image, bird_rect)
    display_surface.blit(bean_image, bean_rect)

    # вывести буфер на экран
    pygame.display.flip()

    # clock.tick() - вернет кол-во миллисекунд прошедшее с момента предыдущего вызова. 
    # Если передать число в clock.tick(), то clock сделает задрежку, чтобы игра работала медленнее, чем заданное кол-во FPS
    # при вызове Clock.tick(60) один раз за кадр игра никогда не будет работатьс со скоростью более 60 кадров в секунду
    clock.tick(FPS)

pygame.quit()