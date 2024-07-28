import pygame

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
PADDLE_HEIGHT = 100
PADDLE_THICKNESS = 10
BALL_RADIUS = 10
FPS = 30
PADDLE_COMPUTER_MOVE_SPEED = 7.0
AI_SIT_STILL_MARGIN = 35
WINNING_SCORE = 3

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Pygame Setup
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

# Font for displaying text
font = pygame.font.Font(None, 36)

# Game Objects
ball = pygame.Rect(WINDOW_WIDTH // 2 - BALL_RADIUS, WINDOW_HEIGHT // 2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_speed_x = 6
ball_speed_y = 8

paddle1 = pygame.Rect(0, 250, PADDLE_THICKNESS, PADDLE_HEIGHT)
paddle2 = pygame.Rect(WINDOW_WIDTH - PADDLE_THICKNESS, 250, PADDLE_THICKNESS, PADDLE_HEIGHT)

# Game State
paddle1_score = 0
paddle2_score = 0
showing_win_screen = False

# Game Functions
def ball_reset():
    global ball_speed_x, paddle1_score, paddle2_score
    if paddle1_score >= WINNING_SCORE or paddle2_score >= WINNING_SCORE:
        showing_win_screen = True
        return

    ball.x = WINDOW_WIDTH // 2 - BALL_RADIUS
    ball.y = WINDOW_HEIGHT // 2 - BALL_RADIUS
    ball_speed_x *= -1

def handle_mouse_click():
    global showing_win_screen, paddle1_score, paddle2_score
    if showing_win_screen:
        paddle1_score = 0
        paddle2_score = 0
        showing_win_screen = False

# ... (move_computer_paddle and move_everything are the same as before)
def move_computer_paddle():
    paddle2_center = paddle2.y + PADDLE_HEIGHT / 2
    top_chase_line = paddle2_center - AI_SIT_STILL_MARGIN
    bottom_chase_line = paddle2_center + AI_SIT_STILL_MARGIN

    if ball.y < top_chase_line:
        paddle2.y -= PADDLE_COMPUTER_MOVE_SPEED
    elif ball.y > bottom_chase_line:
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


# Drawing Functions

def color_rect(x, y, width, height, color):
    pygame.draw.rect(screen, color, (x, y, width, height))

def color_circle(x, y, radius, color):
    pygame.draw.circle(screen, color, (x, y), radius)

def color_text(text, x, y, color):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)


def draw_everything():
    screen.fill(BLACK)
    if showing_win_screen:
        if paddle1_score >= WINNING_SCORE:
            color_text("LEFT PLAYER WINS!", WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, WHITE)
        else:
            color_text("RIGHT PLAYER WINS!", WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, WHITE)
    else:
        # Draw paddles and ball
        color_rect(paddle1.x, paddle1.y, PADDLE_THICKNESS, PADDLE_HEIGHT, WHITE)
        color_rect(paddle2.x, paddle2.y, PADDLE_THICKNESS, PADDLE_HEIGHT, WHITE)
        color_circle(ball.x + BALL_RADIUS, ball.y + BALL_RADIUS, BALL_RADIUS, WHITE)

    # Display scores
    color_text(str(paddle1_score), 100, 100, WHITE)
    color_text(str(paddle2_score), WINDOW_WIDTH - 100, 100, WHITE)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            handle_mouse_click()

    if not showing_win_screen:  # Only move if not on the win screen
        move_everything()
    draw_everything()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
