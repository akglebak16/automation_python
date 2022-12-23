from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    FULL_NAME = (By.XPATH, '//*[@id="userName"]')
    EMAIL = (By.XPATH, '//*[@id="userEmail"]')
    CURRENT_ADDRESS = (By.XPATH, '//textarea[@id="currentAddress"]')
    PERMANENT_ADDRESS = (By.XPATH, '//textarea[@id="permanentAddress"]')
    SUBMIT = (By.XPATH, '//*[@id="submit"]')

    # created form

    CREATED_FULL_NAME = (By.CSS_SELECTOR, '#output #name')
    CREATED_EMAIL = (By.CSS_SELECTOR, '#output #email')
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, '#output #currentAddress')
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#output #permanentAddress')


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.XPATH, '//button[@aria-label="Expand all"]')
    ITEM_LIST = (By.XPATH, "//span[@class='rct-title']")
    SELECTED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
    OUTPUT_RESULT = (By.XPATH, "//span[@class='text-success']")


class RadioButtonPageLocators:
    YES_BUTTON = (By.XPATH, '//*[@for="yesRadio"]')
    IMPRESSIVE_BUTTON = (By.XPATH, '//*[@for="impressiveRadio"]')
    NO_BUTTON = (By.XPATH, '//*[@for="noRadio"]')
    OUTPUT_RESULT = (By.XPATH, '//*[@class="text-success"]')


class WebTablesPageLocators:
    ADD_BUTTON = (By.XPATH, '//*[@id="addNewRecordButton"]')
    FIRST_NAME = (By.XPATH, '//*[@id="firstName"]')
    LAST_NAME = (By.XPATH, '//*[@id="lastName"]')
    EMAIL = (By.XPATH, '//*[@id="userEmail"]')
    AGE = (By.XPATH, '//*[@id="age"]')
    SALARY = (By.XPATH, '//*[@id="salary"]')
    DEPARTMENT = (By.XPATH, '//*[@id="department"]')
    SUBMIT = (By.XPATH, '//*[@id="submit"]')
    #tables

    FULL_PEOPLE_LIST = (By.XPATH, '//*[@class="rt-tr-group"]')
    SERCH_INPUT = (By.XPATH, '//*[@id="searchBox"]')
    DELETE_BUTTON = (By.XPATH, '//span[@title="Delete"]')
    ROW_PARENT = ".//ancestor::div[@class='rt-tr-group']"

    #update
    UPDATE_BUTTON = (By.XPATH, '//*[@id="edit-record-1"]')

    #delete
    NO_DATA_MESSAGE = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[3]/div[3]')

    #tables
    COUNT_ROW_LIST = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[3]/div[2]/div/div[2]/span[2]/select')