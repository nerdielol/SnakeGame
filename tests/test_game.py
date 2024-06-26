import pygame
from snake_game import Game


def test_initial_window_size():
    game = Game()
    window_size = game.screen.get_size()

    assert window_size == (800, 600)


def test_initialize_clock():
    game = Game()

    assert game.clock is not None


def test_initial_snake_position():
    game = Game()
    snake = game.snake

    assert snake == [(400, 300)]


def test_snake_move():
    game = Game()
    game.snake = [(400, 300)]
    game.direction = pygame.K_UP
    game.update()

    assert game.snake[0] == (400, 290)


def test_game_loop_quit():
    game = Game()
    game.running = True
    pygame.event.post(pygame.event.Event(pygame.QUIT))
    game.run()

    assert not game.running


def test_snake_direction_change():
    game = Game()
    pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_LEFT))
    game.handle_input()
    assert game.direction == pygame.K_LEFT


def test_food_spawn():
    game = Game()
    assert game.food is not None


def test_snake_eat_food():
    game = Game()
    game.snake = [(400, 300)]
    game.food = (410, 300)
    game.update()
    assert len(game.snake) == 2


def test_snake_collision_with_wall():
    game = Game()
    game.snake = [(10, 10)]
    game.direction = pygame.K_LEFT
    game.update()
    assert not game.running


def test_game_score():
    game = Game()
    game.snake = [(400, 300)]
    game.food = (410, 300)
    game.update()
    assert game.score == 1


def test_game_over():
    game = Game()
    game.snake = [(400, 300)]
    game.food = (410, 300)
    game.update()
    game.snake = [(410, 300)]
    game.update()
    assert not game.running


def test_game_over_screen():
    game = Game()
    game.snake = [(0, 10)]
    game.direction = pygame.K_LEFT
    game.update()  # This should trigger game over
    assert game.game_over is True
    game.render()
    game_over_text = game.font.render('Game Over! Press R to Restart', True, (255, 255, 255))
    assert game_over_text is not None


def test_restart_game():
    game = Game()
    game.snake = [(0, 10)]
    game.direction = pygame.K_LEFT
    game.update()  # This should trigger game over
    assert game.game_over is True
    game.reset_game()
    assert game.game_over is False
    assert game.snake == [(400, 300)]
    assert game.score == 0
