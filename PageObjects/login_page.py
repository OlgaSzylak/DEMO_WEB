import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Base.basepage import BasePage
import logging
from Util.locators import Locators
import Util.custom_logger as cl
from Util.wait import WaitForElement
from selenium.common.exceptions import TimeoutException


class LoginPage(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def go_to(self, url):
        self.driver.get(url)

    def set_user_name(self, user_name):
        self.log.info("Setting username to {}".format(user_name))
        self.click(Locators.userEmail)
        self.__set__(Locators.userEmail, user_name)

    def set_password(self, password):
        self.log.info("Setting user password")
        self.click(Locators.userPass)
        self.__set__(Locators.userPass, password)

    def click_sign_in(self):
        self.log.info("Clicking 'SIGN IN' button")
        self.click(Locators.BUTTON_SIGNIN)

    def close_alert_and_get_its_text(self):
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        print(alert_text)
        # time.sleep(2)
        alert.accept()

    def log_in_successful(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.url_matches('/*/summary'))
            self.log.info("Overview page loaded")
            return True
        except TimeoutException:
            self.log.error("Wrong page loaded")
            return False
