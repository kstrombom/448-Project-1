
import pygame, sys
from pygame.locals import *
import time
import settings # display settings on settings.py
import feed_HMS # our module
from menu_bar import * 
from clock import *

#input_menu()

time_input = feed_HMS.run()

#change this value to select clocks
toggle = 2

while True:
	
	#displaying background
	bg = pygame.image.load("background.jpg")
	display.blit(bg, (0, 0))
	#uncoment to display white background
	#display.fill(WHITE)

	if (toggle == 0):
		#run menu
		print ('toggle = 1')
	elif (toggle == 1):
		draw_analog_clock(time_input)
	elif toggle == 2:
		draw_digital_clock(time_input)
		
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
                elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_a:
                                toggle = 1
                        elif event.key == pygame.K_d:
                                toggle = 2
	time_input += 1
	time.sleep(1)
