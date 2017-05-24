import sys
import pygame

# Initialize pygame
pygame.init()

# Set the number of rows and columns
COLUMNS, ROWS = 50, 50

# Set the size of each cell by pixels
CELL_SIZE = 10

# Set the size of the pygame window
SIZE = WIDTH, HEIGHT = COLUMNS * CELL_SIZE, ROWS * CELL_SIZE

# Display the window
SCREEN = pygame.display.set_mode(SIZE)

# Start our game loop
while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
