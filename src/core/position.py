from src.settings import OBJECT_PADDING


class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def coordinates(self):
        return self.x, self.y

    def is_clear(self, game_):
        for pos in game_.snake.positions:
            if pos.coordinates == self.coordinates():
                return False
        return True

    def update(self, vector):
        self.x += vector.x
        self.y += vector.y

    def __eq__(self, other):
        return abs(self.x - other.x) < OBJECT_PADDING and abs(self.y - other.y) < OBJECT_PADDING
