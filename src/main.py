# Malachi Eberly
# main.py

from src.cube import Cube

import pygame


# Initialize Pygame
pygame.init()

# Set up the display
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Rubik's Cube")

# Set up the clock (for controlling frame rate)
clock = pygame.time.Clock()

cube = Cube()
color_map = {
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'white': (255, 255, 255),
    'yellow': (255, 255, 0),
    'orange': (255, 165, 0),
    'red': (255, 0, 0)
}

# Function to draw the cube
def draw_cube(window, cube):
    square_size = 50  # Size of each small square
    spacing = 10      # Spacing between squares

    # Example layout
    for i, face in enumerate(cube.cube):
        for j, row in enumerate(face):
            for k, square in enumerate(row):
                color = color_map[cube.colors[square]]
                x = (k * square_size) + (k * spacing) + 100
                y = (j * square_size) + (j * spacing) + (i * 150)
                pygame.draw.rect(window, color, (x, y, square_size, square_size))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    window.fill((0, 0, 0))

    # Draw the cube
    draw_cube(window, cube)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
