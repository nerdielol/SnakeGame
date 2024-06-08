import random
import pygame


class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.snake = [(400, 300)]
        self.direction = pygame.K_RIGHT
        self.running = False
        self.food = self.spawn_food()

    def spawn_food(self):
        return (random.randint(0, 79) * 10, random.randint(0, 59) * 10)

    def update(self):
        head_x, head_y = self.snake[0]
        if self.direction == pygame.K_UP:
            head_y -= 10
        elif self.direction == pygame.K_DOWN:
            head_y += 10
        elif self.direction == pygame.K_LEFT:
            head_x -= 10
        elif self.direction == pygame.K_RIGHT:
            head_x += 10

        new_head = (head_x, head_y)
        if new_head == self.food:
            self.food = self.spawn_food()
        else:
            self.snake.pop()

        self.snake = [new_head] + self.snake

        if head_x < 0 or head_x >= 800 or head_y < 0 or head_y >= 600 \
           or new_head in self.snake[1:]:
            self.running = False

    def run(self):
        self.running = True
        while self.running:
            self.handle_input()
            self.update()
            self.clock.tick(15)
            pygame.display.flip()
        pygame.quit()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.direction = event.key
