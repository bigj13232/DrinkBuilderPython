from helpers.MenuHelper import MenuHelper
from drink.Drink import Drink
from drink.Ingredient import Ingredient
import sqlite3
from sqlite3 import Error

class DrinkHelper(object):
    @staticmethod
    def create_connection():
        """create a datbase connection to sqlite database"""
        conn = None

        try:
            conn = sqlite3.connect(r"drink.db")
        except Error as e:
            print(e)
        return conn

    #Return array of drink variables
    def createDrinkArray(drink):
        sql_variables = (drink.name, drink.source, drink.origin,drink.directions, drink.isMocktail)
        return sql_variables

    #Return array of ingredient variables
    def createIngredientArray(row_id, ingredient):
        sql_variables = (row_id, ingredient.amount, ingredient.measurement, ingredient.name, ingredient.type)
        return sql_variables

    def insert_drink(drink):
        sql = ''' INSERT INTO drink(name,source,origin,directions,mocktail) VALUES(?,?,?,?,?) '''
        drink_variables = DrinkHelper.createDrinkArray(drink)
        conn = DrinkHelper.create_connection()
        cur = conn.cursor()
        cur.execute(sql, drink_variables)
        conn.commit()

    def insert_ingredient(cur_row, ingredient):
        sql = ''' INSERT INTO ingredient(cur_row,amount,measurement,name,type) VALUES(?,?,?,?,?)'''
        ingredient_variables = DrinkHelper.createIngredientArray(ingredient)
        conn = DrinkHelper.create_connection()
        cur = conn.cursor()
        cur.execute(sql, ingredient_variables)
        conn.commit()
        
    @staticmethod
    def create_table(conn, create_table_sql):
        #   create table from the create_table_sql statement
        #   :param conn: Connecion object
        #   :param create_table_sql: a CREATE TABLE statement
        #   :return: none
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    @staticmethod
    def addDrink():
        drinkLoop = 'Y'
        while drinkLoop == 'Y':
            name = input("Enter drink name: ")
            MenuHelper.displaySources()
            sourceChoice = int(-1)
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

            origin = str(input("Enter drink origin: "))
            directions = str(input("Enter drink directions: "))

            mocktailAnswer = str(input("Is the drink a mocktail? T/F "))

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

            drinkLoop = str(input("is the above correct?"))

            addDrink = Drink(name, source, origin, directions, mocktail)

            addingIngredientsLoop = 'Y'
            correctIngredientsLoop = 'N'
            while(addingIngredientsLoop == 'Y'):
                while(correctIngredientsLoop == 'N'):
                    #Get Ingredient amount
                    ingredientAmount = input("Enter ingredient amount: ")

                    #Get Ingredient measurement
                    #begin ingredient measurement loop
                    sourceChoice = int(-1)
                    while(int(sourceChoice) <=0 or int(sourceChoice) > 3):
                        MenuHelper.displayMeasurements()
                        sourceChoice = int(input("Enter selection: "))
                        if (sourceChoice == 1): ingredientMeasurement = 'Ounce(s)'
                        elif (sourceChoice == 2): ingredientMeasurement = 'ML'
                        elif (sourceChoice == 3): ingredientMeasurement = 'each'
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

                addingIngredientsLoop = input("Do you have more ingredients to add? Y/N")
            #end addingIngredientsLoop
            insert_row = DrinkHelper.insert_drink(addDrink)
            drinkLoop = input("Do you wish to add another drink")
        #end drinkLoop
    
    @staticmethod
    def editDrink():
        print("Edit Drink")

    @staticmethod
    def removeDrink():
        print("Remove Drink")

    @staticmethod
    def viewDrink():
        print("View Drink")
