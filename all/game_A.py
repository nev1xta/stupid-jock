import sys
import pygame
from jock import Jock
import controls
from sprite_movement import *


def run():
    pygame.init()
    w, h = 400, 600
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption('Stupid Jock')
    background_color = 'black'
    jock = Jock(screen)
    falling_sprites = pygame.sprite.Group()
    sprite1 = Falling_Sprite(w//2, 1, '../data/box.png')
    falling_sprites.add(sprite1)

    while True:

        controls.events(jock)
        controls.update(background_color, screen, jock)
        jock.update_jock()
        falling_sprites.update(h)
        falling_sprites.draw(screen)
        print('hello')


run()
