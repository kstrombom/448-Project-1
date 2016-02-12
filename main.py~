#!/usr/bin/python

import time
from clock import *
from feed_HMS import * # our module
from menu_bar import *
from tick_sound import *

#input menu() waits for user to input valid time
#in format 00 00 00 to then return and int

#time_input = feed_HMS.run()

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
	bg = pygame.image.load("background.jpg")
	display.blit(bg, (0, 0))
	#uncoment to display white background
	#display.fill(WHITE)

	if time_input > 86400:
		time_input = 0

	if (toggle == 0):
		toggle = runMenu()
		if toggle == 0:
			print ("Insert time using number keys on the pygame window (format hr 00 min 00 sec 00):")
			time_input = input_menu()
	elif (toggle == 1):
		draw_analog_clock(time_input)
	elif (toggle == 2):
		draw_digital_clock(time_input)
		
	if (sound_toggle == True):
		choice = choice - 1
		if choice == 0:
			choice = 4
		sound = select_sound_display(choice)
		sound_toggle = False
	
	#playing sound	
	if(sound != None):
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
				

	time_input += 1
	time.sleep(1)
