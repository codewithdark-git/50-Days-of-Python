import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 150, 10
PADDLE_SPEED = 10
BALL_RADIUS = 10
BALL_SPEED = 5
BRICK_WIDTH, BRICK_HEIGHT = 80, 20
BRICK_ROWS, BRICK_COLUMNS = 4, 10

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout")

# Create fonts for text
font = pygame.font.Font(None, 36)

# Initialize game state
game_over = False
playing_game = False

# Create the paddle
paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT)

# Create the ball
ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS, HEIGHT // 2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_speed = [BALL_SPEED, -BALL_SPEED]

# Create bricks
bricks = []
for row in range(BRICK_ROWS):
    for col in range(BRICK_COLUMNS):
        brick = pygame.Rect(col * BRICK_WIDTH, row * BRICK_HEIGHT, BRICK_WIDTH, BRICK_HEIGHT)
        bricks.append(brick)

# Create a start screen
def draw_start_screen():
    screen.fill(WHITE)
    text = font.render("Press Enter to Start", True, BLUE)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.update()

# Create a game over screen
def draw_game_over_screen():
    screen.fill(WHITE)
    text = font.render("Game Over - Press Enter to Try Again", True, RED)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.update()

# Game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            if game_over:
                # Restart the game
                bricks = [brick for brick in bricks]
                ball_speed = [BALL_SPEED, -BALL_SPEED]
                game_over = False
            playing_game = not playing_game

    if not playing_game:
        if game_over:
            draw_game_over_screen()
        else:
            draw_start_screen()
    else:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle.left > 0:
            paddle.x -= PADDLE_SPEED
        if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
            paddle.x += PADDLE_SPEED

        ball.x += ball_speed[0]
        ball.y += ball_speed[1]

        if ball.left <= 0 or ball.right >= WIDTH:
            ball_speed[0] = -ball_speed[0]
        if ball.top <= 0:
            ball_speed[1] = -ball_speed[1]

        if ball.colliderect(paddle) and ball_speed[1] > 0:
            ball_speed[1] = -ball_speed[1]

        bricks_to_remove = []
        for brick in bricks:
            if ball.colliderect(brick):
                ball_speed[1] = -ball_speed[1]
                bricks_to_remove.append(brick)

        for brick in bricks_to_remove:
            bricks.remove(brick)

        if ball.top >= HEIGHT:
            # Game over
            game_over = True

        if len(bricks) == 0:
            # You win!
            game_over = True

        screen.fill(WHITE)
        pygame.draw.rect(screen, BLUE, paddle)
        pygame.draw.ellipse(screen, RED, ball)
        for brick in bricks:
            pygame.draw.rect(screen, BLUE, brick)

    pygame.display.update()
    clock.tick(60)
