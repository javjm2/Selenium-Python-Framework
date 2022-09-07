import pyodbc
import os


class Helpers:
    @staticmethod
    def read_database_values(column, table):
        db = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                            f'Server={os.environ.get("SERVER_NAME")};'
                            f'Database={os.environ.get("DATABASE_NAME")};'
                            f'Trusted_Connection={os.environ.get("CONNECTION")};')
        cursor = db.cursor()
        cursor.execute(f'SELECT {column} FROM {table}')
        values = cursor.fetchall()
        values = [j for i in values for j in i]
        return values

