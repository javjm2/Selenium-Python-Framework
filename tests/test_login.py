import unittest

import pytest

from tests.base import BaseClass


class TestLogin(BaseClass):
    # @pytest.mark.skip()
    def test_purchases(self, login_as_valid_user):
        added_item = login_as_valid_user.add_item_to_basket()
        basket_page = login_as_valid_user.open_basket()
        assert basket_page.assert_item_in_basket(added_item)
        checkout_info_page = basket_page.click_checkout()
        checkout_overview_page = checkout_info_page.enter_details().click_continue()
        checkout_overview_page.click_finish()

    def test_product_sorting_by_name(self, login_as_valid_user):
        item1 = login_as_valid_user.first_item_name()
        login_as_valid_user.sort_items_by_name('z-a')
        item2 = login_as_valid_user.first_item_name()
        assert login_as_valid_user.compare_item_name(item1, item2)

    def test_product_sort_by_price(self, login_as_valid_user):
        price1 = login_as_valid_user.first_item_price()
        login_as_valid_user.sort_items_by_price('low-high')
        price2 = login_as_valid_user.first_item_price()
        assert login_as_valid_user.compare_item_price(price1, price2)


if __name__ == '__main__':
    unittest.main()
