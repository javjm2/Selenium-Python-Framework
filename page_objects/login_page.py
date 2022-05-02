from page_objects.home_page import HomePage
from page_objects.base import BaseClass
from utilities.helpers import Helpers


class LoginPage:

    def __init__(self, driver, helpers):
        self.helpers = helpers
        self.driver = driver

    def enter_credentials(self):
        self.helpers.locate_elements('id', 'user-name').send_keys('standard_user')
        self.helpers.locate_elements('id', 'password').send_keys('secret_sauce')
        self.helpers.locate_elements('id', 'login-button').click()
        self.helpers.wait_for_element_to_be_visible('class_name', 'app_logo', 5)
        return HomePage(self.driver, self.helpers)