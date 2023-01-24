from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utilities.sqlhelpers import SQLHelpers


class BaseTest:
    def wait_for(self, value,  duration):
        def _element(value):
            return value
        return WebDriverWait(self.driver, duration).until(_element)
