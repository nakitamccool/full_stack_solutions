import sys
import pygame
from colours import DARK_BLUE


def draw_grid():
    """
    Draw the main grid which will contain the
    game's cells
    """
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(SCREEN, DARK_BLUE, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(SCREEN, DARK_BLUE, (0, y), (WIDTH, y))

# Initialize pygame
pygame.init()

# Set the number of rows and columns
COLUMNS, ROWS = 100, 50

# Set the size of each cell by pixels
CELL_SIZE = 10

# Set the size of the pygame window
SIZE = WIDTH, HEIGHT = COLUMNS * CELL_SIZE, ROWS * CELL_SIZE

# Display the window
SCREEN = pygame.display.set_mode(SIZE)

# Start our game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    draw_grid()
    pygame.display.update()
