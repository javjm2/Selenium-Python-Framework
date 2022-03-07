from page_objects.checkout_overview_page import CheckoutOverviewPage


class CheckoutInfoPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_details(self):
        self.driver.find_element_by_name('firstName').send_keys('test_first_name')
        self.driver.find_element_by_id('last-name').send_keys('test_last_name')
        self.driver.find_element_by_id('postal-code').send_keys('nw10 8ef')
        return self

    def click_continue(self):
        self.driver.find_element_by_id('continue').click()
        checkout_overview_page = CheckoutOverviewPage(self.driver)
        return checkout_overview_page
