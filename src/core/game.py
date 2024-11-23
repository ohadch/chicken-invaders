import random

from src.core.position import Position
from src.entities.enemy import EnemyEntity
from src.entities.spaceship import SpaceshipEntity
from src.settings import WIDTH


class Game:

    def __init__(self, screen_):
        self.screen = screen_
        self.ship = SpaceshipEntity(self)
        self.friendly_shots = []
        self.enemy_shots = []
        self.enemies = []
        self.spawn_enemies()

    def spawn_enemies(self):
        positions_ = [Position(x, 20) for x in range(20, WIDTH - 10, 50)]
        for pos in positions_:
            self.enemies.append(EnemyEntity(self, pos))

    def enemies_shoot(self):
        shooting_chance = 0.1
        if random.random() < shooting_chance:
            random.choice(self.enemies).shoot()

