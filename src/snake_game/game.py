import random
import pygame


class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 35)
        self.running = False
        self.reset_game()

    def reset_game(self):
        self.snake = [(400, 300)]
        self.direction = pygame.K_RIGHT
        self.food = self.spawn_food()
        self.score = 0
        self.game_over = False

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
            self.score += 1
        else:
            self.snake.pop()

        self.snake = [new_head] + self.snake

        if head_x < 0 or head_x >= 800 or head_y < 0 or head_y >= 600 \
           or new_head in self.snake[1:]:
            self.game_over = True

    def run(self):
        self.running = True
        while self.running:
            self.handle_input()
            if not self.game_over:
                self.update()
            self.render()
            self.clock.tick(15)

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if not self.game_over:
                    self.direction = event.key
                elif event.key == pygame.K_r:   # Restart game
                    self.reset_game()

    def render(self):
        self.screen.fill((0, 0, 0))
        for segment in self.snake:
            pygame.draw.rect(self.screen, (0, 255, 0), (*segment, 10, 10))
        pygame.draw.rect(self.screen, (255, 0, 0), (*self.food, 10, 10))
        self.display_score()
        if self.game_over:
            self.display_game_over()
        pygame.display.flip()

    def display_score(self):
        text = self.font.render(f'Score: {self.score}', True, (255, 255, 255))
        self.screen.blit(text, (10, 10))

    def display_game_over(self):
        game_over_text = self.font.render('Game Over! Press R to Restart', True, (255, 255, 255))
        score_text = self.font.render(f'Score: {self.score}', True, (255, 255, 255))
        self.screen.blit(game_over_text, [(self.screen.get_width() - game_over_text.get_width()) // 2, self.screen.get_height() // 2 - 30])
        self.screen.blit(score_text, [(self.screen.get_width() - score_text.get_width()) // 2, self.screen.get_height() // 2 + 10])
