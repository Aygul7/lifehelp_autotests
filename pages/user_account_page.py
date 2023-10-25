from base.base_object import BaseObject
from locators.user_account_locators import UserAccountLocators
import allure
from support.assertions import Assertions


filePath = "C:\\Users\\Owner\\PycharmProjects\\LifeHelp\\support\\happy_client.jpeg"


class UserAccountPage(BaseObject, Assertions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('move to terminated sessions')
    def click_to_terminated_sessions_title(self):
        self.to_click(UserAccountLocators.TERMINATED_SESSIONS)

    @allure.step('verify status of the session - terminated')
    def verify_session_status(self):
        actual_result = self.get_text_title_of_element(UserAccountLocators.TERMINATED_SESSION_STATUS)
        expected_result = 'Завершен'
        self.verify(expected_result, actual_result)

    @allure.step('click to title "personal information" in clients menu')
    def click_to_personal_information_menu(self):
        self.to_click(UserAccountLocators.PERSONAL_INFORMATION)

    @allure.step('click to button "save changes"')
    def click_to_button_save_changes(self):
        self.to_click(UserAccountLocators.SAVE_CHANGES)

    @allure.step('verify message "Your data is saved"')
    def verify_message_your_data_is_saved(self):
        actual_result = self.get_text_title_of_element(UserAccountLocators.YOUR_DATA_IS_SAVED_MESSAGE)
        assert 'Ваши данные' in actual_result

    @allure.step('set client name "Aygul-test"')
    def set_client_name(self):
        self.set_value(UserAccountLocators.NAME_FIELD_PERSONAL_DATA, 'Aygul-test')

    @allure.step('delete client name')
    def delete_client_name(self):
        self.is_visible(UserAccountLocators.NAME_FIELD_PERSONAL_DATA).clear()

    @allure.step('refresh the current page')
    def refresh_page(self):
        self.driver.refresh()

    @allure.step('verify client name "Aygul-test"')
    def verify_client_name(self):
        actual_result = self.is_visible(UserAccountLocators.NAME_FIELD_PERSONAL_DATA).get_attribute('value')
        assert actual_result == 'Aygul-test'

    @allure.step('delete client age "99"')
    def delete_client_age(self):
        self.is_visible(UserAccountLocators.AGE_FIELD_PERSONAL_DATA).clear()

    @allure.step('set client age "99"')
    def set_client_age(self):
        self.set_value(UserAccountLocators.AGE_FIELD_PERSONAL_DATA, '99')

    @allure.step('verify client age "99"')
    def verify_client_age(self):
        actual_result = self.is_visible(UserAccountLocators.AGE_FIELD_PERSONAL_DATA).get_attribute('value')
        assert actual_result == '99'

    @allure.step('verify message to the client - "set your email"')
    def verify_message_set_email(self):
        actual_result = self.get_text_title_of_element(UserAccountLocators.MESSAGE_SET_EMAIL_PERSONAL_DATA)
        expected_result = 'Заполните электронную почту и сохраните изменения'
        self.verify(expected_result, actual_result)

    @allure.step('click to flag on the phone field - user account')
    def click_to_flag_phone_field(self):
        self.to_click(UserAccountLocators.FLAG_PHONE_FIELD)

    @allure.step('click to Belarus flag on the phone field - user account')
    def click_to_belarus_flag_phone_field(self):
        self.to_click(UserAccountLocators.BELARUS_FLAG_PHONE_FIELD)

    @allure.step('verify Belarus phone code')
    def verify_belarus_code_phone_field(self):
        actual_result = self.is_visible(UserAccountLocators.PHONE_FIELD_USER_PERSONAL_DATA).get_attribute('value')
        assert actual_result == '+3759274197879'

    @allure.step('click to Belarus flag on the phone field - user account')
    def click_outside_fields_user_personal_data(self):
        self.to_click(UserAccountLocators.SCREEN_OUTSIDE_FIELDS_PERSONAL_DATA)

    @allure.step('verify error message "wrong phone number" if set rus phone w belarus code')
    def verify_error_message_rus_phone_bel_code(self):
        actual_result = self.is_visible(UserAccountLocators.PHONE_FIELD_USER_PERSONAL_DATA).get_attribute('class')
        assert actual_result == 'account__my-account-form-input p-inp p-int-wrp pd-nn error'

    @allure.step('set password "password"')
    def set_password_client_personal_data(self):
        self.set_value(UserAccountLocators.PASSWORD_FIELD, 'password')

    @allure.step('verify hidden mode of the password field')
    def verify_hidden_type_password_field(self):
        actual_result = self.is_visible(UserAccountLocators.PASSWORD_FIELD).get_attribute('type')
        assert actual_result == 'password'

    @allure.step('click to "view password" button in password field in client account')
    def click_to_view_password_button_client_account(self):
        self.to_click(UserAccountLocators.VIEW_PASSWORD_BUTTON_NEW_PASS_FIELD)

    @allure.step('verify view mode of the password field')
    def verify_viewed_type_password_field(self):
        actual_result = self.is_visible(UserAccountLocators.PASSWORD_FIELD).get_attribute('type')
        assert actual_result == 'text'

    @allure.step('click to "hide password" button in password field in client account')
    def click_to_hide_password_button_client_account(self):
        self.to_click(UserAccountLocators.HIDE_PASSWORD_BUTTON_NEW_PASS_FIELD)

    @allure.step('click to "information" button in password field in client account')
    def click_to_information_btn_password_client_account(self):
        self.to_click(UserAccountLocators.PASSWORD_FIELD_INFORMATION)

    @allure.step('verify title of the demands to password')
    def verify_demands_to_password(self):
        actual_result = self.get_text_title_of_element(UserAccountLocators.LATIN_LETTERS_PASSWORD_DEMANDS)
        expected_result = 'включать буквы латинского алфавита'
        self.verify(expected_result, actual_result)

    @allure.step('set password "repeat password"')
    def set_repeat_password_client_personal_data(self):
        self.set_value(UserAccountLocators.REPEAT_PASSWORD_FIELD, 'password')

    @allure.step('verify hidden mode of the "repeat password" field')
    def verify_hidden_type_repeat_password_field(self):
        actual_result = self.is_visible(UserAccountLocators.REPEAT_PASSWORD_FIELD).get_attribute('type')
        assert actual_result == 'password'

    @allure.step('click to "view password" button in "repeat password" field in client account')
    def click_to_view_repeat_password_button_client_account(self):
        self.to_click(UserAccountLocators.VIEW_PASSWORD_BUTTON_REPEAT_PASS_FIELD)

    @allure.step('verify view mode of the "repeat password" field')
    def verify_viewed_type_repeat_password_field(self):
        actual_result = self.is_visible(UserAccountLocators.REPEAT_PASSWORD_FIELD).get_attribute('type')
        assert actual_result == 'text'

    @allure.step('click to "hide password" button in "repeat password" field in client account')
    def click_to_hide_repeat_password_button_client_account(self):
        self.to_click(UserAccountLocators.HIDE_REPEAT_PASSWORD_BUTTON_NEW_PASS_FIELD)

    @allure.step('click to "information" button in "repeat password" field in client account')
    def click_to_information_btn_repeat_password_client_account(self):
        self.to_click(UserAccountLocators.REPEAT_PASSWORD_FIELD_INFORMATION)

    @allure.step('verify title of the demands to "repeat password" field')
    def verify_demands_to_repeat_password(self):
        actual_result = self.get_text_title_of_element(UserAccountLocators.LATIN_LETTERS_REPEAT_PASSWORD_DEMANDS)
        expected_result = 'включать буквы латинского алфавита'
        self.verify(expected_result, actual_result)

    @allure.step('set client email "abrakadaba@mail.ru"')
    def set_client_email(self):
        self.set_value(UserAccountLocators.EMAIL_FIELD_PERSONAL_DATA, 'abrakadaba@mail.ru')

    @allure.step('delete client email')
    def delete_client_email(self):
        self.is_visible(UserAccountLocators.EMAIL_FIELD_PERSONAL_DATA).clear()

    @allure.step('verify client email "abrakadaba@mail.ru"')
    def verify_client_email(self):
        actual_result = self.is_visible(UserAccountLocators.EMAIL_FIELD_PERSONAL_DATA).get_attribute('value')
        assert actual_result == 'abrakadaba@mail.ru'

    @allure.step('verify error message "set your email"')
    def verify_error_set_your_email_message(self):
        actual_result = self.get_text_title_of_element(UserAccountLocators.ERROR_SET_YOUR_EMAIL_MESSAGE)
        expected_result = 'Введите правильный адрес электронной почты'
        self.verify(expected_result, actual_result)

    @allure.step('scroll to button "save changes"')
    def scroll_to_button_save_changes(self):
        self.move_to_element(UserAccountLocators.SAVE_CHANGES)

    @allure.step('set up password-validation')
    def set_password_validation(self, first):
        self.set_value(UserAccountLocators.PASSWORD_FIELD, first)

    @allure.step('repeat password-validation')
    def repeat_password_validation(self, second):
        self.set_value(UserAccountLocators.REPEAT_PASSWORD_FIELD, second)

    @allure.step('verify error message - password validation')
    def verify_error_password_validation(self, third):
        actual_result = self.get_text_title_of_element(UserAccountLocators.ERROR_PASSWORD_VALIDATION_MESSAGE)
        expected_result = third
        self.verify(expected_result, actual_result)

    @allure.step('set password "pass"')
    def set_error_length_password_client_personal_data(self, first):
        self.set_value(UserAccountLocators.PASSWORD_FIELD, first)

    @allure.step('set password "repeat password"')
    def set_error_length_repeat_password_client_personal_data(self, second):
        self.set_value(UserAccountLocators.REPEAT_PASSWORD_FIELD, second)

    @allure.step('verify error message "set your email"')
    def verify_error_length_password(self, third):
        actual_result = self.get_text_title_of_element(UserAccountLocators.ERROR_PASSWORD_LENGTH)
        expected_result = third
        self.verify(expected_result, actual_result)

    @allure.step('verify message "your email is not verified"')
    def verify_message_your_email_not_verified(self):
        actual_result = self.get_text_title_of_element(UserAccountLocators.YOUR_EMAIL_NOT_VERIFIED_MSG)
        assert 'не подтверждена' in actual_result

    @allure.step('click to "get letter" button in message that email is not yet verified in client account')
    def click_to_send_letter_btn_not_verified_email_client_account(self):
        self.to_click(UserAccountLocators.GET_LETTER_TO_VERIFY_EMAIL)

    @allure.step('verify message "successful sent letter to your email"')
    def verify_message_msg_successful_sent_letter_to_your_email(self):
        actual_result = self.get_text_title_of_element(UserAccountLocators.SUCCESSFUL_SENT_LETTER_MSG)
        assert 'Письмо успешно отправлено!' in actual_result

    @allure.step('upload client photo')
    def upload_client_photo(self):
        self.set_value(UserAccountLocators.UPLOAD_PHOTO_FIELD, filePath)

    @allure.step('click to "upload image" field in client account')
    def click_to_upload_image_field_client_account(self):
        self.to_click(UserAccountLocators.UPLOAD_PHOTO_FIELD)

    @allure.step('scroll to button "save changes"')
    def scroll_to_user_avatar(self):
        self.move_to_element(UserAccountLocators.USER_AVATAR)

