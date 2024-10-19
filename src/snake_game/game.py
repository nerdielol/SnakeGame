import pygame
import random
from dataclasses import dataclass, field
from typing import List, Tuple, Optional

# Constants
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

@dataclass
class Player:
    start_pos: Tuple[int, int]
    direction: Tuple[int, int] = field(default_factory=lambda: random.choice([UP, DOWN, LEFT, RIGHT]))
    positions: List[Tuple[int, int]] = field(init=False)
    grow: bool = False
    score: int = 0
    speed_multiplier: int = 1
    speed_boost_counter: int = 0
    move_counter: int = 0
    can_fire_projectile: bool = False

    def __post_init__(self):
        self.positions = [self.start_pos]

    def move(self):
        if self.move_counter >= (10 / self.speed_multiplier):
            head_x, head_y = self.positions[0]
            dir_x, dir_y = self.direction
            new_head = (head_x + dir_x * CELL_SIZE, head_y + dir_y * CELL_SIZE)
            new_head = (new_head[0] % WIDTH, new_head[1] % HEIGHT)

            if self.grow:
                self.positions.insert(0, new_head)
                self.grow = False
            else:
                self.positions = [new_head] + self.positions[:-1]

            if self.speed_boost_counter > 0:
                self.speed_boost_counter -= 1
                if self.speed_boost_counter <= 0:
                    self.speed_multiplier = 1

            self.move_counter = 0
        else:
            self.move_counter += 1

    def change_direction(self, new_direction: Tuple[int, int]):
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.direction = new_direction

    def grow_snake(self):
        self.grow = True
        self.score += 1

    def reset(self):
        self.positions = [self.start_pos]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.grow = False
        self.score = 0
        self.speed_multiplier = 1
        self.speed_boost_counter = 0
        self.move_counter = 0
        self.can_fire_projectile = False

    def activate_speed_boost(self):
        self.speed_multiplier *= 2
        self.speed_boost_counter += 600

    def activate_projectile_ability(self):
        self.can_fire_projectile = True

    def fire_projectile(self) -> Optional['Projectile']:
        if self.can_fire_projectile:
            head_x, head_y = self.positions[0]
            return Projectile((head_x, head_y), self.direction)
        return None

@dataclass
class Item:
    position: Tuple[int, int]
    color: Tuple[int, int] = GREEN

    @staticmethod
    def random_position() -> Tuple[int, int]:
        return (random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
                random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)

    @classmethod
    def create(cls):
        return cls(cls.random_position())

@dataclass
class Projectile:
    position: Tuple[int, int]
    direction: Tuple[int, int]
    active: bool = True

    def move(self):
        if self.active:
            dir_x, dir_y = self.direction
            new_x = self.position[0] + dir_x * CELL_SIZE
            new_y = self.position[1] + dir_y * CELL_SIZE
            self.position = (new_x % WIDTH, new_y % HEIGHT)

    def check_collision(self, player: Player) -> bool:
        if self.position in player.positions:
            self.active = False
            return True
        return False

def game_loop_logic(players: List[Player], items: List[Item], projectiles: List[Projectile], single_player: bool = True):
    for player in players:
        player.move()

        for item in items:
            if player.positions[0] == item.position:
                player.grow_snake()
                items.remove(item)
                items.append(Item.create())

        # Example for player projectile ability activation
        if player.positions[0] in [item.position for item in items if isinstance(item, Item) and item.color == ORANGE]:
            player.activate_projectile_ability()
            items = [item for item in items if not (isinstance(item, Item) and item.color == ORANGE)]

    for projectile in projectiles:
        projectile.move()
        for player in players:
            if projectile.check_collision(player):
                if len(player.positions) > 1:
                    player.positions.pop()
                break

    # Example bot movement logic for a single-player mode
    if single_player:
        bot = players[1]
        item_x, item_y = items[0].position
        bot_head_x, bot_head_y = bot.positions[0]

        if bot_head_x < item_x:
            bot.change_direction(RIGHT)
        elif bot_head_x > item_x:
            bot.change_direction(LEFT)
        elif bot_head_y < item_y:
            bot.change_direction(DOWN)
        elif bot_head_y > item_y:
            bot.change_direction(UP)

# This refactor focuses on moving logic into modular functions and data classes.
# We eliminated Pygame dependency from the logic by isolating `game_loop_logic` and simplifying classes.
# Rendering can be handled separately, allowing `game_loop_logic` to be more easily tested.
