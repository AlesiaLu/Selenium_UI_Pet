from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def go_to_login(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL).send_keys('alesia@mail.ru')

    def go_to_password(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD).send_keys("1234")

    def go_to_button_submit(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_BTN).submit()
