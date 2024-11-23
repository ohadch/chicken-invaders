from src.core.vector import Vector
from src.entities.shot import ShotEntity


class FriendlyShotEntity(ShotEntity):

    def __init__(self, game_, init_pos):
        super().__init__(game_, init_pos)

    def update(self):
        self.position.update(Vector(0, -self.speed))
