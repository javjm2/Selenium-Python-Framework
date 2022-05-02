from page_objects.checkout_overview_page import CheckoutOverviewPage


class CheckoutInfoPage:
    def __init__(self, driver, helpers):
        self.helpers = helpers
        self.driver = driver

    def enter_details(self):
        self.driver.find_element_by_name('firstName').send_keys('test_first_name')
        self.helpers.locate_elements('id', 'last-name').send_keys('test_last_name')
        self.helpers.locate_elements('id', 'postal-code').send_keys('nw10 8ef')
        return self

    def click_continue(self):
        self.helpers.locate_elements('id', 'continue').click()
        checkout_overview_page = CheckoutOverviewPage(self.driver, self.helpers)
        return checkout_overview_page
