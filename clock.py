import math
import time
from settings import *
import tick_sound # our mudule
from decimal import Decimal

DISPLAY = 12


font = pygame.font.Font(None, 25)

#sound, pre-loaded
# sounds below are open-sourced -- from soundbible.com
slap = pygame.mixer.Sound('slap.wav')
woosh = pygame.mixer.Sound('woosh.wav')
punch = pygame.mixer.Sound('punch.wav')

#choose sound
sound = None
#sound = tick_sound.import_sound(slap,woosh,punch)


#need method to draw markers

#infinite loop to run clock
def draw_analog_clock(time_input):
	
	sec = time_input * ((2*math.pi)/60)
	min = time_input * ((2*math.pi)/3600)
	hour = time_input * ((2*math.pi)/(3600*12))	
	
	#play sound
	if(sound != None):
		sound.play()

	#clear and fill the display
	if ANALOG == 0:
                temp = time_input
                seconds = temp % 60
                minutes = time_input % 3600
                temp = temp/3600
                hours = temp

                time_string = font.render("%02d:%02d:%02d" % (hours, minutes, seconds), 1, BLACK)
                display.blit(time_string, (center, center))
                

	elif ANALOG == 1:
                #draw the clock display
                for x in range(0,60):
                    angle = x * ((2*math.pi)/60)
                    y_coor = (r*.9)*(-math.cos(angle))
                    x_coor = (r*.9)*(math.sin(angle))

                    #draw the numbers representing hours
                    if x % 5 == 0:
                            if x == 0:
                                    #indicate that the time is between 0 and 12
                                    if DISPLAY == 24 and time_input < 43200:
                                            number = font.render("12", 1, BLACK)
                                            number2 = font.render("24", 1, RED)
                                    #indicate that the time is between 13 and 24
                                    elif DISPLAY == 24 and time_input >= 43200:
                                            number = font.render("12", 1, RED)
                                            number2 = font.render("24", 1, BLACK)
                                    #assume the user has it on a 12 hour cycle
                                    elif DISPLAY == 12:
                                            number = font.render("12", 1, BLACK)
                            else:
                                    #indicate that the time is between 0 and 12
                                    if DISPLAY == 24 and time_input < 43200:
                                            number = font.render(str(Decimal(x/5)), 1, BLACK)
                                            number2 = font.render(str(Decimal(x/5)+12), 1, RED)
                                    #indicate that the time is between 13 and 24
                                    if DISPLAY == 24 and time_input >= 43200:
                                            number = font.render(str(Decimal(x/5)), 1, RED)
                                            number2 = font.render(str(Decimal((x/5)+12)), 1, BLACK)
                                    #assume the user has it on a 12 hour cycle
                                    elif DISPLAY == 12:
                                            number = font.render(str(Decimal(x/5)), 1, BLACK)

                            display.blit(number, ((center+x_coor) - 5, (center+y_coor) - 10))
                            if DISPLAY == 24:
                                    display.blit(number2, (center+(x_coor*.8) - 5, center+(y_coor*.8) - 10))

                    #draw the lines between the numbers

	
	#display.fill(WHITE)

        #draw the clock display
	for x in range(0,60):
            angle = x * ((2*math.pi)/60)
            y_coor = (r*.9)*(-math.cos(angle))
            x_coor = (r*.9)*(math.sin(angle))

            #draw the numbers representing hours
            if x % 5 == 0:
                    if x == 0:
                            #indicate that the time is between 0 and 12
                            if DISPLAY == 24 and time_input < 43200:
                                    number = font.render("12", 1, BLACK)
                                    number2 = font.render("24", 1, RED)
                            #indicate that the time is between 13 and 24
                            elif DISPLAY == 24 and time_input >= 43200:
                                    number = font.render("12", 1, RED)
                                    number2 = font.render("24", 1, BLACK)
                            #assume the user has it on a 12 hour cycle
                            elif DISPLAY == 12:
                                    number = font.render("12", 1, BLACK)

                    else:
                         pygame.draw.line(display, BLACK, (center+(x_coor*.97),center+(y_coor*.97)), (center+(x_coor*1.03), center+(y_coor*1.03)), 1)

	#draw markers

	#math function to determine end of vector position
	y_sec = (r*.75)*(-math.cos(sec))
	x_sec = (r*.75)*(math.sin(sec))

	y_min = (r*.6)*(-math.cos(min))
	x_min = (r*.6)*(math.sin(min))

	y_hour = (r*.45)*(-math.cos(hour))
	x_hour = (r*.45)*(math.sin(hour))

        #Display AM or PM if in 12 hour mode
	if DISPLAY==12:
                if time_input < 43200:
                        side = font.render("AM", 1, BLACK)
                elif time_input >= 43200:
                        side = font.render("PM", 1, BLACK)

                display.blit(side, (center-10,center+25))

	#drawing line for analog
	pygame.draw.line(display, RED, (center, center), (center+x_sec, center+y_sec), 2)
	pygame.draw.line(display, BLUE, (center, center), (center+x_min, center+y_min), 2)
	pygame.draw.line(display, BLACK, (center, center), (center+x_hour, center+y_hour), 2)

	#update display changes
	pygame.display.update()

        #reset time_input if it reaches the end of the 24 hour period
	if time_input == 86400:
                time_input = 0

	#increase by 1/60 of revolution AKA 1 second
	sec += 2*math.pi/60
	min += 2*math.pi/(3600)
	hour += 2*math.pi/(3600*12)
