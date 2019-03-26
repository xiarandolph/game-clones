import pygame, sys
from random import randint
from pygame.locals import *

# CONSTANTS
FPS = 10
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
CELL_SIZE = 20
assert WINDOW_WIDTH % CELL_SIZE == 0, "WINDOW_WIDTH must be multiple of CELL_SIZE"
assert WINDOW_HEIGHT % CELL_SIZE == 0, "WINDOW_HEIGHT must be multiple of CELL_SIZE"
# coordinates from converting pixels to the cells
GAME_WIDTH = WINDOW_WIDTH / CELL_SIZE
GAME_HEIGHT = WINDOW_HEIGHT / CELL_SIZE

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# CONTROLS
UP_KEYS = [K_UP, K_w]
LEFT_KEYS = [K_LEFT, K_a]
DOWN_KEYS = [K_DOWN, K_s]
RIGHT_KEYS = [K_RIGHT, K_d]

# directions
UP = 'up'
LEFT = 'left'
DOWN = 'down'
RIGHT = 'right'



def snake_collided():
    # check for colliding with end of map
    if snake[0]['x'] in [-1, GAME_WIDTH] or snake[0]['y'] in [-1, GAME_HEIGHT]:
        return True
    # check for collisions with itself
    for part in snake[1:]:
        if part['x'] == snake[0]['x'] and part['y'] == snake[0]['y']:
            print("game over")
            return True
    return False

def draw_snake():    
    for part in snake:
        x = part['x'] * CELL_SIZE
        y = part['y'] * CELL_SIZE
        pygame.draw.rect(DISPLAY, GREEN, (x, y, CELL_SIZE, CELL_SIZE))

def run_game():
    global snake, SCORE

    SCORE = 0
    # get starting location
    start_x = randint(3, GAME_WIDTH - 4)
    start_y = randint(3, GAME_HEIGHT - 4)
    snake = [   {'x': start_x, 'y': start_y},
                {'x': start_x - 1, 'y': start_y},
                {'x' : start_x - 2, 'y': start_y}]
    # starting direction
    direction = RIGHT
    new_dir = RIGHT

    # get random location for food
    start_x = randint(0, GAME_WIDTH - 1)
    start_y = randint(0, GAME_HEIGHT - 1)
    food = {'x': start_x, 'y': start_y}

    # MAIN GAME LOOP
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # update snake direction
            # uses a new_dir in order to not be able to go backwards
            # if keys are pressed fast enough in succession
            elif event.type == KEYDOWN:
                if event.key in UP_KEYS and direction != DOWN:
                    new_dir = UP
                elif event.key in LEFT_KEYS and direction != RIGHT:
                    new_dir = LEFT
                elif event.key in DOWN_KEYS and direction != UP:
                    new_dir = DOWN
                elif event.key in RIGHT_KEYS and direction != LEFT:
                    new_dir = RIGHT
                elif event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        direction = new_dir

        if (snake_collided()):
            print("game over")
            return

        # if food is eaten, generate a new location
        if snake[0]['x'] == food['x'] and snake[0]['y'] == food['y']:
            food = {'x': randint(0, GAME_WIDTH - 1), 'y': randint(0, GAME_HEIGHT - 1)}
            SCORE += 1
        # else, remove tail
        else:
            snake.pop()

        # create new head in direction
        if direction == UP:
            snake.insert(0, {'x': snake[0]['x'], 'y': snake[0]['y'] - 1})
        elif direction == LEFT:
            snake.insert(0, {'x': snake[0]['x'] - 1, 'y': snake[0]['y']})
        elif direction == DOWN:
            snake.insert(0, {'x': snake[0]['x'], 'y': snake[0]['y'] + 1})
        elif direction == RIGHT:
            snake.insert(0, {'x': snake[0]['x'] + 1, 'y': snake[0]['y']})

        DISPLAY.fill(BLACK)
        # draw the food
        pygame.draw.rect(DISPLAY, RED, (food['x'] * CELL_SIZE, food['y'] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        draw_snake()

        pygame.display.update()
        # limit the game speed to FPS
        CLOCK.tick(FPS)

def show_start_screen():
    DISPLAY.fill(BLACK)
    text = FONT.render("Press any key to begin", True, WHITE)
    DISPLAY.blit(text, (WINDOW_WIDTH // 2 - text.get_width() // 2, WINDOW_HEIGHT // 2))
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                return

def show_game_over():
    DISPLAY.fill(BLACK)
    text = FONT.render("GAME OVER!", True, WHITE)
    DISPLAY.blit(text, (WINDOW_WIDTH // 2 - text.get_width() // 2, WINDOW_HEIGHT // 3))
    text = FONT.render("SCORE: " + str(SCORE), True, WHITE)
    DISPLAY.blit(text, (WINDOW_WIDTH // 2 - text.get_width() // 2, WINDOW_HEIGHT // 3 + text.get_height()))
    text = FONT.render("Press any key to restart", True, WHITE)
    DISPLAY.blit(text, (WINDOW_WIDTH // 2 - text.get_width() // 2, WINDOW_HEIGHT // 3 + 2 * text.get_height()))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                return
    

def main():
    global DISPLAY, CLOCK, FONT, SCORE

    pygame.init()
    DISPLAY = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    FONT = pygame.font.Font(None, 24)
    SCORE = 0
    pygame.display.set_caption('Snake')

    show_start_screen()
    while True:
        run_game()
        show_game_over()

if __name__ == '__main__':
    main()
