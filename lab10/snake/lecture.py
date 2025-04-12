import pygame
import random
import sys
import psycopg2
import json


conn = psycopg2.connect(
    dbname="snake_game",
    user="postgres",
    password="admin",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

WIDTH, HEIGHT = 600, 400

pygame.init()

# Настройки окна
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

walls = []

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
def get_username():
    input_active = True
    username = ""
    input_box = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 20, 200, 40)
    color_active = pygame.Color('lightskyblue3')
    color_passive = pygame.Color('gray15')
    color = color_passive

    while input_active:
        screen.fill(BLACK)
        text = font.render("Enter your username:", True, WHITE)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - 60))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and username:
                    return username
                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                else:
                    if len(username) < 15 and event.unicode.isalnum():
                        username += event.unicode

        pygame.draw.rect(screen, color, input_box, 2)
        user_surface = font.render(username, True, WHITE)
        screen.blit(user_surface, (input_box.x + 5, input_box.y + 5))
        pygame.display.flip()
        clock.tick(30)

username = get_username()
with open("levels.json") as f:
    raw_levels = json.load(f)

level_data = {}
for lvl, data in raw_levels.items():
    lvl = int(lvl)
    walls = [pygame.Rect(*w) for w in data["walls"]]
    level_data[lvl] = {
        "walls": walls,
        "speed": data["speed"]
    }


cur.execute("SELECT user_id, level FROM users WHERE username = %s", (username,))
user = cur.fetchone()

if user:
    user_id, level = user
    print(f"Welcome back, {username}! Level: {level}")
else:
    cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING user_id", (username,))
    user_id = cur.fetchone()[0]
    level = 1
    conn.commit()
    print(f"New user {username} created.")
# Загрузка параметров уровня
if level in level_data:
    walls = level_data[level]["walls"]
    speed = level_data[level]["speed"]
else:
    # Если уровень выше всех определённых, повторяем последний
    max_level = max(level_data.keys())
    walls = level_data[max_level]["walls"]
    speed = level_data[max_level]["speed"]
# Get best score and best level for this user
cur.execute("""
    SELECT MAX(score), MAX(level)
    FROM user_scores
    WHERE user_id = %s
""", (user_id,))
best_score, best_level = cur.fetchone()
if best_score is None:
    best_score = 0
if best_level is None:
    best_level = 1


def reset_snake():
    global snake_pos, snake_body, snake_direction
    snake_pos = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50]]
    snake_direction = "RIGHT"
def display_level(level):
    level_text = font.render(f"Level {level}", True, WHITE)
    level_rect = level_text.get_rect()
    level_rect.center = (WIDTH // 2, HEIGHT // 2)
    screen.fill(BLACK)  # Clear screen
    screen.blit(level_text, level_rect)
    pygame.display.update()
def draw_walls(walls):
    for wall in walls:
        x, y, width, height = wall
        pygame.draw.rect(screen, WHITE, pygame.Rect(x, y, width, height))

current_level_data = level_data.get(level, level_data[max(level_data)])
walls = current_level_data["walls"]
speed = current_level_data["speed"]

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
            if event.key == pygame.K_p:
                print("Game paused. Saving progress...")
                paused = True

                cur.execute("""
                    INSERT INTO user_scores (user_id, score, level)
                    VALUES (%s, %s, %s)
                    """, (user_id, game_score, level))
                conn.commit()
                while paused:
                    for pevent in pygame.event.get():
                        if pevent.type == pygame.KEYDOWN and pevent.key == pygame.K_p:
                            print("Resuming game...")
                            paused = False

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
            p_level = game_score // 5
            level += 1
            reset_snake()  # Teleport snake to the initial position
            display_level(level)  # Display level message
            pygame.time.wait(2000)  # Wait for 2 seconds before continuing the game
            current_level_data = level_data.get(level, level_data[max(level_data)])
            walls = current_level_data["walls"]
            speed = current_level_data["speed"]
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

    user_text = font.render(f"Player: {username}", True, WHITE)
    screen.blit(user_text, (WIDTH - user_text.get_width() - 20, 20))

    # Best score and level display
    best_text = font.render(f"Best: {best_score} | Level: {best_level}", True, WHITE)
    screen.blit(best_text, (20, HEIGHT - 30))



    pygame.display.update()
    clock.tick(speed)  # Устанавливаем скорость в зависимости от уровня
# Save score if it's a new best
if game_score > best_score or level > best_level:
    cur.execute("""
        INSERT INTO user_scores (user_id, score, level)
        VALUES (%s, %s, %s)
    """, (user_id, game_score, level))
    conn.commit()

# Отображение сообщения "GAME OVER"
game_over_text = font.render("GAME OVER", True, WHITE)
game_over_rectangle = game_over_text.get_rect()
game_over_rectangle.center = (WIDTH / 2, HEIGHT / 2)
screen.blit(game_over_text, game_over_rectangle)
pygame.display.update()

pygame.time.wait(3000)  # Пауза перед выходом
