from selenium.webdriver.common.by import By

class UserAccountLocators:
    TERMINATED_SESSIONS = (By.CSS_SELECTOR, "a[class='account__my-notes-tabs-nav-link']")
    TERMINATED_SESSION_STATUS = (By.XPATH, "(//span[contains(text(),'Завершен')])[1]")
    YOUR_DATA_IS_SAVED_MESSAGE = (By.CSS_SELECTOR, ".account__success-text")
    PERSONAL_INFORMATION = (By.XPATH, "//span[contains(text(),'Личные данные')]")
    SAVE_CHANGES = (By.CSS_SELECTOR, ".animate__button-filled.button__medium-blue-filled.my__account-save-btn")
    NAME_FIELD_PERSONAL_DATA = (By.CSS_SELECTOR, "#id_first_name")
    AGE_FIELD_PERSONAL_DATA = (By.CSS_SELECTOR, "#id_age")
    MESSAGE_SET_EMAIL_PERSONAL_DATA = (By.CSS_SELECTOR, "div[class='auth__email-text'] h3")
    FLAG_PHONE_FIELD = (By.CSS_SELECTOR, ".iti__flag-container")
    BELARUS_FLAG_PHONE_FIELD = (By.XPATH, "(//div[@class='iti__flag-box'])[2]")
    PHONE_FIELD_USER_PERSONAL_DATA = (By.XPATH, "//input[@name='phone']")
    SCREEN_OUTSIDE_FIELDS_PERSONAL_DATA = (By.CSS_SELECTOR, ".account__main-content.account__main-content--fullwidth")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#password")
    VIEW_PASSWORD_BUTTON_NEW_PASS_FIELD = (By.XPATH, "(//a[@class='auth__form-password-control profile'])[1]")
    HIDE_PASSWORD_BUTTON_NEW_PASS_FIELD = (By.XPATH, "(//a[@class='auth__form-password-control profile view'])[1]")
    PASSWORD_FIELD_INFORMATION = (By.XPATH, "(//div[@class='input__prompt'])[1]")
    DEMANDS_TO_PASSWORD = (By.XPATH, "(//div[contains(text(),'Требования к паролю:')])[1]")
    LATIN_LETTERS_PASSWORD_DEMANDS = (By.XPATH, "(//li[contains(text(),'включать буквы латинского алфавита')])[1]")
    REPEAT_PASSWORD_FIELD = (By.CSS_SELECTOR, "#password2")
    VIEW_PASSWORD_BUTTON_REPEAT_PASS_FIELD = (By.XPATH, "(//a[@class='auth__form-password-control profile'])[2]")
    HIDE_REPEAT_PASSWORD_BUTTON_NEW_PASS_FIELD = (By.XPATH, "(//a[@class='auth__form-password-control profile view'])[2]")
    REPEAT_PASSWORD_FIELD_INFORMATION = (By.XPATH, "(//div[@class='input__prompt'])[2]")
    LATIN_LETTERS_REPEAT_PASSWORD_DEMANDS = (By.XPATH, "(//li[contains(text(),'включать буквы латинского алфавита')])[2]")
    EMAIL_FIELD_PERSONAL_DATA = (By.CSS_SELECTOR, "#id_email")
    ERROR_SET_YOUR_EMAIL_MESSAGE = (By.XPATH, "//p[contains(text(),'Введите правильный адрес электронной почты')]")
    ERROR_PASSWORD_VALIDATION_MESSAGE = (By.CSS_SELECTOR, ".user_data__errors.active")
    ERROR_PASSWORD_LENGTH = (By.CSS_SELECTOR, "#parsley-id-17")
    YOUR_EMAIL_NOT_VERIFIED_MSG = (By.CSS_SELECTOR, "div[class='auth__email-text'] h3")
    GET_LETTER_TO_VERIFY_EMAIL = (By.XPATH, "//button[contains(text(),'Получить письмо')]")
    SUCCESSFUL_SENT_LETTER_MSG = (By.CSS_SELECTOR, ".auth__enter-success-send")
    UPLOAD_PHOTO_FIELD = (By.CSS_SELECTOR, ".account__my-account-file-upload.js-file-upload")
    USER_AVATAR = (By.CSS_SELECTOR,".page-header__user-name")


    MY_DOCTOR_NAME_USER_ACCOUNT = (By.XPATH, "//div[@class='account__my_doctor-text']//h4[contains(text(),"
                                             "'Имя Отчество')]")
    DOCTOR_NAME_CHAT_TITLE_USER_ACCOUNT = (By.XPATH, "//h3[contains(text(),'Имя Отчество')]")
    DOCTOR_NAME_TERMINATED_SESSION_USER_ACCOUNT = (By.XPATH, "(//h4[@class='account__my-notes-results-card-user-name']"
                                                             "[contains(text(),'Имя Отчество')])[3]")
    ACTIVATE_CERTIFICATE_TITLE_MY_SCHEDULE = (By.CSS_SELECTOR, ".page-header__user.js-open-modal")
    MODAL_TITLE_ACTIVATE_CERTIFICATE = (By.CSS_SELECTOR, "div[class='certificate__form-title-wrapper'] h1")

    PAYMENT_HISTORY_TITLE = (By.XPATH, "//a[contains(text(),'История платежей')]")
    DOCTOR_NAME_PAYMENT_HISTORY = (By.XPATH, "(//div[@class='account__my-history-table-specialist']"
                                             "[contains(text(),'Имя Отчество')])[1]")
    DOCTOR_NAME_REGULAR_SESSIONS_PAGE = (By.CSS_SELECTOR, "div[class='regular-schedule__doctor-info'] h4")