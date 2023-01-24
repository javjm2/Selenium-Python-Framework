from page_objects.base_page import BaseClass


class CheckoutOverviewPage(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    def click_finish(self):
        self.locate_element('id', 'finish').click()
        return self
