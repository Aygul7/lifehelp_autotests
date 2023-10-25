from base.base_object import BaseObject
from locators.questionnaire_locators import QuestionnaireLocators
import allure
from support.assertions import Assertions

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
    def set_age(self):
        self.set_value(QuestionnaireLocators.AGE_FIELD, '50')

    @allure.step('close Jivosite widget')
    def click_to_close_Jivosite_widget(self):
        self.to_click(QuestionnaireLocators.CLOSE_WIDGET_BUTTON)

    @allure.step('click to next button')
    def click_next_button(self):
        self.to_click(QuestionnaireLocators.NEXT_BUTTON)

    @allure.step('click to title "Personal questions"')
    def click_personal_questions_title(self):
        self.to_click(QuestionnaireLocators.PERSONAL_QUESTIONS_TITLE)

    @allure.step('check url')
    def get_personal_questions_url(self):
        self.get_url('https://life-help.ru/questionnaire/personal/')




