import pytest

from selenium import webdriver

from pages.login_page import LoginPage


@pytest.fixture(autouse=True)
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()


@pytest.fixture(autouse=True)
def go_to_login(browser):
    link = 'http://34.141.58.52:8080/#/login'
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login()
    page.go_to_password()
    page.go_to_button_submit()
    yield browser
    browser.quit()
