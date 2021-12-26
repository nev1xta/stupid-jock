import pygame

"""тут сам качок его передвежение и т.д."""


class Jock():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('data/led_strips_doge.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.move_r = False
        self.move_l = False

    def output(self):
        """отрисовка качка"""
        self.screen.blit(self.image, self.rect)

    def update_jock(self):
        """обновление качка"""
        speed = 0.5
        #вправо
        if self.move_r and self.rect.right < self.screen_rect.right:
            self.center += speed
         #влево
        if self.move_l and self.rect.left > 0:
            self.center -= speed
        self.rect.centerx = self.center