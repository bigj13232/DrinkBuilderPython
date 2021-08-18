from drink.Drink import Drink
from helpers.MenuHelper import MenuHelper
from helpers.DrinkHelper import DrinkHelper

menuOption = 1

while menuOption != 0:
    MenuHelper.displayMainMenu()
    menuOption = int(input("Please enter selection: "))

    if menuOption == 1: DrinkHelper.addDrink()
    elif menuOption == 2: DrinkHelper.editDrink()
    elif menuOption == 3: DrinkHelper.removeDrink()
    elif menuOption == 4: DrinkHelper.viewDrink()
    elif menuOption == 5: Drink.updateDrink()
    elif menuOption > 5 or menuOption < 0: print("Invalid Option - Please try again")