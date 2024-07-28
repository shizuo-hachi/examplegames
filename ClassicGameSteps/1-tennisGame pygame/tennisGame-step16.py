import pygame

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
PADDLE_HEIGHT = 100
PADDLE_THICKNESS = 10
BALL_RADIUS = 10
FPS = 30

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

# Game objects
ball = pygame.Rect(WINDOW_WIDTH // 2 - BALL_RADIUS, WINDOW_HEIGHT // 2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_speed_x = 6
ball_speed_y = 8

paddle1 = pygame.Rect(0, 250, PADDLE_THICKNESS, PADDLE_HEIGHT)
paddle2 = pygame.Rect(WINDOW_WIDTH - PADDLE_THICKNESS, 250, PADDLE_THICKNESS, PADDLE_HEIGHT)

# Game functions
def ball_reset():
    global ball_speed_x
    ball.x = WINDOW_WIDTH // 2 - BALL_RADIUS
    ball.y = WINDOW_HEIGHT // 2 - BALL_RADIUS
    ball_speed_x *= -1

def move_everything():
    global ball_speed_x, ball_speed_y

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with top/bottom walls
    if ball.top <= 0 or ball.bottom >= WINDOW_HEIGHT:
        ball_speed_y *= -1

    # Ball collision with left paddle
    if ball.left <= 0 and ball.colliderect(paddle1):
        ball_speed_x *= -1

    # Ball collision with right paddle
    if ball.right >= WINDOW_WIDTH and ball.colliderect(paddle2):
        ball_speed_x *= -1

    # Ball goes offscreen
    if ball.left < 0 or ball.right > WINDOW_WIDTH:
        ball_reset()

    # Move paddle2 with mouse
    mouse_pos = pygame.mouse.get_pos()
    paddle2.centery = mouse_pos[1]

def color_rect(x, y, width, height, color):
    pygame.draw.rect(screen, color, (x, y, width, height))

def color_circle(x, y, radius, color):
    pygame.draw.circle(screen, color, (x, y), radius)

def draw_everything():
    # Clear the screen
    color_rect(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT, BLACK)

    # Draw paddles and ball
    color_rect(0, paddle1.y, PADDLE_THICKNESS, PADDLE_HEIGHT, WHITE)
    color_rect(paddle2.x, paddle2.y, PADDLE_THICKNESS, PADDLE_HEIGHT, WHITE)
    color_circle(ball.x + BALL_RADIUS, ball.y + BALL_RADIUS, BALL_RADIUS, WHITE)

# Game loop
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
