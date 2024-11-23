from src.enums import Direction


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __invert__(self):
        return Vector(-self.x, -self.y)

    @classmethod
    def from_direction(cls, direction: Direction, speed: int):
        if direction == Direction.UP:
            return cls(0, -speed)
        if direction == Direction.DOWN:
            return cls(0, speed)
        if direction == Direction.LEFT:
            return cls(-speed, 0)
        if direction == Direction.RIGHT:
            return cls(speed, 0)

        raise ValueError(f"Invalid direction: {direction}")