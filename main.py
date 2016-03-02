"""
@file: main.py
@original authors: Diego Soliz, Shane Chu, Michael Bechtel, Connor Welsh, Dustin Wendt
@New Authors: Quinton Wiley, Omar Alzubbi, Julia Drahozal, Kate Strombom
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
breakLoop = 1

#choice 4 for no sound
sound_toggle = False
choice = 4

sound = select_sound_display(choice)
time_input = 0;



while True:
	#displaying background
	bg = pygame.image.load("material.png")
	display.blit(bg, (0, 0))
	breakLoop = 1
	#uncoment to display white background
	#display.fill(WHITE)

	#reset tracking varaibles when time hits 24:00:00
	if time_input > 86399:
		time_input = 0
		sound_clock_tracker = 0

        #show menu
	if (toggle == 0):
                printMenu_console()
		printMenu_display()
		while (breakLoop):
			for event in pygame.event.get():
                	        #quit the program if the window is closed
				if event.type == QUIT:
						pygame.quit()
						sys.exit()
        	                #perform action according to key pressed
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_a:
        	                                #draw analog clock
						toggle = 1
						breakLoop = 0
					elif event.key == pygame.K_d:
        	                                #draw digital clock
						toggle = 2
						breakLoop = 0
					elif event.key == pygame.K_s:
        	                                #change time/return to menu
						toggle = 99
						print ("input time")
						breakLoop = 0
					elif event.key == pygame.K_m:
        	                                #return to menu
						printMenu_console()
						toggle =-1
						breakLoop = 0
					elif event.key == pygame.K_SPACE:
        	                                #change between 12 and 24 hour mode
						print("need method to change to 24 hour mode")
						breakLoop = 0

					elif event.key == pygame.K_w:
						sound_toggle = True
						breakLoop = 0

			time_input += .1
			time.sleep(.1)

		if toggle == 99:
               		printMenu_console()
			printMenu_display()
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
				toggle = 99
			elif event.key == pygame.K_w:
				sound_toggle = True
			elif event.key == pygame.K_m:
				toggle = 0;
			elif event.key == pygame.K_SPACE:
				changeDisplay()
	#increments and loop sleep
	sound_clock_tracker += 1
	time_input += .1
	time.sleep(.1)

