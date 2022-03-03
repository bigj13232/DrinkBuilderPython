from drink.Drink import Drink
from drink.Ingredient import Ingredient
from helpers.MenuHelper import MenuHelper

class AWSHelper(object):
    @staticmethod
    def checkConnection():
        print("Check Connection")

    @staticmethod
    def addDrinkAWS():
        print("Add drink manually")

    @staticmethod
    def addDrinkFileAWS():
        print("Add drinks from file")

    def addToAWS():
        menuOption = 1

        print("Pushing to AWS")

        while menuOption != 0:
            MenuHelper.displayAWSMenu()
            menuOption = int(input("Please enter selection: "))

            if menuOption == 1: AWSHelper.checkConnection()
            elif menuOption == 2: AWSHelper.addDrinkAWS()
            elif menuOption == 3: AWSHelper.addDrinkFileAWS()
            elif menuOption > 3 or menuOption < 0: print("Invalid Option - Please try again")