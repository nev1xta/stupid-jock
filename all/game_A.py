import sys
import pygame
from jock import Jock
import controls

def run():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('data/stupid-jock')
    background_color = (0, 0, 0)
    jock = Jock(screen)

    while True:
        controls.events(jock)
        jock.update_jock()
        controls.update(background_color, screen, jock)
run()