import pygame

from src.core.game import Game
from src.core.vector import Vector
from src.enums import Direction
from src.settings import SCREEN, WIDTH, WHITE

if __name__ == '__main__':

    game = Game(SCREEN)

    # Loop until the user clicks the close button.
    done = False
    clock = pygame.time.Clock()

    # Mainloop
    while not done:

        # This limits the while loop to a max of 10 times per second.
        # Leave this out and we will use all CPU we can.
        clock.tick(50)

        pressed_keys = pygame.key.get_pressed()

        spaceship_right_vector = Vector.from_direction(direction=Direction.RIGHT, speed=5)
        spaceship_left_vector = Vector.from_direction(direction=Direction.LEFT, speed=5)

        if pressed_keys[pygame.K_RIGHT]:
            if not game.ship.position.x + spaceship_right_vector.x >= WIDTH:
                game.ship.position.update(spaceship_right_vector)
        elif pressed_keys[pygame.K_LEFT]:
            if not game.ship.position.x - spaceship_left_vector.x <= 0:
                game.ship.position.update(spaceship_left_vector)

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game.ship.shoot()

        # Clear the screen and set the screen background
        SCREEN.fill(WHITE)

        # ===========> UPDATE POSITIONS HERE <========

        game.enemies_shoot()

        for shot in game.friendly_shots:
            shot.update()
            for enemy in game.enemies:
                if shot.encounters(enemy):
                    enemy.kill()
                    del enemy
                    del shot
                    break

        for shot in game.enemy_shots:
            shot.update()
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
