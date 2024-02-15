from Util.wait import WaitForElement
from selenium.webdriver.support import expected_conditions as EC
import Util.custom_logger as cl
import logging


class BasePage:
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver
        self.title = "Ditto Music Login | Sign in now"

    def _verify_page(self):
        try:
            actual_title = self.driver.title
            assert actual_title == self.title
            self.log.info("Correct title: " + actual_title)
            return self
        except:
            self.log.error("Wrong title! Should be: " + self.title + ". Fetched title: " + actual_title)
            raise EC.NoSuchElementException("Wrong title! Should be: " + self.title + " Fetched title: " + actual_title)

    def get_title(self):
        return self.driver.title

    def __set__(self, locator, value):
        """Set the supplied text to the specified object"""
        WaitForElement.wait(self.driver, locator)
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(value)

    def __get__(self, locator):
        """Gets the text of the specified object"""
        WaitForElement.wait(self.driver, locator)
        element = self.driver.find_element_by_xpath(locator)
        return element.text

    def click(self, locator):
        WaitForElement.wait(self.driver, locator)
        element = self.driver.find_element(*locator)
        element.click()
