#----------------------------
#WORK IN PROGRESS
#----------------------------
from settings import *
import math
from feed_HMS import *

#need method to draw instruction in display
font = pygame.font.Font(None, 25)
number = font.render("12", 1, BLACK)

def runMenu():
	printMenu_console()
	printMenu_display()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a:
					out_toggle = 1
					return out_toggle
				elif event.key == pygame.K_d:
					out_toggle = 2
					return out_toggle
				elif event.key == pygame.K_s:
					out_toggle = 0
					return out_toggle
					print "input time"
				elif event.key == pygame.K_m:
					printMenu_console()
				elif event.key == pygame.K_SPACE:
					print("need method to change to 24 hour mode")
def printMenu_console():
	print "Press a for analog clock display"
	print "Press d for digital clock display"
	print "press space to change between 24 or 12 hour mode"
	print "Press s to set time"
	print "Press m for menu options"

def printMenu_display():
	display.fill(WHITE)
	my_list = ("Press a for analog clock display" , "Press d for digital clock display" , "Press space to select 24/12 hour mode" , "Press s to set time" , "Press m for menu options")
	for i in range(len(my_list)):
		message = font.render(my_list[i], 1, BLACK)	
		display.blit(message, (0, i*30 + 30))
	pygame.display.update()


#method to accept numeric keyboard input on pygame window
def input_menu():
	input_string = ''
	while True:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				#this gets input from pygame window and adds it to a string
				if event.key in (pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9 ):
					if len(input_string) < 6:
						input_string = input_string + str(event.key-48)
						print input_string
                                if len(input_string)==6:
                                        if str_input_check(input_string)[0]:
                                                return (str_input_check(input_string)[1])
                                        else:
                                                input_string = ''
						#check if input string is valid, else reset it to empty
						#need feed_HMS to accept time in '000000' string format
