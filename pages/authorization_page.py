from base.base_object import BaseObject
from locators.authorization_locators import AuthorizationLocators
import allure
from support.assertions import Assertions




class AuthorizationPage(BaseObject, Assertions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('accept cookies')
    def click_to_accept_cookies(self):
        self.to_click(AuthorizationLocators.COOKIE_BUTTON)

    @allure.step('clicking to "Login" button')
    def click_to_login_button(self):
        self.to_click(AuthorizationLocators.LOGIN_BUTTON)

    @allure.step('clicking to "Login with password" button')
    def click_to_login_w_password_button(self):
        self.to_click(AuthorizationLocators.LOGIN_WITH_PASSWORD_BUTTON)

    @allure.step('set up email')
    def set_email(self, first):
        self.set_value(AuthorizationLocators.EMAIL_PHONE_FIELD, first)

# separate test
    def set_email_email(self):
        self.set_value(AuthorizationLocators.EMAIL_PHONE_FIELD, 'sh.aygul@gmail.com')

    def set_email_bitrix_email(self):
        self.set_value(AuthorizationLocators.EMAIL_PHONE_FIELD, 'bitrix@mail.ru')

    def set_phone_password_authorization(self):
        self.set_value(AuthorizationLocators.EMAIL_PHONE_FIELD, '89274197879')

    # separate test
    def set_email_psychologist(self):
        self.set_value(AuthorizationLocators.EMAIL_PHONE_FIELD, '89520476828')

    def set_email_not_existing_user(self):
        self.set_value(AuthorizationLocators.EMAIL_PHONE_FIELD, 'test_test@mail.ru')

    @allure.step('set up password')
    def set_password(self, second):
        self.set_value(AuthorizationLocators.PASSWORD_FIELD, second)

# separate test
    @allure.step('set up password')
    def set_password_pass(self):
        self.set_value(AuthorizationLocators.PASSWORD_FIELD, 'lifehelp1@')

    @allure.step('clicking to "Authorize" button')
    def click_to_authorize_button(self):
        self.to_click(AuthorizationLocators.AUTH_BUTTON)

    @allure.step('check personal account url')
    def get_personal_account_url(self, third):
        self.get_url(third)

    # @allure.step('verify successful login in user account')
    # def verify_successful_login(self, third):
    #     actual_result = self.get_personal_account_url(third)
    #     expected_result = third
    #     self.verify(expected_result, actual_result)

    @allure.step('verify url of authorization page')
    def verify_url_authorization_page(self):
        self.get_url('https://life-help.ru/auth/')
#separate test
    def get_personal_account_url_email(self):
        self.get_url('https://life-help.ru/user/notes')

    @allure.step('all steps of login in one for user')
    def login_user(self):
        self.click_to_accept_cookies()
        self.click_to_login_button()
        self.click_to_login_w_password_button()
        self.set_email('sh.aygul@gmail.com')
        self.set_password('lifehelp1@')
        self.click_to_authorize_button()

    @allure.step('all steps of login in one for doctor')
    def login_user(self):
        self.click_to_accept_cookies()
        self.click_to_login_button()
        self.click_to_login_w_password_button()
        self.set_email('aygul.shafigullina@life-help.ru')
        self.set_password('lifehelp1@')
        self.click_to_authorize_button()

    @allure.step('input phone number')
    def set_phone_number(self):
        self.set_value(AuthorizationLocators.PHONE_FIELD, '89274197879')

    @allure.step('input german phone number')
    def set_german_phone_number(self):
        self.set_value(AuthorizationLocators.PHONE_FIELD, '4915168462632')

    @allure.step('input german phone number with + ')
    def set_german_phone_number_with_plus(self):
        self.set_value(AuthorizationLocators.PHONE_FIELD, '+4915168462632')

    @allure.step('input short phone number - 9 numbers')
    def set_short_phone_number(self):
        self.set_value(AuthorizationLocators.PHONE_FIELD, '372510880')

    @allure.step('input long phone number - 15 numbers ')
    def set_long_phone_number(self):
        self.set_value(AuthorizationLocators.PHONE_FIELD, '123456789123456')

    @allure.step('input phone number - 10 numbers')
    def set_10_numbers_phone_number(self):
        self.set_value(AuthorizationLocators.PHONE_FIELD, '1234567890')

    @allure.step('input phone number - 10 numbers')
    def set_14_numbers_phone_number(self):
        self.set_value(AuthorizationLocators.PHONE_FIELD, '12345671234567')

    @allure.step('input wrong phone number')
    def set_wrong_phone_number(self):
        self.set_value(AuthorizationLocators.PHONE_FIELD, '00000000000')

    @allure.step('click first check-box')
    def click_first_checkbox(self):
        self.to_click(AuthorizationLocators.FIRST_CHECKBOX_2)

    @allure.step('click second check-box')
    def click_second_checkbox(self):
        self.to_click(AuthorizationLocators.SECOND_CHECKBOX)

    @allure.step('click get-code btn')
    def click_get_code_btn(self):
        self.to_click(AuthorizationLocators.GET_CODE_BTN)

    @allure.step('check code-field appearance')
    def set_code_field(self):
        self.is_visible(AuthorizationLocators.CODE_FIELD)

    @allure.step('verify  verify appearance of the set code field')
    def verify_appearance_set_code_field(self):
        actual_result = self.is_visible(AuthorizationLocators.CODE_FIELD).get_attribute('name')
        assert actual_result == 'code'

    @allure.step('click to "Chat w psychologist')
    def move_to_chat_w_psychologist(self):
        self.to_click(AuthorizationLocators.CHAT_MENU_NAVIGATION)

    @allure.step('click to "three dots" psychologists name in client account My schedule')
    def click_to_three_dots_psychologists_name(self):
        self.to_click(AuthorizationLocators.THREE_DOTS_PSYCHOLOGIST_CLIENTS_AIM)

    @allure.step('click to "go to chat" in three dots menu in client account My schedule')
    def click_go_to_chat_three_dots_menu_client(self):
        self.to_click(AuthorizationLocators.GO_TO_CHAT_THREE_DOTS_MENU_CLIENT)

    @allure.step('click to "Chat w psychologist')
    def move_to_chat_w_client(self):
        self.to_click(AuthorizationLocators.CHAT_MENU_NAVIGATION_PSYCHOLOGIST)

    @allure.step('select client from chats list')
    def select_chat_w_client(self):
        self.to_click(AuthorizationLocators.CHAT_W_CLIENT_AYGUL)

    @allure.step('type "Hello, World!" in the chat text field')
    def type_greeting_chat_field(self):
        self.set_value(AuthorizationLocators.CHAT_TEXT_FIELD, 'Hello, World!')

    @allure.step('type "Hello!" in the chat text field')
    def type_greeting_chat_field_psychologist(self):
        self.set_value(AuthorizationLocators.CHAT_TEXT_FIELD, 'Hello!')

    @allure.step('click button to send message')
    def click_btn_send_msg_chat(self):
        self.to_click(AuthorizationLocators.SEND_MSG_CHAT_BTN)

    @allure.step('verify successful sending of the message')
    def verify_successful_send_msg_chat(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.MESSAGE_TEXT)
        assert actual_result == 'Hello, World!'

    @allure.step('verify successful sending of the message')
    def verify_successful_send_msg_chat_psychologist(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.MESSAGE_TEXT_PSYCHOLOGIST)
        assert actual_result == 'Hello!'

    @allure.step('get page url')
    def get_page_url(self):
        self.get_url('https://life-help.ru/auth/')

    @allure.step('verify page url')
    def verify_page_url(self):
        actual_url = self.get_page_url()
        #print(actual_url)
        assert actual_url == 'https://life-help.ru/auth/'

    @allure.step('click button to context menu dots')
    def click_context_menu_dots_client_account(self):
        self.to_click(AuthorizationLocators.CONTEXT_MENU_DOTS_CLIENT_ACCOUNT)

    @allure.step('click logout button')
    def click_logout_btn(self):
        self.to_click(AuthorizationLocators.LOGOUT_BTN)

    @allure.step('click logo button')
    def click_logo_btn(self):
        self.to_click(AuthorizationLocators.LIFE_HELP_LOGO)

    @allure.step('click terminated sessions title in client account')
    def click_terminated_sessions_title(self):
        self.to_click(AuthorizationLocators.TERMINATED_SESSIONS_CLIENT)

    @allure.step('click order session again in client account')
    def click_order_session_again_button(self):
        self.to_click(AuthorizationLocators.ORDER_SESSION_AGAIN)

    @allure.step('select the nearest time for second session')
    def select_2nd_time_session_rapid_schedule_psychologist(self):
        self.to_click(AuthorizationLocators.RAPID_SCHEDULE_2ND_TIME_DOCTOR)

    @allure.step('scroll to bottom on schedule page')
    def scroll_till_bottom_schedule_page(self):
        self.move_to_page_bottom()

    @allure.step('select the nearest time for session')
    def select_time_action_schedule_psychologist(self):
        self.to_click(AuthorizationLocators.SELECT_TIME_TO_ORDER_SESSION_ACTION)

    @allure.step('click to "go to payment" button')
    def click_rapid_go_payment_btn(self):
        self.to_click(AuthorizationLocators.RAPID_GO_TO_PAYMENT_BTN)

    @allure.step('click to "get psychologist" button')
    def click_get_psychologist_btn(self):
        self.to_click(AuthorizationLocators.GET_PSYCHOLOGIST_BUTTON)

    @allure.step('click to "get psychologist" button')
    def click_personal_questions_title(self):
        self.to_click(AuthorizationLocators.PERSONAL_QUESTIONS_TITLE)

    @allure.step('click to "my balance" in clients menu navigation')
    def click_my_balance_menu_navigation(self):
        self.to_click(AuthorizationLocators.MY_BALANCE_MENU_TITLE)

    @allure.step('scroll to empty element to order session in package')
    def scroll_to_empty_element_order_session_package(self):
        self.move_to_element(AuthorizationLocators.ORDER_SESSION_IN_PACKAGE)

    @allure.step('click to "buy package" button')
    def click_buy_package(self):
        self.to_click(AuthorizationLocators.BUY_PACKAGE_BUTTON)

    @allure.step('click to "buy package of 4 sessions" button')
    def click_buy_package_4_sessions(self):
        self.to_click(AuthorizationLocators.PACKAGE_4_SESSIONS_BUY_BUTTON)

    @allure.step('click to "card RF" button')
    def click_card_rf_button_package(self):
        self.to_click(AuthorizationLocators.CARD_RF_BUTTON_PACKAGE)

    @allure.step('click to "foreign card" button')
    def click_foreign_card_button_package(self):
        self.to_click(AuthorizationLocators.FOREIGN_CARD_PACKAGE)

    @allure.step('click to "pay online" green button')
    def click_pay_online_button_package(self):
        self.to_click(AuthorizationLocators.PAY_ONLINE_ORDER_BUTTON_PACKAGE)

    @allure.step('click to "pay russian card" button on prodamus page')
    def click_russian_card_prodamus_button(self):
        self.to_click(AuthorizationLocators.PAY_RUSSIAN_CARD_PRODAMUS)

    @allure.step('click to "not russian card" button on prodamus page')
    def click_not_russian_card_prodamus_button(self):
        self.to_click(AuthorizationLocators.NOT_RUSSAIN_CARD_PRODAMUS)

    @allure.step('verify presence of Visa/Mastercard/KZT cards on the prodamus page')
    def verify_vs_ms_kzt_card_prodamus_page(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.VISA_MS_KZT_CARD_PRODAMUS)
        assert actual_result == 'Visa/Mastercard, KZT'

    @allure.step('verify correct location on the cloudpayments page')
    def verify_location_cloudpayments_page(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.PAYMENT_HEADING_TEXT)
        assert actual_result == 'К оплате принимаются карты платежных систем VISA, Master Card и МИР. ' \
                                'Для оплаты введите данные вашей банковской карты в соответствующие поля'

    @allure.step('verify correct location on the tinkoff kassa page')
    def verify_location_tinkoff_kassa_page(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.PAY_BY_CARD_TINKOFF_KASSA_PAGE)
        assert actual_result == 'Оплатить картой'

    @allure.step('verify correct location on the tinkoff kassa page')
    def verify_location_tinkoff_kassa_page_rapid_pay(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.RAPID_PAY_TINKOFF_PAGE)
        assert actual_result == 'Быстрая оплата'

    @allure.step('verify correct location on the cloudpayments page')
    def verify_location_prodamus_page(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.PRODAMUS_PAYMENT_HEADING_TEXT)
        assert actual_result == 'Оплата картой любого банка'

    @allure.step('click to "card RF" button')
    def click_card_rf_button_session(self):
        self.to_click(AuthorizationLocators.CARD_RF_BUTTON_SESSION)

    @allure.step('click to "pay online" green button')
    def click_pay_online_button_session(self):
        self.to_click(AuthorizationLocators.PAY_ONLINE_ORDER_BUTTON_SESSION)

    @allure.step('click to "foreign card" button')
    def click_foreign_card_button_session(self):
        self.to_click(AuthorizationLocators.FOREIGN_CARD_SESSION)


    @allure.step('set age in questionnaire')
    def set_age_field_questionnaire(self):
        self.set_value(AuthorizationLocators.AGE_FIELD, '36')

    @allure.step('set age in questionnaire-age field validation')
    def set_age_field_negative_validation_questionnaire(self, first):
        self.set_value(AuthorizationLocators.AGE_FIELD, first)

    @allure.step('set age in questionnaire-age field positive validation')
    def set_age_field_positive_validation_questionnaire(self, age):
        self.set_value(AuthorizationLocators.AGE_FIELD, age)

    @allure.step('click button "Next" in questionnaire')
    def click_next_button_questionnaire(self):
        self.to_click(AuthorizationLocators.NEXT_BUTTON_QUESTIONNAIRE)

    @allure.step('select "Stress" in questionnaire')
    def select_stress_questionnaire(self):
        self.to_click(AuthorizationLocators.STRESS_CHECKBOX_QUESTIONNAIRE)

    @allure.step('click "Psychologist preferences" title in questionnaire')
    def click_psychologist_preferences_title_questionnaire(self):
        self.to_click(AuthorizationLocators.PSYCHOLOGIST_PREFERENCES_TITLE_QUESTIONNAIRE)

    @allure.step('click "age over 30" button in questionnaire')
    def click_age_over_30_questionnaire(self):
        self.to_click(AuthorizationLocators.AGE_OVER_30_BUTTON_QUESTIONNAIRE)

    @allure.step('click "Select psychologist" title in questionnaire')
    def click_select_psychologist_title_questionnaire(self):
        self.to_click(AuthorizationLocators.SELECT_PSYCHOLOGIST_TITLE_QUESTIONNAIRE)

    @allure.step('verify presence of Anna Kapu among "choose specialist" list')
    def verify_presence_anna_kapu_choose_specialist(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.ANNA_KAPU_TITLE_CHOOSE_DOCTOR_LIST)
        assert actual_result == 'Анна'

    @allure.step('verify presence of Irina Pankova among "choose specialist" list')
    def verify_presence_pankova_choose_specialist(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.IRINA_PANOVA_TITLE_CHOOSE_DOCTOR_LIST)
        assert actual_result == 'Ирина'

    @allure.step('click "Individual 90" button in questionnaire')
    def click_pankova_video(self):
        self.to_click(AuthorizationLocators.VIDEO_FRAME)

    @allure.step('click "Individual 90" button in questionnaire')
    def click_ind_90_questionnaire(self):
        self.to_click(AuthorizationLocators.INDIVIDUAL_90_QUESTIONNAIRE_GENERAL)

    @allure.step('verify presence of Alisa Ivannikova among "choose specialist" list')
    def verify_presence_alisa_ivannikova_choose_specialist(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.ALISA_IVANNIKOVA_TITLE_CHOOSE_DOCTOR_LIST)
        assert actual_result == 'Алиса'

    @allure.step('click "tatar" button in questionnaire')
    def click_tatar_button_questionnaire(self):
        self.to_click(AuthorizationLocators.TATAR_BUTTON_QUESTIONNAIRE)

    @allure.step('verify presence of Aliya Askarova among "choose specialist" list')
    def verify_presence_aliya_askarova_choose_specialist(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.ALIYA_ASKAROVA_TITLE_CHOOSE_DOCTOR_LIST)
        assert actual_result == 'Алия'

    @allure.step('click "paired consulation" button in questionnaire')
    def click_paired_consultation_button_questionnaire(self):
        self.to_click(AuthorizationLocators.PAIRED_CONSULTATION_BUTTON_QUESTIONNAIRE)

    @allure.step('click "difficulties in paired relationship" button in questionnaire')
    def click_difficulties_in_relationship_paired_consultation_button_questionnaire(self):
        self.to_click(AuthorizationLocators.DIFFICULTIES_IN_RELATIONSHIP_PAIRED_BUTTON_CONSULTATION)

    @allure.step('verify presence of Elena Kalkan among "choose specialist" list')
    def verify_presence_elena_kalkan_choose_specialist(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.ELENA_KALKAN_TITLE_CHOOSE_DOCTOR_LIST)
        assert actual_result == 'Елена'

    @allure.step('click "flag" button in rapid sms code authorization page')
    def click_elena_kalkan_name(self):
        self.to_click(AuthorizationLocators.ELENA_KALKAN_IMAGE_DOCTOR_LIT)

    @allure.step('click "flag" button in rapid sms code authorization page')
    def click_change_flag_country_authorization(self):
        self.to_click(AuthorizationLocators.COUNTRIES_FLAGS_LIST)

    @allure.step('select "Germany flag" from list of countries')
    def select_germany_flag_authorization(self):
        self.to_click(AuthorizationLocators.GERMANY_FLAG)

    @allure.step('verify presence of Germany flag on the page')
    def verify_presence_germany_flag(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.SELECTED_GERMANY_FLAG)
        assert actual_result == "Germany (Deutschland): +49"

    @allure.step('click "forgot password" hypertext')
    def click_forgot_password(self):
        self.to_click(AuthorizationLocators.FORGOT_PASSWORD_HYPERTEXT)

    @allure.step('set email to send link for recovering password')
    def set_email_forgot_password(self):
        self.set_value(AuthorizationLocators.EMAIL_FIELD_FORGOT_PASSWORD, 'sh.aygul@gmail.com')

    @allure.step('click "recover password" button')
    def click_reset_password_button(self):
        self.to_click(AuthorizationLocators.RECOVER_PASSWORD_BUTTON)

    @allure.step('verify message "A link to reset your password has been sent to your email"')
    def verify_message_sent_link_reset_password(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.TEXT_SENT_LINK_TO_RECOVER_PASSWORD)
        assert actual_result == 'На Ваш email отправлена ссылка для восстановления пароля.'

    @allure.step('click "register" hypertext')
    def click_register_hypertext(self):
        self.to_click(AuthorizationLocators.REGISTER_HYPERTEXT)

    # @allure.step('set email in registration form')
    # def set_email_registration_form(self):
    #     self.set_value(AuthorizationLocators.EMAIL_FIELD_REGISTRATION_FORM, 'aigul.schafigullina.87@yandex.ru')
    #
    # @allure.step('set phone in email field in registration form')
    # def set_phone_registration_form(self):
    #     self.set_value(AuthorizationLocators.EMAIL_FIELD_REGISTRATION_FORM, '71234567890')
    #
    # @allure.step('set email in registration form')
    # def set_email_registered_user_registration_form(self):
    #     self.set_value(AuthorizationLocators.EMAIL_FIELD_REGISTRATION_FORM, 'sh.aygul@gmail.com')
    #
    # @allure.step('set password in registration form')
    # def set_password_registration_form(self):
    #     self.set_value(AuthorizationLocators.PASSWORD1_FIELD_REGISTRATION_FORM, 'password1@')
    #
    # @allure.step('repeat password in registration form')
    # def repeat_password_registration_form(self):
    #     self.set_value(AuthorizationLocators.PASSWORD2_REPEAT_FIELD_REGISTRATION_FORM, 'password1@')
    #
    # @allure.step('repeat wrong password in registration form')
    # def repeat_wrong_password_registration_form(self):
    #     self.set_value(AuthorizationLocators.PASSWORD2_REPEAT_FIELD_REGISTRATION_FORM, 'lifehelp1@')
    #
    # @allure.step('click first checkbox of consent in registration form')
    # def click_first_checkbox_consent_registration_form(self):
    #     self.to_click(AuthorizationLocators.FIRST_CHECKBOX_CONSENT_REGISTRATION_FORM)
    #
    # @allure.step('scroll the page till the "register" button in registration form')
    # def scroll_to_register_button_registration_form(self):
    #     self.move_to_element(AuthorizationLocators.REGISTER_BUTTON)
    #
    # @allure.step('click "to register" button in registration form')
    # def click_to_register_button_registration_form(self):
    #     self.to_click(AuthorizationLocators.REGISTER_BUTTON)
    #
    # @allure.step('verify message "A link to reset your password has been sent to your email"')
    # def verify_sent_msg_registration(self):
    #     actual_result = self.get_text_title_of_element(AuthorizationLocators.REGISTRATION_INFO_TEXT)
    #     assert actual_result == 'На Ваш email отправлена ссылка для подтверждения электронной почты. ' \
    #                             'Пожалуйста, перейдите по ней, чтобы завершить процесс регистрации.'
    #
    # @allure.step('verify message "A link to reset your password has been sent to your email"')
    # def verify_error_enter_right_email_registration(self):
    #     actual_result = self.get_text_title_of_element(AuthorizationLocators.ERROR_MESSAGE_REGISTRATION_FORM)
    #     assert actual_result == 'Пожалуйста, введите правильный адрес электронной почты'
    #
    # @allure.step('verify message "A link to reset your password has been sent to your email"')
    # def verify_error_wrong_repeat_password_registration(self):
    #     actual_result = self.get_text_title_of_element(AuthorizationLocators.ERROR_MESSAGE_WRONG_REPEAT_PASSWORD_REG_FORM)
    #     assert actual_result == 'Введенные пароли не совпадают'
    #
    # @allure.step('verify message "The user with this email is already registered"')
    # def verify_error_msg_registration(self):
    #     actual_result = self.get_text_title_of_element(AuthorizationLocators.REGISTRATION_ERROR_MESSAGE)
    #     assert actual_result == 'Пользователь с введенным email уже зарегистрирован'

    # def verify_button_is_not_clickable(self):
    #     actual_result = self.is_visible(AuthorizationLocators.REGISTER_BUTTON).get_attribute('disabled')
    #     assert actual_result == True

    @allure.step('')
    def scroll_to_main_page_footer(self):
        self.move_to_element(AuthorizationLocators.LANDING_FOOTER_BOTTOM)

    @allure.step('click to "telegram" logo button in main page care block')
    def click_to_telegram_care_button(self):
        self.to_click(AuthorizationLocators.TELEGRAM_CARE_LOGO)

    @allure.step('move to new telegram care page')
    def move_to_new_telegram_care_page(self):
        telegram_care_page = self.driver.window_handles[1]
        self.driver.switch_to.window(telegram_care_page)

    @allure.step('verify url of telegram care page')
    def verify_url_telegram_care_page(self):
        self.get_url('https://t.me/+79600645557')

    @allure.step('click to "whatsapp" logo button in main page care block')
    def click_to_whatsapp_care_button(self):
        self.to_click(AuthorizationLocators.WHATSAPP_CARE_LOGO)

    @allure.step('move to new whatsapp care page')
    def move_to_new_whatsapp_care_page(self):
        whatsapp_care_page = self.driver.window_handles[1]
        self.driver.switch_to.window(whatsapp_care_page)

    @allure.step('verify url of whatsapp care page')
    def verify_whatsapp_care_page(self):
        actual_result = self.is_visible(AuthorizationLocators.WHATSAPP_PAGE_HEADER).get_attribute('src')
        assert actual_result == 'https://static.whatsapp.net/rsrc.php/v3/y7/r/DSxOAUB0raA.png'

    @allure.step('click to "Tg group" document name in main page footer bottom')
    def scroll_to_footer(self):
        self.move_to_element(AuthorizationLocators.AGREEMENT_FOOTER_DOCUMENT)

    @allure.step('click to "view password" button in password field in authorization page')
    def click_to_telegram_group_network_footer(self):
        self.to_click(AuthorizationLocators.TELEGRAM_SOCIAL_NETWORK_GROUP)


    # @allure.step('click to "consent mailing" document name in main page footer bottom')
    # def click_to_consent_mailing_name_footer_bottom(self):
    #     self.move_to_element(AuthorizationLocators.CONSENT_MAILING_DOCUMENT_FOOTER)

    @allure.step('click to "Tg group" document name in main page footer bottom')
    def click_to_consent_mailing_document_footer(self):
        self.move_to_element(AuthorizationLocators.CONSENT_MAILING_DOCUMENT_FOOTER)

    @allure.step('move to new page with consent mailing document')
    def move_to_new_page_w_consent_mailing_document(self):
        consent_mailing_document_page = self.driver.window_handles[1]
        self.driver.switch_to.window(consent_mailing_document_page)

    @allure.step('click to "view password" button in password field in authorization page')
    def click_to_view_password_button_auth_page(self):
        self.to_click(AuthorizationLocators.VIEW_PASSWORD_BUTTON_AUTHORIZATION_FIELD)

    @allure.step('verify view mode of the password field')
    def verify_viewed_type_password_field(self):
        actual_result = self.is_visible(AuthorizationLocators.PASSWORD_FIELD).get_attribute('type')
        assert actual_result == 'text'

    @allure.step('click to "view password" button in password field in authorization page')
    def click_to_hide_password_button_auth_page(self):
        self.to_click(AuthorizationLocators.HIDE_PASSWORD_BUTTON_AUTHORIZATION_FIELD)

    @allure.step('verify hidden mode of the password field')
    def verify_hidden_type_password_field(self):
        actual_result = self.is_visible(AuthorizationLocators.PASSWORD_FIELD).get_attribute('type')
        assert actual_result == 'password'

    @allure.step('set wrong password')
    def set_wrong_password(self):
        self.set_value(AuthorizationLocators.PASSWORD_FIELD, 'lifeehelp')

    @allure.step('verify message "Wrong login or password"')
    def verify_wrong_password_message_authorization(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.ERROR_MESSAGE_WRONG_PASSWORD_AUTH_PAGE)
        assert actual_result == 'Неверный логин или пароль'

    @allure.step('set phone of user without password for authorization form')
    def set_phone_user_wo_password(self):
        self.set_value(AuthorizationLocators.EMAIL_PHONE_FIELD, '70780780780')

    @allure.step('verify message "Wrong login or password"')
    def verify_wrong_password_message_authorization(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.ERROR_MESSAGE_WRONG_PASSWORD_AUTH_PAGE)
        assert actual_result == 'Неверный логин или пароль'

    @allure.step('verify message "User has not set the password jet"')
    def verify_error_msg_authorization_user_wo_password(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.ERROR_MESSAGE_WRONG_PASSWORD_AUTH_PAGE)
        assert actual_result == 'Пароль ранее не был установлен. Пожалуйста, авторизуйтесь с помощью "Быстрого входа" ' \
                                'и установите пароль в личном кабинете'

    @allure.step('set code in the code field by authorization with sms code')
    def type_wrong_sms_code_authorization(self):
        self.set_value(AuthorizationLocators.CODE_FIELD, '1234')

    @allure.step('verify message "Wrong sms code"')
    def verify_error_msg_authorization_user_wrong_sms_code(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.ERROR_MESSAGE_WRONG_SMS_CODE_AUTH_PAGE)
        assert actual_result == 'Введенный код неверен'

    @allure.step('click to "auth code" button to authorize with sms code')
    def click_to_auth_code_button(self):
        self.to_click(AuthorizationLocators.AUTH_CODE_BUTTON)

    @allure.step('click to "come back to cabinet" button on the payment page')
    def click_to_come_back_cabinet_button(self):
        self.to_click(AuthorizationLocators.COME_BACK_TO_CABINET_BUTTON)

    @allure.step('verify session status "waits for payment" in the cabinet')
    def verify_session_status_waits_payment(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.SESSION_WAITS_FOR_PAYMENT_TEXT)
        assert actual_result == 'Ожидает оплаты'

    @allure.step('click to "3 dots" button on automatic order session')
    def click_to_three_dots_button_ordered_session(self):
        self.to_click(AuthorizationLocators.THREE_DOTS_ORDERED_SESSION)

    @allure.step('click to "reschedule order" button on drop down link from three dots in ordered session')
    def click_to_reschedule_ordered_session_drop_down(self):
        self.to_click(AuthorizationLocators.RESCHEDULE_ORDERED_SESSION_DROP_DOWN_LINK)

    @allure.step('click to "reschedule order" button on drop down link from three dots in ordered session')
    def click_to_reschedule_payed_session_drop_down(self):
        self.to_click(AuthorizationLocators.RESCHEDULE_PAIED_SESSION_DROP_DOWN_LINK)

    @allure.step('click to "arrow" button to come back from videosession timer page to my schedule')
    def click_to_arrow_button_to_back_from_videosession_page_to_my_schedule_page(self):
        self.to_click(AuthorizationLocators.ARROW_TO_BACK_FROM_VIDEOSESSION_PAGE_TO_MY_SCHEDULE)

    @allure.step('click to "reschedule only this session" button on modal window of reschedule regular session')
    def click_to_reschedule_only_this_session_button(self):
        self.to_click(AuthorizationLocators.RESCHEDULE_ONLY_THIS_SESSION_BUTTON)

    @allure.step('select the 7th time position on the schedule  to reschedule order')
    def select_seventh_time_to_reschedule_order(self):
        self.to_click(AuthorizationLocators.SELECT_TIME_TO_RESCHEDULE_ORDER)

    @allure.step('click to "change time" button on the schedule to reschedule order')
    def click_to_change_time_button_to_reschedule_order(self):
        self.to_click(AuthorizationLocators.CHANGE_TIME_BUTTON_ORDER)

    @allure.step('click to "deny order payment" button on drop down link from three dots in ordered session')
    def click_to_deny_payment_ordered_session_drop_down(self):
        self.to_click(AuthorizationLocators.DENY_ORDER_PAYMENT_DROP_DOWN_LINK)

    @allure.step('click to "yes, deny oder payment" button on the schedule to deny order')
    def click_to_yes_deny_payment_button_to_deny_order(self):
        self.to_click(AuthorizationLocators.YES_DENY_ORDER_PAYMENT_BUTTON)

    @allure.step('click to "good" button after deny of order payment')
    def click_to_good_button_after_deny_order(self):
        self.to_click(AuthorizationLocators.GOOD_BUTTON_AFTER_DENY_ORDER_PAYMENT)

    @allure.step('click to "clients and aims" button in menu navigation of psychologist account')
    def click_to_clients_and_aims_menu_psychologist(self):
        self.to_click(AuthorizationLocators.CLIENTS_AND_AIMS_MENU_PSYCHOLOGIST)

    @allure.step('select Aygul-test in "clients and aims" of menu navigation of psychologist account')
    def select_aygul_clients_and_aims_menu_psychologist(self):
        self.to_click(AuthorizationLocators.SELECT_AYGUL_TEST_CLIENTS_AIMS)

    @allure.step('click to three dots in client in "clients and aims" of menu navigation of psychologist account')
    def click_to_three_dots_clients_and_aims_menu_psychologist(self):
        self.to_click(AuthorizationLocators.THREE_DOTS_PSYCHOLOGIST_CLIENTS_AIM)

    @allure.step('click "to create new session" button for client in "clients and aims" of menu navigation of psychologist account')
    def click_to_create_new_session_for_clients_menu_psychologist(self):
        self.to_click(AuthorizationLocators.CREATE_NEW_SESSION_PSYCHOLOGIST)

    @allure.step('click to "to create" button for creating new session for client in "clients and aims" of menu navigation of psychologist account')
    def click_to_create_button_to_create_new_session_for_clients_menu_psychologist(self):
        self.to_click(AuthorizationLocators.TO_CREATE_BUTTON_CREATE_SESSION_PSYCHOLOGIST)

    @allure.step('verify successful creation of session from psychologist account')
    def verify_successful_creation_session_text_psychologist(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.FINE_BUTTON_CREATE_SESSION_PSYCHOLOGIST)
        assert actual_result == 'Отлично!'

    @allure.step('verify successful creation of session from psychologist account')
    def verify_successful_creation_order_text_psychologist(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.YOU_HAVE_SUCCESSFULLY_ORDERED_CLIENT_SESSION_MSG)
        assert 'Вы успешно забронировали' in actual_result

    @allure.step('click to "ok" on window of successful order of session by psychologist')
    def click_ok_button_successful_order_by_psychologist(self):
        self.to_click(AuthorizationLocators.FINE_BUTTON_CREATE_SESSION_PSYCHOLOGIST)

    @allure.step('verify unsuccessful creation of session from psychologist account')
    def verify_error_unsuccessful_creation_order_text_psychologist(self):
        actual_result = self.get_text_title_of_element(
            AuthorizationLocators.ERROR_MSG_SELECTED_ORDER_TIME_IS_OCCUPIED)
        assert actual_result == 'Это время уже занято. Пожалуйста, выберите другое время.'

    @allure.step('verify appearance of window with request to set the age')
    def verify_window_to_set_age_questionnaire(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.SET_YOUR_AGE_QUESTIONNAIRE_WINDOW)
        assert actual_result == 'Пожалуйста, укажите свой возраст'

    @allure.step('click to "general questions" title in questionnaire')
    def click_to_general_questions_title_questionnaire(self):
        self.to_click(AuthorizationLocators.GENERAL_QUESTIONS_TITLE_QUESTIONNAIRE)

    @allure.step('verify that we cannot step over personal questions')
    def verify_we_cannot_step_over_personal_questions_questionnaire(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.SET_YOUR_AGE_QUESTIONNAIRE_WINDOW)
        assert actual_result == 'Пожалуйста, укажите свой возраст'

    @allure.step('click to "I have promocode" on order page')
    def click_to_ihave_promocode_order_page(self):
        self.to_click(AuthorizationLocators.I_HAVE_PROMOCODE_TITLE_SESSION_ORDER_PAGE)

    @allure.step('enter "promo" in the promo field on the session order page')
    def enter_free_promocode_session_order_page(self):
        self.set_value(AuthorizationLocators.ENTER_PROMOCODE_FIELD_SESSION_ORDER_PAGE, 'promo_test')

    # @allure.step('verify price on the button is 100 rubbles')
    # def verify_price_100_rubbles_button_order_page_before_promo(self):
    #     actual_result = self.get_text_title_of_element(AuthorizationLocators.PAYMENT_BUTTON_ORDER_PAGE)
    #     assert actual_result == '100,00'

    @allure.step('verify price on the button is 100 rubbles')
    def verify_price_1_rubble_button_order_page_before_promo(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.PAYMENT_BUTTON_ORDER_PAGE)
        assert actual_result == '1,00'

    @allure.step('click to "submit promocode" on the session order page')
    def click_to_submit_promocode_button_session_order_page(self):
        self.to_click(AuthorizationLocators.SUBMIT_PROMOCODE_BUTTON_SESSION_ORDER_PAGE)

    @allure.step('verify price on the button is 0,00 rubbles')
    def verify_price_0_rubbles_button_order_page_after_promo(self):
        promo_result = self.get_text_title_of_element(AuthorizationLocators.FINAL_PRICE_AFTER_PROMOCODE)
        assert promo_result == '0,00'

    @allure.step('click to "order session" in the package')
    def click_to_order_session_package(self):
        self.to_click(AuthorizationLocators.ORDER_SESSION_IN_PACKAGE)

    @allure.step('save selected time in the schedule to order session in the package')
    def save_selected_time_to_order_session_package(self):
        selected_time = self.get_text_title_of_element(AuthorizationLocators.SELECT_TIME_TO_ORDER_SESSION_PACKAGE)

    @allure.step('select time in the schedule to order session in the package')
    def select_time_to_order_session_package(self):
        self.to_click(AuthorizationLocators.SELECT_TIME_TO_ORDER_SESSION_PACKAGE)

    @allure.step('submit selected time in the schedule to order session in the package')
    def submit_selected_time_to_order_session_package(self):
        self.to_click(AuthorizationLocators.SUBMIT_BUTTON_ORDER_SESSION_PACKAGE)

    @allure.step('save ordered time of the session in the package')
    def save_ordered_time_session_package(self):
        ordered_time = self.get_text_title_of_element(AuthorizationLocators.ORDERED_TIME_SESSION_PACKAGE_MY_BALANCE)

    @allure.step('verify presence of ordered in the package session - check in my schedule as a client')
    def verify_presence_ordered_session_package(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.GO_TO_VIDEOSESSION_BUTTON_PACKAGE_SESSION)
        assert actual_result == 'Перейти к сеансу'

    @allure.step('verify appearance of window with info, that service can be used only by person above 16 years old')
    def verify_window_age_above16_questionnaire(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.AGE_ABOVE16_WINDOW_QUESTIONNAIRE)
        assert actual_result == 'Нашим сервисом можно пользоваться с 16 лет'

    # @allure.step('move to new whatsapp Nastya help page') открывается на этой же странице
    # def move_to_new_whatsapp_help_page(self):
    #     whatsapp_help_page = self.driver.window_handles[1]
    #     self.driver.switch_to.window(whatsapp_help_page)

    @allure.step('click to "select psychologist" in action module')
    def click_to_select_psychologyst_button_action(self):
        self.to_click(AuthorizationLocators.TEST_ACTION_SELECT_PSYCHOLOGIST_BUTTON)

    @allure.step('')
    def scroll_to_payment_button_psychologist_action_page(self):
        self.move_to_element(AuthorizationLocators.TRANSFER_TO_PAYMENT_BUTTON_ACTION_PSHOLOGIST_PAGE)

    @allure.step('')
    def scroll_to_come_back_to_cabinet_button_client(self):
        self.move_to_element(AuthorizationLocators.COME_BACK_TO_CABINET_BUTTON)

    @allure.step('')
    def scroll_to_select_psychologist_action(self):
        self.move_to_element(AuthorizationLocators.TEST_ACTION_SELECT_PSYCHOLOGIST_BUTTON)

    @allure.step('click to "help to select" in psychologist list after questionnaire')
    def click_help_to_select_psychologyst_questionnaire(self):
        self.to_click(AuthorizationLocators.HELP_TO_SELECT_PSYCHOLOGYST_QUESTIONNAIRE)

    @allure.step('verify appearance of window with info, that service can be used only by person above 16 years old')
    def verify_choose_manager_help_page(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.ANASTASIYA_SMIKOVA_MANAGER_PAGE)
        assert actual_result == 'Анастасия Смыкова'

    @allure.step('verify appearance of window with info, that service can be used only by person above 16 years old')
    def verify_for_free_button_manager_help_page(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.FOR_FREE_BUTTON_MANAGER)
        assert actual_result == 'Записаться на подбор бесплатно'

    @allure.step('move to new whatsapp care page')
    def move_to_new_whatsapp_help_page(self):
        whatsapp_help_page = self.driver.window_handles[1]
        self.driver.switch_to.window(whatsapp_help_page)

    @allure.step('verify appearance of red filled first checkbox')
    def verify_error_not_selected_1st_checkbox_auth_page(self):
        actual_result = self.is_visible(AuthorizationLocators.WHATSAPP_PAGE_HEADER).get_attribute('class')
        assert actual_result == 'auth__-form-agreements-checkbox validate-wrapper error'

    @allure.step('verify red color of the phone field without phone number')
    def verify_red_phonefield_wo_phonenumber_auth_page(self):
        actual_result = self.is_visible(AuthorizationLocators.PHONE_FIELD).get_attribute('class')
        assert actual_result == 'p-inp validate-field error'

    @allure.step('click first check-box')
    def click_first_agreement(self):
        self.to_click(AuthorizationLocators.FIRST_CHECKBOX_AUTH_NUMBER)

    @allure.step('verify appearance of window with info, that service can be used only by person above 16 years old')
    def verify_error_text_no_personal_questions_questionnaire(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.QUESTIONNAIRE_ERROR_WITHOUT_PERSONAL_QUESTIONS)
        assert actual_result == 'Пожалуйста, отметьте хотя бы одну тему'

    @allure.step('click "Psychologist preferences" title in questionnaire')
    def click_button_next_questionnaire(self):
        self.to_click(AuthorizationLocators.NEXT_BUTTON_QUESTIONNAIRE)

    @allure.step('')
    def scroll_to_next_button_questionnaire(self):
        self.move_to_element(AuthorizationLocators.NEXT_BUTTON_QUESTIONNAIRE)

    @allure.step('click "Aims and conditions" clients account')
    def click_aims_menu_client(self):
        self.to_click(AuthorizationLocators.AIMS_AND_CONDITIONS_THERAPY_CLIENT)

    @allure.step('click "Personal aims" clients account')
    def click_personal_aims_menu_client(self):
        self.to_click(AuthorizationLocators.PERSONAL_AIMS_CLIENT)

    @allure.step('click "Add new aim" button clients account')
    def click_add_new_aim_button_client(self):
        self.to_click(AuthorizationLocators.ADD_NEW_AIM_BUTTON_CLIENT)

    @allure.step('type "my aim" in the aim name field while creating aim in clients account')
    def type_aim_name_create_client(self):
        self.set_value(AuthorizationLocators.AIM_NAME_FIELD_CREATE_CLIENT, 'My aim')

    @allure.step('type "my aim description" in the aim description field while creating aim in clients account')
    def type_aim_description_create_client(self):
        self.set_value(AuthorizationLocators.AIM_DESCRIPTION_FIELD_CREATE_CLIENT, 'My aim description')

    @allure.step('set "start day" of the new aim in clients account')
    def set_start_day_aim_button_client(self):
        self.set_value(AuthorizationLocators.AIM_START_DAY_CREATE_CLIENT, '01.08.2023')

    @allure.step('set "end day" of the new aim in clients account')
    def set_end_day_aim_button_client(self):
        self.set_value(AuthorizationLocators.AIM_END_DAY_CREATE_CLIENT, '10.08.2023')

    @allure.step('click "Add new aim" button clients account')
    def click_create_new_aim_button_client(self):
        self.to_click(AuthorizationLocators.CREATE_NEW_AIM_BUTTON_CLIENT)

    @allure.step('verify appearance of new created aim in the clients account')
    def verify_created_aim_in_client_account(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.NAME_OF_THE_CREATED_AIM_CLIENT)
        assert actual_result == 'My aim'

    @allure.step('click "Add new aim" button psychologist account')
    def click_add_new_aim_button_psychologist(self):
        self.to_click(AuthorizationLocators.ADD_NEW_AIM_BUTTON_PSYCHOLOGIST)

    @allure.step('click to "no, continue payment" button to the question to see the package on the order page ')
    def click_no_continue_payment_button_order_page(self):
        self.to_click(AuthorizationLocators.NO_CONTINUE_PAYMENT_BUTTON)

    @allure.step('click to "yes, see packages offer" button to the question to see the package on the order page ')
    def click_yes_see_packages_offer_button_order_page(self):
        self.to_click(AuthorizationLocators.YES_SEE_PACKAGES_OFFER_BUTTON)

    @allure.step('move to new packages offer page')
    def move_to_new_packages_offer_page(self):
        packages_offer_page = self.driver.window_handles[1]
        self.driver.switch_to.window(packages_offer_page)

    @allure.step('click to "buy package of 54 sessions" by installments button')
    def click_buy_package_54_by_tinkoff_installments(self):
        self.to_click(AuthorizationLocators.TINKOFF_INSTALLMENTS_PACKAGE54_BUTTON)

    @allure.step('click to "continue" by tinkoff installments button')
    def click_continue_button_by_tinkoff_installments(self):
        self.to_click(AuthorizationLocators.TINKOFF_BUTTON_CONTINUE)

    @allure.step('move to new tinkoff installments page')
    def move_to_new_tinkoff_installments_page(self):
        tinkoff_installments_page = self.driver.window_handles[1]
        self.driver.switch_to.window(tinkoff_installments_page)

    # @allure.step('verify title of the page with tinkoff installments application')
    # def verify_tinkoff_installments_application_page_title(self):
    #     actual_result = self.get_text_title_of_element(AuthorizationLocators.TINKOFF_INSTALLMENT_APPLICATION_PAGE_TITLE)
    #     assert actual_result == 'Оформление заявки'

    @allure.step('verify title of the page with tinkoff installments application')
    def verify_tinkoff_installments_application_page_conditions(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.TINKOFF_INSTALLMENTS_CONDITIONS)
        assert actual_result == 'Условия'

    @allure.step('select the time from main schedule for second session')
    def select_time_session_main_schedule_psychologist(self):
        self.to_click(AuthorizationLocators.SELECT_TIME_FROM_MAIN_SCHEDULE_PSYCHOLOGIST)

    @allure.step('scroll to "go to payment" button on psychologyst schedule page')
    def scroll_till_go_to_payment_button_psychologyst_schedule(self):
        self.move_to_element(AuthorizationLocators.MOVE_TO_PAYMENT_BTN_PSY_SCHEDULE)

    @allure.step('scroll to bottom on psychologyst schedule page')
    def scroll_till_bottom_psychologyst_schedule(self):
        self.move_to_page_bottom()

    @allure.step('verify presence of the package 54 on the payment page ')
    def verify_presence_package_test_payment_page(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.PACKAGE_TEST_NAME_PAYMENT_PAGE)
        assert actual_result == 'Пакет из Test сеансов'

    @allure.step('verify presence of the Test package on the payment page ')
    def verify_presence_package_test_order_payment_page(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.PACKAGE_TEST_NAME_PAYMENT_PAGE)
        assert actual_result == 'Пакет из Test сеансов'

    @allure.step('click to the "to pay" button on the payment page')
    def click_to_pay_button_payment_page(self):
        self.to_click(AuthorizationLocators.TO_PAY_BUTTON_PAYMENT_PAGE)

    @allure.step('click to button authorization via VK')
    def click_vk_auth_button(self):
        self.to_click(AuthorizationLocators.VK_AUTHORIZATION_BUTTON)

    @allure.step('verify title of the vk authorization page ')
    def verify_vk_auth_page_title(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.VK_AUTHORIZATION_PAGE_TITLE)
        assert actual_result == 'Вход в VK ID'

    @allure.step('click to help phone call by Skype')
    def click_phone_number_skype_button(self):
        self.to_click(AuthorizationLocators.SKYPE_PHONE_NUMBER_HELP_MAIN_PAGE)



    # @allure.step('verify presence of reCaptcha on the rapid auth page')
    # def hover_to_recaptcha_element(self):
    #     self.move_to_element(AuthorizationLocators.RECAPTCHA_LOGO_RAPID_AUTH).perform()

    @allure.step('verify presence of recaptcha authorization page ')
    def verify_presence_recaptcha_auth_page_title(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.RECAPTCHA_LOGO_RAPID_AUTH)
        assert actual_result == 'Пройдите проверку reCAPTCHA'

    @allure.step('verify presence of recaptcha confidentiality authorization page ')
    def verify_confidentiality_recaptcha_auth_page_title(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.RECAPTCHA_CONFIDENTIALITY_TITLE)
        assert actual_result == 'Конфиденциальность'

    @allure.step('click auth-code btn rapid auth page')
    def click_auth_code_btn(self):
        self.to_click(AuthorizationLocators.AUTH_CODE_BUTTON)

    @allure.step('verify red color of the phone field without phone number')
    def verify_red_codefield_wo_codenumber_auth_page(self):
        actual_result = self.is_visible(AuthorizationLocators.CODE_FIELD).get_attribute('class')
        assert actual_result == 'auth__form-input js-user-code vld-inp error'

    @allure.step('verify red color of the phone field without phone number')
    def verify_red_email_phone_field_wo_email_auth_page(self):
        actual_result = self.is_visible(AuthorizationLocators.EMAIL_PHONE_FIELD).get_attribute('class')
        assert actual_result == 'auth__form-input vld-inp error'

    @allure.step('verify red color of the password field without password number')
    def verify_red_password_field_wo_password_auth_page(self):
        actual_result = self.is_visible(AuthorizationLocators.PASSWORD_FIELD).get_attribute('class')
        assert actual_result == 'auth__form-input account__my-account-password vld-inp error'

    @allure.step('verify wrong number error message - rapid authorization page ')
    def verify_wrong_number_message_rapid_auth_page(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.WRONG_NUMBER_MESSAGE_RAPID_AUTH_PAGE)
        assert actual_result == 'Неправильный номер'

    @allure.step('verify short number error message - rapid authorization page ')
    def verify_short_number_message_rapid_auth_page(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.WRONG_NUMBER_MESSAGE_RAPID_AUTH_PAGE)
        assert actual_result == 'Телефон слишком короткий'

    @allure.step('verify long number error message - rapid authorization page ')
    def verify_long_number_message_rapid_auth_page(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.WRONG_NUMBER_MESSAGE_RAPID_AUTH_PAGE)
        assert actual_result == 'Телефон слишком длинный'

    @allure.step('verify red color of the unselected first checkbox - rapid auth page')
    def verify_red_unselected_first_checkbox_auth_page(self):
        actual_result = self.is_visible(AuthorizationLocators.FIRST_CHECKBOX_2).get_attribute('class')
        assert actual_result == 'auth__-form-agreements-checkbox validate-wrapper error'

    @allure.step('verify German flag with number with + rapid auth page')
    def verify_german_flag_auth_page(self):
        actual_result = self.is_visible(AuthorizationLocators.SELECTED_FLAG).get_attribute('title')
        assert actual_result == 'Germany (Deutschland): +49'

    @allure.step('verify not changed flag from Russian to German, while entering German number w/o + rapid auth page')
    def verify_russian_flag_auth_page(self):
        actual_result = self.is_visible(AuthorizationLocators.SELECTED_FLAG).get_attribute('title')
        assert actual_result == 'Russia (Россия): +7'

    @allure.step('click to flag arrow-button to see the list of countries -  rapid auth page')
    def click_flag_btn_rapid_auth(self):
        self.to_click(AuthorizationLocators.COUNTRIES_ARROW_BUTTON_RAPID_AUTH)

    @allure.step('click auth-code btn rapid auth page')
    def select_georgian_flag_rapid_auth(self):
        self.to_click(AuthorizationLocators.GEORGIA_FLAG)

    @allure.step('verify changed flag from Russian to Georgian - rapid auth page')
    def verify_georgian_flag_auth_page(self):
        actual_result = self.is_visible(AuthorizationLocators.SELECTED_FLAG).get_attribute('data-dial-code')
        assert actual_result == '995'

    @allure.step('verify message "Wrong wuthorization data"')
    def verify_wrong_wrong_auth_data_message_unexisting_user_authorization(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.ERROR_MESSAGE_WRONG_PASSWORD_AUTH_PAGE)
        assert actual_result == 'Неверные данные авторизации'

    @allure.step('click to "back" button on the order page')
    def click_to_back_button_order_page(self):
        self.to_click(AuthorizationLocators.BACK_BUTTON_ORDER_PAGE)

    @allure.step('click to "user avatar" button on the psychologist page')
    def click_to_user_avatar_button_psychologist_page(self):
        self.to_click(AuthorizationLocators.USER_AVATAR_NAME)

    # @allure.step('click "Elena K" element psychologist list page')
    # def click_elena_kalkan_psychologist_list(self):
    #     self.to_click(AuthorizationLocators.SELECT_ELENA_KALKAN_PSYCHOLOGYST_LIST)

    @allure.step('click 7th time in Elena Kalkan schedule')
    def click_3rd_time_pankova_schedule_page(self):
        self.to_click(AuthorizationLocators.SELECT_TIME_3_RAPID_PANKOVA)

    # @allure.step('set up "your email" in registration form')
    # def set_your_email_registration_fixture(self, first):
    #     self.set_value(AuthorizationLocators.EMAIL_FIELD_REGISTRATION_FORM, first)
    #
    # @allure.step('set password in registration form_fixture')
    # def set_password_registration_form_fixture(self, second):
    #     self.set_value(AuthorizationLocators.PASSWORD1_FIELD_REGISTRATION_FORM, second)
    #
    # @allure.step('repeat password in registration form_fixture')
    # def repeat_password_registration_form_fixture(self, third):
    #     self.set_value(AuthorizationLocators.PASSWORD2_REPEAT_FIELD_REGISTRATION_FORM, third)
    #
    # @allure.step('verify error message in registration form')
    # def verify_error_message_registration_fixture(self, fourth):
    #     actual_result = self.get_text_title_of_element(
    #         AuthorizationLocators.ERROR_MESSAGE_WRONG_REPEAT_PASSWORD_REG_FORM)
    #     assert actual_result == fourth

    # @allure.step('click "rapid auth" button in registration page')
    # def click_rapid_auth_btn_registration_page(self):
    #     self.to_click(AuthorizationLocators.RAPID_AUTH_BUTTON_REGISTRATION_PAGE)
    #
    # @allure.step('scroll the page till the "rapid auth" button in registration form')
    # def scroll_to_rapid_auth_button_registration_form(self):
    #     self.move_to_element(AuthorizationLocators.RAPID_AUTH_BUTTON_REGISTRATION_PAGE)

    @allure.step('click "avatar" button in package order page')
    def click_avatar_package_order_page(self):
        self.to_click(AuthorizationLocators.AVATAR_ORDER_PAGE)

    @allure.step('verify correct name of the package payment on the cloudpayments page')
    def verify_name_package_payment_cloudpayments_page(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.PACKAGE_4_PAYMENT_CLOUDPAYMENTS_PAGE)
        assert actual_result == 'Пакет консультаций "4"'

    @allure.step('verify correct name of the session payment on the cloudpayments page')
    def verify_name_session_payment_cloudpayments_page(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.SESSION_PAYMENT_CLOUDPAYMENTS_PAGE)
        assert actual_result == 'Сеанс с психологом'

    @allure.step('click to "go to the session" button on payed session')
    def click_go_to_payed_session_btn(self):
        self.to_click(AuthorizationLocators.GO_TO_SESSION)

    @allure.step('click to "reschedule session time" button on payed session')
    def click_to_reschedule_session_time_btn(self):
        self.to_click(AuthorizationLocators.TO_RESCHEDULE_SESSION_TIME_BTN)

    @allure.step('click to "reschedule session time" button on payed session')
    def click_to_deny_payed_session_btn(self):
        self.to_click(AuthorizationLocators.TO_DENY_PAYED_SESSION)

    @allure.step('click to "reschedule session time" button on payed session')
    def click_click_outside_deny_payed_session_modal_window(self):
        self.to_click(AuthorizationLocators.OUTSIDE_MODAL_WINDOW_DENY_SESSION)

    @allure.step('click to "reschedule session time" button on payed session')
    def click_to_yes_deny_payed_session_btn(self):
        self.to_click(AuthorizationLocators.YES_DENY_PAYED_SESSION_BUTTON)

    @allure.step('click to "cross" button to close modal window to deny session')
    def click_cross_to_close_modal_window_deny_payed_session(self):
        self.to_click(AuthorizationLocators.CROSS_TO_CLOSE_MODAL_WINDOW_DENY_SESSION)

    @allure.step('verify correct name of the session payment on the cloudpayments page')
    def verify_modal_confirmation_message_session_denied(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.CONFIRMATION_SESSION_IS_DENIED)
        assert actual_result == 'Ваш сеанс успешно отменен'

    @allure.step('verify caution text about payment refund during deny of the session')
    def verify_modal_window_caution_refund_session_denied(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.CAUTION_TITLE_DENY_SESSION_MODAL_WINDOW)
        assert actual_result == 'Обращаем ваше внимание'

    @allure.step('verify title of the page with timer before session')
    def verify_title_page_timer_before_session(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.TITLE_PAGE_TIMER_BEFORE_SESSION)
        assert actual_result == 'Дата и время сеанса'

    @allure.step('click to "select new doctor" button on package session')
    def click_to_select_new_doctor_btn_package_session(self):
        self.to_click(AuthorizationLocators.SELECT_NEW_DOCTOR_PACKAGE_SESSION)

    @allure.step('verify url of questionnaire page')
    def verify_url_questionnaire_page(self):
        self.get_url('https://life-help.ru/questionnaire/general/')

    @allure.step('click to "do not deny session" button on package session')
    def click_do_not_deny_btn_package_session(self):
        self.to_click(AuthorizationLocators.DO_NOT_DENY_SESSION_BUTTON)

    @allure.step('verify correct name of the session payment on the cloudpayments page')
    def verify_name_video_sesion_page_heading(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.NAME_VIDEO_SESSION_HEADING)
        assert 'Сеанс с психологом' in actual_result

    # @allure.step('click to "regular session order" icon')
    # def click_regular_session_order_icon(self):
    #     self.to_click(AuthorizationLocators.REGULAR_SESSION_ORDER_ICON)

    @allure.step('move to new regular schedule page')
    def move_to_new_regular_schedule_page(self):
        regular_schedule_page = self.driver.window_handles[1]
        self.driver.switch_to.window(regular_schedule_page)

    @allure.step('verify correct name of the session payment on the cloudpayments page')
    def verify_regular_schedule_page_title(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.REGULAR_SCHEDULE_PAGE_TITLE)
        assert actual_result == 'Регулярное расписание'

    @allure.step('click to "regular session" in dropdown menu list')
    def click_regular_session_order_dropdown_menu_list(self):
        self.to_click(AuthorizationLocators.REGULAR_SESSION_DROPDOWN)

    @allure.step('click to "select psychologist" in action')
    def click_select_psychologist_button_action(self):
        self.to_click(AuthorizationLocators.SELECT_PSYCHOLOGIST_ACTION_BUTTON)

    @allure.step('click to "select psychologist time" in action schedule')
    def click_select_psychologist_time_action_schedule(self):
        self.to_click(AuthorizationLocators.ACTION_DOCTOR_SCHEDULE_1ST_TIME)

    # @allure.step('scroll to button "go to payment" in action schedule page')
    # def scroll_to_go_to_payment_action_schedule_page(self):
    #     self.move_to_element(AuthorizationLocators.ACTION_DOCTOR_SCHEDULE_7TH_TIME)

    @allure.step('click to "to pay" button in clients account - My schedule page')
    def click_to_pay_btn_order_my_schedule_page(self):
        self.to_click(AuthorizationLocators.TO_PAY_BUTTON_ORDER_ACCOUNT_PAGE)

    @allure.step('verify users "my schedule" page url')
    def verify_my_schedule_user_page_url(self):
        self.get_url('https://life-help.ru/user/notes')

    @allure.step('verify url of questionnaire first page')
    def verify_url_get_psychologist_page(self):
        self.get_url('https://life-help.ru/questionnaire/general/')

    @allure.step('click to "to pay" button in clients account - My schedule page')
    def click_to_get_psychologists_btn_client_menu(self):
        self.to_click(AuthorizationLocators.GET_PSYCHOLOGIST_BUTTON_CLIENT_MENU)

    @allure.step('verify video frame of the psychologist')
    def verify_video_frame_psychologist_page(self):
        actual_result = self.is_visible(AuthorizationLocators.VIDEO_FRAME).get_attribute('allow')
        assert actual_result == 'autoplay'

    @allure.step('move to new chat w psychologist page')
    def move_to_chat_w_psychologist_page(self):
        chat_w_psychologist_page = self.driver.window_handles[1]
        self.driver.switch_to.window(chat_w_psychologist_page)

    @allure.step('verify correct name of the page "Chats w psychologist" client account')
    def verify_chats_w_psychologist_page_title(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.CHATS_W_PSYCHOLOGIST_PAGE_HEADING_CLIENT)
        assert actual_result == 'Чаты с психологом'

    @allure.step('click to "order session again" button in three dots in clients account - My schedule page')
    def click_order_session_again_three_dots_menu_btn_client(self):
        self.to_click(AuthorizationLocators.ORDER_SESSION_AGAIN_THREE_DOTS_MENU)

    @allure.step('verify url of psychologist page-order session again')
    def verify_url_psychologist_page_order_session_again(self):
        self.get_url('https://life-help.ru/user/recreate-session/136')

    @allure.step('verify disabled type of the "reset password" button - get link to restore password page')
    def verify_disabled_type_button_reset_password_page(self):
        actual_result = self.is_visible(AuthorizationLocators.RECOVER_PASSWORD_BUTTON).get_attribute('disabled')
        print(actual_result)
        # assert 'disabled' in actual_result

    # @allure.step('verify disabled type of the "reset password" button - get link to restore password page')
    # def verify_disabled_type_button_registration_page(self):
    #     actual_result = self.is_visible(AuthorizationLocators.REGISTER_BUTTON).get_attribute('disabled')
    #     print(actual_result)
        # assert 'disabled' in actual_result

    @allure.step('click to price on the tinkoff session payment page - to check the payment details')
    def click_price_payment_info_tinkoff_page(self):
        self.to_click(AuthorizationLocators.PRICE_TINKOFF_SESSION_PAYMENT)

    @allure.step('click to "my psychologist name" to open her schedule')
    def click_my_psychologist_name(self):
        self.to_click(AuthorizationLocators.MY_PSYCHOLOGIST_NAME_ACCOUNT)

    @allure.step('click to "my psychologist name" in chat page to open her schedule')
    def click_my_psychologist_name_chat(self):
        self.to_click(AuthorizationLocators.CHAT_CLIENT_COMPANION_NAME)

    @allure.step('move to new psychologist schedule page')
    def move_to_new_page_psychologist_schedule(self):
        psychologist_schedule_page = self.driver.window_handles[1]
        self.driver.switch_to.window(psychologist_schedule_page)

    @allure.step('verify url of psychologist schedule page')
    def verify_url_psychologist_schedule_page(self):
        self.get_url('https://life-help.ru/link-to-psychologist/136')

    @allure.step('click to "aim 2" in client aim list')
    def click_aim_2_client_account(self):
        self.to_click(AuthorizationLocators.AIM_2_CLIENT_ACCOUNT)

    @allure.step('click to "aim status" in client aim 2 modal window')
    def click_aim_2_status_client_account(self):
        self.to_click(AuthorizationLocators.AIM_STATUS_CLIENT_ACCOUNT)

    @allure.step('click to "in progress " aim status in client aim 2 modal window')
    def select_aim_status_in_progress_client_account(self):
        self.to_click(AuthorizationLocators.AIM_STATUS_IN_PROGRESS)

    @allure.step('click to "terminated" aim status in client aim 2 modal window')
    def select_aim_status_completed_client_account(self):
        self.to_click(AuthorizationLocators.AIM_STATUS_COMPLETED)

    @allure.step('click to "created" aim status in client aim 2 modal window')
    def select_aim_status_created_client_account(self):
        self.to_click(AuthorizationLocators.AIM_STATUS_CREATED)

    @allure.step('click to "save " button to save aim changes client')
    def click_save_aim_changes_client_account(self):
        self.to_click(AuthorizationLocators.SAVE_AIM_CHANGES_BUTTON_CLIENT)

    @allure.step('verify aim status is "in progress" client')
    def verify_aim_status_in_progress_client(self):
        actual_result = self.is_visible(AuthorizationLocators.AIM_2_CLIENT_ACCOUNT).get_attribute('class')
        assert actual_result == 'client__target-object in-progress'

    @allure.step('verify aim status is "in progress" client')
    def verify_aim_status_completed_client(self):
        actual_result = self.is_visible(AuthorizationLocators.AIM_2_CLIENT_ACCOUNT).get_attribute('class')
        assert actual_result == 'client__target-object completed'

    @allure.step('verify aim status is "created" client')
    def verify_aim_status_created_client(self):
        actual_result = self.is_visible(AuthorizationLocators.AIM_2_CLIENT_ACCOUNT).get_attribute('class')
        assert actual_result == 'client__target-object created'

    @allure.step('click to "remove aim" button in client aim 2 modal window')
    def click_remove_aim_button_client_account(self):
        self.to_click(AuthorizationLocators.REMOVE_AIM_BUTTON_CLIENT)

    @allure.step('verify url of client aims page')
    def verify_url_client_aims_list_page(self):
        self.get_url('https://life-help.ru/target/contract/')

    @allure.step('verify url of psychologist aim page')
    def verify_url_psychologist_aims_list_page(self):
        self.get_url('https://life-help.ru/doctor/contract/')

    @allure.step('click to "activate" certificate button in client my balance')
    def click_activate_certificate_button_client_my_balance(self):
        self.to_click(AuthorizationLocators.TO_ACTIVATE_CERTIFICATE_BUTTON)

    @allure.step('input false certificate code ')
    def set_false_certificate_code(self):
        self.set_value(AuthorizationLocators.INPUT_CODE_CERTIFICATE_FIELD, '1231-2312-3123')

    @allure.step('click to "activate" button after certificate code input')
    def click_activate_certificate_button_client_after_code_input(self):
        self.to_click(AuthorizationLocators.BUTTON_TO_ACTIVATE_AFTER_CERTIFICATE_INPUT)

    @allure.step('verify error message "certificate does not exist"')
    def verify_error_certificate_doesnot_exist_text(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.ERROR_CERTIFICATE_DOESNOT_EXIST)
        assert actual_result == 'Такого сертификата не существует'

    @allure.step('verify first order time is equal to first order time of the rapid schedule')
    def verify_rapid_first_order_time(self):
        actual_result = self.is_clickable(AuthorizationLocators.FIRST_ORDER_TIME)
        actual_result_value = actual_result.get_attribute("value")
        expected_result = self.is_clickable(AuthorizationLocators.RAPID_ORDER_TIME)
        expected_result_value = expected_result.get_attribute("value")
        self.verify_value(actual_result_value, expected_result_value)

    @allure.step('verify short number error message - rapid authorization page ')
    def verify_10number_phone_not_short_rapid_auth_page(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.WRONG_NUMBER_MESSAGE_RAPID_AUTH_PAGE)
        assert 'Телефон слишком короткий' not in actual_result

    @allure.step('verify short number error message - rapid authorization page ')
    def verify_14number_phone_not_long_rapid_auth_page(self):
        actual_result = self.get_text_title_of_element(AuthorizationLocators.WRONG_NUMBER_MESSAGE_RAPID_AUTH_PAGE)
        assert 'Телефон слишком длинный' not in actual_result

    # @allure.step('verify aim status is "created" client') - не сработало
    # def verify_error_class_false_certificate_code(self):
    #     actual_result = self.is_visible(AuthorizationLocators.ACTIVATE_CERTIFICATE_INPUT_WRAPPER).get_attribute('class')
    #     assert actual_result == 'certificate__code-input error'

    # @allure.step('scroll to button with 3rd rapid time in Pankova schedule page')
    # def scroll_to_3rd_rapid_time_button_pankova_schedule(self):
    #     self.move_to_element(AuthorizationLocators.SELECT_TIME_3_RAPID_PANKOVA)

    # @allure.step('verify session status "waits for payment" in the cabinet')
    # def verify_absence_order(self):
    #     actual_result = self.get_text_title_of_element(AuthorizationLocators.SESSION_WAITS_FOR_PAYMENT_TEXT)
    #     assert actual_result != 'Ожидает оплаты'


    # @allure.step('get page choose specialist url')
    # def get_page_choose_doctor_url(self):
    #     self.get_url('https://life-help.ru/questionnaire/choose-doctor/')
    #
    # @allure.step('verify questionnaire choose doctor page url')
    # def verify_choose_doctor_page_url(self):
    #     actual_url = self.get_url()
    #     assert actual_url == 'https://life-help.ru/questionnaire/choose-doctor/'


