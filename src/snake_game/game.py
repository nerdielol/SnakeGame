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
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Player:
    def __init__(self, color, start_pos):
        self.color = color
        self.positions = [start_pos]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.grow = False

    def move(self):
        head_x, head_y = self.positions[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x * CELL_SIZE, head_y + dir_y * CELL_SIZE)
        
        if self.grow:
            self.positions.insert(0, new_head)
            self.grow = False
        else:
            self.positions = [new_head] + self.positions[:-1]

    def change_direction(self, new_direction):
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.direction = new_direction

    def draw(self, screen):
        for pos in self.positions:
            pygame.draw.rect(screen, self.color, (*pos, CELL_SIZE, CELL_SIZE))

    def check_collision(self, other):
        return self.positions[0] in other.positions

# Initialize players
players = [
    Player(RED, (100, 100)),
    Player(BLUE, (200, 200))
]

# Game loop
running = True
clock = pygame.time.Clock()

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
            elif event.key == pygame.K_UP:
                players[1].change_direction(UP)
            elif event.key == pygame.K_DOWN:
                players[1].change_direction(DOWN)
            elif event.key == pygame.K_LEFT:
                players[1].change_direction(LEFT)
            elif event.key == pygame.K_RIGHT:
                players[1].change_direction(RIGHT)

    for player in players:
        player.move()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(BLACK)

    for player in players:
        player.draw(screen)

    pygame.display.flip()
    clock.tick(10)

pygame.quit()