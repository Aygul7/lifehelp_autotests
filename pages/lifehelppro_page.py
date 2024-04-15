from base.base_object import BaseObject
from locators.lifehelppro_locators import LifehelpProLocators
import allure
from support.assertions import Assertions




class LifehelpProPage(BaseObject, Assertions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('click to find psychologist 1st upper button')
    def click_to_find_psychologist_upper_1st_btn(self):
        self.to_click(LifehelpProLocators.FIND_PSYCHOLOGIST_UPPER_1ST_BUTTON)

    @allure.step('move to new page')
    def move_to_new_page(self):
        new_page = self.driver.window_handles[1]
        self.driver.switch_to.window(new_page)

    @allure.step('verify price of the separate session in certificate "54"')
    def verify_title_general_questions_questionnaire(self):
        actual_result = self.get_text_title_of_element(LifehelpProLocators.GENERAL_QUESTIONS_TITLE_QUESTIONNAIRE)
        expected_result = 'Общие вопросы'
        self.verify(expected_result, actual_result)

    @allure.step('verify price of the separate session in certificate "54"')
    def verify_text_ind50_general_questions_questionnaire(self):
        actual_result = self.get_text_title_of_element(LifehelpProLocators.TEXT_INDIVIDUAL_50_GENERAL_QUESIONNAIRE)
        expected_result = 'Индивидуальная 50'
        self.verify(expected_result, actual_result)

    @allure.step('click to want to try button')
    def click_to_want_to_try_btn(self):
        self.to_click(LifehelpProLocators.WANT_TO_TRY_BTN)

    @allure.step('click to login button')
    def click_to_login_btn(self):
        self.to_click(LifehelpProLocators.TO_LOGIN_BTN)

    @allure.step('click to menu button')
    def click_to_menu_btn(self):
        self.to_click(LifehelpProLocators.MENU_BTN)

    @allure.step('click to get psychologist btn in menu list')
    def click_to_get_psychologist_btn_menu_list(self):
        self.to_click(LifehelpProLocators.GET_PSYCHOLOGIST_MENU_BTN)

    @allure.step('click to buy certificate btn in menu list')
    def click_to_buy_certificate_btn_menu_list(self):
        self.to_click(LifehelpProLocators.TO_BUY_CERTIFICATE_MENU_BTN)

    @allure.step('scroll to unit "therapy queries"')
    def scroll_to_therapy_queries_unit(self):
        self.move_to_element(LifehelpProLocators.THERAPY_QUERIES_TITLE)

    @allure.step('scroll to unit "how it works"')
    def scroll_to_how_it_works_unit(self):
        self.move_to_element(LifehelpProLocators.HOW_IT_WORKS_TITLE)

    @allure.step('click to get psychologist btn under therapy queries unit')
    def click_to_get_psychologist_btn_under_therapy_queries_unit(self):
        self.to_click(LifehelpProLocators.GET_PSYCHOLOGIST_BTN_UNDER_THERAPY_QUERIES_UNIT)

    @allure.step('click to get diagnostic btn under how it works unit')
    def click_to_get_diagnostic_btn_under_how_it_works_unit(self):
        self.to_click(LifehelpProLocators.GET_DIAGNOSTIC_BTN_UNDER_HOW_IT_WORKS_UNIT)


    #fill the application for the 20min diagnostic
    @allure.step('click to get diagnostic btn under how it works unit')
    def click_to_leave_credentials_btn_diagnostic_application_form(self):
        self.to_click(LifehelpProLocators.LEAVE_YOUR_CREDENTIALS_BTN_DIAGNOSTIC_APPLICATION_FORM)

    @allure.step('input name in application form for 20min diagnostic')
    def set_name_application_form_for_diagnostic(self):
        self.set_value(LifehelpProLocators.INPUT_NAME_FIELD_APPLICATION_FORM_FOR_DIAGNOSTIC, 'test')

    @allure.step('input phone in application form for 20min diagnostic')
    def set_phone_application_form_for_diagnostic(self):
        self.set_value(LifehelpProLocators.INPUT_PHONE_FIELD_APPLICATION_FORM_FOR_DIAGNOSTIC, '89123123123')

    @allure.step('click to apply psychologist request btn in application form for 20min diagnostic')
    def click_to_apply_psychologist_request_btn_diagnostic_application_form(self):
        self.to_click(LifehelpProLocators.APPLY_PSYCHOLOGIST_REQUEST_BTN)

    @allure.step('click to apply via whatsapp btn in application form for 20min diagnostic')
    def click_to_apply_via_whatsapp_btn_diagnostic_application_form(self):
        self.to_click(LifehelpProLocators.APPLY_VIA_WHATSAPP_BTN_FORM_FOR_DIAGNOSTIC)

    @allure.step('click to apply via telegram btn in application form for 20min diagnostic')
    def click_to_apply_via_telegram_btn_diagnostic_application_form(self):
        self.to_click(LifehelpProLocators.APPLY_VIA_TELEGRAM_BTN_FORM_FOR_DIAGNOSTIC)

    @allure.step('verify successful application notification text')
    def verify_successful_application_notification_text(self):
        actual_result = self.get_text_title_of_element(LifehelpProLocators.SUCCESSFUL_APPLICATION_NOTIFICATION_TEXT)
        assert 'Ваша заявка отправлена.' in actual_result

    @allure.step('scroll to block title "we warrant stability"')
    def scroll_to_block_stability_warranty_title(self):
        self.move_to_element(LifehelpProLocators.TITLE_BLOCK_STABILITY_WARRANTY)

    @allure.step('click to get psychologist btn under unit why users prefer life help')
    def click_to_get_psychologist_btn_under_unit_why_users_prefer_lh(self):
        self.to_click(LifehelpProLocators.GET_PSYCHOLOGIST_BTN_UNDER_WHY_USERS_PREFER_LH)

    @allure.step('scroll to unit "order time" in users step description')
    def scroll_to_title_order_time_in_users_steps_description(self):
        self.move_to_element(LifehelpProLocators.TITLE_ORDER_TIME_USERS_STEPS_DESCRIPTION)

    @allure.step('click to fill questionnaire btn under unit with users steps description')
    def click_to_fill_questionnaire_btn_under_users_step_description_unit(self):
        self.to_click(LifehelpProLocators.GET_PSYCHOLOGIST_BTN_UNDER_WHY_USERS_PREFER_LH)

    @allure.step('click to apply diagnostic btn under unit with users steps description')
    def click_to_apply_diagnostic_btn_under_users_step_description_unit(self):
        self.to_click(LifehelpProLocators.ALLPY_FOR_DIAGNOSTIC_BTN_UNDER_USER_STEPS_DESCRIPTION_UNIT)

    @allure.step('scroll to text time limit under prices unit')
    def scroll_to_text_time_limit_under_prices_unit(self):
        self.move_to_element(LifehelpProLocators.TEXT_TIME_LIMIT_UNDER_PRICES)

    @allure.step('click to get psychologist themselves btn under prices unit')
    def click_to_get_psychologist_themselves_btn_under_prices_unit(self):
        self.to_click(LifehelpProLocators.GET_PSYCHOLOGIST_THEMSELVES_BTN_UNDER_PRICES)

    @allure.step('click to get free psychologist set btn under prices unit')
    def click_to_get_free_psychologist_set_btn_under_prices_unit(self):
        self.to_click(LifehelpProLocators.GET_FREE_PSYCHOLOGIST_SET)

    @allure.step('scroll to users review unit title')
    def scroll_to_users_review_unit_title(self):
        self.move_to_element(LifehelpProLocators.USERS_REVIEW_TITLE_UNIT)

    @allure.step('click to get psychologist btn under users review unit')
    def click_to_get_psychologist_btn_under_users_review_unit(self):
        self.to_click(LifehelpProLocators.GET_PSYCHOLOGIST_BTN_UNDER_USERS_REVIEW_UNIT)

    @allure.step('scroll to text under last question in faq unit')
    def scroll_to_text_under_last_question_faq_unit(self):
        self.move_to_element(LifehelpProLocators.TEXT_UNDER_LAST_QUESTION_FAQ_UNIT)

    @allure.step('click to get psychologist themselves btn under faq unit')
    def click_to_get_psychologist_themselves_btn_under_faq_unit(self):
        self.to_click(LifehelpProLocators.GET_PSYCHOLOGIST_THEMSELVES_BTN_UNDER_FAQ)

    @allure.step('click to get free psychologist set btn under faq unit')
    def click_to_get_free_psychologist_set_btn_under_faq_unit(self):
        self.to_click(LifehelpProLocators.GET_FREE_PSYCHOLOGIST_SET_UNDER_FAQ)

    @allure.step('scroll to text "several clicks to psychologist"')
    def scroll_to_text_several_clicks_to_psychologist(self):
        self.move_to_element(LifehelpProLocators.SEVERAL_CLICKS_TO_PSYCHOLOGIST_TITLE)

    @allure.step('click to whatsapp care icon')
    def click_to_whatsapp_care_icon(self):
        self.to_click(LifehelpProLocators.WHATSAPP_CARE_ICON)

    @allure.step('click to telegram care icon')
    def click_to_telegram_care_icon(self):
        self.to_click(LifehelpProLocators.TELEGRAM_CARE_ICON)

    @allure.step('scroll to text "lifehelp service" on page bottom')
    def scroll_to_page_bottom_till_lifefelp_service(self):
        self.move_to_element(LifehelpProLocators.LIFEHELP_SERVICE_TEXT_PAGE_BOTTOM)

    @allure.step('click to contract offer text on the page bottom')
    def click_to_contract_offer_text_page_bottom(self):
        self.to_click(LifehelpProLocators.CONTRACT_OFFER_TITLE_PAGE_BOTTOM)

    @allure.step('click to agreement text on the page bottom')
    def click_to_agreement_text_page_bottom(self):
        self.to_click(LifehelpProLocators.AGREEMENT_TITLE_PAGE_BOTTOM)

    @allure.step('click to privacy policy text on the page bottom')
    def click_to_privacy_policy_text_page_bottom(self):
        self.to_click(LifehelpProLocators.PRIVACY_POLICY_PAGE_BOTTOM)

    @allure.step('click to consent mailing text on the page bottom')
    def click_to_consent_mailing_text_page_bottom(self):
        self.to_click(LifehelpProLocators.CONSENT_MAILING_PAGE_BOTTOM)

    @allure.step('click to vk icon on the page bottom')
    def click_to_vk_icon_page_bottom(self):
        self.to_click(LifehelpProLocators.VK_ICON_PAGE_BOTTOM)

    @allure.step('click to telegram icon on the page bottom')
    def click_to_telegram_icon_page_bottom(self):
        self.to_click(LifehelpProLocators.TELEGRAM_ICON_PAGE_BOTTOM)

    @allure.step('click to register btn on the page bottom')
    def click_to_register_btn_page_bottom(self):
        self.to_click(LifehelpProLocators.TO_REGISTER_PAGE_BOTTOM)