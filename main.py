import pygame
import sys
from linalg.vector import Vector2
from pygame_controller.init_pygame import init_pygame
from animations.from_circle_to_center import CircleAnimations
clock = pygame.time.Clock()


if __name__ == "__main__":

    screen = init_pygame()

    circ = CircleAnimations(20, screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        circ.draw()
        circ.step()
        pygame.display.flip()
        clock.tick(60)

