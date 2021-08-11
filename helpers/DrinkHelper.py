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
    def addDrink():
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
