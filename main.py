import pygame
from typing import List
from snake_game import Player, Item, Projectile, WIDTH, HEIGHT, BLACK, CELL_SIZE

# Initialize Pygame
pygame.init()

# Setup screen
def initialize_screen():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")
    return screen

# Draw functions
def draw_players(screen, players: List[Player]):
    for player in players:
        for pos in player.positions:
            pygame.draw.rect(screen, (255, 0, 0), (*pos, CELL_SIZE, CELL_SIZE))  # Example for player in red color

def draw_items(screen, items: List[Item]):
    for item in items:
        pygame.draw.rect(screen, item.color, (*item.position, CELL_SIZE, CELL_SIZE))

def draw_projectiles(screen, projectiles: List[Projectile]):
    for projectile in projectiles:
        if projectile.active:
            pygame.draw.rect(screen, (255, 255, 255), (*projectile.position, CELL_SIZE, CELL_SIZE))  # Projectiles in white

# Main Pygame loop
def main_game_loop(players: List[Player], items: List[Item], projectiles: List[Projectile]):
    screen = initialize_screen()
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    players[0].change_direction((0, -1))
                elif event.key == pygame.K_s:
                    players[0].change_direction((0, 1))
                elif event.key == pygame.K_a:
                    players[0].change_direction((-1, 0))
                elif event.key == pygame.K_d:
                    players[0].change_direction((1, 0))
                elif event.key == pygame.K_SPACE:
                    projectile = players[0].fire_projectile()
                    if projectile:
                        projectiles.append(projectile)

        # Update game logic (calls function from logic module)
        from snake_game import game_loop_logic
        game_loop_logic(players, items, projectiles)

        # Draw everything
        draw_players(screen, players)
        draw_items(screen, items)
        draw_projectiles(screen, projectiles)

        # Update display
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

# Entry point for running the game
if __name__ == "__main__":
    # Initialize game elements
    player1 = Player(start_pos=(100, 100))
    player2 = Player(start_pos=(200, 200))
    players = [player1, player2]
    items = [Item.create() for _ in range(5)]
    projectiles = []

    # Start game loop
    main_game_loop(players, items, projectiles)
