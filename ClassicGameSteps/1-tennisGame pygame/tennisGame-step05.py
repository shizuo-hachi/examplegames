import pygame

pygame.init()

# Set window dimensions
window_width = 800
window_height = 600
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Moving Ball")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Ball variables
ball_x = 75
ball_y = 75
ball_speed_x = 2  # Pixels to move per frame

# Game clock
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the ball
    ball_x += ball_speed_x
    if ball_x > window_width:
        ball_x = 0  # Reset position if it goes off screen

    # Drawing
    screen.fill(black)  # Clear screen
    pygame.draw.circle(screen, white, (ball_x, ball_y), 10)  # Draw ball

    # Update the display
    pygame.display.flip()
    clock.tick(30)  # 30 FPS

pygame.quit()
