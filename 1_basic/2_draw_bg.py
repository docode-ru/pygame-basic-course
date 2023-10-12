import pygame

pygame.init()

display_surface = pygame.display.set_mode((600, 400))

# Определине RGB цветов в кортежах 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGNETA = (255, 0, 255)

# закрасить фон заданным цветом
display_surface.fill(RED)

# вывести буфер на экран
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():          # pygame.event.get() -> [ clickEvent, pressPress, Quit ]
        if event.type == pygame.QUIT:    
            running = False

pygame.quit()