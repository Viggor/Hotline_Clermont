__author__ = 'vigor'

import pygame
import random
import math
from constants import *
from characters import *
GRAD = math.pi / 180 # 2 * pi / 360   # math module needs Radiant instead of Grad

class bullet:
    """ a big projectile fired by the tank's main cannon"""
    side = 15 # long side of bullet rectangle
    vel = 200 # velocity
    mass = 10
    color = (200,0,100)
    maxlifetime = 10.0 # seconds

    def __init__(self, character):
        self.character = character
        self.original_sprite = pygame.image.load(bullet_pic).convert_alpha()
        self.sprite = self.original_sprite
        self.dx = 0
        self.dy = 0
        self.angle = 0
        self.lifetime = 0.0
        self.dx += self.character.dx
        self.dy += self.character.dy # add boss movement
        self.pos = [self.character.x, self.character.y] # copy (!!!) of boss position
        self.rect = self.sprite.get_rect()

    def fire(self):
        self.calculate_heading()
        self.calculate_origin()
        self.update() # to avoid ghost sprite in upper left corner,
                      # force position calculation.

    def update(self, seconds=3.0):
        # ------ calculate movement --------
        self.pos[0] += self.dx * seconds
        self.pos[1] += self.dy * seconds
        #------- move -------
        self.rect.centerx = round(self.pos[0],0)
        self.rect.centery = round(self.pos[1],0)

    def calculate_heading(self):
        """overwriting the method because there are some differences
           between a tracer and a main gun bullet"""
        self.radius = bullet.side # for collision detection
        self.angle = 0
        self.angle += self.character.angle
        self.mass = bullet.mass
        self.vel = bullet.vel
        image = self.sprite # a line
        self.image = pygame.transform.rotate(image, self.angle)
        self.rect = self.image.get_rect()

        self.dx = math.cos(degrees_to_radians(self.character.angle)) * self.vel
        self.dy = math.sin(degrees_to_radians(-self.character.angle)) * self.vel

    def calculate_origin(self):
        """overwriting because another point of origin is needed"""
        self.pos[0] += math.cos(degrees_to_radians(30+self.character.angle)) * (32/2)
        self.pos[1] += math.sin(degrees_to_radians(-30-self.character.angle)) * (32/2)
        print(self.pos)


def radians_to_degrees(radians):
    return (radians / math.pi) * 180.0

def degrees_to_radians(degrees):
    return degrees * (math.pi / 180.0)
