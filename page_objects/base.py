from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseClass:
    def wait_for_element_to_be_visible(self, element, value, duration):
        if element == 'id':
            WebDriverWait(self.driver, duration).until(
                EC.visibility_of_element_located((By.ID, value)))
        elif element == 'class_name':
            WebDriverWait(self.driver, duration).until(
                EC.visibility_of_element_located((By.CLASS_NAME, value)))
        elif element == 'xpath':
            WebDriverWait(self.driver, duration).until(
                EC.visibility_of_element_located((By.XPATH, value)))

    def locate_element(self, element, name):
        if element == 'id':
            return self.driver.find_element_by_id(name)
        elif element == 'class_name':
            return self.driver.find_element_by_class_name(name)
        elif element == 'xpath':
            return self.driver.find_element_by_xpath(name)

    def locate_elements(self, element, name):
        if element == 'id':
            return self.driver.find_elements_by_id(name)
        elif element == 'class_name':
            return self.driver.find_elements_by_class_name(name)
        elif element == 'xpath':
            return self.driver.find_elements_by_xpath(name)
