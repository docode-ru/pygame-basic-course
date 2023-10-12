import pygame

pygame.init()

display_surface = pygame.display.set_mode((600, 400))

# Определине RGB цветов в кортежах 
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# закрасить фон заданным цветом
display_surface.fill(BLACK)

# загрузить и отобразить картинку
bird_sprite = pygame.image.load("images/bird.png")
display_surface.blit(bird_sprite, (0, 0))

# вывести красну рамку вокруг спрайта
bird_rect = bird_sprite.get_rect()

display_surface.fill(BLACK)

# телепортировать птичку на 20 пикселей вправо вдоль оси х
display_surface.blit(bird_sprite, (20, 0))

# телепортировать птичку на 2 пикселя вправо при нажатии клавиши вправо

# вывести буфер на экран
pygame.display.flip()

bird_x = 0
bird_y = 0
bird_speed = 10

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:    
            running = False
        
        # если нажали на клавишу и клавиша вправо   
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            bird_x += bird_speed
            
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            bird_x -= bird_speed

        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            bird_y -= bird_speed

        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            bird_y += bird_speed


    display_surface.fill(BLACK)
    display_surface.blit(bird_sprite, (bird_x, bird_y)) # изменить координату птички по x
    pygame.display.flip()



pygame.quit()