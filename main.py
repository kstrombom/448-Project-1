"""
@file: main.py
@original authors: Diego Soliz, Shane Chu, Michael Bechtel, Connor Welsh, Dustin Wendt
@new authors: Quinton Wiley, Omar Alzubbi, Julia Drahozal, Kate Strombom
@date: 2016.03.06
@brief: Main class. Used to give user program options and change the program accordingly.
"""


import time
import math
from clock import *
from feed_HMS import *
from menu_bar import *
from tick_sound import *

# initialize variables

sound_clock_tracker = 0
# toggle = 0 to start menu
# toggle = 1 to draw analog clock
# toggle = 2 to draw digital clock
# toggle = 3 to draw stop watch
# toggle = 4 to draw timer
# toggle = 5 to set timer
# toggle = 6 to black screen
toggle = 0
prevToggle = 0

# breakLoop if 0 breaks while true loop
breakLoop = 1

# choice 4 for no sound
sound_toggle = False
choice = 4
sound = select_sound_display(choice)

timer = 0
curr_time = 0
countdown = curr_time
upcount = 0
pause = 0
black = 0
curr_cal = [0,0]
# january 01, 2016 = friday
curr_day = 4


######################################################################
############################# RUN PROGRAM ############################
######################################################################

while True:

	#display background
	bg = pygame.image.load("material.png")
	display.blit(bg, (0, 0))
	breakLoop = 1

	#reset tracking varaibles when time hits 24:00:00
	if curr_time > (86399 + 1):
		curr_time = 0
		sound_clock_tracker = 0
	if curr_time == 0:
		(curr_cal, curr_day) = update_date(curr_cal, curr_day)

	################ MENU ################
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
						# toggle sounds
						sound_toggle = True
						breakLoop = 0
					elif event.key == pygame.K_k:
						# draw stopwatch
						toggle = 3
						breakLoop = 0
					elif event.key == pygame.K_t:
						# draw timer
						toggle = 4
						breakLoop = 0
					elif event.key == pygame.K_b:
						# set timer
						toggle = 5
						breakLoop = 0
					elif event.key == pygame.K_c:
						# blackout
						if (toggle == 6):
							toggle = prevToggle
						else:
							prevToggle = toggle
							toggle = 6
						breakLoop = 0
					elif event.key == pygame.K_z:
						# zoom
						changeMenuSize ()
						changeClockSize ()
						breakLoop = 0

			curr_time += .1
			time.sleep(.1)

	################ INPUT ################
	if toggle == 99:
		#printMenu_console()
		printMenu_display()
		print ("Insert time using number keys on the pygame window (format hr 00 min 00 sec 00):")
		curr_time = input_time_menu()
		print ("Insert date using number keys on the pygame window (format mo 00 date 00):")
		curr_cal = input_date_menu()
		curr_day = calculateDay (curr_cal)
		toggle = -1
	################ MENU ################
	elif toggle == 5:
		countdown = input_time_menu()
		toggle = -1
	################ ANALOG ################
	elif (toggle == 1):
			draw_analog_clock(int(curr_time), curr_day)
	################ DIGITAL ################
	elif (toggle == 2):
			timer = 0
			draw_digital_clock(int(curr_time),curr_day, timer) #changed this method to have 2 arguments. If The second argument is 1 remove AMPM and 24 hour mode
	################ STOPWATCH ################
	elif (toggle == 3):
			draw_stopwatch(int(upcount))
	################ TIMER ################
	elif (toggle == 4):
			timer = 1
			draw_digital_clock(int(countdown),curr_day, timer)
	################ SOUNDS ################
	if (sound_toggle == True):
		choice = choice - 1
		if choice == 0:
			choice = 4
		sound = select_sound_display(choice)
		sound_toggle = False
	if(sound != None) and (sound_clock_tracker%10 == 0):
		sound.play()

	################ WHILE RUNNING ################
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == pygame.KEYDOWN:
				# analog
				if event.key == pygame.K_a:
					toggle = 1
				# digital
				elif event.key == pygame.K_d:
						toggle = 2
				# stopwatch
				elif event.key == pygame.K_k:
						toggle = 3
				# reset stopwatch
				elif event.key == pygame.K_x:
						upcount = 0
				# timer
				elif event.key == pygame.K_t:
						toggle = 4
				# set timer
				elif event.key == pygame.K_b:
						toggle = 5
				# pause
				elif event.key == pygame.K_p:
						if pause == 0:
							pause =1
						elif pause == 1:
							pause = 0
				# set time
				elif event.key == pygame.K_s:
						toggle = 0
				# toggle sounds
				elif event.key == pygame.K_w:
						sound_toggle = True
				# menu options
				elif event.key == pygame.K_m:
					toggle = 0
				# blackout
				elif event.key == pygame.K_c:
						if (toggle == 6):
							toggle = prevToggle
						else:
							prevToggle = toggle
							toggle = 6
						breakLoop = 0
				# toggle 12/24
				elif event.key == pygame.K_SPACE:
					changeDisplay(timer)
				# zoom
				elif event.key == pygame.K_z:
					changeMenuSize ()
					changeClockSize ()

	#increments and loop sleep
	sound_clock_tracker += 1
	curr_time += 0.1
	if pause == 0 and toggle == 3:
		upcount += 0.1
	if pause == 0 and countdown >= 0:
		countdown -=0.1

	################ BLACKOUT ################
	if(toggle == 6):
			display.fill(BLACK)
			pygame.display.update()

	time.sleep(0.1)
