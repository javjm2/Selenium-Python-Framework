from page_objects.checkout_info_page import CheckoutInfoPage


class BasketPage:
    def __init__(self, driver):
        self.driver = driver

    def click_checkout(self):
        self.driver.find_element_by_id('checkout').click()
        checkout_info_page = CheckoutInfoPage(self.driver)
        return checkout_info_page

    def assert_item_in_basket(self, item):
        basket_item = self.driver.find_element_by_class_name('inventory_item_name').text
        return basket_item == item

    def click_remove_product_button(self):
        self.driver.find_element_by_id('remove-sauce-labs-backpack').click()
        return self
