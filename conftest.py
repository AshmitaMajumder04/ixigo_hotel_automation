import pytest
from selenium import webdriver
from utils.screenshot_utils import take_screenshot
@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    driver.get("https://www.ixigo.com/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver

    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            take_screenshot(driver, item.name)