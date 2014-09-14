import pygame
from pygame.locals import *
from constants import *


class character:
    """Character class"""

    def __init__(self, sprite):
        # character sprite
        self.sprite = pygame.image.load(sprite).convert_alpha()

        #character position
        self.x = 400 - self.sprite.get_rect().width/2
        self.y = 300 - self.sprite.get_rect().height/2
        self.angle = 0

    def rotate(self, angle):
        self.sprite = pygame.transform.rotate(self.sprite, angle)
