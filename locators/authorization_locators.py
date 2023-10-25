from selenium.webdriver.common.by import By

class AuthorizationLocators:
    CLOSE_WIDGET_BUTTON = (By.XPATH, '//jdiv[@id="jivo_close_button"]')
    COOKIE_BUTTON = (By.CSS_SELECTOR, '.animate__button-filled.button__medium-red-filled')
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".animate__button-outline.button__small-small-width-blue-outline")
    LOGIN_WITH_PASSWORD_BUTTON = (By.CSS_SELECTOR, ".auth__switch-link.link__1")
    EMAIL_PHONE_FIELD = (By.CSS_SELECTOR, "#phone-email__field")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#password_auth")
    AUTH_BUTTON = (By.CSS_SELECTOR, "#auth-password__btn")
    PHONE_FIELD = (By.CSS_SELECTOR, "#phone-code__field")
    FIRST_CHECKBOX = (By.CSS_SELECTOR, "label[class='auth__-form-agreements-checkbox validate-wrapper'] "
                                       "span[class='auth__-form-agreements-checkbox-mark']")
    FIRST_CHECKBOX_2 = (By.CSS_SELECTOR, ".auth__-form-agreements-checkbox.validate-wrapper")
    SECOND_CHECKBOX = (By.CSS_SELECTOR, "label[class='auth__-form-agreements-checkbox']")
    GET_CODE_BTN = (By.CSS_SELECTOR, "#get-code__btn")
    CODE_FIELD = (By.CSS_SELECTOR, "#code")
    AUTH_CODE_BUTTON = (By.CSS_SELECTOR, "#auth-code__btn")

    CHAT_MENU_NAVIGATION = (By.XPATH, "//main[@class='page-main']//a[3]//div[1]")
    CHAT_TEXT_FIELD = (By.CSS_SELECTOR, "#message-text__input")
    SEND_MSG_CHAT_BTN = (By.CSS_SELECTOR, "button[type='submit'] span")
    MESSAGE_TEXT = (By.XPATH, "//div[@id='1647']//div[@class='block__message-text'][normalize-space()='Hello, World!']")

    # (// div[@class ='block__message-status'])[3]
    #'// div[ @class = 'block__message.my__message.last-message'] // div[@class ='block__message-text'][normalize-space()='Hello, World!']'

    CHAT_MENU_NAVIGATION_PSYCHOLOGIST = (By.XPATH, "//nav[@class='account__menu']//div[1]")
    CHAT_W_CLIENT_AYGUL = (By.XPATH, "//h3[normalize-space()='Aygul-test']")
    MESSAGE_TEXT_PSYCHOLOGIST = (By.XPATH, "//div[@class='block__message-text'][normalize-space()='Hello!']")

    CONTEXT_MENU_DOTS_CLIENT_ACCOUNT = (By.CSS_SELECTOR, "#context-menu-dots")
    LOGOUT_BTN = (By.XPATH, "//span[contains(text(),'Выйти')]")

    LIFE_HELP_LOGO = (By.CSS_SELECTOR, ".page-header__logo")

    TERMINATED_SESSIONS_CLIENT = (By.XPATH, "//a[contains(text(),'Закрытые сессии')]")
    ORDER_SESSION_AGAIN = (By.CSS_SELECTOR, "div[class='account__my-notes-tab-item active'] li:nth-child(1) "
                                            "div:nth-child(1) div:nth-child(4) a:nth-child(1) button:nth-child(1)")

    NEAREST_TIME_SLOT = (By.CSS_SELECTOR, "body > div:nth-child(4) > main:nth-child(2) > div:nth-child(1) > div:nth-"
                                          "child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:"
                                          "nth-child(1) > div:nth-child(2) > form:nth-child(2) > label:nth-child(5) "
                                          "> span:nth-child(2)")
    RAPID_GO_TO_PAYMENT_BTN = (By.CSS_SELECTOR, "button[type='submit']")

    GET_PSYCHOLOGIST_BUTTON = (By.XPATH, "//button[@class='animate__button-filled button__small-red-filled']")

    PERSONAL_QUESTIONS_TITLE = (By.CSS_SELECTOR, "a:nth-child(2) p:nth-child(1)")

    MY_BALANCE_MENU_TITLE = (By.XPATH, "//a[contains(@class,'balance-link')]//div[1]")
    BUY_PACKAGE_BUTTON = (By.XPATH, "//button[contains(text(),'Купить пакет')]")
    PACKAGE_4_SESSIONS_BUY_BUTTON = (By.XPATH, "//div[@class='package__items']//div[1]//a[1]//button[1]")
    CARD_RF_BUTTON_PACKAGE = (By.CSS_SELECTOR, "label[for='russian']")
    FOREIGN_CARD_PACKAGE = (By.CSS_SELECTOR, "label[for='foreign']")
    PAY_ONLINE_ORDER_BUTTON_PACKAGE = (By.CSS_SELECTOR, "button[type='submit']")
    PAYMENT_HEADING_TEXT = (By.CSS_SELECTOR, ".payment__heading-text")
    PAY_RUSSIAN_CARD_PRODAMUS = (By.CSS_SELECTOR, "a[id='payment-method-614851'] h1[class='no-margin']")
    PRODAMUS_PAYMENT_HEADING_TEXT = (By.CSS_SELECTOR, ".inline.m-l-10.m-r-10.m-b-0.m-t-0.v-align-middle")
    NOT_RUSSAIN_CARD_PRODAMUS = (By.XPATH, "//div[@class='tab-item ']")
    VISA_MS_KZT_CARD_PRODAMUS = (By.XPATH, "//h1[normalize-space()='Visa/Mastercard, KZT']")

    CARD_RF_BUTTON_SESSION = (By.CSS_SELECTOR, "label[for='russian']")
    PAY_ONLINE_ORDER_BUTTON_SESSION = (By.CSS_SELECTOR, "#payment__btn")
    FOREIGN_CARD_SESSION = (By.CSS_SELECTOR, "label[for='foreign']")

    AGE_FIELD = (By.CSS_SELECTOR, "#age")
    NEXT_BUTTON_QUESTIONNAIRE = (By.CSS_SELECTOR, "button[class='animate__button-filled button__medium-blue-filled']")
    STRESS_CHECKBOX_QUESTIONNAIRE = (By.XPATH, "//span[contains(text(),'Стресс')]")
    PSYCHOLOGIST_PREFERENCES_TITLE_QUESTIONNAIRE = (By.CSS_SELECTOR, "a[class='progress_page']")
    AGE_OVER_30_BUTTON_QUESTIONNAIRE = (By.XPATH, "//label[contains(text(),'После 30')]")
    SELECT_PSYCHOLOGIST_TITLE_QUESTIONNAIRE = (By.CSS_SELECTOR, "a:nth-child(4) p:nth-child(1)")
    CHOOSE_SPECIALIST_LIST = (By.CSS_SELECTOR, ".choose-specialist__choices")
    ANNA_KAPU_TITLE_CHOOSE_DOCTOR_LIST = (By.XPATH, "//h4[contains(text(),'Анна')]")
    IRINA_PANOVA_TITLE_CHOOSE_DOCTOR_LIST = (By.XPATH, "//h4[contains(text(),'Ирина')]")
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

    COUNTRIES_ARROW_BUTTON_RAPID_AUTH = (By.CSS_SELECTOR, ".iti__arrow")
    COUNTRIES_FLAGS_LIST = (By.CSS_SELECTOR, ".iti__flag-container")
    GERMANY_FLAG = (By.CSS_SELECTOR, "li[id='iti-0__item-de-preferred'] span[class='iti__country-name']")
    SELECTED_FLAG = (By.CSS_SELECTOR, ".iti__selected-flag")
    SELECTED_GERMANY_FLAG = (By.CSS_SELECTOR, "div[title='Germany (Deutschland): +49']")
    GEORGIA_FLAG = (By.CSS_SELECTOR, "#iti-0__item-ge-preferred")

    FORGOT_PASSWORD_HYPERTEXT = (By.XPATH, "//span[contains(text(),'Забыли пароль')]")
    EMAIL_FIELD_FORGOT_PASSWORD = (By.CSS_SELECTOR, "#email_set_new_password")
    RECOVER_PASSWORD_BUTTON = (By.CSS_SELECTOR, "#password_recovery__form-input-btn")
    TEXT_SENT_LINK_TO_RECOVER_PASSWORD = (By.XPATH, "//p[contains(text(),"
                                                    "'На Ваш email отправлена ссылка для восстановления ')]")
    REGISTER_HYPERTEXT = (By.XPATH, "//span[contains(text(),'Зарегистрироваться')]")
    # EMAIL_FIELD_REGISTRATION_FORM = (By.CSS_SELECTOR, "#email")
    # PASSWORD1_FIELD_REGISTRATION_FORM = (By.CSS_SELECTOR, "#password1")
    # PASSWORD2_REPEAT_FIELD_REGISTRATION_FORM = (By.CSS_SELECTOR, "#password2")
    # FIRST_CHECKBOX_CONSENT_REGISTRATION_FORM = (By.XPATH, "//label[1]//span[1]")
    # REGISTER_BUTTON = (By.XPATH, "//button[@id='registration_form_input_btn']")
    # REGISTRATION_INFO_TEXT = (By.XPATH, "//p[contains(text(),'На Ваш email отправлена ссылка для подтверждения э')]")
    # REGISTRATION_ERROR_MESSAGE = (By.XPATH, "//p[@class='user_data__message-error slowly__show-error']")

    OOO_LIFE_HELP_FOOTER = (By.XPATH, "//div[contains(text(),'© 2023 ООО “Лайф Хелп”')]")
    FOOTER_SOCIAL_NETWORKS = (By.CSS_SELECTOR, ".footer__link-social-title")
    CONSENT_MAILING_DOCUMENT_FOOTER = (By.XPATH, "//a[contains(text(),'Согласие на получение информационных рассылок')]")
    AGREEMENT_FOOTER_DOCUMENT = (By.CSS_SELECTOR, ".landing-footer__policy.landing-footer-docx[href='/agreement/']")


    TELEGRAM_BUTTON_NEAR_HELP = (By.CSS_SELECTOR, ".animate__button-filled.telegram-button")
    TELEGRAM_CARE_LOGO = (By.CSS_SELECTOR, "div[class='care-service-social'] img[alt='telegram-logo']")
    TELEGRAM_SOCIAL_NETWORK_GROUP = (By.CSS_SELECTOR, ".landing-footer__social-link[href='https://t.me/life_help_pro']")

    WHATSAPP_BUTTON_NEAR_HELP = (By.XPATH, "//button[normalize-space()='WhatsApp']")
    WHATSAPP_CARE_LOGO = (By.CSS_SELECTOR, "div[class='care-service-social'] img[alt='whatsapp-logo']")
    WHATSAPP_PAGE_HEADER = (By.XPATH, "//span[@class='_afw1']//img[@alt='Главная страница WhatsApp']")

    LANDING_FOOTER_BOTTOM = (By.CSS_SELECTOR, ".landing-footer__bottom-row")

    VIEW_PASSWORD_BUTTON_AUTHORIZATION_FIELD = (By.CSS_SELECTOR, ".auth__form-password-control")
    HIDE_PASSWORD_BUTTON_AUTHORIZATION_FIELD = (By.CSS_SELECTOR, ".auth__form-password-control.view")

    ERROR_MESSAGE_WRONG_PASSWORD_AUTH_PAGE = (By.CSS_SELECTOR, ".auth__form-password-error.err-txt.active")
    ERROR_MESSAGE_WRONG_SMS_CODE_AUTH_PAGE = (By.CSS_SELECTOR, ".auth__form-code-error.err-txt.active")
    # AUTH_CODE_BUTTON = (By.CSS_SELECTOR, "#auth-code__btn")

    COME_BACK_TO_CABINET_BUTTON = (By.XPATH, "(//button[contains(text(),'Перейти в личный кабинет')])[1]")
    SESSION_WAITS_FOR_PAYMENT_TEXT = (By.XPATH, "//div[@class='account__my-notes-results-card-status grid__area-payed"
                                                " no-payed']")
    THREE_DOTS_ORDERED_SESSION = (By.CSS_SELECTOR, ".account__my-notes-results-card-actions-dots")
    RESCHEDULE_ORDERED_SESSION_DROP_DOWN_LINK = (By.CSS_SELECTOR, "a[class='account__my-notes-results-card-"
                                                                  "actions-dropdown-link']")
    RESCHEDULE_PAIED_SESSION_DROP_DOWN_LINK = (By.XPATH, "(//a[@class='account__my-notes-results-card-actions-dropdown"
                                                         "-link'][contains(text(),'Перенести сеанс')])[1]")
    RESCHEDULE_ONLY_THIS_SESSION_BUTTON = (By.XPATH, "//button[contains(text(),'Перенести только эту')]")
    ARROW_TO_BACK_FROM_VIDEOSESSION_PAGE_TO_MY_SCHEDULE = (By.CSS_SELECTOR, ".account__my-video-back-link")

    SELECT_TIME_TO_RESCHEDULE_ORDER = (By.XPATH, "(//label)[7]")
    CHANGE_TIME_BUTTON_ORDER = (By.XPATH, "//button[contains(text(),'Изменить время')]")
    DENY_ORDER_PAYMENT_DROP_DOWN_LINK = (By.CSS_SELECTOR, ".account__my-notes-results-card-actions-dropdown-link."
                                                          "js-open-modal.js-payment-cancel")
    YES_DENY_ORDER_PAYMENT_BUTTON = (By.CSS_SELECTOR, "div[id='payment-cancel'] button[class='animate__button-filled "
                                                      "button__medium-blue-filled payment_cansel_btn js-close-modal']")
    GOOD_BUTTON_AFTER_DENY_ORDER_PAYMENT = (By.XPATH, "//button[contains(text(),'Хорошо')]")
    CLIENTS_AND_AIMS_MENU_PSYCHOLOGIST = (By.XPATH, "//span[contains(text(),'Клиенты и цели')]")
    SELECT_AYGUL_TEST_CLIENTS_AIMS = (By.CSS_SELECTOR, "div[class='account__my-notes-tab-item active'] a:nth-child(11)")
    THREE_DOTS_PSYCHOLOGIST_CLIENTS_AIM = (By.XPATH, "//a[@class='client__context-menu-button']//*[name()='svg']")
    CREATE_NEW_SESSION_PSYCHOLOGIST = (By.CSS_SELECTOR, ".context__menu-link.create__new-session")
    TO_CREATE_BUTTON_CREATE_SESSION_PSYCHOLOGIST = (By.CSS_SELECTOR, "div[class='form__buttons'] button"
                                                                    "[class='animate__button-filled button__"
                                                                    "medium-blue-filled']")
    SUCCESSFUL_CREATION_SESSION_PSYCHOLOGIST_TEXT = (By.CSS_SELECTOR, "div[id='recreate-session-success'] h1")
    FINE_BUTTON_CREATE_SESSION_PSYCHOLOGIST = (By.XPATH, "//button[contains(text(),'Отлично!')]")
    YOU_HAVE_SUCCESSFULLY_ORDERED_CLIENT_SESSION_MSG = (By.XPATH, "//div[@id='recreate-session-success']//h1")
    ERROR_MSG_SELECTED_ORDER_TIME_IS_OCCUPIED = (By.XPATH, "//p[@class='recreate__session-notification-error-text']")

    SET_YOUR_AGE_QUESTIONNAIRE_WINDOW = (By.XPATH, "//div[@id='empty-age']//div[@class='error__age-text']//div[1]")

    TEST_ACTION_SELECT_PSYCHOLOGIST_BUTTON = (By.XPATH, "//button[contains(text(),'Выбрать психолога')]")

    I_HAVE_PROMOCODE_TITLE_SESSION_ORDER_PAGE = (By.CSS_SELECTOR, "div[class='info__client-promo'] a")
    ENTER_PROMOCODE_FIELD_SESSION_ORDER_PAGE = (By.CSS_SELECTOR, "input[placeholder='Введите промокод']")
    PAYMENT_BUTTON_ORDER_PAGE = (By.XPATH, "//span[@class='order__detail-price button__price']")
    SUBMIT_PROMOCODE_BUTTON_SESSION_ORDER_PAGE = (By.XPATH, "//button[contains(text(),'Применить')]")
    FINAL_PRICE_AFTER_PROMOCODE = (By.XPATH, "//p[@class='total__price-text']//span[@class='order__detail-price']"
                                             "[normalize-space()='0,00']")

    ORDER_SESSION_IN_PACKAGE = (By.XPATH, "(//span[contains(text(),'Записаться на консультацию')])[1]")
    SELECT_TIME_TO_ORDER_SESSION_PACKAGE = (By.XPATH, "(//label)[7]")
    SUBMIT_BUTTON_ORDER_SESSION_PACKAGE = (By.XPATH, "//button[contains(text(),'Записаться')]")
    ORDERED_TIME_SESSION_PACKAGE_MY_BALANCE = (By.CSS_SELECTOR, "//p[@class='package__detail-date-time']")
    GO_TO_VIDEOSESSION_BUTTON_PACKAGE_SESSION = (By.XPATH, "//a[contains(text(),'Перейти к сеансу')]")

    AGE_ABOVE16_WINDOW_QUESTIONNAIRE = (By.CSS_SELECTOR, "div[id='error-age'] div[class='error__age-text'] "
                                                         "div:nth-child(1)")

    SELECT_TIME_TO_ORDER_SESSION_ACTION = (By.XPATH, "(//label)[7]")
    TRANSFER_TO_PAYMENT_BUTTON_ACTION_PSHOLOGIST_PAGE = (By.XPATH, "//button[contains(text(),'Перейти к оплате')]")

    HELP_TO_SELECT_PSYCHOLOGYST_QUESTIONNAIRE = (By.CSS_SELECTOR, ".choose-specialist__manager-icon")
    ANASTASIYA_SMIKOVA_MANAGER_PAGE = (By.CSS_SELECTOR, "div[class='choose__specialist-header-name'] h2")
    FOR_FREE_BUTTON_MANAGER = (By.XPATH, "//button[contains(text(),'Записаться на подбор бесплатно')]")
    FIRST_CHECKBOX_ERROR_AUTH_PAGE = (By.CSS_SELECTOR, ".auth__-form-agreements-checkbox.validate-wrapper.error")
    FIRST_CHECKBOX_AUTH_NUMBER = (By.XPATH, "(//label)[2]")

    QUESTIONNAIRE_ERROR_WITHOUT_PERSONAL_QUESTIONS = (By.CSS_SELECTOR, ".questionnaire__error-container.active")
    DOCTOR_PREFERENCES_UNDERLINE_QUIESTIONNAIRE = (By.CSS_SELECTOR, "a[class='progress_page'] span")
    BUTTON_NEXT_QUESTIONNAIRE = (By.XPATH, "//button[contains(text(),'Далее')]")

    AIMS_AND_CONDITIONS_THERAPY_CLIENT = (By.XPATH, "//span[contains(text(),'Цели и условия')]")
    PERSONAL_AIMS_CLIENT = (By.XPATH, "//a[contains(text(),'Персональные')]")
    ADD_NEW_AIM_BUTTON_CLIENT = (By.XPATH, "//form[@class='new__target-add-form']//button[@class='animate__button-"
                                           "filled button__medium-blue-filled']")
    AIM_NAME_FIELD_CREATE_CLIENT = (By.CSS_SELECTOR, "#target-title")
    AIM_DESCRIPTION_FIELD_CREATE_CLIENT = (By.CSS_SELECTOR, "#target-description")
    AIM_START_DAY_CREATE_CLIENT = (By.CSS_SELECTOR, "input[name='start-date']")
    AIM_END_DAY_CREATE_CLIENT = (By.CSS_SELECTOR, "input[name='end-date']")
    CREATE_NEW_AIM_BUTTON_CLIENT = (By.CSS_SELECTOR, "#target__form-create-button")
    NAME_OF_THE_CREATED_AIM_CLIENT = (By.XPATH, "//h3[normalize-space()='My aim']")

    ADD_NEW_AIM_BUTTON_PSYCHOLOGIST = (By.CSS_SELECTOR, ".animate__button-outline.button__medium-blue-outline")
    NO_CONTINUE_PAYMENT_BUTTON = (By.CSS_SELECTOR, "#continue-payment")
    YES_SEE_PACKAGES_OFFER_BUTTON = (By.CSS_SELECTOR, ".primary__button-filled.full-width.blue")

    TINKOFF_INSTALLMENTS_PACKAGE54_BUTTON = (By.CSS_SELECTOR, ".tinkoff-button__title")
    TINKOFF_BUTTON_CONTINUE = (By.CSS_SELECTOR, "#tinkoff-button")
    TINKOFF_INSTALLMENT_APPLICATION_PAGE_TITLE = (By.CSS_SELECTOR, "div[class='dmbWyicqvIkPm_kBWYv4 zuVgfesmeNN8lpE0RZW"
                                                                   "R vYq2A134kQnyq8OkDyqn'] h3")
    TINKOFF_INSTALLMENTS_CONDITIONS = (By.CSS_SELECTOR, "#условия")

    SELECT_TIME_FROM_MAIN_SCHEDULE_PSYCHOLOGIST = (By.XPATH, "(//label)[15]")
    GO_TO_PAYMENT_BUTTON = (By.XPATH, "//button[contains(text(),'Перейти к оплате')]")

    TO_PAY_BUTTON_PAYMENT_PAGE = (By.CSS_SELECTOR, "div[class='payment__btns payment__btns--existing'] button"
                                                   "[class='animate__button-filled button__medium-blue-filled']")

    PACKAGE_TEST_NAME_PAYMENT_PAGE = (By.CSS_SELECTOR, ".payment__existing-cards-radio-number")
    # ".payment__existing-cards-radio-number"

    VK_AUTHORIZATION_BUTTON = (By.CSS_SELECTOR, "a[title='ВКонтакте']")
    VK_AUTHORIZATION_PAGE_TITLE = (By.XPATH, "//div[contains(text(),'Вход в VK ID')]")

    SKYPE_PHONE_NUMBER_HELP_MAIN_PAGE = (By.CSS_SELECTOR, ".phone__call")
    RECAPTCHA_LOGO_RAPID_AUTH = (By.XPATH, "(//body)[1]")

    WRONG_NUMBER_MESSAGE_RAPID_AUTH_PAGE = (By.CSS_SELECTOR, ".p-inp-err")

    BACK_BUTTON_ORDER_PAGE = (By.CSS_SELECTOR, ".faq__back-link")
    USER_AVATAR_NAME = (By.CSS_SELECTOR, ".page-header__user-name")
    PAY_BY_CARD_TINKOFF_KASSA_PAGE = (By.XPATH, "//span[contains(text(),'Оплатить картой')]")
    RECAPTCHA_CONFIDENTIALITY_TITLE = (By.CSS_SELECTOR, "(.rc-anchor-pt)[1]")
    RAPID_PAY_TINKOFF_PAGE = (By.CSS_SELECTOR, "div[class='tui-text_h6 title'] span[automation-id='payment-item__title']")
    # By.XPATH, "//span[contains(text(),'Быстрая оплата')]"


    # ERROR_MESSAGE_REGISTRATION_FORM = (By.CSS_SELECTOR, ".user_data__message-error.slowly__show-error")
    # ERROR_MESSAGE_WRONG_REPEAT_PASSWORD_REG_FORM = (By.CSS_SELECTOR, ".user_data__message-error.slowly__show-error")

    # SELECT_ELENA_KALKAN_PSYCHOLOGYST_LIST = (By.XPATH, "//a[@class='choose-specialist__choices-item active']")
    SELECT_TIME_3_RAPID_PANKOVA = (By.CSS_SELECTOR, "body > div:nth-child(3) > main:nth-child(2) > section:nth-child(1)"
                                                    " > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > "
                                                    "div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > "
                                                    "div:nth-child(1) > div:nth-child(2) > form:nth-child(2) > "
                                                    "label:nth-child(6) > span:nth-child(2)")

    # RAPID_AUTH_BUTTON_REGISTRATION_PAGE = (By.XPATH, "//button[contains(text(),'Быстрый вход')]")
    AVATAR_ORDER_PAGE = (By.CSS_SELECTOR, ".page-header__user-name")

    PACKAGE_4_PAYMENT_CLOUDPAYMENTS_PAGE = (By.XPATH, "//div[@class='payment__details-data']//div[@class='payment__"
                                                      "details-row']//div[1]//div[1]")
    SESSION_PAYMENT_CLOUDPAYMENTS_PAGE = (By.CSS_SELECTOR, ".payment__details-data-title")
    SELECT_TIME_DOCTOR_SCHEDULE_01 = (By.CSS_SELECTOR, "body > div:nth-child(4) > main:nth-child(2) > div:nth-child(1)"
                                                       " > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > "
                                                       "div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > "
                                                       "div:nth-child(4) > form:nth-child(1) > div:nth-child(3) > "
                                                       "div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > "
                                                       "div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > "
                                                       "div:nth-child(2) > div:nth-child(3) > label:nth-child(2)")
    PSYCHOLOGIST_SCHEDULE_SEVENTH_TIME = (By.XPATH, '(//label.select-time__card-checkbox)[7]')
    PSY_TIME_TEST = (By.XPATH, "//div[@class='doctor-schedule']//div[3]//div[1]//div[2]//div[3]//label[2]//div[1]")
    MOVE_TO_PAYMENT_BTN_PSY_SCHEDULE = (By.CSS_SELECTOR, ".animate__button-filled.button__medium-small-width-blue-filled")

    GO_TO_SESSION = (By.XPATH, "//button[contains(text(),'Перейти к сеансу')]")
    TO_RESCHEDULE_SESSION_TIME_BTN = (By.XPATH, "//button[contains(text(),'Перенести сеанс')]")
    TO_DENY_PAYED_SESSION = (By.XPATH, "//button[contains(text(),'Отменить сеанс')]")
    YES_DENY_PAYED_SESSION_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    CONFIRMATION_SESSION_IS_DENIED = (By.CSS_SELECTOR, "div[id='cancelled'] div[class='modals__modal-cancelled']")
    CAUTION_TITLE_DENY_SESSION_MODAL_WINDOW = (By.CSS_SELECTOR, "div[id='cancel'] h2[class='modals__modal-cancel-heading']")
    OUTSIDE_MODAL_WINDOW_DENY_SESSION = (By.XPATH, "//div[@id='cancel']")
    TITLE_PAGE_TIMER_BEFORE_SESSION = (By.CSS_SELECTOR, ".account__my-video-change-time-current-text")
    CROSS_TO_CLOSE_MODAL_WINDOW_DENY_SESSION = (By.CSS_SELECTOR, "div[id='cancel'] button[class='modals__modal-close"
                                                                 " js-close-modal']")


    SELECT_NEW_DOCTOR_PACKAGE_SESSION = (By.CSS_SELECTOR, ".select__session-package-new-doctor")
    DO_NOT_DENY_SESSION_BUTTON = (By.XPATH, "//button[contains(text(),'Нет, не отменять')]")
    NAME_VIDEO_SESSION_HEADING = (By.CSS_SELECTOR, ".account__my-video-heading")
    # REGULAR_SESSION_ORDER_ICON = (By.CSS_SELECTOR, "li:nth-child(1) div:nth-child(1) div:nth-child(2) span:nth-child(1)")
    REGULAR_SESSION_ORDER_ICON = (By.CSS_SELECTOR, "body > div:nth-child(4) > main:nth-child(2) > div:nth-child(1) > "
                                                   "div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-"
                                                   "child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)"
                                                   " > div:nth-child(1) > div:nth-child(1) > div:nth-child(5) > ul:nth"
                                                   "-child(1) > li:nth-child(3) > div:nth-child(1) > div:nth-child(2)"
                                                   " > span:nth-child(2)")
    REGULAR_SCHEDULE_PAGE_TITLE = (By.CSS_SELECTOR, ".account__my-account-heading")
    REGULAR_SESSION_DROPDOWN = (By.XPATH, "(//a[contains(text(),'Регулярное расписание')])[1]")
    ACTION_DOCTOR_SCHEDULE_1ST_TIME = (By.XPATH, "(//div[@class='select-time__card-checkbox-content'])[1]")
    RAPID_SCHEDULE_2ND_TIME_DOCTOR = (By.XPATH, "//div[@class='choose__specialist-schedule-left']//label[2]")
    SELECT_PSYCHOLOGIST_ACTION_BUTTON = (By.XPATH, "(//button[@class='animate__button-filled button__medium-blue-filled']"
                                            "[contains(text(),'Выбрать психолога')])[1]")
    GO_TO_PAYMENT_ACTION_PAGE = (By.XPATH, "//button[contains(text(),'Перейти к оплате')]")
    BACKWARDS_BUTTON_ACTION_PAGE = (By.XPATH, "//button[contains(text(),'Перейти к оплате')]")
    TO_PAY_BUTTON_ORDER_ACCOUNT_PAGE = (By.XPATH, "//button[contains(text(),'Оплатить')]")

    GET_PSYCHOLOGIST_BUTTON_CLIENT_MENU = (By.XPATH, "//a[contains(text(),'Подобрать психолога')]")

    PANKOVA_VIDEO_PAGE = (By.XPATH, "//a[@class='choose__specialist-schedule-avatar video ']//*[name()='svg']")
    VIDEO_FRAME = (By.XPATH, "//div[@class='doctor__video-container']//iframe")

    THREE_DOTS_MY_SCHEDULE_CLIENT = (By.XPATH, "//a[@class='client__context-menu-button']//*[name()='svg']")
    GO_TO_CHAT_THREE_DOTS_MENU_CLIENT = (By.XPATH, "(//*[name()='svg'][@id='context-menu-chat'])[1]")
    CHATS_W_PSYCHOLOGIST_PAGE_HEADING_CLIENT = (By.CSS_SELECTOR, ".chat__heading")
    ORDER_SESSION_AGAIN_THREE_DOTS_MENU = (By.XPATH, "//a[@class='context__menu-link']")

    PRICE_TINKOFF_SESSION_PAYMENT = (By.XPATH, "//div[@class='amount ng-star-inserted']")

    MY_PSYCHOLOGIST_NAME_ACCOUNT = (By.CSS_SELECTOR, ".account__my_doctor-text")
    CHAT_CLIENT_COMPANION_NAME = (By.CSS_SELECTOR, ".chat__right-companion-name")
    AIM_2_CLIENT_ACCOUNT = (By.XPATH, "(//a[contains(@class,'client__target-object')])[2]")
    AIM_STATUS_CLIENT_ACCOUNT = (By.XPATH, "//div[contains(@class,'update__target-subform')]//select[contains"
                                           "(@name,'target-status')]")
    AIM_STATUS_IN_PROGRESS = (By.XPATH, "(//option[@value='1'][contains(text(),'В работе')])[2]")
    SAVE_AIM_CHANGES_BUTTON_CLIENT = (By.CSS_SELECTOR, "#target__form-update-button")
    AIM_STATUS_COMPLETED = (By.XPATH, "//option[@value='2']")
    AIM_STATUS_CREATED = (By.XPATH, "//div[@class='update__target-subform']//option[@value='0'][contains(text(),"
                                    "'Создана')]")
    REMOVE_AIM_BUTTON_CLIENT = (By.CSS_SELECTOR, "#target__form-remove-button")
    TO_ACTIVATE_CERTIFICATE_BUTTON = (By.CSS_SELECTOR, ".animate__button-outline.button__small-blue-outline")
    INPUT_CODE_CERTIFICATE_FIELD = (By.CSS_SELECTOR, "#code")
    BUTTON_TO_ACTIVATE_AFTER_CERTIFICATE_INPUT = (By.CSS_SELECTOR, "div[class='certificate__form-button-wrapper'] "
                                                                   "button[class='animate__button-filled button__medium"
                                                                   "-blue-filled']")
    ACTIVATE_CERTIFICATE_INPUT_WRAPPER = (By.CSS_SELECTOR, ".activate__certificate-input-wrapper")
    ERROR_CERTIFICATE_DOESNOT_EXIST = (By.CSS_SELECTOR, ".activate__certificate-error.active")
    FIRST_ORDER_TIME = (By.XPATH, "//div[@class='swiper-slide swiper-slide-next']//label[1]")
    RAPID_ORDER_TIME = (By.XPATH, "//div[@class='choose__specialist-schedule-left']//label[1]")
