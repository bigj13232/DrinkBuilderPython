from helpers.DatabaseHelper import DatabaseHelper
from helpers.MenuHelper import MenuHelper
from helpers.XMLHelper import XMLHelper

from drink.Drink import Drink
from drink.Ingredient import Ingredient


class DrinkHelper(object):
    @staticmethod
    def addDrink():
        #   Gather drink/ingredient details and add to database
        drinkLoop = 'Y'
        
        #begin drinkLoop loop
        while drinkLoop == 'Y':
            #Get drink name
            name = input("Enter drink name: ")
            MenuHelper.displaySources()
            
            #Get drink source
            sourceChoice = int(-1)            
            #begin sourceChoice loop
            while(sourceChoice <=0 or sourceChoice > 8):
                sourceChoice = int(input("Enter drink source: "))
                if sourceChoice == 1: source = "Anime"
                elif sourceChoice == 2: source = "Books"
                elif sourceChoice == 3: source = "Cartoons"
                elif sourceChoice == 4: source = "Comic Books"
                elif sourceChoice == 5: source = "Games"
                elif sourceChoice == 6: source = "Movies"
                elif sourceChoice == 7: source = "TV"
                elif sourceChoice == 8: source = "Video Games"
                else: print("Invalid Choice - Try again.")
            #end sourceChoice loop

            #Get drink origin
            origin = str(input("Enter drink origin: "))

            #Get drink direcrions
            directions = str(input("Enter drink directions: "))

            #Get whether or not drink is a mocktail(T/F)
            mocktailAnswer = str(input("Is the drink a mocktail? T/F: "))
            mocktail = -1
            if mocktailAnswer == 'T': mocktail = 1
            elif mocktailAnswer == 'F': mocktail = 0

            #   Confirm drink details
            print("Entered drink name:   " + name)
            print("Entered drink source: " + source)
            print("Entered drink origin: " + origin)
            if mocktail == 1: print("Entered cocktail is a mocktail")
            elif mocktail == 0: print("Entered cocktail is not a mocktail")
            else: print("Mocktail option invalid - " + str(mocktail))
            print("Entered drink directions: \n" + directions)
            drinkLoop = str(input("is the above correct? "))

            #Create drink w/o ingredients
            addDrink = Drink(name, source, origin, directions, mocktail)

            addingIngredientsLoop = 'Y'
           

            #Begin addingIngredientsLoop loop
            while(addingIngredientsLoop == 'Y'):
                correctIngredientsLoop = 'N'
                #Begin correctIngredientsLoop loop
                while(correctIngredientsLoop == 'N'):
                    #Get Ingredient amount
                    ingredientAmount = input("Enter ingredient amount: ")

                    #Get Ingredient measurement
                    #begin ingredient measurement loop
                    sourceChoice = int(-1)
                    while(int(sourceChoice) <=0 or int(sourceChoice) > 4):
                        MenuHelper.displayMeasurements()
                        sourceChoice = int(input("Enter selection: "))
                        if (sourceChoice == 1): ingredientMeasurement = 'Ounce(s)'
                        elif (sourceChoice == 2): ingredientMeasurement = 'ML'
                        elif (sourceChoice == 3): ingredientMeasurement = 'each'
                        elif (sourceChoice == 4): ingredientMeasurement = 'dash(s)'
                        else: print("Invalid Option( " + sourceChoice + " ) - Try Again.")                   
                    #end ingredientMeasurementAnswer

                    #Get ingredient name
                    ingredientName = input("Enter ingredient name: ")

                    #Get ingredient type
                    ingredientType = input("Enter ingredient type: ")

                    ingredient = Ingredient(ingredientAmount, ingredientMeasurement, ingredientName, ingredientType)
                    ingredient.toString()
                    correctIngredientsLoop = input("Is the above correct? Y/N ")
                    if (correctIngredientsLoop == 'N'): ingredient = None
                #end correctIngredientsLoop

                addDrink.addIngredient(ingredient)
                print("Added Ingredients: \n")
                addDrink.listIngredients()
                addingIngredientsLoop = input("Do you have more ingredients to add? Y/N ")
            #end addingIngredientsLoop

            #Insert drink into database and get last row
            insert_row = DatabaseHelper.insert_drink(addDrink)

            print("Insert row is: " + str(insert_row))

            #Iterate through drink ingredients and add them to database
            for ingredient in addDrink.ingredients:
                DatabaseHelper.insert_ingredient(insert_row, ingredient)
            drinkLoop = input("Do you wish to add another drink? ")
        #end drinkLoop
    

    @staticmethod
    def editDrink():
        drink_name = input("Enter drink name to search for: ")


    @staticmethod
    def removeDrink():
        print("Remove Drink")

    @staticmethod
    def viewDrink():
        print("View Drink")

    def chunker(seq, size):
        return (seq[pos:pos + size] for pos in range(0, len(seq), size))

    @staticmethod
    def addFromFile():
        #Open text file, parse to drink_lines variable
        with open('drinks.txt', 'r') as drinks_text:
            drink_lines = drinks_text.readlines()
            

        line_count = 0
        for line in drink_lines:
            line_count+=1
            #Odd Numbered Lines contain drink details
            if line_count % 2 == 1:
                drink_details = line.split("|")
                print("Getting Drink details")
                drinkName = drink_details[0]
                drinkSource = drink_details[1]
                drinkOrigin = drink_details[2]
                drinkMocktail = drink_details[3]
                drinkDirectionsList = []
                for i in drink_details[4:]:
                    drinkDirectionsList.append(i)

                drinkDirections = XMLHelper.createXML(drinkDirectionsList)
                ###print(drinkDirections)
                addDrink = Drink(drinkName,drinkSource,drinkOrigin,drinkDirections,drinkMocktail)
            #Even numbered lines contain ingredient details
            elif line_count % 2 == 0:
                ingredient_list = line.split("|")

                for ingredients in DrinkHelper.chunker(ingredient_list, 4):
                    ingredient = Ingredient(ingredients[0], ingredients[1], ingredients[2], ingredients[3])
                    addDrink.addIngredient(ingredient)
                row = DatabaseHelper.insert_drink(addDrink)

                for ingredient in addDrink.ingredients:
                    DatabaseHelper.insert_ingredient(row, ingredient)

                    
