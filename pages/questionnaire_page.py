from base.base_object import BaseObject
from locators.questionnaire_locators import QuestionnaireLocators
import allure
from support.assertions import Assertions
from selenium.webdriver.common.keys import Keys




class QuestionnairePage(BaseObject, Assertions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('click to individual consultation button')
    def click_individual_consultation(self):
        self.to_click(QuestionnaireLocators.INDIVIDUAL_CONSULTATION_BUTTON)

    @allure.step('click to paired consultation button')
    def click_paired_consultation(self):
        self.to_click(QuestionnaireLocators.PAIRED_CONSULTATION_BUTTON)

    @allure.step('click to russian language')
    def click_russian_language(self):
        self.to_click(QuestionnaireLocators.RUSSIAN_LANGUAGE_BUTTON)

    @allure.step('click to tatar language')
    def click_tatar_language(self):
        self.to_click(QuestionnaireLocators.TATAR_LANGUAGE_BUTTON)

    @allure.step('click to video button')
    def click_video_consultation(self):
        self.to_click(QuestionnaireLocators.VIDEO_BUTTON)

    @allure.step('click to audio button')
    def click_audio_consultation(self):
        self.to_click(QuestionnaireLocators.AUDIO_BUTTON)

    @allure.step('click to chat button')
    def click_chat_consultation(self):
        self.to_click(QuestionnaireLocators.CHAT_BUTTON)

    @allure.step('set up age')
    def set_age_questionnaire(self):
        self.set_value(QuestionnaireLocators.AGE_FIELD, '50')


    @allure.step('click to next button')
    def click_next_button(self):
        self.to_click(QuestionnaireLocators.NEXT_BUTTON)

    @allure.step('click to title "Personal questions"')
    def click_personal_questions_title(self):
        self.to_click(QuestionnaireLocators.PERSONAL_QUESTIONS_TITLE)

    @allure.step('click to "get psychologist" button')
    def click_personal_questions_title(self):
        self.to_click(QuestionnaireLocators.PERSONAL_QUESTIONS_TITLE)
    @allure.step('select "Stress" in questionnaire')
    def select_stress_questionnaire(self):
        self.to_click(QuestionnaireLocators.STRESS_CHECKBOX_QUESTIONNAIRE)

    @allure.step('click "Psychologist preferences" title in questionnaire')
    def click_psychologist_preferences_title_questionnaire(self):
        self.to_click(QuestionnaireLocators.PSYCHOLOGIST_PREFERENCES_TITLE_QUESTIONNAIRE)

    @allure.step('click "age over 30" button in questionnaire')
    def click_age_over_30_questionnaire(self):
        self.to_click(QuestionnaireLocators.AGE_OVER_30_BUTTON_QUESTIONNAIRE)

    @allure.step('click "Select psychologist" title in questionnaire')
    def click_select_psychologist_title_questionnaire(self):
        self.to_click(QuestionnaireLocators.SELECT_PSYCHOLOGIST_TITLE_QUESTIONNAIRE)

    @allure.step('verify presence of Irina Pankova among "choose specialist" list')
    def verify_presence_pankova_choose_specialist(self):
        actual_result = self.get_text_title_of_element(QuestionnaireLocators.IRINA_PANKOVA_TITLE_CHOOSE_DOCTOR_LIST)
        assert actual_result == 'Ирина'

    @allure.step('click "Individual 90" button in questionnaire')
    def click_ind_90_questionnaire(self):
        self.to_click(QuestionnaireLocators.INDIVIDUAL_90_QUESTIONNAIRE_GENERAL)

    @allure.step('verify presence of Alisa Ivannikova among "choose specialist" list')
    def verify_presence_alisa_ivannikova_choose_specialist(self):
        actual_result = self.get_text_title_of_element(QuestionnaireLocators.ALISA_IVANNIKOVA_TITLE_CHOOSE_DOCTOR_LIST)
        assert actual_result == 'Алиса'

    @allure.step('click "tatar" button in questionnaire')
    def click_tatar_button_questionnaire(self):
        self.to_click(QuestionnaireLocators.TATAR_BUTTON_QUESTIONNAIRE)

    @allure.step('verify presence of Aliya Askarova among "choose specialist" list')
    def verify_presence_aliya_askarova_choose_specialist(self):
        actual_result = self.get_text_title_of_element(QuestionnaireLocators.ALIYA_ASKAROVA_TITLE_CHOOSE_DOCTOR_LIST)
        assert actual_result == 'Алия'

    @allure.step('click "paired consulation" button in questionnaire')
    def click_paired_consultation_button_questionnaire(self):
        self.to_click(QuestionnaireLocators.PAIRED_CONSULTATION_BUTTON_QUESTIONNAIRE)

    @allure.step('click "difficulties in paired relationship" button in questionnaire')
    def click_difficulties_in_relationship_paired_consultation_button_questionnaire(self):
        self.to_click(QuestionnaireLocators.DIFFICULTIES_IN_RELATIONSHIP_PAIRED_BUTTON_CONSULTATION)

    @allure.step('verify presence of Elena Kalkan among "choose specialist" list')
    def verify_presence_elena_kalkan_choose_specialist(self):
        actual_result = self.get_text_title_of_element(QuestionnaireLocators.ELENA_KALKAN_TITLE_CHOOSE_DOCTOR_LIST)
        assert actual_result == 'Елена'

    @allure.step('verify appearance of window with request to set the age')
    def verify_window_to_set_age_questionnaire(self):
        actual_result = self.get_text_title_of_element(QuestionnaireLocators.SET_YOUR_AGE_QUESTIONNAIRE_WINDOW)
        assert actual_result == 'Пожалуйста, укажите свой возраст'

    @allure.step('set age in questionnaire-age field validation')
    def set_age_field_negative_validation_questionnaire(self, first):
        self.set_value(QuestionnaireLocators.AGE_FIELD, first)

    @allure.step('verify appearance of window with info, that service can be used only by person above 16 years old')
    def verify_window_age_above16_questionnaire(self):
        actual_result = self.get_text_title_of_element(QuestionnaireLocators.AGE_ABOVE16_WINDOW_QUESTIONNAIRE)
        assert actual_result == 'Нашим сервисом можно пользоваться с 16 лет'

    @allure.step('set age in questionnaire-age field positive validation')
    def set_age_field_positive_validation_questionnaire(self, age):
        self.set_value(QuestionnaireLocators.AGE_FIELD, age)

    @allure.step('clicking to "Next" button')
    def enter_instead_click_to_next_button_questionnaire(self):
        self.is_clickable(QuestionnaireLocators.NEXT_BUTTON_QUESTIONNAIRE).send_keys(Keys.RETURN)

    @allure.step('click "age till 30" button in questionnaire - doctor preferences')
    def click_age_till_30_questionnaire_preferences(self):
        self.to_click(QuestionnaireLocators.DOCTOR_AGE_TILL_30_QUESTIONNAIRE_PREFERENCES)

    @allure.step('verify presence of Medina Nunueva among "choose specialist" list')
    def verify_presence_nunueva_choose_specialist(self):
        actual_result = self.get_text_title_of_element(QuestionnaireLocators.MEDINA_NUNUEVA_TITLE_CHOOSE_DOCTOR_LIST)
        assert actual_result == 'Медина'

    @allure.step('click "male" button in questionnaire - doctor preferences')
    def click_male_button_questionnaire_preferences(self):
        self.to_click(QuestionnaireLocators.DOCTOR_MALE_QUESTIONNAIRE_PREFERENCES)

    @allure.step('verify presence of Nikita Yujhakov among "choose specialist" list')
    def verify_presence_nikita_choose_specialist(self):
        actual_result = self.get_text_title_of_element(QuestionnaireLocators.NIKITA_YUJHAKOV_TITLE_CHOOSE_DOCTOR_LIST)
        assert actual_result == 'Никита'

    @allure.step('verify presence of Dmitrii Prokopov among "choose specialist" list')
    def verify_presence_dmitrii_choose_specialist(self):
        actual_result = self.get_text_title_of_element(QuestionnaireLocators.DMITRII_PROKOPOV_TITLE_CHOOSE_DOCTOR_LIST)
        assert actual_result == 'Дмитрий'

    @allure.step('click "wo children" button in questionnaire - doctor preferences')
    def click_wo_children_questionnaire_preferences(self):
        self.to_click(QuestionnaireLocators.DOCTOR_WO_CHILDREN_QUESTIONNAIRE_PREFERENCES)

    @allure.step('verify presence of Lilia Seregina among "choose specialist" list')
    def verify_presence_lilia_choose_specialist(self):
        actual_result = self.get_text_title_of_element(QuestionnaireLocators.LILIA_SEREGINA_TITLE_CHOOSE_DOCTOR_LIST)
        assert actual_result == 'Лилия'

    @allure.step('verify name of Lilia Sergeevna among "choose specialist" list')
    def verify_lilia_sergeevna_name_choose_specialist(self):
        actual_result = self.get_text_title_of_element(QuestionnaireLocators.LILIA_SEREGINA_FULL_NAME_WO_SURNAME_DOCTOR_LIST)
        assert actual_result == 'Лилия Сергеевна'

    @allure.step('verify price 2950 of ind50 - Lilia Seregina questionnaire page')
    def verify_lilia_price_2950_choose_specialist(self):
        actual_result = self.get_text_title_of_element(
            QuestionnaireLocators.DOCTOR_PRICE_SPECIALIST_PAGE_QUESTIONNAIRE)
        assert actual_result == 'Индивидуальная консультация 50 минут • 2950.00 ₽'

    @allure.step('verify price 4200 of ind90 questionnaire page')
    def verify_ind90_price_4200_choose_specialist(self):
        actual_result = self.get_text_title_of_element(
            QuestionnaireLocators.DOCTOR_PRICE_SPECIALIST_PAGE_QUESTIONNAIRE)
        assert actual_result == 'Индивидуальная консультация 1.5 часа • 4200.00 ₽'

    @allure.step('verify price 4850 of paired questionnaire page')
    def verify_paired_price_4850_choose_specialist(self):
        actual_result = self.get_text_title_of_element(
            QuestionnaireLocators.DOCTOR_PRICE_SPECIALIST_PAGE_QUESTIONNAIRE)
        assert actual_result == 'Парная консультация 1.5 часа • 4850.00 ₽'

    @allure.step('click "terrible" personal state in questionnaire')
    def click_terrible_personal_state_questionnaire(self):
        self.to_click(QuestionnaireLocators.TERRIBLE_PERSONAL_STATE_QUESTIONNAIRE)

    @allure.step('click to tatar language')
    def click_first_rapid_time_choose_doctor_page(self):
        self.to_click(QuestionnaireLocators.FIRST_ORDER_TIME_DOCTOR_PAGE_AFTER_QUESTIONNAIRE)

    @allure.step('click to btn "order selected time" in rapid schedule')
    def click_to_btn_order_rapid_time_choose_doctor_page(self):
        self.to_click(QuestionnaireLocators.TO_ORDER_RAPID_TIME_BTN_DOCTOR_PAGE_AFTER_QUESTIONNAIRE)

    @allure.step('scroll to "order time" button on psychologyst rapid schedule')
    def scroll_till_btn_order_rapid_time_psychologist_schedule(self):
        self.move_to_element(QuestionnaireLocators.TO_ORDER_RAPID_TIME_BTN_DOCTOR_PAGE_AFTER_QUESTIONNAIRE)

    @allure.step('verify auth form after choose specialist questionnaire page')
    def verify_auth_form_after_choose_specialist(self):
        actual_result = self.get_text_title_of_element(
            QuestionnaireLocators.SUBMIT_PERSONAL_INFO_AUTH_FORM_AFTER_QUESTIONNAIRE)
        assert actual_result == 'Укажите ваши данные:'

    @allure.step('click to btn "find psychologist" from user account page')
    def click_to_btn_find_psychologist_account_page(self):
        self.to_click(QuestionnaireLocators.FIND_PSYCHOLOGIST_ACCOUNT_BTN)

    @allure.step('verify auth form after choose specialist questionnaire page')
    def verify_auth_form_after_choose_specialist(self):
        actual_result = self.get_text_title_of_element(
            QuestionnaireLocators.SUBMIT_PERSONAL_INFO_AUTH_FORM_AFTER_QUESTIONNAIRE)
        assert actual_result == 'Укажите ваши данные:'

    @allure.step('clicking to "Login" button')
    def click_to_login_button(self):
        self.to_click(QuestionnaireLocators.LOGIN_BUTTON)

    @allure.step('clicking to "Login with password" button')
    def click_to_login_w_password_button(self):
        self.to_click(QuestionnaireLocators.LOGIN_WITH_PASSWORD_BUTTON)

    def set_phone_password_authorization(self):
        self.set_value(QuestionnaireLocators.EMAIL_PHONE_FIELD, '89274197879')

    @allure.step('set up password')
    def set_password_pass(self):
        self.set_value(QuestionnaireLocators.PASSWORD_FIELD, 'lifehelp1@')

    @allure.step('clicking to "Authorize" button')
    def click_to_authorize_button(self):
        self.to_click(QuestionnaireLocators.AUTH_BUTTON)

    @allure.step('clicking to "Move to order" button on auth_order page')
    def click_to_move_to_order_button_auth_order_page(self):
        self.to_click(QuestionnaireLocators.MOVE_TO_ORDER_BTN_ORDER_AUTH_PAGE)

    @allure.step('set up user name on the order_auth page')
    def set_user_name_order_auth_page(self):
        self.set_value(QuestionnaireLocators.NAME_INPUT_FIELD_ORDER_AUTH_PAGE, 'Test_wo_package')

    @allure.step('set up user phone on the order_auth page')
    def set_user_phone_order_auth_page(self):
        self.set_value(QuestionnaireLocators.PHONE_INPUT_FIELD_ORDER_AUTH_PAGE, '79274197879')

    @allure.step('click to first agreement checkbox on order_auth page')
    def select_agreement_checkbox_auth_order_page(self):
        self.to_click(QuestionnaireLocators.AGREEMENT_OFFER_CHECKBOX_ORDER_AUTH_PAGE)

    @allure.step('click to unselect second checkbox "mailing" on order_auth page')
    def unselect_mailing_checkbox_auth_order_page(self):
        self.to_click(QuestionnaireLocators.MAILING_CONSENT_CHECKBOX_ORDER_AUTH_PAGE)

    @allure.step('verify auth form after choose specialist questionnaire page')
    def verify_title_modal_window_enter_sms_code(self):
        actual_result = self.get_text_title_of_element(
            QuestionnaireLocators.ENTER_SMS_CODE_MODAL_WINDOW_TITLE)
        assert actual_result == 'Введите код из SMS'

    @allure.step('verify error class of the empty user name field after click on "Move to order" btn')
    def verify_error_empty_user_name_field_order_auth_page(self):
        actual_result = self.is_visible(QuestionnaireLocators.NAME_INPUT_FIELD_ORDER_AUTH_PAGE).get_attribute('class')
        assert actual_result == 'text-filed big invalid'

    @allure.step('verify error class of the empty user phone field after click on "Move to order" btn')
    def verify_error_empty_user_phone_field_order_auth_page(self):
        actual_result = self.is_visible(QuestionnaireLocators.PHONE_INPUT_FIELD_ORDER_AUTH_PAGE).get_attribute('class')
        assert actual_result == 'text-filed p-inp validate-field required error'

    @allure.step('click to title "doctor profile" on order_auth page')
    def click_doctor_profile_auth_order_page(self):
        self.to_click(QuestionnaireLocators.DOCTOR_PROFILE_TITLE_AUTH_ORDER_PAGE)

    @allure.step('move to new page')
    def move_to_new_page(self):
        new_page = self.driver.window_handles[1]
        self.driver.switch_to.window(new_page)