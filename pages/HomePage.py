from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class HomePage(BasePage):
    HEADER = (By.XPATH, '//*[contains(@class,"header-title")]/span')
    clk_LOGOUT = (By.XPATH, '//a[contains(text(),"Logout")]')
    PROFILE_IMG = (By.CSS_SELECTOR, '[class*=header] img[alt="profile picture"]')

    def __int__(self, driver):
        super.__init__(driver)

    def get_header_value(self):
        """ Get home page header value """
        return self.get_element_text(self.HEADER)

    def is_profile_img_visible(self):
        """ Return profile image is visible or not """
        return self.element_is_visible(self.PROFILE_IMG)
