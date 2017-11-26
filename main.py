import random
import pygame

# ========== Pygame Config ================

WIDTH = 400
HEIGHT = 400
screen_size = [WIDTH, HEIGHT]

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize the game engine
pygame.init()

# Set the height and width of the screen
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Ohad's Snake")


# ========== Functions ===================


def p5_map(n, start1, stop1, start2, stop2):
    return ((n - start1) / (stop1 - start1)) * (stop2 - start2) + start2


# ========== Classes =====================


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __invert__(self):
        return Vector(-self.x, -self.y)


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
        return abs(self.x - other.x) < game.object_padding and abs(self.y - other.y) < game.object_padding


VECTOR_SIZE = 5

RIGHT = Vector(VECTOR_SIZE, 0)
LEFT = Vector(-VECTOR_SIZE, 0)
UP = Vector(0, -VECTOR_SIZE)
DOWN = Vector(0, VECTOR_SIZE)


# ========== Game Objects ================


class Shot:

    def __init__(self, game_, init_pos):
        self.game = game_
        self.position = Position(init_pos.x, init_pos.y)
        self.speed = 5

    def update(self):
        pass

    def encounters(self, other):
        return self.position == other.position

    def show(self):
        pygame.draw.circle(self.game.screen, RED, self.position.coordinates(), 5)


class FriendlyShot(Shot):

    def __init__(self, game_, init_pos):
        Shot.__init__(self, game_, init_pos)

    def update(self):
        self.position.update(Vector(0, -self.speed))


class EnemyShot(Shot):

    def __init__(self, game_, init_pos):
        Shot.__init__(self, game_, init_pos)

    def update(self):
        self.position.update(Vector(0, self.speed))


class Spaceship:

    def __init__(self, game_):
        self.game = game_
        self.position = Position(WIDTH / 2, HEIGHT - 20)

    def shoot(self):
        self.game.friendly_shots.append(FriendlyShot(self.game, self.position))

    def show(self):
        pygame.draw.circle(self.game.screen, BLACK, self.position.coordinates(), 10)


class Enemy:
    def __init__(self, game_, position_, vibration_rate=1):
        self.game = game_
        self.position = position_
        self.vibration_rate = vibration_rate
        self.vibration_pattern = ['U', 'L', 'D', 'R']
        self.vibration_counter = 0

    def vibrate(self):
        vibration_move = self.vibration_pattern[self.vibration_counter]
        if vibration_move == 'U':
            self.position.y -= self.vibration_rate
        elif vibration_move == 'L':
            self.position.x -= self.vibration_rate
        elif vibration_move == 'D':
            self.position.y += self.vibration_rate
        elif vibration_move == 'R':
            self.position.x += self.vibration_rate
        self.vibration_counter += 1
        if self.vibration_counter == len(self.vibration_pattern):
            self.vibration_counter = 0

    def kill(self):
        self.game.enemies.remove(self)

    def shoot(self):
        self.game.enemy_shots.append(EnemyShot(self.game, self.position))

    def show(self):
        self.vibrate()
        pygame.draw.circle(self.game.screen, GREEN, self.position.coordinates(), 10)


class Game:

    def __init__(self, screen_, object_padding=10):
        self.screen = screen_
        self.ship = Spaceship(self)
        self.object_padding = object_padding
        self.friendly_shots = []
        self.enemy_shots = []
        self.enemies = []
        self.spawn_enemies()

    def spawn_enemies(self):
        positions_ = [Position(x, 20) for x in range(20, WIDTH - 10, 50)]
        for pos in positions_:
            self.enemies.append(Enemy(self, pos))


if __name__ == '__main__':

    game = Game(screen)

    # Loop until the user clicks the close button.
    done = False
    clock = pygame.time.Clock()

    # Mainloop
    while not done:

        # This limits the while loop to a max of 10 times per second.
        # Leave this out and we will use all CPU we can.
        clock.tick(50)

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_RIGHT]:
            if not game.ship.position.x + RIGHT.x >= WIDTH:
                game.ship.position.update(RIGHT)
        elif pressed_keys[pygame.K_LEFT]:
            if not game.ship.position.x - LEFT.x <= 0:
                game.ship.position.update(LEFT)

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game.ship.shoot()

        # Clear the screen and set the screen background
        screen.fill(WHITE)

        # ===========> UPDATE POSITIONS HERE <========

        if len(game.enemy_shots) < 10:
            pass

        for shot in game.friendly_shots:
            shot.update()

        for shot in game.enemy_shots:
            shot.update()

        for shot in game.friendly_shots:
            for enemy in game.enemies:
                if shot.encounters(enemy):
                    enemy.kill()

        for shot in game.enemy_shots:
            if shot.encounters(game.ship):
                exit(1)

        # ===========> START DRAWING HERE <===========

        game.ship.show()
        for shot in game.friendly_shots:
            shot.show()

        for shot in game.enemy_shots:
            shot.show()

        for enemy in game.enemies:
            enemy.show()

        # ===========> END DRAWING HERE <=============

        # Go ahead and update the screen with what we've drawn.
        # This MUST happen after all the other drawing commands.
        pygame.display.flip()
