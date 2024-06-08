from snake_game import Game


def test_initial_window_size():
    game = Game()
    window_size = game.window_size

    assert window_size == (800, 600)