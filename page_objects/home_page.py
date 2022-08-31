import string
from page_objects.basket_page import BasketPage


class HomePage:
    def __init__(self, driver, helpers):
        self.helpers = helpers
        self.driver = driver

    def add_item_to_basket(self):
        el = self.helpers.read_database_values("name", "shopping_items")
        first_item = el[0]
        item = first_item.lower().split(' ')
        new_item = '-'.join(item)
        self.helpers.locate_element('id', f'add-to-cart-{new_item}').click()
        return first_item

    def open_basket(self):
        self.helpers.locate_element('id', 'shopping_cart_container').click()
        basket_page = BasketPage(self.driver, self.helpers)
        return basket_page

    def sort_items_by_price(self, sort_type):
        self.helpers.locate_element('class_name', 'product_sort_container').click()
        if sort_type == 'low-high':
            self.helpers.locate_element('xpath', '//*[contains(text(), "Price (low to high)")]').click()
        elif sort_type == 'high-low':
            self.helpers.locate_element('xpath', '//*[contains(text(), "Price (high to low)")]').click()
        return self

    def sort_items_by_name(self, sort_type):
        self.helpers.locate_element('class_name', 'product_sort_container').click()
        if sort_type == 'a-z':
            self.helpers.locate_element('xpath', '//*[contains(text(), "Name (A to Z)")]').click()
        elif sort_type == 'z-a':
            self.helpers.locate_element('xpath', '//*[contains(text(), "Name (Z to A)")]').click()
        return self

    def first_item_name(self):
        return self.helpers.locate_element('class_name', 'inventory_item_name').text

    def first_item_price(self):
        price = self.helpers.locate_element('class_name', 'inventory_item_price').text
        return float(price[1:])

    @staticmethod
    def compare_item_name(item1, item2):
        alphabet = string.ascii_lowercase
        for letter in alphabet:
            for j, k in zip(item1, item2):
                if alphabet.index(j.lower()) != alphabet.index(k.lower()):
                    return True
                else:
                    continue
            return False

    @staticmethod
    def compare_item_price(price1, price2):
        return price1 != price2
