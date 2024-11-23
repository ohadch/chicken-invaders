import pygame

from src.core.position import Position
from src.entities.entity import Entity
from src.entities.friendly_shot import FriendlyShotEntity
from src.settings import WIDTH, HEIGHT, BLACK


class SpaceshipEntity(Entity):

    def __init__(self, game_):
        super().__init__(game_)
        self.position = Position(WIDTH / 2, HEIGHT - 20)

    def shoot(self):
        self.game.friendly_shots.append(FriendlyShotEntity(self.game, self.position))

    def show(self):
        pygame.draw.circle(self.game.screen, BLACK, self.position.coordinates(), 10)
