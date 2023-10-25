from base.base_object import BaseObject
from locators.veb_life_help_locators import VebLifeHelpLocators
from locators.authorization_locators import AuthorizationLocators
import allure
from support.assertions import Assertions


class VebLhPage(BaseObject):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('clicking to "Login" button')
    def click_to_login_button_veb_lh(self):
        self.to_click(VebLifeHelpLocators.LOGIN_BUTTON_VEB_LH)

    @allure.step('clicking to "Registration" button')
    def click_to_registration_button_veb_lh(self):
        self.to_click(VebLifeHelpLocators.REGISTRATION_BUTTON_VEB_LH)

    @allure.step('clicking to "Present certificate" button')
    def click_to_present_certificate_button_veb_lh(self):
        self.to_click(VebLifeHelpLocators.PRESENT_CERTIFICATE_BUTTON)

    @allure.step('move to new certificate page')
    def move_to_new_certificate_page(self):
        certificate_page = self.driver.window_handles[1]
        self.driver.switch_to.window(certificate_page)

    @allure.step('scroll to bottom on veb.life-help.pro page')
    def scroll_till_bottom_veb_lh_page(self):
        self.move_to_page_bottom()

    @allure.step('clicking to "Whatsapp widget element" button')
    def click_to_whatsapp_button_veb_lh(self):
        self.to_click(VebLifeHelpLocators.WHATSAPP_WIDGET_VEB_LH)

    @allure.step('move to new whatsapp page')
    def move_to_new_whatsapp_page(self):
        whatsapp_page = self.driver.window_handles[1]
        self.driver.switch_to.window(whatsapp_page)

    @allure.step('verify url of whatsapp care page')
    def verify_whatsapp_care_page(self):
        actual_result = self.is_visible(AuthorizationLocators.WHATSAPP_PAGE_HEADER).get_attribute('src')
        assert actual_result == 'https://static.whatsapp.net/rsrc.php/v3/y7/r/DSxOAUB0raA.png'

    @allure.step('clicking to "Telegram widget element" button')
    def click_to_telegram_button_veb_lh(self):
        self.to_click(VebLifeHelpLocators.TELEGRAM_WIDGET_VEB_LH)

    @allure.step('move to new whatsapp page')
    def move_to_new_telegram_page(self):
        telegram_page = self.driver.window_handles[1]
        self.driver.switch_to.window(telegram_page)

    @allure.step('verify url of telegram care page')
    def verify_url_telegram_care_page(self):
        self.get_url('https://t.me/+79600645557')

    @allure.step('clicking to "Terms of usage" button of footer')
    def click_to_terms_of_usage_button_veb_lh(self):
        self.to_click(VebLifeHelpLocators.TERMS_OF_USAGE_VEB_LH)

    @allure.step('move to new whatsapp page')
    def move_to_new_document_page(self):
        document_page = self.driver.window_handles[1]
        self.driver.switch_to.window(document_page)

    @allure.step('clicking to "Privacy-policy" button of footer')
    def click_to_privacy_policy_button_veb_lh(self):
        self.to_click(VebLifeHelpLocators.PRIVACY_POLICY_VEB_LH)

    @allure.step('clicking to "Consent mailing" button of footer')
    def click_to_consent_mailing_button_veb_lh(self):
        self.to_click(VebLifeHelpLocators.CONSENT_MAILING_VEB_LH)

    @allure.step('clicking to "Consent mailing" button of footer')
    def click_order_20min_session_button_veb_lh(self):
        self.to_click(VebLifeHelpLocators.ORDER_20_MIN_SESSION_VEB_LH)

    @allure.step('set name Aygul-test in the form for 20min session request')
    def set_name_20min_order_veb_lh(self):
        self.set_value(VebLifeHelpLocators.NAME_20MIN_ORDER_VEB_LH, 'Aygul-test')

    @allure.step('set phone in the form for 20min session request')
    def set_phone_20min_order_veb_lh(self):
        self.set_value(VebLifeHelpLocators.PHONE_20MIN_ORDER_VEB_LH, '89274197879')

    @allure.step('clicking to "Consent mailing" button of footer')
    def click_send_order_20min_session_button_veb_lh(self):
        self.to_click(VebLifeHelpLocators.SEND_20MIN_ORDER_VEB_LH)

    @allure.step('verify successful sending of the request to order 20min session ')
    def verify_successful_send_request_20min_session_veb_lh(self):
        actual_result = self.get_text_title_of_element(VebLifeHelpLocators.SUCCESSFUL_ANSWER_SEND_ORDER_20MIN_VEB_LH)
        assert 'Ваша заявка отправлена.' in actual_result

    # @allure.step('verify successful sending of the request to order 20min session ')
    # def verify_presence_utm_url_veb_lh(self):
    #     actual_result = self.get_url('https://life-help.ru/auth/?utm_source=veb.life-help.pro&utm_medium=&utm_'
    #                                  'campaign=&utm_content=&utm_term=%C2%A0').text
    #     assert 'utm_content' in actual_result
