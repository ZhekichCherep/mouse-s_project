import pygame as pg

from linalg.vector import Vector2
from pygame_controller.init_pygame import init_pygame
from linalg.matrix import Matrix2D
from screen_objects.buttons import create_scale_button, create_descale_button


class PlayController:
    def __init__(self, n_points: int=10):
        self.screen = init_pygame()
        self.p1 = Vector2(10, 10)
        self.p2 = Vector2(110, 10)
        self.p3 = Vector2(110, 110)
        self.p4 = Vector2(10, 110)
        self.scale_button = create_scale_button()
        self.descale_button = create_descale_button()
        self.font = pg.font.Font(None, 24)
        self.scale_text = self.font.render("Enlarge", True, (0, 0, 0))
        self.descale_text = self.font.render("Reduce", True, (0, 0, 0))
        self.scale_text_rect = self.scale_text.get_rect(center=self.scale_button.center)
        self.descale_text_rect = self.scale_text.get_rect(center=self.descale_button.center)

        self.draw()


    def scale_polygon(self, s):
        scale_matrix = Matrix2D.scale_matrix(s)
        self.p1 = scale_matrix @ self.p1
        self.p2 = scale_matrix @ self.p2
        self.p3 = scale_matrix @ self.p3
        self.p4 = scale_matrix @ self.p4

    def draw(self):
        pg.draw.polygon(self.screen, (0, 255, 0), (
            self.p1.get_coordinates(), self.p2.get_coordinates(), self.p3.get_coordinates(), self.p4.get_coordinates()
        ))

    def run(self):
        running = True
        clock = pg.time.Clock()
        while running:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    if self.scale_button.collidepoint(event.pos):
                        self.scale_polygon(1.2)
                    elif self.descale_button.collidepoint(event.pos):
                        self.scale_polygon(0.8)

            self.screen.fill((255, 255, 255))
            pg.draw.rect(self.screen, (0, 128, 0), self.scale_button)
            pg.draw.rect(self.screen, (128, 0, 0), self.descale_button, 2)
            self.screen.blit(self.scale_text, self.scale_text_rect)
            self.screen.blit(self.descale_text, self.descale_text_rect)
            self.draw()
            pg.display.flip()
            clock.tick(60)




