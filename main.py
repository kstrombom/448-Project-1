"""
@file: main.py
@original_authors: Diego Soliz, Shane Chu, Michael Bechtel, Connor Welsh, Dustin Wendt
@new_authors: Quinton Wiley, Omar Alzubbi, Julia Drahozal, Kate Strombom
@date: 2016.02.14
@brief: Main class. Used to run program.
"""

#!/usr/bin/python

import time
import math
from clock import *
from feed_HMS import * # our module
from menu_bar import *
from tick_sound import *

sound_clock_tracker = 0
# 0:menu, 1:analog, 2:digital
toggle = 0
breakLoop = 1

#choice 4 for no sound
sound_toggle = False
choice = 4

sound = select_sound_display (choice)
curr_time = 0;
curr_cal = [0, 0]
# jan 01 2016 = friday
curr_day = 5

while True:

	# display background
	bg = pygame.image.load("material.png")
	display.blit (bg, (0, 0))
	breakLoop = 1

	# reset tracking varaibles when time hits 24:00:00
	if curr_time > 86399:
		curr_time = 0
		sound_clock_tracker = 0
		updateDate (curr_cal)

        # menu screen
	if (toggle == 0):
	
                printMenu_console ()
		printMenu_display ()
		
		while (breakLoop):
			for event in pygame.event.get ():
                	        #quit the program if the window is closed
				if event.type == QUIT:
						pygame.quit ()
						sys.exit ()
        	                #perform action according to key pressed
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_a:
        	                                # draw analog clock
						toggle = 1
						breakLoop = 0
					elif event.key == pygame.K_d:
        	                                # draw digital clock
						toggle = 2
						breakLoop = 0
					elif event.key == pygame.K_s:
        	                                # change time/return to menu
						toggle = 99
						print ("input time")
						breakLoop = 0
					elif event.key == pygame.K_m:
        	                                # return to menu
						printMenu_console()
						toggle = -1
						breakLoop = 0
					elif event.key == pygame.K_SPACE:
        	                                # change between 12 and 24 hour mode
						print("need method to change to 24 hour mode")
						breakLoop = 0
					elif event.key == pygame.K_w:
						#turn on sound
						sound_toggle = True
						breakLoop = 0
			curr_time += .1
			time.sleep(.1)

		if toggle == 99:
               		printMenu_console ()
			printMenu_display ()
			print ("Insert time using number keys on the pygame window (format hr 00 min 00 sec 00):")
			curr_time = input_time_menu ()
			print ("Insert date using number keys on the pygame window (format mo 00 date 00):")
			curr_cal = input_date_menu ()
			curr_day = calculateDay (curr_cal);
			
        # analog clock screen
	elif (toggle == 1):
		draw_analog_clock (int (curr_time), curr_day)
		
        # digital clock
	elif (toggle == 2):
		draw_digital_clock (int (curr_time), curr_day)

	if (sound_toggle == True):
		choice = choice - 1
		if choice == 0:
			choice = 4
		sound = select_sound_display(choice)
		sound_toggle = False

	# play sound
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
				toggle = 99
			elif event.key == pygame.K_w:
				sound_toggle = True
			elif event.key == pygame.K_m:
				toggle = 0;
			elif event.key == pygame.K_SPACE:
				changeDisplay()
				
	#increments and loop sleep
	sound_clock_tracker += 1
	curr_time += .1
	time.sleep (.1)

