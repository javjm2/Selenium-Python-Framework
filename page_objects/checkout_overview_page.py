class CheckoutOverviewPage:

    def __init__(self, driver):
        self.driver = driver

    def click_finish(self):
        self.driver.find_element_by_id('finish').click()
        return self
