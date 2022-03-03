from helpers.MenuHelper import MenuHelper
from helpers.DrinkHelper import DrinkHelper
from helpers.AWSHelper import AWSHelper

menuOption = 1

while menuOption != 0:
    MenuHelper.displayMainMenu()
    menuOption = int(input("Please enter selection: "))

    if menuOption == 1: DrinkHelper.addDrink()
    elif menuOption == 2: DrinkHelper.editDrink()
    elif menuOption == 3: DrinkHelper.removeDrink()
    elif menuOption == 4: DrinkHelper.viewDrink()
    elif menuOption == 5: DrinkHelper.addFromFile()
    elif menuOption == 6: AWSHelper.addToAWS()