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
