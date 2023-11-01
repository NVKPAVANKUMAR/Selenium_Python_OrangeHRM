from pytest_html_reporter import attach

from config.config import TestData
from pages.LoginPage import LoginPage


class TestHomePage:

    def test_home_page_header(self, setup):
        self.driver = setup  # initialize  driver from conf-test file
        lpobj = LoginPage(self.driver)  # LoginPage Object
        homeobj = lpobj.login(TestData.username_valid, TestData.password_valid)  # HomePage Object
        actual_header_value = homeobj.get_header_value()
        assert actual_header_value == TestData.homePageHeader  # verify home page header
        attach(data=self.driver.get_screenshot_as_png())

    def test_invalid_login(self, setup):
        self.driver = setup  # initialize  driver from conf-test file
        lpobj = LoginPage(self.driver)  # LoginPage Object
        lpobj.enter_username(TestData.username_Invalid)
        lpobj.enter_password(TestData.password_Invalid)
        lpobj.click_login()
        lpobj.is_invalid_credentials_is_visible()
        attach(data=self.driver.get_screenshot_as_png())

    def test_profile_img_visible(self, setup):
        self.driver = setup  # initialize  driver from conf-test file
        lpobj = LoginPage(self.driver)  # LoginPage Object
        homeobj = lpobj.login(TestData.username_valid, TestData.password_valid)  # HomePage Object
        profile_img = homeobj.is_profile_img_visible()  # verify profile image
        attach(data=self.driver.get_screenshot_as_png())
        assert profile_img == True
