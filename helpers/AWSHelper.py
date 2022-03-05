from drink.Drink import Drink
from drink.Ingredient import Ingredient
from helpers.MenuHelper import MenuHelper

import pandas as pd
import pymysql

class AWSHelper(object):
    @staticmethod
    def getConnection():
        host="drinkbuilder-test.c4gyhhqjwthj.us-east-2.rds.amazonaws.com"
        port=3306
        dbname="drinkbuildertest"
        user="admin"
        password="chowmanchowman1!"
        conn = pymysql.connect(host=host, user=user,port=port,passwd=password,db=dbname)        
        return conn
    
    @staticmethod
    def checkConnection():
        print("Check Connection")

        dbConn = AWSHelper.getConnection()

        print(dbConn.is_connected())
    

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