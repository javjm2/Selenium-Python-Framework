import pdb

import pytest
from selenium import webdriver
from utilities.helpers import Helpers
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from page_objects.home_page import HomePage

driver = None
helpers = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture()
def driver_init(request):
    global driver
    global helpers
    firefox_options = FirefoxOptions()
    firefox_options.add_argument('--headless')
    chrome_options = ChromeOptions()
    chrome_options.add_argument('--headless')
    browser_name = request.config.getoption('--browser_name')

    if browser_name == 'chrome':
        driver = webdriver.Chrome(executable_path='C:/chromedriver.exe', chrome_options=chrome_options)
    elif browser_name == 'firefox':
        driver = webdriver.Firefox(executable_path='C:/geckodriver.exe', firefox_options=firefox_options)
    else:
        driver = webdriver.Chrome(executable_path='C:/chromedriver.exe', chrome_options=chrome_options)

    driver.get("https://www.saucedemo.com")
    request.instance.driver = driver
    request.instance.browser_name = browser_name
    helpers = Helpers(driver)
    request.instance.helpers = helpers

    yield
    driver.close()
    driver.quit()

@pytest.fixture()
def login_as_valid_user(driver_init):
    helpers.locate_elements('id', 'user-name').send_keys('standard_user')
    helpers.locate_elements('id', 'password').send_keys('secret_sauce')
    helpers.locate_elements('id', 'login-button').click()
    helpers.wait_for_element_to_be_visible('class_name', 'app_logo', 5)
    return HomePage(driver, helpers)


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)