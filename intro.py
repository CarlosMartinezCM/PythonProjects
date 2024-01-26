# This app will list text from the bottom of the page up
# and try to imitate the Stars Wars intro story line
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1200, 800
FPS = 150
FONT_SIZE = 20
FONT_COLOR = (0, 255, 0)
NUM_COLUMNS = 20  # Adjust the number of columns as needed

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("reader")
clock = pygame.time.Clock()

# Create a font
font = pygame.font.Font(None, FONT_SIZE)

# Set the text lines with random asterisks
text_lines = [
    "*" * random.randint(1, 10),
    "*" * random.randint(1, 10),
    "*" * random.randint(1, 10),
    "*" * random.randint(1, 10),
    "*" * random.randint(1, 10),
  
    
]

# Create a list to store falling text
falling_text = []

# Initialize falling text elements
for line_index, line in enumerate(text_lines):
    falling_text.append({
        "text": line,
        "x": random.randint(0, WIDTH - FONT_SIZE),
        "y": HEIGHT + line_index * FONT_SIZE,
        "speed_x": random.uniform(-1, 1),
        "speed_y": random.uniform(-2, -1)
    })

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update falling text positions
    for text in falling_text:
        text["y"] += text["speed_y"]
        if text["y"] < -FONT_SIZE:
            text["y"] = HEIGHT + len(text_lines) * FONT_SIZE

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw falling text
    for text in falling_text:
        rendered_text = font.render(text["text"], True, FONT_COLOR)
        screen.blit(rendered_text, (int(text["x"]), int(text["y"])))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
