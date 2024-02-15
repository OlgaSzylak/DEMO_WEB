from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

"""
This class wait for element with specified time, If not getting it throws exception
"""


class WaitForElement:
    @staticmethod
    def wait(driver, element, time_out=50):
        try:
            WebDriverWait(driver, time_out).until(lambda x: x.find_element(*element))
        except TimeoutException:
            print('Element ' + str(element) + 'could not be found')
