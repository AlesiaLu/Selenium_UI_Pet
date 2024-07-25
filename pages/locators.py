from selenium.webdriver.common.by import By


class MainPageLocators:
    PROFILE = (By.XPATH, '//*[@id="app"]/header/div/ul/li[1]/a/span[2]')
    QUIT = (By.XPATH, '//*[@id="app"]/header/div/ul/li[2]/a/span[2]')
    FILTER_BY_TYPE_DROPDOWN = (By.ID, "typesSelector")
    FILTER_BY_TYPE = (By.XPATH, '//*[@id="pv_id_4"]')
    FILTER_BY_PET_NAME = (By.XPATH, '//*[@id="petName"]')


class LoginPageLocators:
    LOGIN_EMAIL = (By.XPATH, '//*[@id="login"]')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#password > input")
    LOGIN_BTN = (By.CLASS_NAME, "p-button-label")


class ProfilePageLocators:
    ADD_PET = (By.XPATH, "//div[@id='app']/main/div/div/div/div/div/button/span")
    PET_NAME = (By.XPATH, '//*[@id="name"]')
    PET_TYPE_DROPDOWN = (By.CLASS_NAME, "p-dropdown-trigger")
    PET_TYPE_CAT = (By.ID, "pv_id_4_1")
    PET_TYPE_DOG = (By.ID, "pv_id_4_0")
    PET_AGE = (By.XPATH, '//*[@id="age"]/input')
    PET_GENDER_DROPDOWN = (By.XPATH, '//*[@id="pv_id_5"]/div')
    PET_GENDER = (By.ID, "pv_id_5_1")
    CREATE_PET_BTN = (By.CLASS_NAME, "p-button-label")
    CHOOSE_AVA = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div[2]/div/span/input')
    DOWNLOAD_PET_AVA = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div[2]/div/span/span[2]')
    PET_PROFILE_NAME = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div/div[1]/div/div[1]/div[1]')
    WARNING_EMPTY_PET = (By.CLASS_NAME, "text-red-500")
    DELETE_PET = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div/div[1]/div/div[2]/button[2]/span[2]')
    DELETE_PET_CONFIRM = (By.XPATH, '/html/body/div[3]/div[2]/button[2]')
    EDIT_PET = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div/div/div/div[2]/button[1]/span[1]')
    EDIT_PET_NAME = (By.XPATH, '//*[@id="name"]')
    EDIT_SAVE = (By.XPATH, '//*[@id="app"]/main/div/form/div/div[2]/div[3]/button')
    DELETE_PROFILE = (By.XPATH, '//*[@id="app"]/main/div/div/div[1]/div/div[2]/button/span[1]')
    DELETE_PROFILE_CONFIRM = (By.XPATH, '/html/body/div[3]/div[2]/button[2]')
