import pygame

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
PADDLE_HEIGHT = 100
PADDLE_THICKNESS = 10
BALL_RADIUS = 10
FPS = 30
PADDLE_COMPUTER_MOVE_SPEED = 7.0

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Pygame Setup
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

# Font for displaying score
font = pygame.font.Font(None, 36)

# Game Objects
ball = pygame.Rect(WINDOW_WIDTH // 2 - BALL_RADIUS, WINDOW_HEIGHT // 2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_speed_x = 6
ball_speed_y = 8

paddle1 = pygame.Rect(0, 250, PADDLE_THICKNESS, PADDLE_HEIGHT)
paddle2 = pygame.Rect(WINDOW_WIDTH - PADDLE_THICKNESS, 250, PADDLE_THICKNESS, PADDLE_HEIGHT)

# Score variables
paddle1_score = 0
paddle2_score = 0

# Game Functions
def ball_reset():
    global ball_speed_x
    ball.x = WINDOW_WIDTH // 2 - BALL_RADIUS
    ball.y = WINDOW_HEIGHT // 2 - BALL_RADIUS
    ball_speed_x *= -1

def move_computer_paddle():
    paddle2_center = paddle2.y + PADDLE_HEIGHT / 2
    if ball.y < paddle2_center:
        paddle2.y -= PADDLE_COMPUTER_MOVE_SPEED
    elif ball.y > paddle2_center:
        paddle2.y += PADDLE_COMPUTER_MOVE_SPEED
    paddle2.y = max(0, min(paddle2.y, WINDOW_HEIGHT - PADDLE_HEIGHT))

def move_everything():
    global ball_speed_x, ball_speed_y, paddle1_score, paddle2_score
    move_computer_paddle()
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with top/bottom walls
    if ball.top <= 0 or ball.bottom >= WINDOW_HEIGHT:
        ball_speed_y *= -1

    # Ball collision with paddles with angle adjustment
    for paddle in [paddle1, paddle2]:
        if ball.colliderect(paddle):
            ball_speed_x *= -1
            delta_y = ball.centery - paddle.centery
            ball_speed_y = delta_y * 0.35

    # Score logic
    if ball.left < 0:
        paddle2_score += 1
        ball_reset()
    if ball.right > WINDOW_WIDTH:
        paddle1_score += 1
        ball_reset()

    # Move paddle1 (left) with mouse
    mouse_pos = pygame.mouse.get_pos()
    paddle1.centery = mouse_pos[1]
    paddle1.y = max(0, min(paddle1.y, WINDOW_HEIGHT - PADDLE_HEIGHT))

def color_rect(x, y, width, height, color):
    pygame.draw.rect(screen, color, (x, y, width, height))

def color_circle(x, y, radius, color):
    pygame.draw.circle(screen, color, (x, y), radius)

def draw_everything():
    screen.fill(BLACK)  # Clear the screen

    # Draw paddles and ball
    color_rect(paddle1.x, paddle1.y, PADDLE_THICKNESS, PADDLE_HEIGHT, WHITE)
    color_rect(paddle2.x, paddle2.y, PADDLE_THICKNESS, PADDLE_HEIGHT, WHITE)
    color_circle(ball.x + BALL_RADIUS, ball.y + BALL_RADIUS, BALL_RADIUS, WHITE)

    # Display scores
    score1_text = font.render(str(paddle1_score), True, WHITE)
    score2_text = font.render(str(paddle2_score), True, WHITE)
    screen.blit(score1_text, (100, 100))
    screen.blit(score2_text, (WINDOW_WIDTH - 100, 100))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    move_everything()
    draw_everything()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
