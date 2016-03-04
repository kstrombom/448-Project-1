"""
@file: main.py
@author: Diego Soliz, Shane Chu, Michael Bechtel, Connor Welsh, Dustin Wendt
@author: Project 2 authors: Omar Alzubbi, Quinten Wiley, Kate Strombo, Julia Drahozal
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
#toggle = 3 to draw stop watch
#toggle = 4 to pause
#toggle = 5 to resume
#toggle = 6 to black screen
toggle = 0

#choice 4 for no sound
sound_toggle = False
choice = 4

sound = select_sound_display(choice)
countdown = time_input
upcount = 0
pause = 0
black = 0
while True:
	#displaying background
	bg = pygame.image.load("material.png")
	#black out screen uses black background
	if black == 0:
		bg = pygame.image.load("material.png")
	else:
		bg = pygame.image.load("black.png")
	display.blit(bg, (0, 0))

	#reset tracking varaibles when time hits 24:00:00

	if time_input > 86399:
		time_input = 0
		sound_clock_tracker = 0

        #show menu
	if (toggle == 0 or toggle == 5):
                toggle = runMenu()
		if toggle == 0:
			print ("Insert time using number keys on the pygame window (format hr 00 min 00 sec 00):")
			time_input = input_menu()
                elif (toggle == 5):
                    countdown = input_menu();
        #draw analog clock
	elif (toggle == 1 and black == 0):
		draw_analog_clock(int(time_input))
	elif black == 1:#wipes out the screen
		pygame.display.update()
        #draw digial clock
	elif (toggle == 2 and black == 0):
                timer = 0
		draw_digital_clock(int(time_input),timer) #changed this method to have 2 arguments. If The second argument is 1 remove AMPM and 24 hour mode
	elif (toggle == 3 and black == 0):
		draw_stopwatch(int(upcount))
	elif (toggle == 4 and black == 0):
                timer = 1
                draw_digital_clock(int(countdown),timer)
	#elif (toggle == 6):
	#	black_screen()

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
			elif event.key == pygame.K_k:
				toggle = 3
                        elif event.key == pygame.K_b:
				toggle = 5
			elif event.key == pygame.K_s:
				toggle = 0
			elif event.key == pygame.K_w:
				sound_toggle = True
			elif event.key == pygame.K_x:
				upcount = 0
			elif event.key == pygame.K_u:
				if black == 0:
					black = 1
				elif black == 1:
					black = 0
			elif event.key == pygame.K_m:
				toggle = runMenu()
			#elif event.key == pygame.K_c:
			#	toggle = 6
			elif event.key == pygame.K_SPACE:
				changeDisplay(timer)
			elif event.type == pygame.MOUSEMOTION:
				if black == 1:
					black = 0
	#increments and loop sleep
	sound_clock_tracker += 1
	time_input += 0.1
	if pause == 0 and toggle == 3:
		upcount += 0.1
	if pause == 0 and countdown >= 0:
            countdown -=0.1

	time.sleep(0.1)
Status API Training Shop Blog About Pricing
© 2016 GitHub, Inc. Terms Privacy Security Contact Help
