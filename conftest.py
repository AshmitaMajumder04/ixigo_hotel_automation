import pytest
from selenium import webdriver

from utils.driver_factory import get_driver
from utils.screenshot_utils import take_screenshot

@pytest.fixture
def driver(request):
    driver=webdriver.Chrome()
    driver.get("https://www.ixigo.com/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver

    # if request.node.rep_call.failed:
    #     take_screenshot(driver, request.node.name)
    #
    # driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
