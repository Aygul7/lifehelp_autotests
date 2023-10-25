from base.base_object import BaseObject
from locators.restore_password_link_locators import RestorePasswordLinkLocators
from locators.authorization_locators import AuthorizationLocators
import allure
from support.assertions import Assertions




class RestorePasswordLinkPage(BaseObject):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('verify mrqz test page "parental burnout"')
    def verify_page_restore_password(self):
        actual_result = self.get_text_title_of_element(RestorePasswordLinkLocators.RESTORE_PASSWORD_PAGE_HEADING)
        assert actual_result == 'Обновление пароля'

    @allure.step('set up new password')
    def set_new_password(self):
        self.set_value(RestorePasswordLinkLocators.NEW_PASSWORD_FIELD, 'lifehelp1@')

    @allure.step('repeat new password')
    def repeat_new_password(self):
        self.set_value(RestorePasswordLinkLocators.REPEAT_PASSWORD_FIELD, 'lifehelp1@')

    @allure.step('click to "save" btn')
    def click_to_save_btn_restore_password(self):
        self.to_click(RestorePasswordLinkLocators.TO_SAVE_BUTTON)

    @allure.step('verify invalid token error message')
    def verify_invalid_token_error_message(self):
        actual_result = self.get_text_title_of_element(RestorePasswordLinkLocators.INVALID_TOKEN_ERROR_MESSAGE)
        assert 'Токен для обновления пароля недействителен' in actual_result

    @allure.step('verify message about successful password restore')
    def verify_message_successful_password_restore(self):
        actual_result = self.get_text_title_of_element(RestorePasswordLinkLocators.SUCCESSFUL_RESTORE_PASSWORD_TEXT)
        assert 'Вы успешно установили новый пароль!' in actual_result

    @allure.step('click to "link" btn in invalid token error message')
    def click_to_link_btn_password_error_message(self):
        self.to_click(RestorePasswordLinkLocators.LINK_TO_RESTORE_PASSWORD_IN_ERROR_MESSAGE)

    @allure.step('verify url of forgot password page')
    def verify_url_forgot_password_page(self):
        self.get_url('https://life-help.ru/forgot/')

    @allure.step('set up "new password" in restore password form')
    def set_new_password_fixture(self, first):
        self.set_value(RestorePasswordLinkLocators.NEW_PASSWORD_FIELD, first)

    @allure.step('repeat "new password" in restore password form')
    def repeat_new_password_fixture(self, second):
        self.set_value(RestorePasswordLinkLocators.REPEAT_PASSWORD_FIELD, second)

    @allure.step('verify error message in restore password form')
    def verify_error_message_restore_password_fixture(self, third):
        actual_result = self.get_text_title_of_element(
            RestorePasswordLinkLocators.ERROR_PASSWORD_MESSAGE)
        assert actual_result == third

    @allure.step('verify hidden mode of the password field')
    def verify_hidden_type_password_field(self):
        actual_result = self.is_visible(RestorePasswordLinkLocators.NEW_PASSWORD_FIELD).get_attribute('type')
        assert actual_result == 'password'

    @allure.step('click to "view password" button in password field in restore password page')
    def click_to_view_password_button_restore_password_page(self):
        self.to_click(RestorePasswordLinkLocators.VIEW_PASSWORD_BUTTON_RESTORE_PASSWORD_FIELD)

    @allure.step('verify view mode of the password field')
    def verify_viewed_type_password_field_restore_password_page(self):
        actual_result = self.is_visible(RestorePasswordLinkLocators.NEW_PASSWORD_FIELD).get_attribute('type')
        assert actual_result == 'text'

    @allure.step('click to "hide password" button in password field in restore password page')
    def click_to_hide_password_button_restore_password_page(self):
        self.to_click(RestorePasswordLinkLocators.HIDE_PASSWORD_BUTTON_RESTORE_PASSWORD_FIELD)

    @allure.step('verify disabled type of the "save" button - reset password page')
    def verify_disabled_type_button_save_reset_password_page(self):
        actual_result = self.is_visible(RestorePasswordLinkLocators.TO_SAVE_BUTTON).get_attribute('disabled')
        print(actual_result)

    @allure.step('verify disabled type of the "save" button - reset password page')
    def verify_not_disabled_type_button_save_reset_password_page(self):
        actual_result = self.is_visible(RestorePasswordLinkLocators.TO_SAVE_BUTTON).get_attribute('disabled')
        assert 'disabled' not in actual_result