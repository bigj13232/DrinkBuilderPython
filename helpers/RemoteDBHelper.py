import mysql.connector
from mysql.connector import Error
from helpers.DatabaseHelper import DatabaseHelper

class RemoteDBHelper():
    def get_cursor():
        conn = mysql.connector.connect(
        host="192.168.0.87",
        user="drinkuser",
        password="chowman",
        database="drinkdb"
        )

        cursor = conn.cursor()
        return conn, cursor

    def insert_drink(drink):
        conn, cursor = RemoteDBHelper.get_cursor()

        print("inserting drink")
        insert_query = """INSERT INTO drinks (name, source, origin, directions, mocktail, drink_source, drink_source_url) VALUES (%s, %s, %s, %s, %s, %s, %s)"""

        # Execute and commit
        cursor.execute(insert_query, drink.toInsert())
        conn.commit()

        print("Inserted row with ID:", cursor.lastrowid)

        last_id = cursor.lastrowid

        # Clean up
        cursor.close()
        conn.close()

        return last_id


    def insert_ingredient(cur_row, ingredient):
        #   insert ingredient into database
        #   :param: cur_row
        #   :param: ingredient

        conn, cursor = RemoteDBHelper.get_cursor()

        sql = """INSERT INTO ingredients (drink_id, amount, measurement, name, type) VALUES (%s, %s, %s, %s, %s)"""
        ingredient_variables = DatabaseHelper.createIngredientArray(cur_row, ingredient)
      
        cursor.execute(sql, ingredient_variables)
        conn.commit()
        print("inserting ingredient")