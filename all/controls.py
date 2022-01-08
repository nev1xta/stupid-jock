import pygame
import sys
"""все события"""


def events(jock):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #вправо
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                jock.move_r = True
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                jock.move_l = True
        elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    jock.move_r = False
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    jock.move_l = False


def update(background_color, screen, jock):
    """обновление экрана"""
    screen.fill(background_color)
    jock.output()
    pygame.display.flip()