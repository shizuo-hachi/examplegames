import pygame

pygame.init()

# Set window dimensions
window_width = 800
window_height = 600
screen = pygame.display.set_mode((window_width, window_height))

# Set title
pygame.display.set_caption("Tennis Game")

# Fill background with black
black = (0, 0, 0)
screen.fill(black)

# Update the display to show the filled background
pygame.display.flip()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()
