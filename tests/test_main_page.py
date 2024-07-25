import pytest

from pages.main_page import MainPage

link = 'http://34.141.58.52:8080/#/'


@pytest.mark.regression
def test_go_to_profile(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_profile()


@pytest.mark.regression
def test_go_to_quit(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_quit()


@pytest.mark.xfail
@pytest.mark.regression
def test_go_to_filter_by_type(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_filter_by_type()
    page.go_filter_by_dog()


@pytest.mark.regression
def test_go_to_filter_by_pet_name(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_filter_by_pet_name()
