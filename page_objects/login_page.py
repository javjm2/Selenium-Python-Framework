from page_objects.base_page import BaseClass
from page_objects.home_page import HomePage


class LoginPage(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    def username_field(self):
        return self.locate_element('id', 'user-name')

    def password_field(self):
        return self.locate_element('id', 'password')

    def click_login_button(self):
        self.locate_element('id', 'login-button').click()
        self.wait_for_element_to_be_visible('class_name', 'app_logo', 5)
        return HomePage(self.driver)
