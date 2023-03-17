import random
from generator.generator import generated_new_user
from locators.registration_page_locators import RegistrationPageLocators
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    """Methods for registration process: checking requiring fields, filling user information."""

    locators = RegistrationPageLocators()

    def validation_message(self):
        self.element_is_present(self.locators.REGISTER_MENU_BUTTON).click()
        self.element_is_present(self.locators.REGISTER_BUTTON).click()
        return self.element_is_present(self.locators.FIRST_NAME_VALIDATION_ERROR).text, self.element_is_present(
            self.locators.LAST_NAME_VALIDATION_ERROR).text, self.element_is_present(
            self.locators.EMAIL_VALIDATION_ERROR).text, self.element_is_present(
            self.locators.PASSWORD_VALIDATION_ERROR).text, self.element_is_present(
            self.locators.CONFIRM_PASSWORD_VALIDATION_ERROR).text

    def new_user_input_data(self):
        self.element_is_present(self.locators.REGISTER_MENU_BUTTON).click()
        gender_list = self.elements_are_present(self.locators.GENDER_LIST)
        gender_button = gender_list[random.randint(0, 1)]
        self.go_to_element(gender_button)
        gender_button.click()
        user_info = next(generated_new_user())
        first_name = user_info.first_name
        last_name = user_info.last_name
        email = user_info.email
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.PASSWORD).send_keys('123456')
        self.element_is_visible(self.locators.CONFIRM_PASSWORD).send_keys('123456')
        self.element_is_visible(self.locators.REGISTER_BUTTON).click()
        return self.element_is_present(self.locators.COMPLETED_REGISTRATION_TEXT).text
