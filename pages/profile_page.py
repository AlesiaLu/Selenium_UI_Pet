import time

from .base_page import BasePage
from .locators import ProfilePageLocators


class ProfilePage(BasePage):

    def go_to_add_pet(self):
        self.browser.find_element(*ProfilePageLocators.ADD_PET).click()

    def go_to_add_pet_name_cat(self):
        self.browser.find_element(*ProfilePageLocators.PET_NAME).send_keys("murka")
        time.sleep(2)

    def go_to_add_pet_name_dog(self):
        self.browser.find_element(*ProfilePageLocators.PET_NAME).send_keys("tuzik")
        time.sleep(2)

    def go_to_pet_type_dropdown(self):
        self.browser.find_element(*ProfilePageLocators.PET_TYPE_DROPDOWN).click()

    def go_to_pet_type_cat(self):
        self.browser.find_element(*ProfilePageLocators.PET_TYPE_CAT).click()

    def go_to_pet_type_dog(self):
        self.browser.find_element(*ProfilePageLocators.PET_TYPE_DOG).click()

    def go_to_submit_creation_pet(self):
        self.browser.find_element(*ProfilePageLocators.CREATE_PET_BTN).submit()
        time.sleep(2)

    def go_to_add_pet_age(self):
        self.browser.find_element(*ProfilePageLocators.PET_AGE).send_keys("2")

    def go_to_pet_gender_dropdown(self):
        self.browser.find_element(*ProfilePageLocators.PET_GENDER_DROPDOWN).click()

    def go_to_pet_gender(self):
        self.browser.find_element(*ProfilePageLocators.PET_GENDER).click()

    def go_to_choose_pet_ava(self):
        choose_pet_ava = self.browser.find_element(*ProfilePageLocators.CHOOSE_AVA)
        choose_pet_ava.send_keys('/Users/alesyalu/PycharmProjects/Selenium_UI_Pet/tests/dog.jpg')

    def go_to_download_pet_ava(self):
        self.browser.find_element(*ProfilePageLocators.DOWNLOAD_PET_AVA).click()
        time.sleep(2)

    def go_to_delete_first_pet(self):
        self.browser.find_element(*ProfilePageLocators.DELETE_PET).click()

    def go_to_delete_pet_confirm(self):
        self.browser.find_element(*ProfilePageLocators.DELETE_PET_CONFIRM).click()
        time.sleep(2)

    def go_to_edit_first_pet(self):
        self.browser.find_element(*ProfilePageLocators.EDIT_PET).click()
        time.sleep(2)

    def go_to_edit_pet_name(self):
        edit_pet_name = self.browser.find_element(*ProfilePageLocators.EDIT_PET_NAME)
        edit_pet_name.clear()
        edit_pet_name.send_keys("mia")

    def go_to_save_edited_pet(self):
        self.browser.find_element(*ProfilePageLocators.EDIT_SAVE).click()
        time.sleep(2)

    def go_to_delete_profile(self):
        self.browser.find_element(*ProfilePageLocators.DELETE_PROFILE).click()

    def go_to_confirm_delete_profile(self):
        self.browser.find_element(*ProfilePageLocators.DELETE_PROFILE_CONFIRM).click()
        time.sleep(2)
