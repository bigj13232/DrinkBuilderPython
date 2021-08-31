import sqlite3
from sqlite3 import Error


class DatabaseHelper():
    def createDrinkArray(drink):
        #   creates drink variables to pass into sql execution
        #   :param: drink
        #   :return: sql_variables
        sql_variables = (drink.name, drink.source, drink.origin,drink.directions, drink.isMocktail)
        return sql_variables
    def createIngredientArray(row_id, ingredient):
        #   creates ingredient variables to pass into sql execution
        #   :param: row_id
        #   :param: ingredient
        #   :return: sql_variables
        sql_variables = (row_id, ingredient.amount, ingredient.measurement, ingredient.name, ingredient.type)
        return sql_variables    
    @staticmethod
    def create_connection():
        #   create database connection
        #   :return: conn
        """create a datbase connection to sqlite database"""
        conn = None
        try:
            conn = sqlite3.connect(r"drink.db")
        except Error as e:
            print(e)
        return conn
    def insert_drink(drink):
        #   inserts drink into database
        #   :param: drink
        sql = ''' INSERT INTO drinks(name,source,origin,directions,mocktail) VALUES(?,?,?,?,?) '''
        drink_variables = DatabaseHelper.createDrinkArray(drink)
        conn = DatabaseHelper.create_connection()
        cur = conn.cursor()
        cur.execute(sql, drink_variables)
        conn.commit()
        return cur.lastrowid
    def insert_ingredient(cur_row, ingredient):
        #   insert ingredient into database
        #   :param: cur_row
        #   :param: ingredient
        sql = ''' INSERT INTO ingredients(drink_id,amount,measurement,name,type) VALUES(?,?,?,?,?)'''
        ingredient_variables = DatabaseHelper.createIngredientArray(cur_row, ingredient)
        conn = DatabaseHelper.create_connection()
        cur = conn.cursor()
        cur.execute(sql, ingredient_variables)
        conn.commit()
