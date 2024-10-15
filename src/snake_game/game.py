import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Player:
    def __init__(self, texture_path, start_pos):
        self.texture = pygame.image.load(texture_path)
        self.texture = pygame.transform.scale(self.texture, (CELL_SIZE, CELL_SIZE))
        self.start_pos = start_pos
        self.positions = [start_pos]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.grow = False
        self.score = 0
        self.speed_boost = False
        self.speed_boost_counter = 0

    def move(self):
        head_x, head_y = self.positions[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x * CELL_SIZE, head_y + dir_y * CELL_SIZE)

        # Wrap around screen boundaries
        new_head = (new_head[0] % WIDTH, new_head[1] % HEIGHT)
        
        if self.grow:
            self.positions.insert(0, new_head)
            self.grow = False
        else:
            self.positions = [new_head] + self.positions[:-1]

        # Handle speed boost duration
        if self.speed_boost:
            self.speed_boost_counter -= 1
            if self.speed_boost_counter <= 0:
                self.speed_boost = False

    def change_direction(self, new_direction):
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.direction = new_direction

    def draw(self, screen):
        for pos in self.positions:
            screen.blit(self.texture, pos)

    def check_collision(self, other):
        return self.positions[0] in other.positions

    def grow_snake(self):
        self.grow = True
        self.score += 1

    def reset(self):
        self.positions = [self.start_pos]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.grow = False
        self.score = 0
        self.speed_boost = False
        self.speed_boost_counter = 0

    def activate_speed_boost(self):
        self.speed_boost = True
        self.speed_boost_counter = 50  # Speed boost lasts for 50 frames

class Item:
    def __init__(self):
        self.position = (random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
                         random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)
        self.color = GREEN

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (*self.position, CELL_SIZE, CELL_SIZE))

class AdvantageItem:
    def __init__(self):
        self.position = (random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
                         random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)
        self.color = YELLOW

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (*self.position, CELL_SIZE, CELL_SIZE))

# Game loop
running = True
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
mode_selected = False
single_player = False

while running:
    if not mode_selected:
        screen.fill(BLACK)
        font = pygame.font.Font(None, 36)
        text = font.render("Press 1 for Single Player or 2 for Two Players", True, WHITE)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    single_player = True
                    mode_selected = True
                elif event.key == pygame.K_2:
                    single_player = False
                    mode_selected = True
    else:
        # Initialize players and items based on selected mode
        if single_player:
            players = [Player('red_texture.png', (100, 100)), Player('blue_texture.png', (200, 200))]  # Add bot player
        else:
            players = [
                Player('red_texture.png', (100, 100)),
                Player('blue_texture.png', (200, 200))
            ]
        items = [Item()]
        advantage_items = [AdvantageItem()]

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        players[0].change_direction(UP)
                    elif event.key == pygame.K_s:
                        players[0].change_direction(DOWN)
                    elif event.key == pygame.K_a:
                        players[0].change_direction(LEFT)
                    elif event.key == pygame.K_d:
                        players[0].change_direction(RIGHT)
                    if not single_player:
                        if event.key == pygame.K_UP:
                            players[1].change_direction(UP)
                        elif event.key == pygame.K_DOWN:
                            players[1].change_direction(DOWN)
                        elif event.key == pygame.K_LEFT:
                            players[1].change_direction(LEFT)
                        elif event.key == pygame.K_RIGHT:
                            players[1].change_direction(RIGHT)

            for player in players:
                player.move()

                # Check for collisions with items
                for item in items:
                    if player.positions[0] == item.position:
                        player.grow_snake()
                        items.remove(item)
                        items.append(Item())

                # Check for collisions with advantage items
                for advantage_item in advantage_items:
                    if player.positions[0] == advantage_item.position:
                        player.activate_speed_boost()
                        advantage_items.remove(advantage_item)
                        advantage_items.append(AdvantageItem())
                        break  # Ensure only the player who collides gets the boost

            # Check for collisions between players
            if players[0].check_collision(players[1]):
                players[1].reset()
            elif players[1].check_collision(players[0]):
                players[0].reset()

            # Bot player logic (if single player, the second player is a bot)
            if single_player:
                bot = players[1]
                bot_head_x, bot_head_y = bot.positions[0]
                item_x, item_y = items[0].position
                
                # Simple logic for bot to move towards the item
                if bot_head_x < item_x:
                    bot.change_direction(RIGHT)
                elif bot_head_x > item_x:
                    bot.change_direction(LEFT)
                elif bot_head_y < item_y:
                    bot.change_direction(DOWN)
                elif bot_head_y > item_y:
                    bot.change_direction(UP)

            screen.fill(BLACK)

            # Draw players, items, and scores
            for player in players:
                player.draw(screen)

            for item in items:
                item.draw(screen)

            for advantage_item in advantage_items:
                advantage_item.draw(screen)

            # Display scores and speeds
            font = pygame.font.Font(None, 36)
            for i, player in enumerate(players):
                score_text = font.render(f"Player {i + 1} Score: {player.score}", True, WHITE)
                speed_text = font.render(f"Player {i + 1} Speed: {'Fast' if player.speed_boost else 'Normal'}", True, WHITE)
                screen.blit(score_text, (10, 10 + i * 60))
                screen.blit(speed_text, (10, 40 + i * 60))

            pygame.display.flip()
            for player in players:
                if player.speed_boost:
                    clock.tick(40)
                else:
                    clock.tick(20)

pygame.quit()