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