import pygame

pygame.init()

display_surface = pygame.display.set_mode((600, 400))

# Определине RGB цветов в кортежах 
BLACK = (0, 0, 0)

SPEED = 5

# загрузить картинку с птичкой
bird_image = pygame.image.load("images/bird.png")

# получить инофрмацию о поверхности (аналог слоя) на которой расположена картинки
bird_rect = bird_image.get_rect()
#                   bird_x, bird_y
bird_rect.center = (600/2, 400/2)

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

    # закрасить фон заданным цветом
    display_surface.fill(BLACK)
    
    # отобразить спрайты
    display_surface.blit(bird_image, bird_rect)

    # вывести буфер на экран
    pygame.display.flip()

    # clock.tick() - вернет кол-во миллисекунд прошедшее с момента предыдущего вызова. 
    # Если передать число в clock.tick(), то clock сделает задрежку, чтобы игра работала медленнее, чем заданное кол-во FPS
    # при вызове Clock.tick(60) один раз за кадр игра никогда не будет работатьс со скоростью более 60 кадров в секунду
    clock.tick(FPS)

pygame.quit()