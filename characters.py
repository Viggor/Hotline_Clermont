import pygame
import math
from pygame.locals import *
from constants import *


class character:
    """Character class"""

    def __init__(self, sprite):
        # character sprite
        self.original_sprite = pygame.image.load(sprite).convert_alpha()
        self.original_sprite = pygame.transform.rotate(self.original_sprite, -90)
        self.sprite = self.original_sprite

        #character position
        self.x = 400 - self.sprite.get_rect().width/2
        self.y = 300 - self.sprite.get_rect().height/2
        self.angle = 0

        self.last_pos_x = 0
        self.last_pos_y = 0

    def rotate(self):
        angleRadian = math.atan2(self.last_pos_x - self.x, self.last_pos_y - self.y)
        angleDegree = angleRadian * (180 / math.pi)
        self.sprite = pygame.transform.rotate(self.original_sprite, angleDegree)

    def move(self, direction):

        if direction == 'right':
            self.x += 10

        if direction == 'left':
            self.x -= 10

        if direction == 'up':
            self.y -= 10

        if direction == 'down':
            self.y += 10

        if direction == 'up_right':
            self.x += 10
            self.y -= 10

        if direction == 'down_right':
            self.x += 10
            self.y += 10

        if direction == 'up_left':
            self.x -= 10
            self.y -= 10

        if direction == 'down_left':
            self.x -= 10
            self.y += 10
