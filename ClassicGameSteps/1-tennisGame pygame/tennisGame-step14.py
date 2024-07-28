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
    ball.x = WINDOW_WIDTH // 2 - BALL_RADIUS
    ball.y = WINDOW_HEIGHT // 2 - BALL_RADIUS

def move_ball():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Collision detection
    if ball.top <= 0 or ball.bottom >= WINDOW_HEIGHT:
        ball_speed_y *= -1
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed_x *= -1

def move_paddle(paddle, mouse_pos):
    paddle.centery = mouse_pos[1]

def draw():
    screen.fill(BLACK)  # Clear screen
    pygame.draw.ellipse(screen, WHITE, ball)  # Draw ball
    pygame.draw.rect(screen, WHITE, paddle1)   # Draw paddles
    pygame.draw.rect(screen, WHITE, paddle2)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_pos = pygame.mouse.get_pos()
    move_paddle(paddle1, mouse_pos)  # Move the left paddle with the mouse
    move_ball()

    draw()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
