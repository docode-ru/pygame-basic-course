
import pygame

# Инициализация pygame
pygame.init()

# Установить размеры окна игры и заголовок
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
pygame.display.set_caption("Tic Tac Toe")
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Игровые переменные
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CELL_LINE_WIDTH = 5

CROSS_COLOR = (76, 76, 76)
CIRCLE_COLOR = (239, 231, 200)
STROKE_LINE_COLOR = CIRCLE_COLOR

# Установить ширину и высоту ячейки
CELL_WIDTH = WINDOW_WIDTH // 3
CELL_HEIGHT = WINDOW_HEIGHT // 3
CROSS_LINE_PADDING = CELL_HEIGHT // 6

# Двухмерный список, который хранит значения игрового поля
# X - поле занято крестиком, O - поле занято ноликом, "" - ячейка не занята
board = [["", "", ""], ["", "", ""], ["", "", ""]]

current_player = "X"
prev_player = "O"

# Установить шрифт
font = pygame.font.Font("Franxurter.ttf", WINDOW_HEIGHT // 3)


# Установить FPS и часы для управления частотой обновлений кадров в окне
FPS = 60
clock = pygame.time.Clock()

def draw_board():
    # Нарисовать вертикальные линии
    pygame.draw.line(display_surface, LINE_COLOR, (CELL_WIDTH, 0), (CELL_WIDTH, WINDOW_HEIGHT), CELL_LINE_WIDTH)
    pygame.draw.line(display_surface, LINE_COLOR, (2 * CELL_HEIGHT, 0), (2 * CELL_WIDTH, WINDOW_HEIGHT), CELL_LINE_WIDTH)
    # Нарисовать горизонтальные линии
    pygame.draw.line(display_surface, LINE_COLOR, (0, CELL_HEIGHT), (WINDOW_WIDTH, CELL_HEIGHT), CELL_LINE_WIDTH)
    pygame.draw.line(display_surface, LINE_COLOR, (0, 2 * CELL_HEIGHT), (WINDOW_WIDTH, 2 * CELL_HEIGHT), CELL_LINE_WIDTH)

def draw_XO():
    for row in range(3):
        for col in range(3):
            text = None
            text_rect = None

            if board[row][col] == "X":
                text = font.render("X", True, CROSS_COLOR)
                text_rect = text.get_rect()
                text_x = col * CELL_WIDTH + CELL_WIDTH // 2
                text_y = row * CELL_HEIGHT + CELL_HEIGHT // 2
                text_rect.center = (text_x, text_y)
            elif board[row][col] == "O":
                text = font.render("O", True, CIRCLE_COLOR)
                text_rect = text.get_rect()
                text_x = col * CELL_WIDTH + CELL_WIDTH // 2
                text_y = row * CELL_HEIGHT + CELL_HEIGHT // 2
                text_rect.center = (text_x, text_y)

            if text and text_rect:
                display_surface.blit(text, text_rect)

# Функция для обработки клика игрока в ячейке
def handle_user_input():
    global current_player, prev_player

    # Если игрок кликнул мышкой в окне
    if event.type == pygame.MOUSEBUTTONUP:
        # Получить x,y координаты клика
        pos = pygame.mouse.get_pos()
        # Вычислить значение строки и столбца в месте клика
        col = pos[0] // CELL_WIDTH
        row = pos[1] // CELL_HEIGHT

        # Проверить, что ячейка поля еще не занята
        if board[row][col] == "":
            # Сделать значение ячейки равным текущему игроку
            board[row][col] = current_player
            prev_player = current_player
            # Сменить ход игрока
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"

def check_win():
    # проверка по вертикали
    for col in range(len(board)):
        if board[0][col] == prev_player and board[1][col] == prev_player and board[2][col] == prev_player:
            pos_x = col * CELL_WIDTH + CELL_WIDTH//2
            pygame.draw.line( display_surface, STROKE_LINE_COLOR, (pos_x, CROSS_LINE_PADDING), (pos_x, WINDOW_HEIGHT - CROSS_LINE_PADDING), 10 )
            return True

	# проверка по горизонтали
    for row in range(len(board)):
        if board[row][0] == prev_player and board[row][1] == prev_player and board[row][2] == prev_player:
            pos_y = row * CELL_WIDTH + CELL_WIDTH//2
            pygame.draw.line( display_surface, STROKE_LINE_COLOR, (CROSS_LINE_PADDING, pos_y), (WINDOW_WIDTH - CROSS_LINE_PADDING, pos_y), 10 )
            return True

	#   проверка по возрастающей диагонали
    if board[2][0] == prev_player and board[1][1] == prev_player and board[0][2] == prev_player:
        pygame.draw.line( display_surface, STROKE_LINE_COLOR, 
                        (CROSS_LINE_PADDING, WINDOW_HEIGHT - CROSS_LINE_PADDING), (WINDOW_WIDTH - CROSS_LINE_PADDING, CROSS_LINE_PADDING), 10 )
        return True

	#   проверка по убывающей диагонали
    if board[0][0] == prev_player and board[1][1] == prev_player and board[2][2] == prev_player:
        pygame.draw.line( display_surface, STROKE_LINE_COLOR, 
        (CROSS_LINE_PADDING, CROSS_LINE_PADDING), (WINDOW_WIDTH - CROSS_LINE_PADDING, WINDOW_HEIGHT - CROSS_LINE_PADDING), 10 )
        return True


running = True
# Главный игоровой цикл
while running:
    # Обработать событие закрытия окна, если пользователь хочет выйти
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif not check_win():
            handle_user_input()

    # Рисуем фон
    display_surface.fill(BG_COLOR)

    
    # Рисуем поле с линиями
    draw_board()
    draw_XO()
    check_win()

    # Обновить экран и замедлить цикл while
    pygame.display.update()
    clock.tick(FPS)

# Выйти из игры
pygame.quit()