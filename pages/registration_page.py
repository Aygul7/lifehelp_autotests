from base.base_object import BaseObject
from locators.registration_page_locators import RegistrationLocators
import allure
from support.assertions import Assertions
from selenium.webdriver.common.keys import Keys




class RegistrationPage(BaseObject, Assertions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('set email in registration form')
    def set_email_registration_form(self):
        self.set_value(RegistrationLocators.EMAIL_FIELD_REGISTRATION_FORM, 'aigul.schafigullina.87@yandex.ru')

    @allure.step('set password in registration form')
    def set_password_registration_form(self):
        self.set_value(RegistrationLocators.PASSWORD1_FIELD_REGISTRATION_FORM, 'password1@')

    @allure.step('repeat password in registration form')
    def repeat_password_registration_form(self):
        self.set_value(RegistrationLocators.PASSWORD2_REPEAT_FIELD_REGISTRATION_FORM, 'password1@')

    @allure.step('click first checkbox of consent in registration form')
    def click_first_checkbox_consent_registration_form(self):
        self.to_click(RegistrationLocators.FIRST_CHECKBOX_CONSENT_REGISTRATION_FORM)

    @allure.step('scroll the page till the "register" button in registration form')
    def scroll_to_register_button_registration_form(self):
        self.move_to_element(RegistrationLocators.REGISTER_BUTTON)

    @allure.step('click "to register" button in registration form')
    def click_to_register_button_registration_form(self):
        self.to_click(RegistrationLocators.REGISTER_BUTTON)

    @allure.step('click enter instead of "to register" button in registration form')
    def click_enter_instead_register_button_registration_form(self):
        self.is_clickable(RegistrationLocators.REGISTER_BUTTON).send_keys(Keys.RETURN)

    @allure.step('verify message "A link to reset your password has been sent to your email"')
    def verify_sent_msg_registration(self):
        actual_result = self.get_text_title_of_element(RegistrationLocators.REGISTRATION_INFO_TEXT)
        assert actual_result == 'На Ваш email отправлена ссылка для подтверждения электронной почты. ' \
                                'Пожалуйста, перейдите по ней, чтобы завершить процесс регистрации.'

    @allure.step('set email in registration form - registered user')
    def set_email_registered_user_registration_form(self):
        self.set_value(RegistrationLocators.EMAIL_FIELD_REGISTRATION_FORM, 'sh.aygul@gmail.com')

    @allure.step('verify message "The user with this email is already registered"')
    def verify_error_msg_registration(self):
        actual_result = self.get_text_title_of_element(RegistrationLocators.REGISTRATION_ERROR_MESSAGE)
        assert actual_result == 'Пользователь с введенным email уже зарегистрирован'

    @allure.step('set up "your email" in registration form')
    def set_your_email_registration_fixture(self, first):
        self.set_value(RegistrationLocators.EMAIL_FIELD_REGISTRATION_FORM, first)

    @allure.step('set password in registration form_fixture')
    def set_password_registration_form_fixture(self, second):
        self.set_value(RegistrationLocators.PASSWORD1_FIELD_REGISTRATION_FORM, second)

    @allure.step('repeat password in registration form_fixture')
    def repeat_password_registration_form_fixture(self, third):
        self.set_value(RegistrationLocators.PASSWORD2_REPEAT_FIELD_REGISTRATION_FORM, third)

    @allure.step('verify error message in registration form')
    def verify_error_message_registration_fixture(self, fourth):
        actual_result = self.get_text_title_of_element(
            RegistrationLocators.ERROR_MESSAGE_WRONG_REPEAT_PASSWORD_REG_FORM)
        assert actual_result == fourth

    @allure.step('click "rapid auth" button in registration page')
    def click_rapid_auth_btn_registration_page(self):
        self.to_click(RegistrationLocators.RAPID_AUTH_BUTTON_REGISTRATION_PAGE)

    @allure.step('scroll the page till the "register" button in registration form')
    def scroll_to_rapid_auth_button_registration_form(self):
        self.move_to_element(RegistrationLocators.RAPID_AUTH_BUTTON_REGISTRATION_PAGE)

    @allure.step('verify disabled type of the "reset password" button - get link to restore password page')
    def verify_disabled_type_button_registration_page(self):
        actual_result = self.is_visible(RegistrationLocators.REGISTER_BUTTON).get_attribute('disabled')
        print(actual_result)

    @allure.step('set password in registration form')
    def set_short_password_7_registration_form(self):
        self.set_value(RegistrationLocators.PASSWORD1_FIELD_REGISTRATION_FORM, 'passwod1@')

    @allure.step('repeat password in registration form')
    def repeat_short_password_7_registration_form(self):
        self.set_value(RegistrationLocators.PASSWORD2_REPEAT_FIELD_REGISTRATION_FORM, 'passwod1@')

    @allure.step('verify hidden mode of the password field')
    def verify_hidden_type_password_field(self):
        actual_result = self.is_visible(RegistrationLocators.PASSWORD1_FIELD_REGISTRATION_FORM).get_attribute('type')
        assert actual_result == 'password'

    @allure.step('click to "view password" button in password field in registration page')
    def click_to_view_password_button_registration_page(self):
        self.to_click(RegistrationLocators.VIEW_PASSWORD_BUTTON_REGISTRATION_FIELD)

    @allure.step('verify view mode of the password field')
    def verify_viewed_type_password_field(self):
        actual_result = self.is_visible(RegistrationLocators.PASSWORD1_FIELD_REGISTRATION_FORM).get_attribute('type')
        assert actual_result == 'text'

    @allure.step('click to "view password" button in password field in registration page')
    def click_to_hide_password_button_registration_page(self):
        self.to_click(RegistrationLocators.HIDE_PASSWORD_BUTTON_REGISTRATION_FIELD)

    @allure.step('click to "view password" button in repeat password field in registration page')
    def click_to_hide_repeat_password_button_registration_page(self):
        self.to_click(RegistrationLocators.HIDE_REPEAT_PASSWORD_BUTTON_REGISTRATION_FIELD)