from page_objects.checkout_info_page import CheckoutInfoPage
from page_objects.base_page import BaseClass


class BasketPage(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    def click_checkout(self):
        self.locate_element('id', 'checkout').click()
        checkout_info_page = CheckoutInfoPage(self.driver)
        return checkout_info_page

    def assert_item_in_basket(self, item):
        basket_item = self.locate_element('class_name', 'inventory_item_name').text
        return basket_item == item

    def click_remove_product_button(self):
        self.locate_element('id', 'remove-sauce-labs-backpack').click()
        return self
