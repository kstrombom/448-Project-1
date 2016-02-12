#----------------------------
#WORK IN PROGRESS
#----------------------------
from settings import *
import math
import time
from feed_HMS import *

#need method to draw instruction in display
#font = pygame.font.Font("Anita semi square.ttf", 25)
font = pygame.font.Font("Anita semi square.ttf", 20)
number = font.render("12", 1, BLACK)

def runMenu():
	printMenu_console()
	printMenu_display()
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
					pygame.quit()
					sys.exit()
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
					print ("input time")
				elif event.key == pygame.K_m:
					printMenu_console()
				elif event.key == pygame.K_SPACE:
					print("need method to change to 24 hour mode")
def printMenu_console():
	print ("Press a for analog clock display")
	print ("Press d for digital clock display")
	print ("press space to change between 24 or 12 hour mode")
	print ("Press s to set time")
	print ("Press m for menu options")
	print ("Press w to toggle through sounds")

def printMenu_display():
	display.fill(PALE_BLUE)
	my_list = ("A for analog clock" , "D for digital clock" , "SPACE for 24/12 hr mode" , "S to set time" , "M for menu options","W to select tick sound")
	for i in range(len(my_list)):
		message = font.render(my_list[i], 1, WHITE)
		display.blit(message, (8, i*45 + 30))
	pygame.display.update()

def draw_string(string_in,x,y):
	time_str = font.render(string_in, 1, WHITE)
	display.blit(time_str, (x, y))
	pygame.display.update()


#method to accept numeric keyboard input on pygame window
def input_menu():
	i = 0
	input_string = list("00:00:00")
	while True:
		draw_string("Input Time (00:00:00-23:59:59):",10,6*45 + 30)
		draw_string(''.join(input_string),8,7*45 + 30)
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key in (pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9 ):
					if i <= 8:
						if input_string[i] == ':':
							i += 1
							input_string[i] = str(event.key-48)
							i += 1
						else:
							input_string[i] = str(event.key-48)
							i += 1
						display.fill(PALE_BLUE)
						printMenu_display()
						draw_string(''.join(input_string),8,7*45 + 30)
						print (input_string)
						if i == 8:
							if str_input_check(input_string)[0]:
								draw_string("Time Set Successfully!",130,7*45 + 30)
								i = 0
								time.sleep(0.2)
								return (str_input_check(input_string)[1])
							else:
								draw_string("Invalid input try again!",130,7*45 + 30)
								time.sleep(1.5)
								i = 0
								display.fill(PALE_BLUE)
								printMenu_display()
								input_string = list("00:00:00")
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
	time.sleep(0.1)
