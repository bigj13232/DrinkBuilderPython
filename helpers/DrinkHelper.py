from helpers.MenuHelper import MenuHelper
import sqlite3
from sqlite3 import Error

class DrinkHelper(object):
    @staticmethod
    def create_connection(db_file):
        """create a datbase connection to sqlite database"""
        conn = None

        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)
        return conn

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
        drinkLoop = 'X'
        while drinkLoop != 'Y':
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
            print("Entered drink directions: \r" + directions + "\n")

            drinkLoop = str(input("is the above correct?"))

        DrinkHelper.create_connection(r"drink.db")
        print("Add Drink")
    
    @staticmethod
    def editDrink():
        print("Edit Drink")

    @staticmethod
    def removeDrink():
        print("Remove Drink")

    @staticmethod
    def viewDrink():
        print("View Drink")
