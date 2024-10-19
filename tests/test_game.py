import pygame
from snake_game import Projectile, Player, Item, AdvantageItem, ProjectileItem, Particle


def test_player_initial_position():
    player = Player('red_texture.png', (100, 100))
    assert player.positions == [(100, 100)]


def test_player_move():
    player = Player('red_texture.png', (100, 100))
    player.direction = (0, -1)  # UP
    player.move()
    assert player.positions[0] == (100, 80)


def test_player_grow_snake():
    player = Player('red_texture.png', (100, 100))
    player.grow_snake()
    player.move()
    assert len(player.positions) == 2


def test_player_change_direction():
    player = Player('red_texture.png', (100, 100))
    player.change_direction((0, 1))  # DOWN
    assert player.direction == (0, 1)


def test_player_reset():
    player = Player('red_texture.png', (100, 100))
    player.positions = [(200, 200), (180, 200)]
    player.reset()
    assert player.positions == [(100, 100)]
    assert player.score == 0


def test_player_activate_speed_boost():
    player = Player('red_texture.png', (100, 100))
    player.activate_speed_boost()
    assert player.speed_multiplier == 2
    assert player.speed_boost_counter == 600


def test_player_activate_projectile_ability():
    player = Player('red_texture.png', (100, 100))
    player.activate_projectile_ability()
    assert player.can_fire_projectile is True


def test_fire_projectile():
    player = Player('red_texture.png', (100, 100))
    player.activate_projectile_ability()
    projectile = player.fire_projectile()
    assert projectile is not None
    assert projectile.position == (100, 100)


def test_projectile_move():
    projectile = Projectile((100, 100), (1, 0))  # Moving RIGHT
    projectile.move()
    assert projectile.position == (120, 100)


def test_projectile_check_collision():
    player = Player('red_texture.png', (100, 100))
    player.positions = [(200, 200), (180, 200)]
    projectile = Projectile((200, 200), (1, 0))
    assert projectile.check_collision(player) is True
    assert not projectile.active


def test_item_spawn_position():
    item = Item()
    assert 0 <= item.position[0] < WIDTH
    assert 0 <= item.position[1] < HEIGHT


def test_advantage_item_spawn_position():
    advantage_item = AdvantageItem()
    assert 0 <= advantage_item.position[0] < WIDTH
    assert 0 <= advantage_item.position[1] < HEIGHT


def test_projectile_item_spawn_position():
    projectile_item = ProjectileItem()
    assert 0 <= projectile_item.position[0] < WIDTH
    assert 0 <= projectile_item.position[1] < HEIGHT


def test_particle_lifetime():
    particle = Particle((100, 100))
    initial_lifetime = particle.lifetime
    particle.update()
    assert particle.lifetime == initial_lifetime - 1


def test_particle_velocity():
    particle = Particle((100, 100))
    assert len(particle.velocity) == 2
    assert -1 <= particle.velocity[0] <= 1
    assert -1 <= particle.velocity[1] <= 1
