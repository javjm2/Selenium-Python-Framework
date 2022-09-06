from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utilities.helpers import Helpers


@pytest.mark.usefixtures('driver_init')
class BaseTest:
    def wait_for(self, value, duration):
        WebDriverWait(self.driver, duration).until(lambda _: value)
