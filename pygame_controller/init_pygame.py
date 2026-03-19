import pygame
from config import *


def init_pygame():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    screen.fill((0, 0, 0))

    return screen

