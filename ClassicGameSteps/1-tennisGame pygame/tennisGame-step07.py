import pygame

pygame.init()

# Set window dimensions
window_width = 800
window_height = 600
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Bouncing Ball")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Ball variables
ball_x = 75
ball_y = 75
ball_speed_x = 6  # Initial speed is positive (moving right)

# Game clock for controlling frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the ball
    if ball_x > window_width:  # Check if ball hits right edge
        ball_speed_x = -abs(ball_speed_x)  # Reverse direction and keep the speed positive

    ball_x += ball_speed_x  

    # Drawing
    screen.fill(black)  # Clear screen
    pygame.draw.circle(screen, white, (ball_x, ball_y), 10)  # Draw ball

    # Update the display
    pygame.display.flip()
    clock.tick(30)  # 30 FPS

pygame.quit()
