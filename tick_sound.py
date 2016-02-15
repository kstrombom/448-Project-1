"""
@file: tick_sound.py
@author: Diego Soliz, Shane Chu, Michael Bechtel, Connor Welsh, Dustin Wendt
@date: 2016.02.14
@brief: Tick sound class. Used to play the user's desired tick sound.
"""

import pygame.mixer

pygame.init()
# sound, pre-loaded
# sounds below are open-sourced -- from soundbible.com
slap = pygame.mixer.Sound('slap.wav')
woosh = pygame.mixer.Sound('woosh.wav')
punch = pygame.mixer.Sound('punch.wav')

def sound_menu():
    #prompt user for tick sound
    print("Please enter your tick: \n1)Slap tick\n2)Woosh tick\n3)Punch tick\n4)No tick\nYou choose: ")

def import_sound():
    choice = -1
    print("\n[Bouns -- Artificial tick!]")

    #get tick sound choice from user
    while choice not in [1,2,3,4]:
        sound_menu()
        choice = int(input())

        #return sound that the user chose
        try:
            if choice == 1:
                return slap
            elif choice == 2:
                return woosh
            elif choice == 3:
                return punch
            elif choice == 4:
                print("OK. NO SOUND.")
            else:
                choice = -1
                print("Please enter a valid option.")

        except:
            choice = -1
            print ("User entered a non-numeric argument.")

def select_sound_display(choice):
	#show the selected sound
	if choice == 1:
		print("Slap Sound")
		return slap
	elif choice == 2:
		print("Woosh Sound")
		return woosh
	elif choice == 3:
		print("Punch Sound")
		return punch
	elif choice == 4:
		print("OK. NO SOUND.")
