from page_objects.checkout_info_page import CheckoutInfoPage


class BasketPage:
    def __init__(self, driver, helpers):
        self.helpers = helpers
        self.driver = driver

    def click_checkout(self):
        self.helpers.locate_elements('id', 'checkout').click()
        checkout_info_page = CheckoutInfoPage(self.driver, self.helpers)
        return checkout_info_page

    def assert_item_in_basket(self, item):
        basket_item = self.helpers.locate_elements('class_name', 'inventory_item_name').text
        return basket_item == item

    def click_remove_product_button(self):
        self.helpers.locate_elements('id', 'remove-sauce-labs-backpack').click()
        return self
