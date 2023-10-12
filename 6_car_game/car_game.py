import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 800
WIDTH_HALF = WIDTH // 2

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car game")

# Параметры дороги
ROAD_WIDTH = 374
ROADMARK_WIDTH = 7
ROAD_HALF = ROAD_WIDTH // 2

# позиции левой и правой полос
LEFT_LANE = WIDTH_HALF - ROAD_WIDTH // 4
RIGHT_LANE = WIDTH_HALF + ROAD_WIDTH // 4 # 393

# Цвета
GRASS_COLOR = (60, 220, 0)

# Шрифты
font = pygame.font.SysFont('gabriola', 48)
game_over_text = font.render("GAMEOVER", True, (255, 255, 255))
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WIDTH//2, HEIGHT//2)

continue_text = font.render("Press any key to play again", True, (255, 255, 255))
continue_rect = continue_text.get_rect()
continue_rect.center = (WIDTH//2, HEIGHT//2 + 64)

# очки
score = 0
score_text = font.render("0", True, (255, 255, 255))
score_rect = score_text.get_rect()
score_rect.center = (20, 20)


# загрузить картинку машины игрока
car = pygame.image.load("images/car.png")
car_rect = car.get_rect()
car_rect.center = RIGHT_LANE, HEIGHT * 0.8

# загрузить картинку машины врага
enemy_car = pygame.image.load("images/enemyCar.png")
enemy_car_rect = enemy_car.get_rect()
enemy_car_rect.center = LEFT_LANE, HEIGHT * 0.1

enemy_speed = 8

FPS = 60
clock = pygame.time.Clock()



def draw_road():
    pygame.draw.rect(screen, (50, 50, 50), (WIDTH_HALF - ROAD_HALF, 0, ROAD_WIDTH, HEIGHT))
    # центральная линия
    pygame.draw.rect(screen, (255, 240, 60), (WIDTH_HALF - ROADMARK_WIDTH // 2, 0, ROADMARK_WIDTH, HEIGHT))
    # левая линия
    pygame.draw.rect(screen, (255, 255, 255), (WIDTH_HALF - ROAD_HALF + ROADMARK_WIDTH*2, 0, ROADMARK_WIDTH, HEIGHT))
    # правая линия
    pygame.draw.rect(screen, (255, 255, 255), (WIDTH_HALF + ROAD_HALF - ROADMARK_WIDTH*3, 0, ROADMARK_WIDTH, HEIGHT))


def drive_enemy_car():
    global score
    enemy_car_rect.y += enemy_speed
    if enemy_car_rect.y > HEIGHT:
        score += 1
        if random.randint(0, 1) == 0:
            enemy_car_rect.center = LEFT_LANE, -enemy_car_rect.height // 2
        else:
            enemy_car_rect.center = RIGHT_LANE, -enemy_car_rect.height // 2

def increase_difficulty():
    if score % 2 == 0:
        enemy_speed += 0.15

def check_gameover():
    global running, score

    if car_rect.colliderect(enemy_car_rect):
        screen.blit(game_over_text, game_over_rect)
        screen.blit(continue_text, continue_rect)

        pygame.display.update()

        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

                if event.type == pygame.KEYDOWN:
                    is_paused = False
                    enemy_car_rect.center = LEFT_LANE, HEIGHT * 0.1
                    score = 0


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and car_rect.left + ROAD_HALF > RIGHT_LANE:
                car_rect.left -= ROAD_HALF
            if event.key == pygame.K_RIGHT and car_rect.left < LEFT_LANE:
                car_rect.left += ROAD_HALF

    screen.fill(GRASS_COLOR)
    draw_road()

    check_gameover()
    drive_enemy_car()
    
    score_text = font.render(str(score), True, (255, 255, 255))
    screen.blit(score_text, score_rect)

    screen.blit(enemy_car, enemy_car_rect)
    screen.blit(car, car_rect)

    pygame.display.update()
    clock.tick(FPS)



pygame.quit()