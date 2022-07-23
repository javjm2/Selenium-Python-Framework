import unittest
from tests.base import BaseClass


class TestLogin(BaseClass):
    def test_purchases(self, login_as_valid_user):
        added_item = login_as_valid_user.add_item_to_basket()
        basket_page = login_as_valid_user.open_basket()
        assert basket_page.assert_item_in_basket(added_item)
        checkout_info_page = basket_page.click_checkout()
        checkout_overview_page = checkout_info_page.enter_details().click_continue()
        checkout_overview_page.click_finish()
        self.helpers.wait_for_element_to_be_visible()

    def test_product_sorting_by_name(self, login_as_valid_user):
        home_page = login_as_valid_user.enter_credentials()
        item1 = home_page.first_item_name()
        home_page.sort_items_by_name('z-a')
        item2 = home_page.first_item_name()
        assert home_page.compare_item_name(item1, item2)

    def test_product_sort_by_price(self, login_as_valid_user):
        home_page = login_as_valid_user.enter_credentials()
        price1 = home_page.first_item_price()
        home_page.sort_items_by_price('low-high')
        price2 = home_page.first_item_price()
        assert home_page.compare_item_price(price1, price2)


if __name__ == '__main__':
    unittest.main()
