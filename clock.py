"""
@file: clock.py
@author: Diego Soliz, Shane Chu, Michael Bechtel, Connor Welsh, Dustin Wendt
@date: 2016.02.14
@brief: Clock class. Used to draw analog or digital clocks in pygame window.
"""

import math
import time
from settings import *
from decimal import Decimal

DISPLAY = 12

font = pygame.font.Font("Vonique_64_Bold.ttf", 30)

# switch between 12 and 24 hours
def changeDisplay():

        #tell method to use DISPLAY variable declared at the top of the class
        global DISPLAY

        #complement the value of DISPLAY
        if DISPLAY == 12:
                DISPLAY = 24
        elif DISPLAY == 24:
                DISPLAY = 12

######################################################################
############################### DIGITAL ##############################
######################################################################

# draw digital clock
def draw_digital_clock (curr_time, curr_count):

	# variables:
	temp_t = curr_time
	# hour
	hr = temp_t / 3600
        if DISPLAY == 12:
            hr = hr / 13 + hr % 13
	hours = str (hr)            
	temp_t = temp_t%3600
	# minutes
	mins = temp_t / 60
	minutes = str (mins)
	# seconds
	secs = temp_t % 60
	seconds = str (secs)
	# size
	size = 130

	# font -- number display
	font = pygame.font.Font ("Open 24 Display St.ttf", 80)
	# font -- am / pm 
	font2 = pygame.font.Font ("Open 24 Display St.ttf", 40)

        # single digit seconds
	if secs < 10:
                # render seconds with an additional 0
                number = font.render (":0"+seconds, 1, WHITE)
        else:
                # render seconds normally
                number = font.render (":"+seconds, 1, WHITE)

        # single digit minutes
        if mins < 10:
                # render minutes with an additional 0
                number2 = font.render (":0"+minutes, 1, WHITE)
        else:
                # render minutes normally
                number2 = font.render (":"+minutes, 1, WHITE)

        # 12 hour display
        if DISPLAY == 12:
        	if (hr == 0):
               		# change the 0 hour mark to 12 for 12 hour mode
               		number3 = font.render ("12", 1, WHITE)
               		display.blit (number3, (center - size, center - (size / 2)))
            	elif (hr < 10):
                	# render hours normally but display then more to the right than normal
                	number3 = font.render (hours, 1, WHITE)
                	display.blit (number3, (center - (size / 1.25), center - (size / 2)))
            	else:
                    	# display remaining hours that aren't accounted for above
                    	if (hr == 10 or hr == 11 or hr == 12):
                       		number3 = font.render(hours, 1, WHITE)
                        	display.blit(number3, (center - size, center - (size / 2)))
                    	# display adjusted hour variable so that hours above 12 don't get displayed
                    	if (DISPLAY == 12 and hr > 12):
                        	number3 = font.render (hours, 1, WHITE)
                        	display.blit(number3, (center - size, center - (size / 2)))
                    	elif (DISPLAY == 24 and hr > 12):
                        	number3 = font.render(temp, 1, WHITE)
                        	display.blit (number3, (center - size, center - (size / 2)))

		# am
            	if (curr_time < 43200):
                	# print AM if total seconds is less than 12 hours
			period = font2.render ("AM", 1, WHITE)
			display.blit (period, (center + size, center - (size / 2)))
		# pm
            	else:
                	# print PM if total seconds is greater than 12 hours
                	period = font2.render ("PM", 1, WHITE)
			display.blit (period, (center + size, center - (size / 7)))

	# 24 hour display
        elif (DISPLAY == 24):
            	if (hr < 10):
                    	# print hours more to the right if single digit
                    	number3 = font.render(hours, 1, WHITE)
                    	display.blit (number3, (center - (size / 1.25), center - (size / 2)))
            	else:
                	# print hours not accounted for
                    	if (hr == 10 or hr == 11 or hr == 12):
                        	number3 = font.render(hours, 1, WHITE)
                        	display.blit (number3, (center - size, center - (size / 2)))
                    	elif (hr > 12):
                        	number3 = font.render(hours, 1, WHITE)
                        	display.blit (number3, (center - size, center-(size/2)))

        # display the seconds and minutes
        display.blit (number, (center + (size / 5), center - (size / 2)))
	display.blit (number2, (center - (size / 2), center - (size / 2)))

	# display day of the week
	day = ""
	if (curr_count == 1):
		day = "MONDAY"
	elif (curr_count == 2):
		day = "TUESDAY"
	elif (curr_count == 3):
		day = "WEDNESDAY"
	elif (curr_count == 4):
		day = "THURSDAY"
	elif (curr_count == 5):
		day = "FRIDAY"
	elif (curr_count == 6):
		day = "SATURDAY"
	elif (curr_count == 7):
		day = "SUNDAY"
	
	day = font2.render (day, 1, WHITE)
	display.blit (day, (center - (size / 2), center + (size / 2)))
		
        # update the window
	pygame.display.update()

######################################################################
################################ ANALOG ##############################
######################################################################

def draw_analog_clock(curr_time, curr_count):
        #calculate the seconds, minutes, and hour
	sec = curr_time * ((2*math.pi)/60)
	min = curr_time * ((2*math.pi)/3600)
	hour = curr_time * ((2*math.pi)/(3600*12))

        #draw the clock display
	for x in range(0,60):
            angle = x * ((2*math.pi)/60)
            y_coor = (r*.9)*(-math.cos(angle))
            x_coor = (r*.9)*(math.sin(angle))

            #draw the numbers representing hours
            if x % 5 == 0:
                    if x == 0:
                            #indicate that the time is between 0 and 12
                            if DISPLAY == 24 and curr_time < 43200:
                                    number = font.render("12", 1, WHITE)
                                    number2 = font.render("24", 1, RED)
                            #indicate that the time is between 13 and 24
                            elif DISPLAY == 24 and curr_time >= 43200:
                                    number = font.render("12", 1, RED)
                                    number2 = font.render("24", 1, WHITE)
                            #assume the user has it on a 12 hour cycle
                            elif DISPLAY == 12:
                                    number = font.render("12", 1, WHITE)
                    else:
                            #indicate that the time is between 0 and 12
                            if DISPLAY == 24 and curr_time < 43200:
                                    number = font.render(str(Decimal(x/5)), 1, WHITE)
                                    number2 = font.render(str(Decimal(x/5)+12), 1, RED)
                            #indicate that the time is between 13 and 24
                            if DISPLAY == 24 and curr_time >= 43200:
                                    number = font.render(str(Decimal(x/5)), 1, RED)
                                    number2 = font.render(str(Decimal((x/5)+12)), 1, WHITE)
                            #assume the user has it on a 12 hour cycle
                            elif DISPLAY == 12:
                                    number = font.render(str(Decimal(x/5)), 1, WHITE)

                    display.blit(number, ((center+x_coor) - 5, (center+y_coor) - 10))
                    if DISPLAY == 24:
                            display.blit(number2, (center+(x_coor*.8) - 5, center+(y_coor*.8) - 10))

            #draw the lines between the numbers
            else:
                 pygame.draw.line(display, WHITE, (center+(x_coor*.97),center+(y_coor*.97)), (center+(x_coor*1.03), center+(y_coor*1.03)), 1)

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
                if curr_time < 43200:
                        side = font.render("AM", 1, WHITE)
                elif curr_time >= 43200:
                        side = font.render("PM", 1, WHITE)

                display.blit(side, (center-10,center+25))
                
	# display day of the week
	day = ""
	if (curr_count == 1):
		day = "MONDAY"
	elif (curr_count == 2):
		day = "TUESDAY"
	elif (curr_count == 3):
		day = "WEDNESDAY"
	elif (curr_count == 4):
		day = "THURSDAY"
	elif (curr_count == 5):
		day = "FRIDAY"
	elif (curr_count == 6):
		day = "SATURDAY"
	elif (curr_count == 7):
		day = "SUNDAY"
	
	day = font.render (day, 1, WHITE)
	display.blit (day, (center - 35, center + 50))

	#drawing line
	pygame.draw.line(display, BLACK, (center, center), (center+x_hour, center+y_hour), 5)
	pygame.draw.line(display, BLUE, (center, center), (center+x_min, center+y_min), 4)
	pygame.draw.line(display, RED, (center, center), (center+x_sec, center+y_sec), 3)


	#update display changes
	pygame.display.update()

        #reset curr_time if it reaches the end of the 24 hour period
	if curr_time == 86400:
                curr_time = 0

	#increase by 1/60 of revolution AKA 1 second
	sec += 2*math.pi/60
	min += 2*math.pi/(3600)
	hour += 2*math.pi/(3600*12)

