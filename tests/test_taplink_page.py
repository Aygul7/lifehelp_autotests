import allure
import pytest

from locators.taplink_locators import TaplinkLocators

# 1 - Проверка, клик на кнопку "Записаться к психологу" ведет на главную страницу ленда veb.life-help.pro
def test_create_order_btn_leads_veb_lh_page_taplink(taplink_page):
    taplink_page.click_to_create_order_btn_taplink()
    taplink_page.get_url('https://veb.life-help.pro/?roistat=Instagram_smm+LifeHelp_Taplink&utm_campaign=smm+'
                         'LifeHelp&utm_content=Taplink&utm_source=Instagram&utm_medium=Taplink')

# 2 - Проверка, клик на кнопку "Пройти тест на родительское выгорание" ведет на страницу mrqz с тестом
def test_parental_burnout_test_btn_taplink(taplink_page):
    taplink_page.click_to_take_test_parental_burnout_taplink()
    taplink_page.verify_mrqz_page_parental_burnout()

# 3 - Проверка, клик на кнопку "Пройти тест на созависимость" ведет на страницу mrqz с тестом
def test_codependency_test_btn_taplink(taplink_page):
    taplink_page.click_to_codependency_test_btn_taplink()
    taplink_page.verify_mrqz_page_codependency()

# 4 - Проверка, клик на кнопку "Пройти тест на самооценку" ведет на страницу mrqz с тестом
def test_selfestimation_test_btn_taplink(taplink_page):
    taplink_page.click_to_selfestimation_test_btn_taplink()
    taplink_page.verify_mrqz_page_feel_diffidence()

# 5 - Проверка, клик на кнопку "Задать вопрос в Telegram" ведет на страницу cлужбы заботы в Telegram
def test_ask_question_telegram_btn_taplink(taplink_page):
    taplink_page.click_to_ask_question_telegram_btn_taplink()
    taplink_page.verify_url_telegram_care_page()

# 6 - Проверка, клик на кнопку "Задать вопрос в Whatsapp" ведет на страницу cлужбы заботы в Whatsapp
def test_ask_question_whatsapp_btn_taplink(taplink_page):
    taplink_page.click_to_ask_question_whatsapp_btn_taplink()
    taplink_page.verify_whatsapp_care_page()

# 7 - Проверка, клик на кнопку "Стать частью команды LIFE HELP" ведет на страницу google.doc анкеты для психологов
def test_btn_become_psychologists_team_member_btn_taplink(taplink_page):
    taplink_page.click_to_become_team_psychologists_member_btn_taplink()
    taplink_page.verify_url_psychologists_questionnaire_page()

# 8 - Проверка, клик на кнопку "Получить консультацию бесплатно" ведет на страницу mrqz с анкетой
def test_get_free_counsulation_questionnaire_taplink(taplink_page):
    taplink_page.click_to_get_free_consultation_button_taplink()
    taplink_page.verify_url_questionnaire_page()



    # taplink_page.get_url('https://life-help-roditel.mrqz.me/?roistat=Instagram_smm+LifeHelp_marquiz_roditel+vigoranie'
    #                      '&utm_campaign=smm+LifeHelp&utm_medium=marquiz_roditel+vigoranie=&utm_source=Instagram&tpclid'
    #                      '=facebook.PAAabbNtUe7s7U-9lF4ZdkavdAN4ryIbWyZEIi9sAtHUZn8dwG-RzN0rtcFmg')

