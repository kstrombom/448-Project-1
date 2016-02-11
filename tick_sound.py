import pygame.mixer


pygame.init()


sound_range = [1,2,3,4]


#sound, pre-loaded
# sounds below are open-sourced -- from soundbible.com
slap = pygame.mixer.Sound('slap.wav')
woosh = pygame.mixer.Sound('woosh.wav')
punch = pygame.mixer.Sound('punch.wav')

def sound_menu():
    print("Please enter your tick: \n1)Slap tick\n2)Woosh tick\n3)Punch tick\n4)No tick")


def import_sound():
    choice = -1
    print("\n[Bouns -- Artificial tick!]")


    while choice not in sound_range:
        sound_menu()
        print("\nYou choose: ")
        choice = input()
        int(choice)

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
