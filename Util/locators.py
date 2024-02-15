from selenium.webdriver.common.by import By


class Locators(object):
    """
    This class contains elements located on each screen in Intellin standard app
    """

    userEmail = (By.ID, "fc-EmailAddress")
    userPass = (By.ID, "fc-Password")
    btnContinue = (By.XPATH, "//button[@type='submit']")
