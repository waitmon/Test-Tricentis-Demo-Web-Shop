from pages.registration_page import RegistrationPage


class TestRegistrationPage:
    """Checking validation required fields, performing full process of registration of a new user"""
    def test_required_fields_assertion(self, driver):
        register_page = RegistrationPage(driver, 'https://demowebshop.tricentis.com/')
        register_page.open()
        first_name, last_name, email, password, confirm_password = register_page.validation_message()
        assert first_name == 'First name is required.'
        assert last_name == 'Last name is required.'
        assert email == 'Email is required.'
        assert password == 'Password is required.' and confirm_password == 'Password is required.'

    def test_signup_form_data_input(self, driver):
        register_page = RegistrationPage(driver, 'https://demowebshop.tricentis.com/')
        register_page.open()
        full_registration = register_page.new_user_input_data()
        assert full_registration == 'Your registration completed'

