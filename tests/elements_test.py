import time
import random
from pages.elements_page import TextBoxPage
from pages.elements_page import CheckBoxPage
from pages.elements_page import RadioButtonPage
from pages.elements_page import WebTablesPage
from pages.elements_page import ButtonsPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            full_name_output, email_output, current_address_output, per_adr_output = text_box_page.check_filled_form()
            assert full_name == full_name_output, 'the fullname does not match'
            assert email == email_output, "the email does not match"
            assert current_address == current_address_output, 'the current_address does not match'
            assert permanent_address == per_adr_output, "the permanent does not match"

    class TestCheckBox:

        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.selected_checkboxes()
            out_put_tesult = check_box_page.get_output_result()
            assert input_checkbox == out_put_tesult, "input and output results doesn't match"

    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.press_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.press_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.press_radio_button('no')
            output_no = radio_button_page.get_output_result()
            assert output_yes == 'Yes', "'Yes' have not been selected"
            assert output_impressive == 'Impressive', "'Impressive' have not been selected"
            assert output_no == 'No', "'No' have not been selected"
            time.sleep(5)

    class TestWebTable:
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_new_added_person()
            print(new_person)
            print(table_result)
            assert new_person in table_result

        def test_web_table_search_person(self, driver):
            web_table_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            time.sleep(5)
            web_table_page.search_some_person(key_word)
            data = web_table_page.check_search_person()
            print(data)
            print(key_word)
            assert key_word in data

        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]
            web_table_page.search_some_person(lastname)
            age = web_table_page.update_person_info()
            time.sleep(4)
            row = web_table_page.check_search_person()
            print(age)
            print(row)
            assert age in row, "the person card has not been changed"

        def test_web_table_delete_person_info(self, driver):
            web_table_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_some_person(email)
            web_table_page.delete_person()
            text = web_table_page.check_deleted()
            assert text == "No rows found"
        def test_web_table_change_count_row(self,driver):
            web_table_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()
            assert count == [5, 10, 20, 25, 50,
                             100], 'The number of rows in the table has not been changed or has changed incorrectly'


class TestButtonPage():

    def test_double_click(self,driver):
        web_table_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
        web_table_page.open()
        web_table_page.double_click_button()
        btn = web_table_page.check_clicked_on_the_double()
        assert 'You have done a double click' == btn

    def test_right_click(self,driver):
        web_table_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
        web_table_page.open()
        web_table_page.right_click_button()
        btn = web_table_page.check_clicked_on_the_right()
        assert 'You have done a right click' == btn

    def test_click_on_me_btn(self,driver):
        web_table_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
        web_table_page.open()
        web_table_page.click_me_button()
        btn = web_table_page.check_clicked_on_me()
        assert 'You have done a dynamic click' == btn


