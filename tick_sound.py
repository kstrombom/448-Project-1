import pygame.mixer


pygame.init()


sound_range = [1,2,3,4]


def sound_menu():
    print("Please enter your tick: \n1)Slap tick\n2)Woosh tick\n3)Punch tick\n4)No tick")


def import_sound(slapping, wooshing, punch):
    choice = -1
    print("Bouns -- Artificial tick")


    while choice not in sound_range:
        sound_menu()
        choice = input()
        int(choice)

        try:
            if choice == 1:
                return slapping
            elif choice == 2:
                return wooshing
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
