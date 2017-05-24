import sys
import random
import pygame
from colours import DARK_BLUE, GREEN, BLACK


def evolve():
    """
    Update the cells on each cycle
    """
    global cells

    # Create a fresh copy of the global `cells` dict
    new_cells = cells.copy()

    # For each coordinate and health status in `cells`
    for position, alive in cells.items():
        # Get the total number of live neighbours
        live_neighbours = sum(get_neighbours(position))
        # If the cell is alive
        if alive:
            # And if the number of `live_neighbours` is neither
            # 2 nor 3 then the cell dies and is added to the dict of
            # `new_cells`
            if live_neighbours not in [2, 3]:
                new_cells[position] = False
        # Else if the number of `live_neighbours` is 3
        # then the cell is alive and gets added to the
        # `new_cells` dict
        elif live_neighbours == 3:
            new_cells[position] = True
    cells = new_cells


def get_neighbours(coords):
    """
    Get the neighbours of a cell
    """
    x = coords[0]
    y = coords[1]
    positions = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x + 1, y),
                 (x + 1, y + 1), (x, y + 1), (x - 1, y + 1), (x - 1, y)]
    return [cells[c, r] for (c, r) in positions if 0 <= c < COLUMNS and 0 <= r < ROWS]


def get_cells(density=0.2):
    """
    Get the coords and state (dead or alive) for each of the cells
    """
    return {(c, r): random.random() < density for c in range(COLUMNS) for r in range(ROWS)}


def draw_cells():
    """
    Get the x and y coordinates of each cell, check to see
    if it's dead or alive and choose the appropriate colour (green for alive and
    black for dead). And then draw them to the grid
    """
    for (x, y) in cells:
        colour = GREEN if cells[x, y] else BLACK
        rectangle = (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(SCREEN, colour, rectangle)


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

# Set our cells
cells = get_cells()

CLOCK = pygame.time.Clock()

# Start our game loop
while True:
    CLOCK.tick(2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    draw_cells()
    evolve()
    draw_grid()

    pygame.display.update()
