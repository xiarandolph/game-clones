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

def main():
    global DISPLAY, CLOCK

    pygame.init();
    DISPLAY = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT));
    CLOCK = pygame.time.Clock()
    pygame.display.set_caption('Snake')

    while True:
        run_game()

def run_game():
    # get starting location
    start_x = randint(3, GAME_WIDTH - 4)
    start_y = randint(3, GAME_HEIGHT - 4)
    snake = [   {'x': start_x, 'y': start_y},
                {'x': start_x - 1, 'y': start_y},
                {'x' : start_x - 2, 'y': start_y}]
    # starting direction
    dir = RIGHT
    new_dir = RIGHT

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
                if event.key in UP_KEYS and dir != DOWN:
                    new_dir = UP
                elif event.key in LEFT_KEYS and dir != RIGHT:
                    new_dir = LEFT
                elif event.key in DOWN_KEYS and dir != UP:
                    new_dir = DOWN
                elif event.key in RIGHT_KEYS and dir != LEFT:
                    new_dir = RIGHT
                elif event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        dir = new_dir

        # check for colliding with end of map
        if snake[0]['x'] in [-1, GAME_WIDTH] or snake[0]['y'] in [-1, GAME_HEIGHT]:
            print("game over")
            return
        # check for collisions with itself
        for part in snake[1:]:
            if part['x'] == snake[0]['x'] and part['y'] == snake[0]['y']:
                print("game over")
                return

        # delete tail if no food eaten
        if True:
            snake.pop()

        # create new head in direction
        if dir == UP:
            snake.insert(0, {'x': snake[0]['x'], 'y': snake[0]['y'] - 1})
        elif dir == LEFT:
            snake.insert(0, {'x': snake[0]['x'] - 1, 'y': snake[0]['y']})
        elif dir == DOWN:
            snake.insert(0, {'x': snake[0]['x'], 'y': snake[0]['y'] + 1})
        elif dir == RIGHT:
            snake.insert(0, {'x': snake[0]['x'] + 1, 'y': snake[0]['y']})

        DISPLAY.fill(BLACK)
        # draw snake
        for part in snake:
            x = part['x'] * CELL_SIZE
            y = part['y'] * CELL_SIZE
            pygame.draw.rect(DISPLAY, GREEN, (x, y, CELL_SIZE, CELL_SIZE))

        pygame.display.update()
        # limit the game speed to FPS
        CLOCK.tick(FPS)


if __name__ == '__main__':
    main()
