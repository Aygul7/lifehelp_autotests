from base.base_object import BaseObject
from locators.index_page_locators import IndexLocators
import allure
from support.assertions import Assertions




class IndexPage(BaseObject, Assertions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('accept cookies')
    def click_to_accept_cookies(self):
        self.to_click(IndexLocators.COOKIE_BUTTON)

    @allure.step('click to "get psychologist" button')
    def click_get_psychologist_btn(self):
        self.to_click(IndexLocators.GET_PSYCHOLOGIST_BUTTON)

    @allure.step('verify url of questionnaire first page')
    def verify_url_get_psychologist_page(self):
        self.get_url('https://life-help.ru/questionnaire/general/')

    @allure.step('clicking to "Login" button')
    def click_to_login_button(self):
        self.to_click(IndexLocators.LOGIN_BUTTON)

    @allure.step('verify url of authorization page')
    def verify_url_authorization_page(self):
        self.get_url('https://life-help.ru/auth/')

    @allure.step('click to "telegram" logo button in main page care block')
    def click_to_telegram_care_button(self):
        self.to_click(IndexLocators.TELEGRAM_CARE_LOGO)

    @allure.step('move to new telegram care page')
    def move_to_new_telegram_care_page(self):
        telegram_care_page = self.driver.window_handles[1]
        self.driver.switch_to.window(telegram_care_page)

    @allure.step('verify url of telegram care page')
    def verify_url_telegram_care_page(self):
        self.get_url('https://t.me/+79600645557')

    @allure.step('click to "whatsapp" logo button in main page care block')
    def click_to_whatsapp_care_button(self):
        self.to_click(IndexLocators.WHATSAPP_CARE_LOGO)

    @allure.step('move to new whatsapp care page')
    def move_to_new_whatsapp_care_page(self):
        whatsapp_care_page = self.driver.window_handles[1]
        self.driver.switch_to.window(whatsapp_care_page)

    @allure.step('verify url of whatsapp care page')
    def verify_whatsapp_care_page(self):
        actual_result = self.is_visible(IndexLocators.WHATSAPP_PAGE_HEADER).get_attribute('src')
        assert actual_result == 'https://static.whatsapp.net/rsrc.php/v3/y7/r/DSxOAUB0raA.png'

    @allure.step('click to help phone call by Skype')
    def click_phone_number_skype_button(self):
        self.to_click(IndexLocators.SKYPE_PHONE_NUMBER_HELP_MAIN_PAGE)

    @allure.step('click to help phone call by Skype')
    def click_vk_group_widget_footer(self):
        self.to_click(IndexLocators.VK_GROUP_FOOTER_WIDGET)

    @allure.step('scroll to bottom on psychologyst schedule page')
    def scroll_till_bottom_psychologyst_schedule(self):
        self.move_to_page_bottom()

    @allure.step('verify client name "Aygul-test"')
    def verify_price_2950(self):
        actual_result = self.get_text_title_of_element(IndexLocators.PAY_2990_PRICE)
        assert '2950' in actual_result

