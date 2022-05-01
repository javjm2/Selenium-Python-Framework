from page_objects.home_page import HomePage
from page_objects.base import BaseClass
from utilities.helpers import Helpers

class LoginPage(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    def enter_credentials(self):
        # helper = Helpers(self.driver)
        # helper.locate_elements()
        self.driver.find_element_by_id('user-name').send_keys('standard_user')
        self.driver.find_element_by_id('password').send_keys('secret_sauce')
        self.driver.find_element_by_id('login-button').click()
        home_page = HomePage(self.driver)
        return home_page
