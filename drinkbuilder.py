from helpers.MenuHelper import MenuHelper
from helpers.DrinkHelper import DrinkHelper

menuOption = 1

while menuOption != 0:
    MenuHelper.displayMainMenu()
    menuOption = int(input("Please enter selection: "))

#    if menuOption == 1: DrinkHelper.addDrink()
#    elif menuOption == 2: DrinkHelper.editDrink()
#    elif menuOption == 3: DrinkHelper.removeDrink()
#    elif menuOption == 4: DrinkHelper.viewDrink()
#    elif menuOption == 5: DrinkHelper.addFromFile()
#    elif menuOption > 5 or menuOption < 0: print("Invalid Option - Please try again")

    match menuOption:
        case 0:
            print("Quitting.")
        case 1:
            DrinkHelper.addDrink()
        case 2:
            DrinkHelper.editDrink()
        case 3:
            DrinkHelper.removeDrink()
        case 4:
            DrinkHelper.viewDrink()
        case 5:
            DrinkHelper.addFromFile()
        case 6:
            DrinkHelper.addToDatabase()
        case _:
            print("Invalid option - Please enter valid option")