import pygame


class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.snake = [(400, 300)]
        self.direction = pygame.K_RIGHT

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
        self.snake = [(head_x, head_y)] + self.snake[:-1]

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
