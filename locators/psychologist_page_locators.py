from selenium.webdriver.common.by import By

class PsychologistPageLocators:

    PSYCHOLOGIST_ELENA_KALKAN_TITLE = (By.XPATH, "//h2[contains(text(),'Елена Геннадьевна')]")
    FIRST_ORDER_KALKAN = (By.CSS_SELECTOR, "body > div:nth-child(4) > main:nth-child(2) > section:nth-child(2) >"
                                           " div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) >"
                                           " div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) >"
                                           " div:nth-child(1) > form:nth-child(2) > div:nth-child(2) > div:nth-child(3) >"
                                           " div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) >"
                                           " div:nth-child(2) > div:nth-child(3) > label:nth-child(1) > div:nth-child(2)")
    FIRST_ORDER_TIME = (By.XPATH, "//div[@class='swiper-slide swiper-slide-next']//label[1]")
    RAPID_ORDER_TIME = (By.XPATH, "//div[@class='choose__specialist-schedule-left']//label[1]")
    MOVE_TO_PAYMENT_BUTTON = (By.CSS_SELECTOR, "button[class='animate__button-filled button__medium-small-width-blue-"
                                               "filled']")
    ORDER_TIME_TEST = (By.CSS_SELECTOR, "div[class='swiper-slide swiper-slide-next'] label:nth-child(1)")

    ELENA_KALKAN_RAPID_TIME_3 = (By.XPATH, "//div[@class='choose__specialist-schedule-left']//label[3]")
    ELENA_KALKAN_VIDEO = (By.XPATH, "//a[@class='choose__specialist-schedule-avatar video ']//*[name()='svg']")
    VIDEO_FRAME = (By.XPATH, "//div[@class='doctor__video-container']//iframe")
    RAPID_SCHEDULE_3RD_TIME_DOCTOR = (By.XPATH, "//div[@class='choose__specialist-schedule-left']//label[3]")
    RAPID_GO_TO_PAYMENT_BTN = (By.CSS_SELECTOR, ".quick__appointment.animate__button-filled.button__medium-small"
                                                "-width-blue-filled")
    NAME_FIELD_ORDER_PAGE = (By.CSS_SELECTOR, "input[placeholder='Имя']")
    PHONE_FIELD_ORDER_PAGE = (By.CSS_SELECTOR, "#id_phone")
    EMAIL_FIELD_ORDER_PAGE = (By.CSS_SELECTOR, "input[placeholder='Email']")
    I_HAVE_PROMOCODE = (By.CSS_SELECTOR, "div[class='info__client-promo'] a")
    INPUT_PROMOCODE_FIELD_ORDER_PAGE = (By.CSS_SELECTOR, "input[placeholder='Введите промокод']")
    SUBMIT_PROMOCODE_BUTTON_ORDER_PAGE = (By.CSS_SELECTOR, "button[type='submit']")
    CARD_RF_BUTTON = (By.CSS_SELECTOR, "label[for='russian']")
    FOREIGN_CARD_BUTTON = (By.CSS_SELECTOR, "label[for='foreign']")
    PAYMENT_GREEN_BTN_ORDER_PAGE = (By.CSS_SELECTOR, "#payment__btn")
    NOT_INTERESTING_BTN = (By.CSS_SELECTOR, "#continue-payment")
    PRICE_2950_DOCTOR_PAGE = (By.XPATH, "//span[contains(text(),'2950.00 ₽')]")
    PRICE_4200_DOCTOR_PAGE = (By.XPATH, "//span[contains(text(),'4200.00 ₽')]")
    PRICE_4850_DOCTOR_PAGE = (By.XPATH, "//span[contains(text(),'4850.00 ₽')]")
    DOCTOR_NAME_DOCTOR_PAGE = (By.XPATH, "//h2[contains(text(),'Елена Геннадьевна')]")
