from selenium.webdriver.common.by import By

class RestorePasswordLinkLocators:
    RESTORE_PASSWORD_PAGE_HEADING = (By.XPATH, "//h1[contains(text(),'Обновление пароля')]")
    NEW_PASSWORD_FIELD = (By.XPATH, "//input[@id='password1']")
    REPEAT_PASSWORD_FIELD = (By.XPATH, "//input[@id='password2']")
    TO_SAVE_BUTTON = (By.CSS_SELECTOR, ".auth__form-bottom-btns")
    INVALID_TOKEN_ERROR_MESSAGE = (By.CSS_SELECTOR, ".user_data__message-error.slowly__show-error")
    LINK_TO_RESTORE_PASSWORD_IN_ERROR_MESSAGE = (By.CSS_SELECTOR, "a[href='/forgot/']")
    ERROR_PASSWORD_MESSAGE = (By.CSS_SELECTOR, ".user_data__message-error.slowly__show-error")
    VIEW_PASSWORD_BUTTON_RESTORE_PASSWORD_FIELD = (By.CSS_SELECTOR, ".auth__form-password-control")
    HIDE_PASSWORD_BUTTON_RESTORE_PASSWORD_FIELD = (By.CSS_SELECTOR, ".auth__form-password-control.view")
    SUCCESSFUL_RESTORE_PASSWORD_TEXT = (By.XPATH, "//h1[contains(text(),'Вы успешно установили новый пароль!')]")