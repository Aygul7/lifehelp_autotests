from selenium.webdriver.common.by import By

class PromotionLocators:
    SUCCESSFUL_REGISTRATION_PROMOTION_TITLE = (By.CSS_SELECTOR, ".auth__heading")
    GET_DOCTOR_PROMOTION_BTN = (By.CSS_SELECTOR, "button[class='animate__button-filled button__medium-blue-filled']")
    MOVE_TO_USER_ACCOUNT_BTN = (By.CSS_SELECTOR, "button[class='animate__button-outline button__medium-blue-outline']")

    LOGIN_WITH_PASSWORD_BUTTON = (By.CSS_SELECTOR, ".auth__switch-link.link__1")
    EMAIL_PHONE_FIELD = (By.CSS_SELECTOR, "#phone-email__field")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#password_auth")
    AUTH_BUTTON = (By.CSS_SELECTOR, "#auth-password__btn")

    PROMOTION_TITLE_USER_ACCOUNT = (By.CSS_SELECTOR, ".promotions-card__title")
    SELECT_DOCTOR_PROMOTION_BUTTON = (By.XPATH, "//button[contains(text(),'Выбрать психолога')]")

    RAPID_SCHEDULE_2ND_TIME_DOCTOR = (By.XPATH, "//div[@class='choose__specialist-schedule-left']//label[2]")
    RAPID_GO_TO_PAYMENT_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    ORANGE_PAY_BUTTON_ORDER_PAGE = (By.CSS_SELECTOR, ".payment-button__text")
    ORDER_SESSION_BLUE_BTN_DOCTOR_SCHEDULE_PAGE = (By.CSS_SELECTOR, "button[class='animate__button-filled button__"
                                                                    "medium-small-width-blue-filled']")
    SELECT_RAPID_TIME_BLOCK = (By.CSS_SELECTOR, "#select__time-form-136")

    PROMOTION_SESSION_PRICE = (By.CSS_SELECTOR, ".promotions-card__cost")
    PROMOTION_SESSION_COUNT = (By.CSS_SELECTOR, ".promotions-card__count-session")
    PROMOTION_END_DATE = (By.CSS_SELECTOR, ".promotions-card__end-date")