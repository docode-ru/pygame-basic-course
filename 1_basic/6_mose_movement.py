import pygame

pygame.init()

display_surface = pygame.display.set_mode((600, 400))

# Определине RGB цветов в кортежах 
BLACK = (0, 0, 0)

# загрузить картинку с птичкой
bird_image = pygame.image.load("images/bird.png")

# получить инофрмацию о поверхности (аналог слоя) на которой расположена картинки
bird_rect = bird_image.get_rect()
#                   bird_x, bird_y
bird_rect.center = (600/2, 400/2)


running = True
while running:
    for event in pygame.event.get():          # pygame.event.get() -> [ clickEvent, pressPress, Quit ]
        if event.type == pygame.QUIT:    
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            #print(event)
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            print(mouse_x, mouse_y)
            # изменить координаты птички по x и y, чтобы они соответствовали координатам клика мышки
            bird_rect.center = (mouse_x, mouse_y)
            # bird_rect.centerx = mouse_x
            # bird_rect.centery = mouse_y

        # перетаскивать объект при нажатии левой кнопки мыши
        if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
            print(event)
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            bird_rect.center = (mouse_x, mouse_y)
        

    # закрасить фон заданным цветом
    display_surface.fill(BLACK)

    # отобразить спрайты
    display_surface.blit(bird_image, bird_rect)

    # вывести буфер на экран
    pygame.display.flip()

pygame.quit()