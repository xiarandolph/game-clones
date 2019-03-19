import pygame, sys
from pygame.locals import *

# CONSTANTS
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

# Main game loop
pygame.init();
DISPLAY = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT));
pygame.display.set_caption("Snake")
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAY.fill(BLACK)
    x = (GAME_WIDTH // 2) * CELL_SIZE;
    y = (GAME_HEIGHT // 2) * CELL_SIZE;
    pygame.draw.rect(DISPLAY, GREEN, (x, y, CELL_SIZE, CELL_SIZE))
    pygame.display.update()
