import sqlite3


class SQLUtil:

    def read_data(self, column, table):
        with sqlite3.connect("C:/python appium/user_info.db") as db:
            cursor = db.cursor()

        cursor.execute(f"SELECT {column} FROM {table}")
        values = cursor.fetchall()
        return values
