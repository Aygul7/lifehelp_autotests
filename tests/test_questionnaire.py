import allure
import time
from pages.questionnaire_page import QuestionnairePage

# @allure.description('Questionnaire - general questions')
# @allure.label('owner', 'Aygul')
# @allure.title('Questionnaire')
# @allure.suite('Questionnaire pack')
# @allure.severity(allure.severity_level.BLOCKER)
# тест 1 - анкета - индивидуальная консультация на русском языке в формате видео
def test_questionnaire_ind_rus_video(setup_questionnaire, questionnaire_page):
    questionnaire_page.click_individual_consultation()
    questionnaire_page.click_russian_language()
    questionnaire_page.click_video_consultation()
    questionnaire_page.set_age()
    #questionnaire_page.click_next_button()
    questionnaire_page.click_personal_questions_title()
    time.sleep(5)
    # questionnaire_page.get_personal_questions_url()

def test_questionnaire_paired_tatar_audio(setup_questionnaire, questionnaire_page):
    questionnaire_page.click_paired_consultation()
    questionnaire_page.click_tatar_language()
    questionnaire_page.click_audio_consultation()
    questionnaire_page.set_age()
    questionnaire_page.click_next_button()

def test_questionnaire_ind_tatar_chat(setup_questionnaire, questionnaire_page):
    questionnaire_page.click_individual_consultation()
    questionnaire_page.click_tatar_language()
    questionnaire_page.click_chat_consultation()
    questionnaire_page.set_age()
    questionnaire_page.click_next_button()