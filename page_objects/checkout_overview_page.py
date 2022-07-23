class CheckoutOverviewPage:

    def __init__(self, driver, helpers):
        self.helpers = helpers
        self.driver = driver

    def click_finish(self):
        self.helpers.locate_element('id', 'finish').click()
        return self
