import pytest
from PageObjects.login_page import LoginPage
from Util.constants import TC_Constants


class LoginTests:

    @pytest.fixture(autouse=True)
    def classSetup(self, driver_init):
        self.lp = LoginPage(self.driver)

    def test_valid_login(self):
        self.lp._verify_page()
        self.lp.set_user_name((TC_Constants['userEmail']))
        self.lp.set_password((TC_Constants['userPasswordValid']))
        # self.lp.click_sign_in()
        # assert self.lp.log_in_successful()