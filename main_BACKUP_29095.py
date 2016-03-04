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
<<<<<<< HEAD
time_input = 0;



||||||| merged common ancestors

=======
countdown = time_input
pause = 0
	
>>>>>>> origin/oalzubbi-timer
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
<<<<<<< HEAD
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
||||||| merged common ancestors
	if (toggle == 0):
                toggle = runMenu()
		if toggle == 0:
=======
	if (toggle == 0 or toggle == 5):
                toggle = runMenu()
		if toggle == 0:
>>>>>>> origin/oalzubbi-timer
			print ("Insert time using number keys on the pygame window (format hr 00 min 00 sec 00):")
			time_input = input_menu()
                elif (toggle == 5):
                    countdown = input_menu();
        #draw analog clock
	elif (toggle == 1):
		draw_analog_clock(int(time_input))
        #draw digial clock
	elif (toggle == 2):
                timer = 0
		draw_digital_clock(int(time_input),timer) #changed this method to have 2 arguments. If The second argument is 1 remove AMPM and 24 hour mode
        elif (toggle == 4):
                timer = 1 
                draw_digital_clock(int(countdown),timer)
        
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
                        #this next elif is to pause the timer or stopwatch
			elif event.key == pygame.K_p:
				if pause == 0:
                                    pause =1
                                elif pause == 1:
                                    pause = 0
			elif event.key == pygame.K_d:
				toggle = 2
                        elif event.key == pygame.K_b:
				toggle = 5
			elif event.key == pygame.K_s:
				toggle = 99
			elif event.key == pygame.K_w:
				sound_toggle = True
			elif event.key == pygame.K_m:
				toggle = 0;
			elif event.key == pygame.K_SPACE:
				changeDisplay(timer)
	#increments and loop sleep
	sound_clock_tracker += 1
<<<<<<< HEAD
	time_input += .1
	time.sleep(.1)

||||||| merged common ancestors
	time_input += 0.1
	time.sleep(0.1)
=======
	time_input += 0.1
	if pause == 0 and countdown >= 0:
            countdown -=0.1
        else:
            print("Time's up")
	time.sleep(0.1)
>>>>>>> origin/oalzubbi-timer
