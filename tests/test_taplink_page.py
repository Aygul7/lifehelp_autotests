import allure
import pytest

from locators.taplink_locators import TaplinkLocators

# 1 - Проверка, клик на кнопку "Записаться к психологу" ведет на главную страницу ленда veb.life-help.pro
def test_create_order_btn_leads_veb_lh_page_taplink(taplink_page):
    taplink_page.click_to_create_order_btn_taplink()
    taplink_page.get_url('https://lifehelp.pro/?roistat=Instagram_smm+LifeHelp_Taplink&utm_campaign=smm+LifeHelp&utm_'
                         'content=Taplink&utm_source=Instagram&utm_medium=Taplink')

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

# 8 - Проверка, клик на кнопку "Записаться на бесплатную диагностику" ведет на страницу
# https://lifehelp.pro/20mins?roistat=Instagram_smm+LifeHelp_Taplink_20min&utm_campaign=smm+LifeHelp&utm_content=
# 20min&utm_source=Instagram&utm_medium=Taplink
def test_btn_free_diagnostik_moves_to_lhpro_page(taplink_page):
    taplink_page.click_to_free_daignostik_btn_taplink()
    taplink_page.verify_url_lifehelp_pro_page()
