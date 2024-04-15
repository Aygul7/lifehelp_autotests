from selenium.webdriver.common.by import By

class QuestionnaireLocators:
    CLOSE_WIDGET_BUTTON = (By.XPATH, '//jdiv[@id="jivo_close_button"]')
    INDIVIDUAL_CONSULTATION_BUTTON = (By.XPATH, '//label[contains(text(),"Индивидуальная")]')
    PAIRED_CONSULTATION_BUTTON = (By.XPATH, '//label[contains(text(),"Индивидуальная")]')
    RUSSIAN_LANGUAGE_BUTTON = (By.XPATH, '//label[contains(text(),"Русский")]')
    TATAR_LANGUAGE_BUTTON = (By.XPATH, '//label[contains(text(),"Татарский")]')
    VIDEO_BUTTON = (By.XPATH, '//label[contains(text(),"Видео")]')
    AUDIO_BUTTON = (By.XPATH, '//label[contains(text(),"Аудио")]')
    CHAT_BUTTON = (By.XPATH, '//label[contains(text(),"Чат")]')
    AGE_FIELD = (By.XPATH, '//input[@id="age"]')
    NEXT_BUTTON = (By.XPATH, '//button[contains(text(),"Далее")]')
    PERSONAL_QUESTIONS_TITLE = (By.CSS_SELECTOR, "a:nth-child(2) p:nth-child(1)")

    NEXT_BUTTON_QUESTIONNAIRE = (By.CSS_SELECTOR, "button[class='animate__button-filled button__medium-blue-filled']")
    STRESS_CHECKBOX_QUESTIONNAIRE = (By.XPATH, "//span[contains(text(),'Стресс')]")
    PSYCHOLOGIST_PREFERENCES_TITLE_QUESTIONNAIRE = (By.CSS_SELECTOR, "a[class='progress_page']")
    AGE_OVER_30_BUTTON_QUESTIONNAIRE = (By.XPATH, "//label[contains(text(),'После 30')]")
    SELECT_PSYCHOLOGIST_TITLE_QUESTIONNAIRE = (By.CSS_SELECTOR, "a:nth-child(4) p:nth-child(1)")
    CHOOSE_SPECIALIST_LIST = (By.CSS_SELECTOR, ".choose-specialist__choices")
    IRINA_PANKOVA_TITLE_CHOOSE_DOCTOR_LIST = (By.XPATH, "//h4[contains(text(),'Ирина')]")
    GENERAL_QUESTIONS_TITLE_QUESTIONNAIRE = (By.XPATH, "//a[@class='progress_page active']//p[1]")

    INDIVIDUAL_90_QUESTIONNAIRE_GENERAL = (By.CSS_SELECTOR, "label[for='71']")
    ALISA_IVANNIKOVA_TITLE_CHOOSE_DOCTOR_LIST = (By.XPATH, "//h4[contains(text(),'Алиса')]")

    TATAR_BUTTON_QUESTIONNAIRE = (By.CSS_SELECTOR, "label[for='4']")
    ALIYA_ASKAROVA_TITLE_CHOOSE_DOCTOR_LIST = (By.XPATH, "//h4[contains(text(),'Алия')]")

    PAIRED_CONSULTATION_BUTTON_QUESTIONNAIRE = (By.CSS_SELECTOR, "label[for='2']")
    DIFFICULTIES_IN_RELATIONSHIP_PAIRED_BUTTON_CONSULTATION = (By.XPATH, "//span[contains(text(),'Сложности в отношениях')]")
    ELENA_KALKAN_TITLE_CHOOSE_DOCTOR_LIST = (By.XPATH, "//h4[contains(text(),'Елена')]")
    ELENA_KALKAN_IMAGE_DOCTOR_LIT = (By.XPATH, "//a[@class='choose-specialist__choices-item active']//div[@class="
                                               "'choose-specialist__choices-item-image-container']")
    SET_YOUR_AGE_QUESTIONNAIRE_WINDOW = (By.XPATH, "//div[@id='empty-age']//div[@class='error__age-text']//div[1]")
    AGE_ABOVE16_WINDOW_QUESTIONNAIRE = (By.CSS_SELECTOR, "div[id='error-age'] div[class='error__age-text'] "
                                                         "div:nth-child(1)")

    DOCTOR_AGE_TILL_30_QUESTIONNAIRE_PREFERENCES = (By.CSS_SELECTOR, "label[for='49']")
    MEDINA_NUNUEVA_TITLE_CHOOSE_DOCTOR_LIST = (By.XPATH, "//h4[contains(text(),'Медина')]")

    DOCTOR_MALE_QUESTIONNAIRE_PREFERENCES = (By.CSS_SELECTOR, "label[for='56']")
    NIKITA_YUJHAKOV_TITLE_CHOOSE_DOCTOR_LIST = (By.XPATH, "//h4[contains(text(),'Никита')]")
    DMITRII_PROKOPOV_TITLE_CHOOSE_DOCTOR_LIST = (By.XPATH, "//h4[contains(text(),'Дмитрий')]")

    DOCTOR_WO_CHILDREN_QUESTIONNAIRE_PREFERENCES = (By.CSS_SELECTOR, "label[for='53']")
    LILIA_SEREGINA_TITLE_CHOOSE_DOCTOR_LIST = (By.XPATH, "//h4[contains(text(),'Лилия')]")
    LILIA_SEREGINA_FULL_NAME_WO_SURNAME_DOCTOR_LIST = (By.XPATH, "//h2[contains(text(),'Лилия Сергеевна')]")

    DOCTOR_PRICE_SPECIALIST_PAGE_QUESTIONNAIRE = (By.XPATH, "//div[@class='choose__specialist-header-price']")
    TERRIBLE_PERSONAL_STATE_QUESTIONNAIRE = (By.CSS_SELECTOR, "label[for='14']")

    FIRST_ORDER_TIME_DOCTOR_PAGE_AFTER_QUESTIONNAIRE = (By.XPATH, "//div[@class='choose__specialist-schedule-left']//label[1]")
    SUBMIT_PERSONAL_INFO_AUTH_FORM_AFTER_QUESTIONNAIRE = (By.CSS_SELECTOR, ".conent-right__sub-header")
    TO_ORDER_RAPID_TIME_BTN_DOCTOR_PAGE_AFTER_QUESTIONNAIRE = (By.CSS_SELECTOR, ".quick__appointment.animate__button-"
                                                                                "filled.button__medium-small-width-blue-filled")
    FIND_PSYCHOLOGIST_ACCOUNT_BTN = (By.CSS_SELECTOR, ".account__find-psycho")

    LOGIN_BUTTON = (By.CSS_SELECTOR, ".animate__button-outline.button__small-small-width-blue-outline")
    LOGIN_WITH_PASSWORD_BUTTON = (By.CSS_SELECTOR, ".auth__switch-link.link__1")
    EMAIL_PHONE_FIELD = (By.CSS_SELECTOR, "#phone-email__field")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#password_auth")
    AUTH_BUTTON = (By.CSS_SELECTOR, "#auth-password__btn")


    NAME_INPUT_FIELD_ORDER_AUTH_PAGE = (By.XPATH, "//input[@id='name']")
    PHONE_INPUT_FIELD_ORDER_AUTH_PAGE = (By.XPATH, "//input[@id='phone']")
    AGREEMENT_OFFER_CHECKBOX_ORDER_AUTH_PAGE = (By.CSS_SELECTOR, "label[for='agreement'] span[class='checkbox']")
    MAILING_CONSENT_CHECKBOX_ORDER_AUTH_PAGE = (By.XPATH, "//label[@for='agreement-email']//span[@class='checkbox']")
    MOVE_TO_ORDER_BTN_ORDER_AUTH_PAGE = (By.CSS_SELECTOR, ".primary__button-filled.azure.order-auth__button")

    ENTER_SMS_CODE_MODAL_WINDOW_TITLE = (By.CSS_SELECTOR, ".modal-heading")

    DOCTOR_PROFILE_TITLE_AUTH_ORDER_PAGE = (By.CSS_SELECTOR, ".order-nav__link[href='https://life-help.ru/"
                                                             "questionnaire/choose-doctor/']")





