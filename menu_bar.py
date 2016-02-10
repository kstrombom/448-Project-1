import pygame, sys
from pygame.locals import *
import math
import feed_HMS
import clock

HEIGHT = WIDTH = 400

pygame.init()
display = pygame.display.set_mode((HEIGHT,WIDTH),0,32)

#colors
BLACK =(0,0,0)
RED = (255,0,0)
WHITE =(255,255,255)

def printMenu():
	print "Press a for analog clock display"
	print "Press d for digital clock display"
	print "Press s to set time"
	print "Press m for menu options"
				
time_input= feed_HMS.run()


while True:

	for event in pygame.event.get():		
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				clock.analog(time_input)
			
			elif event.key == pygame.K_d:
				clock.digital(time_input)
				
			elif event.key == pygame.K_s:
				time_input=feed_HMS.run()
					
			elif event.key == pygame.K_m:
				printMenu()




for event in pygame.event.get():
	if event.type == QUIT:
		pygame.quit()
		sys.exit()	