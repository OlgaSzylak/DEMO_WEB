from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import IEDriverManager
from Util.constants import TC_Constants
from selenium import webdriver


class WebDriverFactory:

    def __init__(self, browser):
        self.browser = browser

    def webdriver_instance(self):
        driver = webdriver.Chrome()


        # if self.browser == "chrome":
        #     driver = webdriver.Chrome()
        # elif self.browser == "ie":
        #     driver = webdriver.Ie(IEDriverManager().install())
        # else:
        #     driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(3)
        # driver.maximize_window()
        driver.get(TC_Constants['Base_URL'])
        return driver
