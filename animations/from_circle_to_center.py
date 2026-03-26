import math

import pygame
from linalg.vector import Vector2
from random import choice
from config import *

class CircleAnimations:
    def __init__(self, n_points, screen: pygame.Surface):
        self.screen = screen
        self.center = Vector2(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        # a = SCREEN_WIDTH / 2 - 10
        # b = SCREEN_HEIGHT / 2 - 10
        a = SCREEN_HEIGHT / 2 - 10
        b = a

        self.vectors = []
        for i in range(n_points):
            t = (i / n_points) * 2 * math.pi

            x = self.center.x + a * math.cos(t)
            y = self.center.y + b * math.sin(t)

            self.vectors.append([Vector2(x, y), choice(COLORS)])

    def draw(self):
        for point in self.vectors:
            pygame.draw.circle(self.screen, point[1], (int(point[0].x), int(point[0].y)), 1)

    def step(self):
        n_points = len(self.vectors)
        for i in range(0, len(self.vectors)):
            diff = (self.vectors[(i+1) % n_points][0] - self.vectors[i][0]).normalize()
            self.vectors[i][0] = self.vectors[i][0] + diff


