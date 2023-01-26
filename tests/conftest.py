import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from page_objects.login_page import LoginPage
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from utilities.sql_helpers import SQLHelpers

db = SQLHelpers()


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture()
def driver_init(request):
    global driver

    edge_options = EdgeOptions()
    edge_options.add_argument('--headless')
    chrome_options = ChromeOptions()
    chrome_options.add_argument('--headless')
    browser_name = request.config.getoption('--browser_name')
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": r"C:\Users\javjm\Downloads\New folder"
    })
    if browser_name == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    elif browser_name == 'edge':
        driver = webdriver.Edge(EdgeChromiumDriverManager().install(), options=edge_options)

    driver.get("https://www.saucedemo.com")
    request.instance.driver = driver
    request.instance.browser_name = browser_name

    yield
    driver.close()
    driver.quit()


@pytest.fixture(params=db.get_all_shopping_items())
def list_of_all_products(request):
    return request.param


@pytest.fixture()
def login_as_valid_user(driver_init):
    login = LoginPage(driver)
    login.username_field().send_keys('standard_user')
    login.password_field().send_keys('secret_sauce')
    return login.click_login_button()


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
    pass
