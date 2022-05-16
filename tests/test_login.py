import unittest
from page_objects.login_page import LoginPage
from tests.base import BaseClass


class TestLogin(BaseClass):
    def test_purchases(self):
        login_page = LoginPage(self.driver, self.helpers)
        home_page = login_page.enter_credentials()
        added_item = home_page.add_item_to_basket()
        basket_page = home_page.open_basket()
        assert basket_page.assert_item_in_basket(added_item)
        checkout_info_page = basket_page.click_checkout()
        checkout_overview_page = checkout_info_page.enter_details().click_continue()
        checkout_overview_page.click_finish()

    def test_product_sorting_by_name(self):
        login_page = LoginPage(self.driver, self.helpers)
        home_page = login_page.enter_credentials()
        # super().verify_login()
        item1 = home_page.first_item_name()
        home_page.sort_items_by_name('z-a')
        item2 = home_page.first_item_name()
        assert home_page.compare_item_name(item1, item2)

    def test_product_sort_by_price(self):
        login_page = LoginPage(self.driver, self.helpers)
        home_page = login_page.enter_credentials()
        price1 = home_page.first_item_price()
        home_page.sort_items_by_price('low-high')
        price2 = home_page.first_item_price()
        assert home_page.compare_item_price(price1, price2)


if __name__ == '__main__':
    unittest.main()
