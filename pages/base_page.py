from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.logger import get_logger
logger = get_logger()

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        try:
            logger.info(f"Clicking on element: {locator}")
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except TimeoutException:
            logger.error(f"Element not clickable: {locator}")
            raise

    def send_keys(self, locator, value):
        logger.info(f"Entering text '{value}' in element: {locator}")
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(value)

    def wait_for_element(self, locator):
        logger.info(f"Waiting for element visibility: {locator}")
        return self.wait.until(EC.visibility_of_element_located(locator))

    def get_text(self, locator):
        return self.wait_for_element(locator).text

    def scroll_to_element(self, locator):
        logger.info(f"Scrolling to element: {locator}")

        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

        return element

    def js_click(self, locator):
        logger.warning(f"Using JS click for: {locator}")
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)

    def switch_to_new_tab(self):
        self.wait.until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @staticmethod
    def validate_text(actual, expected):
        logger.info(f"Validating text. Expected: {expected} | Actual: {actual}")
        assert expected in actual, f"Expected '{expected}' not found in '{actual}'"
