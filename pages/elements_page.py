import time
import random
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from generator.generator import generated_person
from locators.elements_pages_locators import TextBoxPageLocators
from locators.elements_pages_locators import CheckBoxPageLocators
from locators.elements_pages_locators import RadioButtonPageLocators
from locators.elements_pages_locators import WebTablesPageLocators
from locators.elements_pages_locators import ButtonsPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 21
        while count != 0:
            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    def selected_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.SELECTED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element(By.XPATH, (self.locators.TITLE_ITEM))
            data.append(title_item.text)
        return str(data).replace(' ', '').replace('doc', '').replace(".", '').lower()

    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(" ", '').lower()


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    def press_radio_button(self, choice):
        choices = {'yes': self.locators.YES_BUTTON,
                   'impressive': self.locators.IMPRESSIVE_BUTTON,
                   'no': self.locators.NO_BUTTON}

        radio = self.element_is_visible(choices[choice]).click()

    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text


class WebTablesPage(BasePage):
    locators = WebTablesPageLocators()

    def add_new_person(self, count=1):
        count = 1
        while count != 0:
            person_info = next(generated_person())
            firstname = person_info.firstname
            lastname = person_info.lastname
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRST_NAME).send_keys(firstname)
            self.element_is_visible(self.locators.LAST_NAME).send_keys(lastname)
            self.element_is_visible(self.locators.EMAIL).send_keys(email)
            self.element_is_visible(self.locators.AGE).send_keys(age)
            self.element_is_visible(self.locators.SALARY).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT).send_keys(department)
            self.element_is_visible(self.locators.SUBMIT).click()
            count -= 1
            return [firstname, lastname, str(age), email, str(salary), department]

    def check_new_added_person(self):
        people_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data = []
        for i in people_list:
            data.append(i.text.splitlines())
        return data

    def search_some_person(self, key_words):
        self.element_is_present(self.locators.SERCH_INPUT).send_keys(key_words)

    def check_search_person(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element(By.XPATH, ".//ancestor::div[@class='rt-tr-group']")
        return row.text.splitlines()

    def update_person_info(self):
        person_info = next(generated_person())
        age = person_info.age
        self.element_is_visible(self.locators.UPDATE_BUTTON).click()
        self.element_is_visible(self.locators.AGE).clear()
        self.element_is_visible(self.locators.AGE).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT).click()
        return str(age)
    def delete_person(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    def check_deleted(self):
        return self.element_is_present(self.locators.NO_DATA_MESSAGE).text


    def select_up_to_some_rows(self):
        count = [5, 10, 20, 25, 50, 100]
        data = []
        for x in count:
            cont_row_button = self.element_is_visible(self.locators.COUNT_ROW_LIST)
            self.go_to_element(cont_row_button)
            self.element_is_visible(By.CSS_SELECTOR, f'option[value="{x}"]').click()
            data.append(self.check_count_rows())
        return data

    def check_count_rows(self):
        list_rows = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        return len(list_rows)

class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    def double_click_button(self):
        self.action_double_click(self.element_is_visible(self.locators.DOUBLE_BUTTON))

    def right_click_button(self):
        self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON))

    def click_me_button(self):
        self.element_is_visible(self.locators.CLICK_ME_BUTTON).click()

    def check_clicked_on_the_double(self):
        double_click_msg = self.element_is_visible(self.locators.DOUBLE_CLICK_MESSAGE).text
        return double_click_msg
    def check_clicked_on_the_right(self):
        right_click_msg = self.element_is_visible(self.locators.DOUBLE_RIGHT_MESSAGE).text
        return right_click_msg
    def check_clicked_on_me(self):
        click_me_msg = self.element_is_visible(self.locators.CLICK_ME_MESSAGE).text
        return click_me_msg

