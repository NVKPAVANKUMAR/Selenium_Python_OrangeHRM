from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.HomePage import HomePage


class LoginPage(BasePage):
    txt_USERNAME = (By.XPATH, '//input[@name="username"]')
    txt_PASSWORD = (By.XPATH, '//input[@name="password"]')
    btn_LOGIN = (By.XPATH, '//button[@type="submit"]')
    lnk_FORGOT_PASSWORD = (By.CSS_SELECTOR, '[class*=login-forgot]>p')
    txt_LoginError = (By.CSS_SELECTOR, '.oxd-alert-content-text')

    def __init__(self, driver):
        super().__init__(driver)

    def verify_title(self, title):
        """ Get title """
        return self.get_title(title)

    def login(self, username, password):
        """ Login """
        self.do_send_keys(self.txt_USERNAME, username)  # set username
        self.do_send_keys(self.txt_PASSWORD, password)  # set password
        self.do_click(self.btn_LOGIN)
        return HomePage(self.driver)

    def enter_username(self, username):
        """ Login """
        self.do_send_keys(self.txt_USERNAME, username)  # set username

    def enter_password(self, password):
        """ Login """
        self.do_send_keys(self.txt_PASSWORD, password)  # set password

    def click_login(self):
        """ Login """
        self.do_click(self.btn_LOGIN)

    def is_forgot_password_link_is_visible(self):
        """ Return forgot link is visible or not """
        return self.element_is_visible(self.lnk_FORGOT_PASSWORD)

    def is_invalid_credentials_is_visible(self):
        """ Return forgot link is visible or not """
        return self.element_is_visible(self.txt_LoginError)
