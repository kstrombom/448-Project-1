"""
@file: main.py
@original authors: Diego Soliz, Shane Chu, Michael Bechtel, Connor Welsh, Dustin Wendt
@New Authors: Quinton Wiley, Omar Alzubbi, Julia Drahozal, Kate Strombom
@date: 2016.02.14
@brief: Main class. Used to give user program options and change the program accordingly.
"""


import time
import math
from clock import *
from feed_HMS import * # our module
from menu_bar import *
from tick_sound import *

# input menu() waits for user to input valid time
# in format 00 00 00 to then return and int


sound_clock_tracker = 0
# toggle = 0 to start menu
# toggle = 1 to draw analog clock
# toggle = 2 to draw digital clock
# toggle = 3 to draw stop watch
# toggle = 4 to draw timer
# toggle = 5 to set timer
# toggle = 6 to black screen
toggle = 0

# breakLoop if 0 breaks while true loop
breakLoop = 1

# choice 4 for no sound
sound_toggle = False
choice = 4
sound = select_sound_display(choice)

# initialize variables
curr_time = 0
countdown = curr_time
upcount = 0
pause = 0
black = 0
curr_cal = [0,0]
# january 01, 2016 = friday
curr_day = 4

while True:
	#displaying background
	bg = pygame.image.load("material.png")
	display.blit(bg, (0, 0))
	breakLoop = 1

	#reset tracking varaibles when time hits 24:00:00
	if curr_time > (86399 + 1):
		curr_time = 0
		sound_clock_tracker = 0
	if curr_time == 0:
		(curr_cal, curr_day) = update_date(curr_cal, curr_day)

	#for Blackout ***not done***
	bg = pygame.image.load("material.png")

	#blackout screen uses black background
	if black == 0:
		bg = pygame.image.load("material.png")
	else:
		bg = pygame.image.load("black.png")
	display.blit(bg, (0, 0))

	# show menu
	if (toggle == 0):

		printMenu_console ()
		printMenu_display ()

		while (breakLoop):
			for event in pygame.event.get():
				# quit the program if the window is closed
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
					elif event.key == pygame.K_k:
						toggle = 3
						breakLoop = 0
					elif event.key == pygame.K_t:
						toggle = 4
						breakLoop = 0
					elif event.key == pygame.K_b:
						toggle = 5
						breakLoop = 0
					elif event.key == pygame.K_c:
						toggle = 6
						breakLoop = 0
					elif event.key == pygame.K_z:
						changeMenuSize ()
						changeClockSize ()
						breakLoop = 0

			curr_time += .1
			time.sleep(.1)

	if toggle == 99:
		#printMenu_console()
		printMenu_display()
		print ("Insert time using number keys on the pygame window (format hr 00 min 00 sec 00):")
		curr_time = input_time_menu()
		print ("Insert date using number keys on the pygame window (format mo 00 date 00):")
		curr_cal = input_date_menu()
		curr_day = calculateDay (curr_cal)
		toggle = -1
	elif toggle == 5:
		countdown = input_time_menu()
		toggle = -1
	elif (toggle == 1 and black == 0):
			draw_analog_clock(int(curr_time), curr_day)
		#draw digial clock
	elif (toggle == 2 and black == 0):
			timer = 0
			draw_digital_clock(int(curr_time),curr_day, timer) #changed this method to have 2 arguments. If The second argument is 1 remove AMPM and 24 hour mode
	elif (toggle == 3 and black == 0):
			draw_stopwatch(int(upcount))
	elif (toggle == 4 and black == 0):
			timer = 1
			draw_digital_clock(int(countdown),curr_day, timer)

	elif event.key == pygame.K_z:
			changeMenuSize ()
			changeClockSize ()
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


		#################GGGGGGGGGGGGOOOOOOOOOOOOOOOOOODDDDDDDDDDDD


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
					# digital clock
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
					toggle = 0
				#elif event.key == pygame.K_c:
				#	toggle = 6
				elif event.key == pygame.K_SPACE:
					changeDisplay(timer)
				elif event.type == pygame.MOUSEMOTION:
					if black == 1:
						black = 0
	#increments and loop sleep
	sound_clock_tracker += 1
	curr_time += 0.1
	if pause == 0 and toggle == 3:
		upcount += 0.1
	if pause == 0 and countdown >= 0:
		countdown -=0.1

	if(toggle == 6):
			display.fill(BLACK)
			pygame.display.update()


	time.sleep(0.1)
