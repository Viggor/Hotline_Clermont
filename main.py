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

# init window
window = pygame.display.set_mode((main_window_width, main_window_height))

#window title
pygame.display.set_caption(main_window_title)

main_loop = 1
while main_loop:

    # refresh
    pygame.display.flip()

    #reset loop var
    game_loop = 1
    continuer_accueil = 1

    background = pygame.image.load(background_pic).convert()

    #butcher creation
    butcher = character(main_character)

    pygame.key.set_repeat(10, 30)

    while game_loop:

        #loop speed limit
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():

            #If escape, quit
            if event.type == KEYDOWN:
                keys = pygame.key.get_pressed()
                if event.key == K_ESCAPE:
                    game_loop = 0
                    main_loop = 0
                elif keys[K_d] and keys[K_w]:
                    butcher.move('up_right')
                    butcher.rotate()
                elif keys[K_d] and keys[K_s]:
                    butcher.move('down_right')
                    butcher.rotate()
                elif keys[K_a] and keys[K_w]:
                    butcher.move('up_left')
                    butcher.rotate()
                elif keys[K_a] and keys[K_s]:
                    butcher.move('down_left')
                    butcher.rotate()
                elif keys[K_d]:
                    butcher.move('right')
                    butcher.rotate()
                elif keys[K_a]:
                    butcher.move('left')
                    butcher.rotate()
                elif keys[K_w]:
                    butcher.move('up')
                    butcher.rotate()
                elif keys[K_s]:
                    butcher.move('down')
                    butcher.rotate()

            elif event.type == MOUSEMOTION:  #mouse mouvement
                butcher.last_pos_x = event.pos[0]
                butcher.last_pos_y = event.pos[1]
                butcher.rotate()

        #Refresh position
        window.blit(background, (0, 0))
        window.blit(butcher.sprite, (butcher.x, butcher.y))

        pygame.display.flip()