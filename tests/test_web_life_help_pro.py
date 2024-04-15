import allure
import pytest
from pages.web_life_help_page import WebLhPage
from locators.web_life_help_pro_locators import WebLifeHelpLocators
from locators.authorization_locators import AuthorizationLocators


# 1 - проверка перехода на страницу подбора психолога по клику на кнопку "Подобрать психолога" на web.life-help.pro
def test_select_doctor_web_lh(web_lh_page):
    web_lh_page.click_to_select_doctor_button_web_lh()
    web_lh_page.get_url('https://life-help.ru/questionnaire/general/')

# 2 - проверка перехода на страницу службы поддержки в Telegram по клику на виджет Telegram
def test_telegram_help_web_lh(web_lh_page):
    web_lh_page.click_to_telegram_help_web_lh()
    web_lh_page.move_to_new_telegram_page()
    web_lh_page.verify_url_telegram_care_page()

#3 - проверка перехода на страницу службы поддержки в Whatsapp по клику на виджет Whatsapp
def test_whatsapp_widget_web_lh(web_lh_page):
    web_lh_page.click_to_whatsapp_button_web_lh()
    web_lh_page.move_to_new_whatsapp_page()
    web_lh_page.verify_whatsapp_care_page()


#4 - проверка перехода на страницу с документом "Условиями пользования"
def test_terms_of_usage_document_web_lh(web_lh_page):
    web_lh_page.scroll_till_bottom_web_lh_page()
    web_lh_page.click_to_terms_of_usage_button_web_lh()
    web_lh_page.move_to_new_document_page()
    web_lh_page.get_url('https://life-help.ru/agreement/')

#5 - проверка перехода на страницу с документом "Политика конфиденциальности"
def test_privacy_policy_document_web_lh(web_lh_page):
    web_lh_page.scroll_till_bottom_web_lh_page()
    web_lh_page.click_to_privacy_policy_button_web_lh()
    web_lh_page.move_to_new_document_page()
    web_lh_page.get_url('https://life-help.ru/privacy-policy/')

#6 - проверка перехода на страницу с документом "Согласие на получение информационных рассылок"
def test_consent_mailing_document_web_lh(web_lh_page):
    web_lh_page.scroll_till_bottom_web_lh_page()
    web_lh_page.click_to_consent_mailing_button_web_lh()
    web_lh_page.move_to_new_document_page()
    web_lh_page.get_url('https://life-help.ru/consent-mailing/')

#7 - проверка перехода на страницу группы life-help.pro ВКонтакте по клику на виджет VK
def test_vk_button_footer_web_lh(web_lh_page):
    web_lh_page.scroll_till_bottom_web_lh_page()
    web_lh_page.click_to_vk_button_web_lh()
    web_lh_page.move_to_new_document_page()
    web_lh_page.get_url('https://vk.com/life_help')

#8 - проверка перехода на страницу группы life-help.pro Telegram по клику на виджет TG
def test_telegram_group_button_footer_web_lh(web_lh_page):
    web_lh_page.scroll_till_bottom_web_lh_page()
    web_lh_page.click_to_telegram_group_button_web_lh()
    web_lh_page.move_to_new_document_page()
    web_lh_page.get_url('https://t.me/life_help_pro')