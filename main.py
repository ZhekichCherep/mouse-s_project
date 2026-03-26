import pygame
import sys
from linalg.vector import Vector2
from pygame_controller.init_pygame import init_pygame
from animations.from_circle_to_center import CircleAnimations
clock = pygame.time.Clock()
speed = 10
st = ''

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


if __name__ == "__main__":


    screen = init_pygame()

    circ = CircleAnimations(20, screen)

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if is_number(event.unicode):
                    st+=event.unicode
                    
                    # print (f'скорость {int(event.unicode)}')
                elif event.key == pygame.K_RETURN:
                    print(st)
                    speed = int(st)
                    st = ''
        circ.draw()
        circ.step()
        pygame.display.flip()
        clock.tick(speed)




