import pygame

pygame.init()

# Set window dimensions
window_width = 800
window_height = 600
screen = pygame.display.set_mode((window_width, window_height))

# Set title
pygame.display.set_caption("Tennis Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

def draw_everything():
    # Clear screen
    screen.fill(black)

    # Draw white circle
    pygame.draw.circle(screen, white, (75, 75), 10)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_everything()
    pygame.display.flip()  # Update the full display Surface to the screen

pygame.quit()
