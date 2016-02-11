import math
import time
from settings import *
from decimal import Decimal

DISPLAY = 12



font = pygame.font.Font(None, 25)


#need method to draw markers

def draw_digital_clock(time_input):
	temp_t = time_input
	hr = temp_t/3600
	hr = hr/13+ hr%13
	temp_t = temp_t%3600
	mins = temp_t/60
	secs = temp_t%60

	#clear and fill the display
	#display.fill(WHITE)

	seconds = str(secs)
	minutes = str(mins)
	hours = str(hr)

	size = 130
	font = pygame.font.Font(None, size)


	if mins < 10 and secs < 10 and hr >= 10:
		number = font.render(":"+seconds, 1, BLACK)
		number2 = font.render(minutes, 1, BLACK)
		number3 = font.render(hours, 1, BLACK)
		colon = font.render(":", 1, BLACK)
		display.blit(number, ((center)+(size/8), (center)-(size/2)))
		display.blit(number2, ((center)-(size/2), (center)-(size/2)))
		display.blit(number3, ((center)-(size*1.5), (center)-(size/2)))
		display.blit(colon, ((center)-(size/1.5), (center)-(size/2)))
	elif mins < 10 and secs >= 10 and hr >= 10:
		number = font.render(":"+seconds, 1, BLACK)
		number2 = font.render(minutes, 1, BLACK)
		number3 = font.render(hours, 1, BLACK)
		colon = font.render(":", 1, BLACK)
		display.blit(number, ((center)+(size/16), (center)-(size/2)))
		display.blit(number2, ((center)-(size/2), (center)-(size/2)))
		display.blit(number3, ((center)-(size*1.5), (center)-(size/2)))
		display.blit(colon, ((center)-(size/1.5), (center)-(size/2)))
	elif mins < 10 and secs >= 10 and hr < 10:
		number = font.render(":"+seconds, 1, BLACK)
		number2 = font.render(minutes, 1, BLACK)
		number3 = font.render(hours, 1, BLACK)
		colon = font.render(":", 1, BLACK)
		display.blit(number, ((center)+(size/16), (center)-(size/2)))
		display.blit(number2, ((center)-(size/2), (center)-(size/2)))
		display.blit(number3, ((center)-(size), (center)-(size/2)))
		display.blit(colon, ((center)-(size/1.5), (center)-(size/2)))
	elif mins >= 10 and secs >= 10 and hr < 10:
		number = font.render(":"+seconds, 1, BLACK)
		number2 = font.render(minutes, 1, BLACK)
		number3 = font.render(hours, 1, BLACK)
		colon = font.render(":", 1, BLACK)
		display.blit(number, ((center)+(size/2), (center)-(size/2)))
		display.blit(number2, ((center)-(size/2), (center)-(size/2)))
		display.blit(number3, ((center)-(size), (center)-(size/2)))
		display.blit(colon, ((center)-(size/1.5), (center)-(size/2)))
	elif mins < 10 and secs < 10 and hr < 10:
		number = font.render(":"+seconds, 1, BLACK)
		number2 = font.render(minutes, 1, BLACK)
		number3 = font.render(hours, 1, BLACK)
		colon = font.render(":", 1, BLACK)
		display.blit(number, ((center)+(size/16), (center)-(size/2)))
		display.blit(number2, ((center)-(size/2), (center)-(size/2)))
		display.blit(number3, ((center)-(size), (center)-(size/2)))
		display.blit(colon, ((center)-(size/1.5), (center)-(size/2)))
	elif mins >= 10 and secs >= 10 and hr >= 10:
		number = font.render(":"+seconds, 1, BLACK)
		number2 = font.render(minutes, 1, BLACK)
		number3 = font.render(hours, 1, BLACK)
		colon = font.render(":", 1, BLACK)
		display.blit(number, ((center)+(size/2), (center)-(size/2)))
		display.blit(number2, ((center)-(size/2), (center)-(size/2)))
		display.blit(number3, ((center)-(size*1.5), (center)-(size/2)))
		display.blit(colon, ((center)-(size/1.5), (center)-(size/2)))

	pygame.display.update()

def draw_analog_clock(time_input):

	sec = time_input * ((2*math.pi)/60)
	min = time_input * ((2*math.pi)/3600)
	hour = time_input * ((2*math.pi)/(3600*12))


	#clear and fill the display

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

	#drawing line
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
