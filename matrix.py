# Implementation of the matrix screen, 1s and 0s

import pygame
import sys
import random

# Initialize the game/Board
pygame.init()

# Declare the constants
WIDTH, HEIGHT = 1200, 800  # Size of the window box
FPS = 250  # Frame speed
FONT_SIZE = 20
FONT_COLOR = (0, 255, 0)
NUM_COLUMNS = 30  # Adjust the number of columns as needed

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Matrix")
clock = pygame.time.Clock()

# Create the font 
font = pygame.font.SysFont("none", FONT_SIZE)

# Generate random binary values (1 or 0)
binary_values = [random.choice(["0", "1"]) for _ in range( NUM_COLUMNS * WIDTH // FONT_SIZE)]

# Create a list to store falling text, if I add an a + "1" after binary is declared, it will add a 1 next the values. 
falling_text = [{"text": binary, "x": i % (WIDTH // FONT_SIZE) * FONT_SIZE, "y": -FONT_SIZE,
                 "speed_x": random.uniform(-1, 1), "speed_y": random.uniform(1, 3)} for i, binary in enumerate(binary_values)]

# Main program loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

   # Update falling text positions
    for text in falling_text:
        text["y"] += text["speed_y"]
        if text["y"] > HEIGHT:
            text["y"] = -FONT_SIZE
            
    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw falling numbers
    for text in falling_text:
        rendered_text = font.render(text["text"], True, FONT_COLOR)
        screen.blit(rendered_text, (int(text["x"]), int(text["y"])))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
