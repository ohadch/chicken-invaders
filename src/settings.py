import pygame

WIDTH = 400
HEIGHT = 400
SCREEN_SIZE = [WIDTH, HEIGHT]

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

OBJECT_PADDING = 10

# Initialize the game engine
pygame.init()

# Set the height and width of the screen
SCREEN = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Pygame Chicken Invaders")
