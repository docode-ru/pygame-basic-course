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
display_surface.fill(WHITE)

# рисуем примитивные фигуры
# Линия
# line(surface, color, starting_point, ending_point, thickness)   
pygame.draw.line(display_surface, BLACK, (0, 0), (600/2, 400/2), 4)

# Оси координат
pygame.draw.line(display_surface, BLUE, (0, 0), (600, 0), 5)
pygame.draw.line(display_surface, RED, (0, 0), (0, 400), 5)

# Круг
# сircle(surface, color, center, radius, width)
pygame.draw.circle(display_surface, GREEN, (600/2, 400/2), 100, 10)

# Прямоугольник
# rect(surface, color, (top-left x, top-left y, width, height))
pygame.draw.rect(display_surface, MAGNETA, (50, 50, 200, 100), 10)
pygame.draw.rect(display_surface, MAGNETA, (300, 100, 100, 100))

# вывести буфер на экран
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():          # pygame.event.get() -> [ clickEvent, pressPress, Quit ]
        if event.type == pygame.QUIT:    
            running = False

pygame.quit()