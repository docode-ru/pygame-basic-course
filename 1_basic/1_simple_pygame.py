import pygame

pygame.init()

pygame.display.set_mode((600, 400))

running = True
while running:
    for event in pygame.event.get():          # pygame.event.get() -> [ clickEvent, pressPress, Quit ]
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

print('Программа работает')