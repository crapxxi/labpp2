import pygame
import random
import sys

pygame.init()

# Настройки окна
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game Demo")
clock = pygame.time.Clock()

# Шрифт для отображения счета и уровня
font = pygame.font.Font(None, 30)

# Цвета
WHITE = (255, 255, 255)
BLUE = (0, 0,255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Настройки змеи
snake_pos = [100, 50]  # Начальная позиция змеи
snake_body = [[100, 50], [90, 50], [80, 50]]  # Тело змеи
snake_direction = "RIGHT"  # Начальное направление
change_to = snake_direction
speed = 10  # Начальная скорость

# Стены
walls = [
    pygame.Rect(50, 50, 10, 50),  # Вертикальная стена
    pygame.Rect(200, 250, 200, 10)  # Горизонтальная стена
]

# Генерация еды, чтобы не попасть на стену или тело змеи
def spawn_food():
    while True:
        food = [random.randrange(1, WIDTH // 10) * 10, random.randrange(1, HEIGHT // 10) * 10]
        if food not in snake_body and not any(wall.collidepoint(food[0], food[1]) for wall in walls):
            return food
# Переменные пищи
food_pos = spawn_food()
food_spawn = True
food_weighted = False
food_dis = False
# Счет игры
game_score = 0
p_level = 0
level = 1  # Уровень игры
start = 0 # Таймер

# Основной игровой цикл
isRunning = True

while isRunning:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "DOWN":
                change_to = "UP"
            if event.key == pygame.K_DOWN and snake_direction != "UP":
                change_to = "DOWN"
            if event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                change_to = "RIGHT"

    # Движение змеи
    snake_direction = change_to
    if snake_direction == "UP":
        snake_pos[1] -= 10
    elif snake_direction == "DOWN":
        snake_pos[1] += 10
    elif snake_direction == "LEFT":
        snake_pos[0] -= 10
    elif snake_direction == "RIGHT":
        snake_pos[0] += 10

    # Добавление новой позиции змеи
    snake_body.insert(0, list(snake_pos))

    # Проверка на поедание еды
    if snake_pos == food_pos:
        #Весовые пищи
        if food_weighted:
            game_score += 3
        else:
            game_score += 1
        # Повышение уровня каждые 5 очка
        if game_score // 5 > p_level:
            p_level = level
            level += 1
            speed += 2  # Увеличиваем скорость
        # Рандомизация пищ
        if random.randint(0,1) == 1:
            food_weighted = True
            if random.randint(0,1) == 1:
                food_dis = True
        else:
            food_weighted = False
            food_dis = False 
        food_spawn = False
    else:
        snake_body.pop()

    # Генерация новой еды
    if not food_spawn:
        food_pos = spawn_food()
        if food_dis and start == 0:
            start = pygame.time.get_ticks()
    food_spawn = True
    # Логика исчезновении
    el_time = (pygame.time.get_ticks()-start)//1000
    if el_time == 10 and food_dis:
        food_dis = False
        el_time = 0
        start = 0
        food_spawn= False


    # Проверка на столкновение со стеной
    for wall in walls:
        if wall.collidepoint(snake_pos[0], snake_pos[1]):
            isRunning = False

    # Проверка на столкновение с границами экрана
    if snake_pos[0] < 0 or snake_pos[0] >= WIDTH or snake_pos[1] < 0 or snake_pos[1] >= HEIGHT:
        isRunning = False

    # Проверка на столкновение с самим собой
    for block in snake_body[1:]:
        if snake_pos == block:
            isRunning = False

    # Обновление экрана
    screen.fill(BLACK)

    # Отрисовка змеи
    for p in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(p[0], p[1], 10, 10))

    # Отрисовка еды
    if food_spawn:
        if not food_weighted:
            pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))
        else:
            if food_dis:
                pygame.draw.rect(screen, BLUE, pygame.Rect(food_pos[0],food_pos[1], 15,15))
            else:
                pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], 15, 15))
    # Отрисовка стен
    for wall in walls:
        pygame.draw.rect(screen, WHITE, wall)

    # Отображение счета и уровня
    score_text = font.render(f"Score: {game_score}  Level: {level}", True, WHITE)
    screen.blit(score_text, (20, 20))

    pygame.display.update()
    clock.tick(speed)  # Устанавливаем скорость в зависимости от уровня

# Отображение сообщения "GAME OVER"
game_over_text = font.render("GAME OVER", True, WHITE)
game_over_rectangle = game_over_text.get_rect()
game_over_rectangle.center = (WIDTH / 2, HEIGHT / 2)
screen.blit(game_over_text, game_over_rectangle)
pygame.display.update()
pygame.time.wait(3000)  # Пауза перед выходом
