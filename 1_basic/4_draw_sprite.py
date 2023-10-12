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
pygame.draw.rect(display_surface, RED, bird_rect, 4)

pygame.draw.line(display_surface, RED, (600/2, 0), (600/2, 400), 2)
pygame.draw.line(display_surface, RED, (0, 400/2), (600, 400/2), 2)

# отобразить птичку по центру
display_surface.blit(bird_sprite, (600/2 - (64/2), 400/2 - (64/2)))

# вывести буфер на экран
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:    
            running = False

pygame.quit()