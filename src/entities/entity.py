import abc
import random

from src.core.position import Position
from src.settings import HEIGHT, WIDTH


class Entity(abc.ABC):

    def __init__(self, game):
        self.game = game

    def random_position(self):
        x = random.randint(1, WIDTH - 1)
        y = random.randint(1, HEIGHT - 1)
        p = Position(x, y)
        if p.is_clear(self.game):
            return p
        return self.random_position()

    @abc.abstractmethod
    def show(self):
        pass
