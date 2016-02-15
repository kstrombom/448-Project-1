"""
@file: settings.py
@author: Diego Soliz, Shane Chu, Michael Bechtel, Connor Welsh, Dustin Wendt
@date: 2016.02.14
@brief: Settings class. Used to initialize settings for the pygame window.
"""

import pygame, sys
from pygame.locals import *

#start pygame
pygame.init()

#set pygame window settings
HEIGHT = WIDTH = 400
display = pygame.display.set_mode((HEIGHT,WIDTH),0,32)
icon = pygame.image.load("clock.png")
pygame.display.set_icon(icon)

pygame.display.set_caption("Best Clock")

time_input = 0.0

#r = desired radius
r = HEIGHT/2

#clock center for vector start positions
center = HEIGHT/2

#colors

BLACK = (0,0,0)
RED = (255, 0, 0)
WHITE =(255,255,255)
BLUE = (0,0,255)
PALE_BLUE = (26, 45, 73)

def change_time_input(new_time):
    time_input = new_time
