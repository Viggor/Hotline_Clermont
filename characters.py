import pygame
from pygame.locals import *
from constants import *


class character:
    """Character class"""

    def __init__(self, sprite):
        # character sprite
        self.sprite = pygame.image.load(sprite).convert_alpha()

        #character position
        self.x = 100
        self.y = 100
        self.angle = 0

    def rotate(self, angle):
        self.sprite = pygame.transform.rotate(self.sprite, angle)
