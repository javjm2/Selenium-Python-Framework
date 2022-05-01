import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture()
def driver_init(request):
    global driver
    browser_name = request.config.getoption('--browser_name')
    if browser_name == 'chrome':
        driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
    elif browser_name == 'firefox':
        driver = webdriver.Firefox(executable_path='C:/geckodriver.exe')
    driver.get("https://www.saucedemo.com")
    request.instance.driver = driver
    request.instance.browser_name = browser_name
    yield
    driver.close()
    driver.quit()


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