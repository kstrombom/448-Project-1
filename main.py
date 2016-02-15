"""
@file: main.py
@author: Diego Soliz, Shane Chu, Michael Bechtel, Connor Welsh, Dustin Wendt
@date: 2016.02.14
@brief: Main class. Used to give user program options and change the program accordingly.
"""

#!/usr/bin/python

import time
import math
from clock import *
from feed_HMS import * # our module
from menu_bar import *
from tick_sound import *

#input menu() waits for user to input valid time
#in format 00 00 00 to then return and int

#time_input = feed_HMS.run()
sound_clock_tracker = 0
#toggle = 0 to start menu
#toggle = 1 to draw analog clock
#toggle = 2 to draw digital clock
toggle = 0


#choice 4 for no sound
sound_toggle = False
choice = 4

sound = select_sound_display(choice)

while True:
	#displaying background
	bg = pygame.image.load("material.png")
	display.blit(bg, (0, 0))
	#uncoment to display white background
	#display.fill(WHITE)

	#reset tracking varaibles when time hits 24:00:00
	if time_input > 86399:
		time_input = 0
		sound_clock_tracker = 0

        #show menu
	if (toggle == 0):
                toggle = runMenu()
		if toggle == 0:
			print ("Insert time using number keys on the pygame window (format hr 00 min 00 sec 00):")
			time_input = input_menu()
        #draw analog clock
	elif (toggle == 1):
		draw_analog_clock(int(time_input))
        #draw digial clock
	elif (toggle == 2):
		draw_digital_clock(int(time_input))

	if (sound_toggle == True):
		choice = choice - 1
		if choice == 0:
			choice = 4
		sound = select_sound_display(choice)
		sound_toggle = False

	#playing sound
	if(sound != None) and (sound_clock_tracker%10 == 0):
		sound.play()
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				toggle = 1
			elif event.key == pygame.K_d:
				toggle = 2
			elif event.key == pygame.K_s:
				toggle = 0
			elif event.key == pygame.K_w:
				sound_toggle = True
			elif event.key == pygame.K_m:
				toggle = runMenu()
			elif event.key == pygame.K_SPACE:
				changeDisplay()
	#increments and loop sleep
	sound_clock_tracker += 1
	time_input += 0.1
	time.sleep(0.1)
