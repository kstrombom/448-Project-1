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
	printMenu()
	while True:
		for event in pygame.event.get():		
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a:
					toggle = 1
			
				elif event.key == pygame.K_d:
					toggle = 2
				
				elif event.key == pygame.K_s:
					time_input = feed_HMS.run()
					print "time set press x to load clock"
					
				elif event.key == pygame.K_m:
					printMenu()
				elif event.key == pygame.K_x:
					return


def printMenu():
	print "Press a for analog clock display"
	print "Press d for digital clock display"
	print "Press s to set time"
	print "Press m for menu options"

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
