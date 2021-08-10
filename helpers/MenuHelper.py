from enums import Source
from enums import Measurements

class MenuHelper():
    @staticmethod
    def displayMainMenu():
        menuOptions = ["Please select a menu option from below:","1: Add a drink to the database","2: Edit a drink in the database","3: Remove a drink in the database","4: View a drink","0: Exit"]
        for i in menuOptions:
            print(i + "\n")

    @staticmethod
    def displaySources():
        sourceCount = 1
        for source in Source:
            print(sourceCount + ") " + source)
            sourceCount+=1

    @staticmethod
    def displayMeasurements():
        measurementCount = 1
        for measurement in Measurements:
            print(measurementCount + ") " + measurement)
            measurementCount+=1

