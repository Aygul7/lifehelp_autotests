from base.base_object import BaseObject
from locators.taplink_locators import TaplinkLocators
from locators.authorization_locators import AuthorizationLocators
import allure
from support.assertions import Assertions




class TaplinkPage(BaseObject):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('click to "create an order" btn')
    def click_to_create_order_btn_taplink(self):
        self.to_click(TaplinkLocators.CREATE_ORDER_SESSION_BTN)

    @allure.step('click to "parental burnout test" btn taplink page')
    def click_to_take_test_parental_burnout_taplink(self):
        self.to_click(TaplinkLocators.PARENTAL_BURNOUT_BTN_TEST)

    @allure.step('verify mrqz test page "parental burnout"')
    def verify_mrqz_page_parental_burnout(self):
        actual_result = self.get_text_title_of_element(TaplinkLocators.TAKE_TEST_PARENTAL_BURNOUT_BTN_MRQZ)
        assert actual_result == 'Пройти тест на выгорание'

    @allure.step('click to "codependency test" btn taplink page')
    def click_to_codependency_test_btn_taplink(self):
        self.to_click(TaplinkLocators.CODEPENDENCY_BTN_TEST_TAPLINK)

    @allure.step('verify mrqz test page "codependency"')
    def verify_mrqz_page_codependency(self):
        actual_result = self.get_text_title_of_element(TaplinkLocators.TAKE_CODEPENDENCY_TEST_BTN_MRQZ)
        assert actual_result == 'Тест на созависимость «Я не могу без тебя»'

    @allure.step('click to "selfestimation test" btn taplink page')
    def click_to_selfestimation_test_btn_taplink(self):
        self.to_click(TaplinkLocators.SELFESTIMATION_TEST_BTN)

    @allure.step('verify mrqz test page "diffidence"')
    def verify_mrqz_page_feel_diffidence(self):
        actual_result = self.get_text_title_of_element(TaplinkLocators.FEEL_DIFFIDENCE_MRQZ)
        assert actual_result == 'Чувствуешь неуверенность в себе?'

    @allure.step('click to "ask question in telegram" btn taplink page')
    def click_to_ask_question_telegram_btn_taplink(self):
        self.to_click(TaplinkLocators.ASK_QUESTION_TELEGRAM)

    @allure.step('verify url of telegram care page')
    def verify_url_telegram_care_page(self):
        self.get_url('https://t.me/+79600645557?tpclid=facebook.PAAabbNtUe7s7U-9lF4ZdkavdAN4ryIbWyZEIi'
                                  '9sAtHUZn8dwG-RzN0rtcFmg')

    @allure.step('click to "ask question in whatsapp" btn taplink page')
    def click_to_ask_question_whatsapp_btn_taplink(self):
        self.to_click(TaplinkLocators.ASK_QUESTION_WHATSAPP)

    @allure.step('verify url of whatsapp care page')
    def verify_whatsapp_care_page(self):
        actual_result = self.is_visible(AuthorizationLocators.WHATSAPP_PAGE_HEADER).get_attribute('src')
        assert actual_result == 'https://static.whatsapp.net/rsrc.php/v3/y7/r/DSxOAUB0raA.png'

    @allure.step('click to "become a psychologists team member" btn taplink page')
    def click_to_become_team_psychologists_member_btn_taplink(self):
        self.to_click(TaplinkLocators.TO_BECOME_PSYCHOLOGISTS_TEAM_MEMBER)

    @allure.step('verify url of psychologists questionnaire page')
    def verify_url_psychologists_questionnaire_page(self):
        self.get_url('https://docs.google.com/forms/d/e/1FAIpQLSenANZG0ddW6iTI-ZSd65ztBdCWSKYKPrRBQjYIJ49kDBofcA'
                     '/viewform')

    @allure.step('click to "get free consultation after questionnaire" btn taplink page')
    def click_to_get_free_consultation_button_taplink(self):
        self.to_click(TaplinkLocators.GET_FREE_CONSULTATION_BUTTON)

    @allure.step('verify url of questionnaire page')
    def verify_url_questionnaire_page(self):
        self.get_url('https://life-help-anketa.mrqz.me/?roistat=Instagram_smm%20LifeHelp_marquiz_anketa&utm_campaign'
                     '=smm%20LifeHelp&utm_medium=marquiz_anketa%3D&utm_source=Instagram&tpclid=facebook.PAAabbNtUe7s7U'
                     '-9lF4ZdkavdAN4ryIbWyZEIi9sAtHUZn8dwG-RzN0rtcFmg')