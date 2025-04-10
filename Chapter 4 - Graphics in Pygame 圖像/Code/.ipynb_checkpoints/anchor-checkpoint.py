import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Anchor Points at Cursor")

# Set up font
font = pygame.font.Font(None, 36)

# Define anchor points
anchor_points = [
    (0, 0),   # Top Left
    (0.5, 0), # Top Center
    (1, 0),   # Top Right
    (0, 0.5), # Middle Left
    (0.5, 0.5), # Center
    (1, 0.5), # Middle Right
    (0, 1),   # Bottom Left
    (0.5, 1), # Bottom Center
    (1, 1)    # Bottom Right
]

# Initial anchor point index
anchor_index = 4  # Center anchor point

# Rectangle properties
rect_width, rect_height = 100, 50
rect_color = (255, 0, 0)

# Anchor point names
anchor_names = [
    "topleft", "midtop", "topright",
    "midleft", "center", "midright",
    "bottomleft", "midbottom", "boittomright"
]

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key >= pygame.K_1 and event.key <= pygame.K_9:
                anchor_index = event.key - pygame.K_1  # Set anchor point based on key press

    # Get the current mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Calculate rectangle position based on anchor point
    anchor_x, anchor_y = anchor_points[anchor_index]
    rect_x = mouse_x - (rect_width * anchor_x)
    rect_y = mouse_y - (rect_height * anchor_y)

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw the rectangle
    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, rect_height))

    # Render the anchor point information
    anchor_text = f"Anchor: {anchor_names[anchor_index]} | Coordinates: ({mouse_x}, {mouse_y})"
    text = font.render(anchor_text, True, (255, 255, 255))
    screen.blit(text, (20, 20))

    # Update the display
    pygame.display.flip()