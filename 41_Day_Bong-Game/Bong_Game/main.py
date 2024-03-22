import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1000, 600
BALL_SPEED = 1
BALL_SIZE = 20
PADDLE_SPEED = 1
WHITE = (255,255,225)

# Create the window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")


# Define paddles and ball
paddle_width, paddle_height = 10, 100
paddle_a = pygame.Rect(10, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
paddle_b = pygame.Rect(WIDTH - 10 - paddle_width, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

ball_speed_x = BALL_SPEED * random.choice((1, -1))
ball_speed_y = BALL_SPEED * random.choice((1, -1))
paddle_a_speed = 0
paddle_b_speed = 0

# Score variables
score_a = 0
score_b = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and paddle_b.top > 0:
        paddle_b_speed = -PADDLE_SPEED
    elif keys[pygame.K_DOWN] and paddle_b.bottom < HEIGHT:
        paddle_b_speed = PADDLE_SPEED
    else:
        paddle_b_speed = 0

     # Computer AI for paddle A
    if ball.y < paddle_a.y:
        paddle_a_speed = -PADDLE_SPEED
    elif ball.y > paddle_a.y + paddle_a.height:
        paddle_a_speed = PADDLE_SPEED
    else:
        paddle_a_speed = 0

   

    # Move paddles
    paddle_a.y += paddle_a_speed
    paddle_b.y += paddle_b_speed

    # Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collisions
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    if ball.colliderect(paddle_a) or ball.colliderect(paddle_b):
        ball_speed_x *= -1

    if ball.left <= 0:
        score_b += 1
        ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
        ball_speed_x *= random.choice((1, -1))

    if ball.right >= WIDTH:
        score_a += 1
        ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
        ball_speed_x *= random.choice((1, -1))

    # Draw everything
    window.fill((0, 0, 0))
    pygame.draw.rect(window, WHITE, paddle_a)
    pygame.draw.rect(window, WHITE, paddle_b)
    pygame.draw.ellipse(window, WHITE, ball)
    # pygame.draw.aaline(window, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    score_display = font.render(f"{score_a} - {score_b}", True, WHITE)
    window.blit(score_display, (WIDTH // 2 - score_display.get_width() // 2, 20))

    pygame.display.flip()

pygame.quit()
