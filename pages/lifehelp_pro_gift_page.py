from base.base_object import BaseObject
from locators.lifehelp_pro_gift_locators import LhproGiftLocators
import allure
from support.assertions import Assertions




class LhproGiftPage(BaseObject, Assertions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('click to "buy certificate" upper 1st btn')
    def click_to_buy_certificate_upper_1st_btn(self):
        self.to_click(LhproGiftLocators.BUY_CERTIFICATE_UPPER_1ST_BTN)

    @allure.step('verify title of the block "you can select the gift"')
    def verify_title_block_you_can_select_gift(self):
        actual_result = self.get_text_title_of_element(LhproGiftLocators.YOU_CAN_SELECT_GIFT_BLOCK_TITLE)
        expected_result = 'Вы можете выбрать подарок:'
        self.verify(expected_result, actual_result)

    @allure.step('click to "buy certificate" 2nd btn')
    def click_to_buy_certificate_2nd_btn(self):
        self.to_click(LhproGiftLocators.BUY_CERTIFICATE_2ND_BTN)

    @allure.step('click to "to know details" btn')
    def click_to_know_details_btn(self):
        self.to_click(LhproGiftLocators.TO_KNOW_DETAILS_BTN)

    @allure.step('verify title of the block "how it works"')
    def verify_title_block_how_it_works(self):
        actual_result = self.get_text_title_of_element(LhproGiftLocators.HOW_IT_WORKS_DETAILS_BLOCK_TITLE)
        expected_result = 'Как это работает?'
        self.verify(expected_result, actual_result)

    @allure.step('verify text of the step one of the block "how it works"')
    def verify_text_first_step_how_it_works(self):
        actual_result = self.get_text_title_of_element(LhproGiftLocators.SELECT_CERTIFICATE_STEP_ONE)
        expected_result = 'Выбирайте номинал сертификата и нажимайте кнопку "Подарить"'
        self.verify(expected_result, actual_result)

    @allure.step('click to certificate "slider to the right" btn')
    def click_to_certificate_slider_right_btn(self):
        self.to_click(LhproGiftLocators.CERTIFICATES_SLIDER_RIGHT_BTN)

    @allure.step('verify title of the certificate "4 sessions"')
    def verify_title_certificate_4_sessions(self):
        actual_result = self.get_text_title_of_element(LhproGiftLocators.CERTIFICATE_4_SESSIONS_TITLE)
        expected_result = '4 сессии'
        self.verify(expected_result, actual_result)

    @allure.step('click to certificate "slider to the left" btn')
    def click_to_certificate_slider_left_btn(self):
        self.to_click(LhproGiftLocators.CERTIFICATES_SLIDER_LEFT_BTN)

    @allure.step('scroll to "you can select certificate" unit title')
    def scroll_till_title_you_can_select_certificate(self):
        self.move_to_element(LhproGiftLocators.YOU_CAN_SELECT_GIFT_BLOCK_TITLE)

    @allure.step('scroll to "54 sessions certificate" image')
    def scroll_till_54_sessions_certificate_image(self):
        self.move_to_element(LhproGiftLocators.CERTIFICATE_54_IMAGE)

    @allure.step('verify title of the certificate "54 sessions"')
    def verify_title_certificate_54_sessions(self):
        actual_result = self.get_text_title_of_element(LhproGiftLocators.CERTIFICATE_54_SESSIONS_TITLE)
        expected_result = '54 сессии'
        self.verify(expected_result, actual_result)

    @allure.step('verify price of the certificate "54 sessions"')
    def verify_price_certificate_54_sessions(self):
        actual_result = self.get_text_title_of_element(LhproGiftLocators.PRICE_125000_CERTIFICATE_54)
        expected_result = '125 000 ₽'
        self.verify(expected_result, actual_result)

    @allure.step('verify price of the certificate "12 sessions"')
    def verify_price_certificate_12_sessions(self):
        actual_result = self.get_text_title_of_element(LhproGiftLocators.PRICE_28800_CERTIFICATE_12)
        expected_result = '28 800 ₽'
        self.verify(expected_result, actual_result)

    @allure.step('verify price of the certificate "8 sessions"')
    def verify_price_certificate_8_sessions(self):
        actual_result = self.get_text_title_of_element(LhproGiftLocators.PRICE_20800_CERTIFICATE_8)
        expected_result = '20 800 ₽'
        self.verify(expected_result, actual_result)

    @allure.step('verify price of the certificate "4 sessions"')
    def verify_price_certificate_4_sessions(self):
        actual_result = self.get_text_title_of_element(LhproGiftLocators.PRICE_10800_CERTIFICATE_4)
        expected_result = '10 800 ₽'
        self.verify(expected_result, actual_result)

    @allure.step('verify price of the certificate "1 session"')
    def verify_price_certificate_1_session(self):
        actual_result = self.get_text_title_of_element(LhproGiftLocators.PRICE_2950_CERTIFICATE_1)
        expected_result = '2 950 ₽'
        self.verify(expected_result, actual_result)

    @allure.step('click to btn "present" on certificate 54')
    def click_to_present_certificate_54_btn(self):
        self.to_click(LhproGiftLocators.TO_PRESENT_CERTIFICATE_54_SESSIONS_BTN)

    @allure.step('click to btn "present" on certificate 12')
    def click_to_present_certificate_12_btn(self):
        self.to_click(LhproGiftLocators.TO_PRESENT_CERTIFICATE_12_SESSIONS_BTN)

    @allure.step('click to btn "present" on certificate 8')
    def click_to_present_certificate_8_btn(self):
        self.to_click(LhproGiftLocators.TO_PRESENT_CERTIFICATE_8_SESSIONS_BTN)

    @allure.step('click to btn "present" on certificate 4')
    def click_to_present_certificate_4_btn(self):
        self.to_click(LhproGiftLocators.TO_PRESENT_CERTIFICATE_4_SESSIONS_BTN)

    @allure.step('click to btn "present" on certificate 1')
    def click_to_present_certificate_1_btn(self):
        self.to_click(LhproGiftLocators.TO_PRESENT_CERTIFICATE_1_SESSIONS_BTN)

    @allure.step('move to new page')
    def move_to_new_page(self):
        new_page = self.driver.window_handles[1]
        self.driver.switch_to.window(new_page)

    @allure.step('scroll to bottom on https://lifehelp.pro/gifts page')
    def scroll_till_bottom_lh_gift_page(self):
        self.move_to_page_bottom()

    @allure.step('scroll to "privacy policy" button')
    def scroll_till_btn_privacy_policy(self):
        self.move_to_element(LhproGiftLocators.PRIVACY_POLICY_TITLE)

    @allure.step('click to "privacy policy" document title on bottom of the main page')
    def click_to_privacy_policy_title(self):
        self.to_click(LhproGiftLocators.PRIVACY_POLICY_TITLE)

    @allure.step('verify price of the separate session in certificate "54"')
    def verify_price_separate_session_certificate_54_sessions(self):
        actual_result = self.get_text_title_of_element(LhproGiftLocators.SEPARATE_SESSION_PRICE_CERTIFICATE_54)
        expected_result = '2 315 ₽/встреча'
        self.verify(expected_result, actual_result)

    @allure.step('verify price of the separate session in certificate "12"')
    def verify_price_separate_session_certificate_12_sessions(self):
        actual_result = self.get_text_title_of_element(LhproGiftLocators.SEPARATE_SESSION_PRICE_CERTIFICATE_12)
        expected_result = '2 400 ₽/встреча'
        self.verify(expected_result, actual_result)

    @allure.step('verify price of the separate session in certificate "8"')
    def verify_price_separate_session_certificate_8_sessions(self):
        actual_result = self.get_text_title_of_element(LhproGiftLocators.SEPARATE_SESSION_PRICE_CERTIFICATE_8)
        expected_result = '2 600 ₽/встреча'
        self.verify(expected_result, actual_result)

    @allure.step('verify price of the separate session in certificate "4"')
    def verify_price_separate_session_certificate_4_sessions(self):
        actual_result = self.get_text_title_of_element(LhproGiftLocators.SEPARATE_SESSION_PRICE_CERTIFICATE_4)
        expected_result = '2 700 ₽/встреча'
        self.verify(expected_result, actual_result)


