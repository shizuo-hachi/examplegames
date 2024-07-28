import pygame

# Initialize Pygame
pygame.init()

# Set window dimensions (same as canvas)
window_width = 800
window_height = 600
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Bouncing Ball")

# Ball variables
ball_x = window_width // 2 # Start at center of screen
ball_y = window_height // 2 # Start at center of screen
ball_speed_x = 6
ball_speed_y = 8

# Paddle variables
paddle1_y = 250
paddle_height = 100
paddle_width = 10

# Game clock for controlling frame rate
clock = pygame.time.Clock()
frames_per_second = 30

# Helper functions for drawing
def color_rect(x, y, width, height, color):
    pygame.draw.rect(screen, color, (x, y, width, height))

def color_circle(x, y, radius, color):
    pygame.draw.circle(screen, color, (x, y), radius)

# Function to reset the ball
def ball_reset():
    return window_width // 2, window_height // 2

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle mouse movement for paddle control
    mouse_pos = pygame.mouse.get_pos()
    paddle1_y = mouse_pos[1] - paddle_height // 2

    # Move the ball
    if ball_x < 0:  # if ball goes off left edge
        if paddle1_y < ball_y < paddle1_y + paddle_height:
            ball_speed_x *= -1  # bounce off the paddle
        else:
            ball_x, ball_y = ball_reset()  # reset ball to center
    if ball_x > window_width:  # if ball goes off right edge
        ball_speed_x *= -1
    if ball_y < 0 or ball_y > window_height:
        ball_speed_y *= -1

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Drawing
    color_rect(0, 0, window_width, window_height, (0, 0, 0))  # Clear the screen

    # Draw left paddle
    color_rect(0, paddle1_y, paddle_width, paddle_height, (255, 255, 255))

    # Draw ball
    color_circle(ball_x, ball_y, 10, (255, 255, 255))

    # Update the display
    pygame.display.flip()

    # Control frame rate
    clock.tick(frames_per_second)

# Quit Pygame
pygame.quit()
