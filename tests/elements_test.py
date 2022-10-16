import time

from pages.elements_page import TextBoxPage


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
