import pygame

pygame.init()

# Set window dimensions
window_width = 800
window_height = 600
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Pong")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Game variables
ball_x = 75
ball_y = 75
ball_speed_x = 6
ball_speed_y = 8
paddle1_y = 250
paddle2_y = 250
paddle1_score = 0
paddle2_score = 0
showing_win_screen = False

PADDLE_HEIGHT = 100
PADDLE_THICKNESS = 10
WINNING_SCORE = 3
PADDLE_COMPUTER_MOVE_SPEED = 7.0

font = pygame.font.Font(None, 36)  # Font for text display

# --- Functions ---

def ball_reset():
    global ball_speed_x, ball_x, ball_y, showing_win_screen
    
    if paddle1_score >= WINNING_SCORE or paddle2_score >= WINNING_SCORE:
        showing_win_screen = True
    
    ball_speed_x = -ball_speed_x
    ball_x = window_width // 2
    ball_y = window_height // 2

def move_computer_paddle():
    global paddle2_y
    paddle2_center = paddle2_y + (PADDLE_HEIGHT // 2)
    if ball_y < paddle2_center - 35:
        paddle2_y -= PADDLE_COMPUTER_MOVE_SPEED
    elif ball_y > paddle2_center + 35:
        paddle2_y += PADDLE_COMPUTER_MOVE_SPEED

def move_everything():
    global ball_x, ball_y, ball_speed_x, ball_speed_y, paddle1_score, paddle2_score

    if showing_win_screen:
        return

    move_computer_paddle()

    if ball_x < 0:  # Left edge
        if paddle1_y < ball_y < paddle1_y + PADDLE_HEIGHT:
            ball_speed_x *= -1
            delta_y = ball_y - (paddle1_y + PADDLE_HEIGHT // 2)
            ball_speed_y = delta_y * 0.35
        else:
            paddle2_score += 1
            ball_reset()
    
    if ball_x > window_width:  # Right edge
        if paddle2_y < ball_y < paddle2_y + PADDLE_HEIGHT:
            ball_speed_x *= -1
            delta_y = ball_y - (paddle2_y + PADDLE_HEIGHT // 2)
            ball_speed_y = delta_y * 0.35
        else:
            paddle1_score += 1
            ball_reset()
    
    if ball_y < 0 or ball_y > window_height:  # Top/bottom edges
        ball_speed_y *= -1
    
    ball_x += ball_speed_x
    ball_y += ball_speed_y

def draw_everything():
    screen.fill(black)

    if showing_win_screen:
        if paddle1_score >= WINNING_SCORE:
            text = font.render("LEFT PLAYER WINS!", True, white)
        else:
            text = font.render("RIGHT PLAYER WINS!", True, white)
        text_rect = text.get_rect(center=(window_width // 2, window_height // 2))
        screen.blit(text, text_rect)

        text = font.render("-- click to start new game --", True, white)  # Fixed typo here
        text_rect = text.get_rect(center=(window_width // 2, window_height - 20))
        screen.blit(text, text_rect)
    else:
        pygame.draw.rect(screen, white, (0, paddle1_y, PADDLE_THICKNESS, PADDLE_HEIGHT))
        pygame.draw.rect(screen, white, (window_width - PADDLE_THICKNESS, paddle2_y, PADDLE_THICKNESS, PADDLE_HEIGHT))
        pygame.draw.circle(screen, white, (ball_x, ball_y), 10)

    score_text = font.render(f"{paddle1_score}    {paddle2_score}", True, white)
    screen.blit(score_text, (window_width // 2 - score_text.get_width() // 2, 100))

# Main game loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and showing_win_screen:
            paddle1_score = 0
            paddle2_score = 0
            showing_win_screen = False
            ball_reset()

    if not showing_win_screen:
        paddle1_y = pygame.mouse.get_pos()[1] - PADDLE_HEIGHT // 2

    move_everything()
    draw_everything()
    pygame.display.flip()
    clock.tick(30)  # 30 FPS

pygame.quit()
