from selenium.webdriver.common.by import By

class RegistrationLocators:
    EMAIL_FIELD_REGISTRATION_FORM = (By.CSS_SELECTOR, "#email")
    PASSWORD1_FIELD_REGISTRATION_FORM = (By.CSS_SELECTOR, "#password1")
    PASSWORD2_REPEAT_FIELD_REGISTRATION_FORM = (By.CSS_SELECTOR, "#password2")
    FIRST_CHECKBOX_CONSENT_REGISTRATION_FORM = (By.XPATH, "//label[1]//span[1]")
    REGISTER_BUTTON = (By.XPATH, "//button[@id='registration_form_input_btn']")
    REGISTRATION_INFO_TEXT = (By.XPATH, "//p[contains(text(),'На Ваш email отправлена ссылка для подтверждения э')]")
    REGISTRATION_ERROR_MESSAGE = (By.XPATH, "//p[@class='user_data__message-error slowly__show-error']")
    ERROR_MESSAGE_REGISTRATION_FORM = (By.CSS_SELECTOR, ".user_data__message-error.slowly__show-error")
    ERROR_MESSAGE_WRONG_REPEAT_PASSWORD_REG_FORM = (By.CSS_SELECTOR, ".user_data__message-error.slowly__show-error")
    RAPID_AUTH_BUTTON_REGISTRATION_PAGE = (By.XPATH, "//button[contains(text(),'Быстрый вход')]")

    VIEW_PASSWORD_BUTTON_REGISTRATION_FIELD = (By.CSS_SELECTOR, ".auth__form-password-control")
    HIDE_PASSWORD_BUTTON_REGISTRATION_FIELD = (By.CSS_SELECTOR, ".auth__form-password-control.view")
    HIDE_REPEAT_PASSWORD_BUTTON_REGISTRATION_FIELD = (By.XPATH, "(//a[@class='auth__form-password-control view'])[2]")