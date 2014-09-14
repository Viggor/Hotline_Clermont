#!/usr/bin/python3
# -*- coding: Utf-8 -*
__author__ = 'vigor'

"""
Hotline clermont
(inspired by hotline miami)
"""

import math
import pygame
from pygame.locals import *

from characters import *
from constants import *

pygame.init()

#init window
fenetre = pygame.display.set_mode((main_window_width, main_window_height))

#window title
pygame.display.set_caption(main_window_title)



main_loop = 1
while main_loop:

    # refresh
    pygame.display.flip()

    #reset loop var
    game_loop = 1
    continuer_accueil = 1

    #butcher creation
    butcher = character(r"C:\Users\vigor\PycharmProjects\Hotline Clermont\static\src\img\HM_ButcherWalking.png")


    while game_loop:

        #loop speed limit
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():

                #If escape, quit
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        game_loop = 0
                        main_loop = 0

                elif event.type == MOUSEMOTION: #mouse mouvement
                    mouse_pos = event.pos[0] * event.pos[1]
                    angleRadian = math.atan2(event.pos[0] - butcher.x, event.pos[1] - butcher.y)
                    angleDegree = angleRadian * (180 / math.pi)
                    print(angleDegree)

                    butcher.rotate(angleDegree)
                    butcher_centerx = butcher.x + butcher.sprite.get_rect().width/2
                    butcher_centery = butcher.y + butcher.sprite.get_rect().height/2
                    butcher.x = butcher_centerx - butcher.sprite.get_rect().width/2
                    butcher.y = butcher_centery - butcher.sprite.get_rect().height/2


        #Refresh position
        fenetre.blit(butcher.sprite, (butcher.x, butcher.y))

        pygame.display.flip()