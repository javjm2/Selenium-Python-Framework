from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures('driver_init')
class BaseClass:

    def verify_login(self):
        self.driver.find_element_by_class_name('app_logo')
        wait = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'app_logo')))
