import time

from selenium.webdriver import Keys

from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):

    def go_to_profile(self):
        self.browser.find_element(*MainPageLocators.PROFILE).click()
        time.sleep(2)

    def go_to_quit(self):
        self.browser.find_element(*MainPageLocators.QUIT).click()
        time.sleep(2)

    def go_to_filter_by_type(self):
        self.browser.find_element(*MainPageLocators.FILTER_BY_TYPE_DROPDOWN).click()
        time.sleep(2)

    def go_filter_by_dog(self):
        self.browser.find_element(*MainPageLocators.FILTER_BY_TYPE).click()
        time.sleep(2)

    def go_to_filter_by_pet_name(self):
        filter_by_pet_name = self.browser.find_element(*MainPageLocators.FILTER_BY_PET_NAME)
        filter_by_pet_name.click()
        filter_by_pet_name.send_keys("tuzik")
        filter_by_pet_name.send_keys(Keys.ENTER)
        time.sleep(2)
