import os
import pytest
from datetime import datetime
from Base.webdriverfactory import WebDriverFactory


@pytest.fixture(scope="function")
def driver_init(request, browser):
    wdf = WebDriverFactory(browser,)
    driver = wdf.webdriver_instance()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config._metadata = None
    if not os.path.exists('__reports'):
        os.makedirs('__reports')
    # config.option.htmlpath = '__reports/' + 'Test Run ' + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html"
    config.option.htmlpath = '__reports/' + 'Test Report.html'
