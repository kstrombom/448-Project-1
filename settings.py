import pygame, sys
from pygame.locals import *
pygame.init()
HEIGHT = WIDTH = 400
display = pygame.display.set_mode((HEIGHT,WIDTH),0,32)

time_input = 69

#r = desired radius
r = HEIGHT/2

#clock center for vector start positions
center = HEIGHT/2

#colors

BLACK =(0,0,0)
RED = (255,0,0)
WHITE =(255,255,255)
BLUE = (0,0,255)

def change_time_input(new_time):
    time_input = new_time
