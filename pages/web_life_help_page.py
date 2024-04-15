from base.base_object import BaseObject
from locators.web_life_help_pro_locators import WebLifeHelpLocators
import allure
from support.assertions import Assertions


class WebLhPage(BaseObject):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('clicking to "Login" button')
    def click_to_select_doctor_button_web_lh(self):
        self.to_click(WebLifeHelpLocators.SELECT_DOCTOR_BUTTON_WEB_LH)

    @allure.step('clicking to "Telegram" care widget')
    def click_to_telegram_help_web_lh(self):
        self.to_click(WebLifeHelpLocators.TELEGRAM_HELP_WEB_LH_PRO)

    @allure.step('move to new whatsapp page')
    def move_to_new_telegram_page(self):
        telegram_page = self.driver.window_handles[1]
        self.driver.switch_to.window(telegram_page)

    @allure.step('verify url of telegram care page')
    def verify_url_telegram_care_page(self):
        self.get_url('https://t.me/+79600645557')

    @allure.step('clicking to "Whatsapp widget element" button')
    def click_to_whatsapp_button_web_lh(self):
        self.to_click(WebLifeHelpLocators.WHATSAPP_WIDGET_WEB_LH)

    @allure.step('move to new whatsapp page')
    def move_to_new_whatsapp_page(self):
        whatsapp_page = self.driver.window_handles[1]
        self.driver.switch_to.window(whatsapp_page)

    @allure.step('verify url of whatsapp care page')
    def verify_whatsapp_care_page(self):
        actual_result = self.is_visible(WebLifeHelpLocators.WHATSAPP_PAGE_HEADER).get_attribute('src')
        assert actual_result == 'https://static.whatsapp.net/rsrc.php/v3/y7/r/DSxOAUB0raA.png'

    @allure.step('scroll to bottom on web.life-help.pro page')
    def scroll_till_bottom_web_lh_page(self):
        self.move_to_page_bottom()

    @allure.step('clicking to "Terms of usage" button of footer')
    def click_to_terms_of_usage_button_web_lh(self):
        self.to_click(WebLifeHelpLocators.TERMS_OF_USAGE_WEB_LH)

    @allure.step('move to new whatsapp page')
    def move_to_new_document_page(self):
        document_page = self.driver.window_handles[1]
        self.driver.switch_to.window(document_page)

    @allure.step('clicking to "Privacy-policy" button of footer')
    def click_to_privacy_policy_button_web_lh(self):
        self.to_click(WebLifeHelpLocators.PRIVACY_POLICY_WEB_LH)

    @allure.step('clicking to "Consent mailing" button of footer')
    def click_to_consent_mailing_button_web_lh(self):
        self.to_click(WebLifeHelpLocators.CONSENT_MAILING_WEB_LH)

    @allure.step('clicking to "VK" button of footer')
    def click_to_vk_button_web_lh(self):
        self.to_click(WebLifeHelpLocators.VK_WIDGET_WEB_LH)

    @allure.step('clicking to "Telegram" button of footer')
    def click_to_telegram_group_button_web_lh(self):
        self.to_click(WebLifeHelpLocators.TELEGRAM_GROUP_WIDGET_WEB_LH)
