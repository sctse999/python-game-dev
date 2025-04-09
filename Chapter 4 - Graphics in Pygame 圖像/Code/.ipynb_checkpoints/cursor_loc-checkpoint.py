import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cursor Location Display")

# Set up font
font = pygame.font.Font(None, 36)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the current mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Render the cursor position
    text = font.render(f"Cursor Position: ({mouse_x}, {mouse_y})", True, (255, 255, 255))
    screen.blit(text, (20, 20))

    # Update the display
    pygame.display.flip()