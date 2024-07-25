import pytest

from pages.profile_page import ProfilePage
from pages.locators import ProfilePageLocators

link = 'http://34.141.58.52:8080/#/profile'


@pytest.mark.smoke
@pytest.mark.regression
def test_go_to_add_pet(browser):
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_add_pet()
    page.go_to_add_pet_name_cat()
    page.go_to_pet_type_dropdown()
    page.go_to_pet_type_cat()
    page.go_to_submit_creation_pet()
    page.open()

    pet_name = browser.find_element(*ProfilePageLocators.PET_PROFILE_NAME).text
    expected_name = "murka 0"
    assert pet_name == expected_name, f"'{expected_name}' is not our expectation"


@pytest.mark.regression
def test_go_to_add_pet_full(browser):
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_add_pet()
    page.go_to_add_pet_name_dog()
    page.go_to_pet_type_dropdown()
    page.go_to_pet_type_dog()
    page.go_to_add_pet_age()
    page.go_to_pet_gender_dropdown()
    page.go_to_pet_gender()
    page.go_to_submit_creation_pet()
    page.go_to_choose_pet_ava()
    page.go_to_download_pet_ava()


@pytest.mark.regression
def test_go_to_add_pet_empty(browser):
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_add_pet()
    page.go_to_submit_creation_pet()

    warning = browser.find_element(*ProfilePageLocators.WARNING_EMPTY_PET).text
    expected_text = "This field is email"
    assert warning == expected_text, f" '{expected_text}' is not our expectation"


@pytest.mark.regression
def test_go_to_delete_first_pet(browser):
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_delete_first_pet()
    page.go_to_delete_pet_confirm()


@pytest.mark.regression
def test_go_to_edit_first_pet(browser):
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_edit_first_pet()
    page.go_to_edit_pet_name()
    page.go_to_save_edited_pet()


@pytest.mark.skip
def test_go_to_delete_profile(browser):
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_delete_profile()
    page.go_to_confirm_delete_profile()
