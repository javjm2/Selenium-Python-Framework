from contextlib import contextmanager
import pyodbc
import os


class SQLHelpers:
    @contextmanager
    def connect_to_database(self):
        db_connection = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                            f'Server=Test;'
                            f'Database=Random;'
                            f'Trusted_Connection=yes;')
        try:
            yield db_connection
        finally:
            db_connection.close()

    @contextmanager
    def cursor(self):
        with self.connect_to_database() as conn:
            cursor = conn.cursor()
            try:
                yield cursor
            finally:
                cursor.close()

    def get_all_shopping_items(self):
        with self.cursor() as cursor:
            cursor.execute(f'SELECT name FROM shopping_items')
            values = cursor.fetchall()
            values = (j for i in values for j in i)
            return values

