import pygame

# Initialize Pygame
pygame.init()

# Set window dimensions (same as canvas)
window_width = 800
window_height = 600
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Bouncing Ball")

# Ball variables
ball_x = 75
ball_y = 75
ball_speed_x = 6
ball_speed_y = 8

# Game clock for controlling frame rate
clock = pygame.time.Clock()
frames_per_second = 30

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the ball
    if ball_x < 0 or ball_x > window_width:
        ball_speed_x *= -1
    if ball_y < 0 or ball_y > window_height:
        ball_speed_y *= -1

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Drawing
    screen.fill((0, 0, 0))  # Clear the screen (black)

    # Draw left paddle
    paddle_rect = pygame.Rect(0, 250, 10, 100)
    pygame.draw.rect(screen, (255, 255, 255), paddle_rect) 

    # Draw ball
    pygame.draw.circle(screen, (255, 255, 255), (ball_x, ball_y), 10)

    # Update the display
    pygame.display.flip()

    # Control frame rate
    clock.tick(frames_per_second)

# Quit Pygame
pygame.quit()
