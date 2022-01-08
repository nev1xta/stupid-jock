import pygame


class Falling_Sprite(pygame.sprite.Sprite):
    def __init__(self, x, speed, filename):
        super().__init__()
        self.image = pygame.image.load(filename).convert_alpha()
        # self.image = self.image = pygame.Surface((50, 50),
        #                             pygame.SRCALPHA, 32)
        self.rect = self.image.get_rect(center=(x, 0))
        self.speed = speed

    def update(self, *args):
        if self.rect.y < args[0] - 20:
            # self.rect.move_ip((self.speed, 0))
            self.rect.y += self.speed
        else:
            self.rect.y = 0

    def output(self, screen):
        """отрисовка качка"""
        screen.blit(self.image, self.rect)
