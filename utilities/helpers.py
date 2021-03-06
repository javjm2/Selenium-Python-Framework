from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sqlite3


class Helpers:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_to_be_visible(self, element, value, duration):

        if element == 'id':
            wait = WebDriverWait(self.driver, duration).until(
                EC.visibility_of_element_located((By.ID, value)))
        elif element == 'class_name':
            wait = WebDriverWait(self.driver, duration).until(
                EC.visibility_of_element_located((By.CLASS_NAME, value)))
        elif element == 'xpath':
            wait = WebDriverWait(self.driver, duration).until(
                EC.visibility_of_element_located((By.XPATH, value)))

    def locate_element(self, element, name):
        if element == 'id':
            return self.driver.find_element_by_id(name)
        elif element == 'class_name':
            return self.driver.find_element_by_class_name(name)
        elif element == 'xpath':
            return self.driver.find_element_by_xpath(name)

    def locate_elements(self, element, name):
        if element == 'id':
            return self.driver.find_elements_by_id(name)
        elif element == 'class_name':
            return self.driver.find_elements_by_class_name(name)
        elif element == 'xpath':
            return self.driver.find_elements_by_xpath(name)

    def read_database_values(self, column, table):
        with sqlite3.connect("C:/python appium/user_info.db") as db:
            cursor = db.cursor()

        cursor.execute(f"SELECT {column} FROM {table}")
        values = cursor.fetchall()
        values = [j for i in values for j in i]
        return values
