import pygame
from . import constants


class Collider(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        #self.image.fill((constants.RED))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


