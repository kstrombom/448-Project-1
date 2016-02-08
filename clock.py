import pygame, sys
from pygame.locals import *
import math
import time
import feed_HMS
from decimal import Decimal

HEIGHT = WIDTH = 400
SIZE = 60

pygame.init()
display = pygame.display.set_mode((HEIGHT,WIDTH),0,32)
font = pygame.font.Font(None, 20)

#colors
BLACK =(0,0,0)
RED = (255,0,0)
WHITE =(255,255,255)
BLUE = (0,0,255)

#r = desired radius
r = HEIGHT/2

radius = r*r

#clock center for vector start positions
center = HEIGHT/2

time_input = feed_HMS.run()

sec = time_input * ((2*math.pi)/60)
min = time_input * ((2*math.pi)/3600)
hour = time_input * ((2*math.pi)/(3600*12))

#need method to draw markers

#infinite loop to run clock
while True:
	#clear and fill the display
	display.fill(WHITE)

	for x in range(0,SIZE):
            angle = x * ((2*math.pi)/SIZE)
            y_coor = (r*.9)*(-math.cos(angle))
            x_coor = (r*.9)*(math.sin(angle))
                
            if x % 5 == 0:
                    if x == 0:
                            number = font.render("12", 1, BLACK, display)
                    else:
                            number = font.render(str(Decimal(x/5)), 1, BLACK, display)
                    display.blit(number, ((center+x_coor) - 5, (center+y_coor) - 10))
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
	
	#drawing line
	pygame.draw.line(display, RED, (center, center), (center+x_sec, center+y_sec), 2)
	pygame.draw.line(display, BLUE, (center, center), (center+x_min, center+y_min), 2)
	pygame.draw.line(display, BLACK, (center, center), (center+x_hour, center+y_hour), 2)
	
	#update display changes
	pygame.display.update()
	
	#increase by 1/60 of revolution AKA 1 second
	sec += 2*math.pi/60
	min += 2*math.pi/3600
	hour += 2*math.pi/(3600*12)	
	#time interval between each loop run set to 1 second
	time.sleep(1)
	
	#for loop used check quit command from pygame window AKA press the X to quit
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
