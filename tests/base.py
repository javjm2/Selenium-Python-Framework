from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utilities.helpers import Helpers


@pytest.mark.usefixtures('driver_init')
class BaseClass:
    def verify_login(self):
        self.helpers.locate_element('class_name', 'app_logo')
        wait = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'app_logo')))
