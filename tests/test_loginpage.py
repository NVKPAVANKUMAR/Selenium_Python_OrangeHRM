from config.config import TestData
from pages.LoginPage import LoginPage


class TestLogin:

    def test_login(self, setup):
        self.driver = setup  # initialize  driver from conftest file
        lpobj = LoginPage(self.driver)  # LoginPage Object
        lpobj.verify_title(TestData.loginPageTitle)
        is_link_visible = lpobj.is_forgot_password_link_is_visible()
        assert is_link_visible == True
        lpobj.login(TestData.username_valid, TestData.password_valid)  # login
