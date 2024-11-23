from typing import List

import pygame

from src.entities.enemy_shot import EnemyShotEntity
from src.enums import Direction
from src.settings import GREEN


class EnemyEntity:
    def __init__(self, game_, position_, vibration_rate=1):
        self.game = game_
        self.position = position_
        self.vibration_rate = vibration_rate
        # self.vibration_pattern = ['U', 'L', 'D', 'R']
        self.vibration_pattern: List[Direction] = [Direction.UP, Direction.LEFT, Direction.DOWN, Direction.RIGHT]
        self.vibration_counter = 0

    def vibrate(self):
        vibration_move = self.vibration_pattern[self.vibration_counter]

        if vibration_move is Direction.UP:
            self.position.y -= self.vibration_rate
        elif vibration_move is Direction.LEFT:
            self.position.x -= self.vibration_rate
        elif vibration_move is Direction.DOWN:
            self.position.y += self.vibration_rate
        elif vibration_move is Direction.RIGHT:
            self.position.x += self.vibration_rate

        self.vibration_counter += 1
        if self.vibration_counter == len(self.vibration_pattern):
            self.vibration_counter = 0

    def kill(self):
        self.game.enemies.remove(self)

    def shoot(self):
        self.game.enemy_shots.append(EnemyShotEntity(self.game, self.position))

    def show(self):
        self.vibrate()
        pygame.draw.circle(self.game.screen, GREEN, self.position.coordinates(), 10)
