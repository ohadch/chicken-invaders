import pygame

from src.core.position import Position
from src.entities.entity import Entity
from src.settings import BLUE


class ShotEntity(Entity):

    def __init__(self, game_, init_pos):
        super().__init__(game_)
        self.position = Position(
            x=init_pos.x,
            y=init_pos.y
        )
        self.speed = 5

    def update(self):
        pass

    def encounters(self, other):
        return self.position == other.position

    def show(self):
        pygame.draw.circle(self.game.screen, BLUE, self.position.coordinates(), 5)
