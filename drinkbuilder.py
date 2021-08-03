from drink.Drink import Drink
from helpers.MenuHelper import MenuHelper

menuOption = 1

while menuOption != 0:
    MenuHelper.displayMainMenu()
    menuOption = int(input("Please enter selection: "))
    if menuOption > 4 or menuOption < 0: print("Invalid Option - Please try again")