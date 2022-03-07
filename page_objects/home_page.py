import string
from telnetlib import EC
from utilities.sql_util import SQLUtil
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.basket_page import BasketPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def add_item_to_basket(self):
        el = SQLUtil.read_data(self, "name", "shopping_items")
        item = el[0][0].lower().split(' ')
        new_item = '-'.join(item)
        self.driver.find_element_by_id(f'add-to-cart-{new_item}').click()
        return el[0][0]

    def open_basket(self):
        self.driver.find_element_by_id('shopping_cart_container').click()
        basket_page = BasketPage(self.driver)
        return basket_page

    def sort_items_by_price(self, sort_type):
        self.driver.find_element_by_class_name('product_sort_container').click()
        if sort_type == 'low-high':
            self.driver.find_element_by_xpath('//*[contains(text(), "Price (low to high)")]').click()
        elif sort_type == 'high-low':
            self.driver.find_element_by_xpath('//*[contains(text(), "Price (high to low)")]').click()
        return self
        return self

    def sort_items_by_name(self, sort_type):
        self.driver.find_element_by_class_name('product_sort_container').click()
        if sort_type == 'a-z':
            self.driver.find_element_by_xpath('//*[contains(text(), "Name (A to Z)")]').click()
        elif sort_type == 'z-a':
            self.driver.find_element_by_xpath('//*[contains(text(), "Name (Z to A)")]').click()
        return self

    def first_item_name(self):
        return self.driver.find_element_by_class_name('inventory_item_name').text

    def first_item_price(self):
        price = self.driver.find_element_by_class_name('inventory_item_price').text
        return float(price[1:])

    def compare_item_name(self, item1, item2):
        alphabet = string.ascii_lowercase
        for letter in alphabet:
            for j, k in zip(item1, item2):
                if alphabet.index(j.lower()) != alphabet.index(k.lower()):
                    return True
                else:
                    continue
                return False

    def compare_item_price(self, price1, price2):
        return price1 != price2
