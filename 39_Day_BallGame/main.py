import db
import pygame
import random


# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_SPEED = 50, 10, 2
ENEMY_SIZE = 15
EAT_SIZE = 15
BG_COLOR = (0, 0, 0)
PLAYER_COLOR = (0, 128, 255)
ENEMY_COLOR = (255, 0, 0)
EAT_COLOR1 = (0, 255, 0)
EAT_COLOR2 = (255, 255, 0)
SPEED = 1  # Increased speed

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Unlimited Objects Game")

# Player attributes
player_x = WIDTH // 2
player_y = (HEIGHT - 20) - PLAYER_HEIGHT  # Start the player at the bottom

# Score
score = 0

# Game variables
game_over = False

# Lists to store objects
enemies = []
eats = []

# Define a function to reset the game
def reset_game():
    global player_x, player_y, score, game_over, enemies, eats
    player_x = WIDTH // 2
    player_y = (HEIGHT - 20) - PLAYER_HEIGHT
    score = 0
    game_over = False
    enemies = []
    eats = []

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        # Player controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] and player_x < WIDTH - PLAYER_WIDTH:
            player_x += PLAYER_SPEED

        # Generate new enemies and eats
        if len(enemies) < 3 and random.randint(1, 100) < 5:
            enemies.append([random.randint(0, WIDTH - ENEMY_SIZE), -ENEMY_SIZE])

        if len(eats) < 3 and random.randint(1, 100) < 5:
            eats.append([random.randint(0, WIDTH - EAT_SIZE), -EAT_SIZE])

        # Update enemy and eat positions (move top to bottom)
        for enemy in enemies:
            enemy[1] += SPEED

        for eat in eats:
            eat[1] += SPEED

        # Check for collisions with enemies
        for enemy in enemies:
            if (
                player_x < enemy[0] + ENEMY_SIZE
                and player_x + PLAYER_WIDTH > enemy[0]
                and player_y < enemy[1] + ENEMY_SIZE
                and player_y + PLAYER_HEIGHT > enemy[1]
            ):
                game_over = True

        # Check for collisions with eats
        for eat in eats:
            if (
                player_x < eat[0] + EAT_SIZE
                and player_x + PLAYER_WIDTH > eat[0]
                and player_y < eat[1] + EAT_SIZE
                and player_y + PLAYER_HEIGHT > eat[1]
            ):
                score += 1
                eats.remove(eat)

        # Remove off-screen objects
        enemies = [enemy for enemy in enemies if enemy[1] < HEIGHT]
        eats = [eat for eat in eats if eat[1] < HEIGHT]

    # Draw the background
    screen.fill(BG_COLOR)

    # Draw the player as a rectangle
    pygame.draw.rect(screen, PLAYER_COLOR, (player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT))

    # Draw the enemies as circles
    for enemy in enemies:
        pygame.draw.circle(screen, ENEMY_COLOR, (enemy[0] + ENEMY_SIZE // 2, enemy[1] + ENEMY_SIZE // 2), ENEMY_SIZE // 2)

    # Draw the eats as circles
    for eat in eats:
        pygame.draw.circle(screen, EAT_COLOR1, (eat[0] + EAT_SIZE // 2, eat[1] + EAT_SIZE // 2), EAT_SIZE // 2)

    # Display the score
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Display game over message and "Try Again" button
    if game_over:
        game_over_text = font.render(f"Game Over Score : {str(score)}", True, (255, 255, 255))
        screen.blit(game_over_text, (WIDTH // 2 - 70, HEIGHT // 2 - 18))
        
        try_again_text = font.render("Try Again", True, (255, 255, 255))
        try_again_rect = try_again_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 40))
        screen.blit(try_again_text, try_again_rect)

        # Check if the "Try Again" button is clicked
        mouse_pos = pygame.mouse.get_pos()
        if try_again_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:  # Left mouse button
                reset_game()

    pygame.display.update()

# Quit the game
pygame.quit()
