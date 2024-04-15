import allure
import pytest
from pages.veb_life_help_page import VebLhPage
from locators.veb_life_help_locators import VebLifeHelpLocators
from locators.authorization_locators import AuthorizationLocators


# 1 - проверка перехода на страницу авторизации по клику на кнопку "Вход" на veb.life-help.pro
def test_authorization_veb_lh(setup_veb_lh, veb_lh_page):
    veb_lh_page.click_to_login_button_veb_lh()
    veb_lh_page.get_url('https://life-help.ru/auth/?utm_source=veb.life-help.pro&utm_medium=&utm_campaign=&utm_'
                        'content=&utm_term=%C2%A0')

#2 - проверка перехода на страницу авторизации по клику на кнопку "Регистрация" на veb.life-help.pro
def test_registration_veb_lh(setup_veb_lh, veb_lh_page):
    veb_lh_page.click_to_registration_button_veb_lh()
    veb_lh_page.get_url('https://life-help.ru/auth/?utm_source=veb.life-help.pro&utm_medium=&utm_campaign=&utm_'
                        'content=&utm_term=%C2%A0')

#3 - проверка перехода на страницу подарочного сертификата по клику на кнопку "Подарочный сертификат" на veb.life-help.pro
def test_present_certificate_veb_lh(setup_veb_lh, veb_lh_page):
    veb_lh_page.click_to_present_certificate_button_veb_lh()
    veb_lh_page.move_to_new_certificate_page()
    veb_lh_page.get_url('https://lifehelp.pro/gifts')

#4 - проверка перехода на страницу службы поддержки в Whatsapp по клику на виджет Whatsapp
def test_whatsapp_widget_veb_lh(setup_veb_lh, veb_lh_page):
    veb_lh_page.scroll_till_bottom_veb_lh_page()
    veb_lh_page.click_to_whatsapp_button_veb_lh()
    veb_lh_page.move_to_new_whatsapp_page()
    veb_lh_page.verify_whatsapp_care_page()

#5 - проверка перехода на страницу службы поддержки в Telegram по клику на виджет Telegram
def test_telegram_widget_veb_lh(setup_veb_lh, veb_lh_page):
    veb_lh_page.scroll_till_bottom_veb_lh_page()
    veb_lh_page.click_to_telegram_button_veb_lh()
    veb_lh_page.move_to_new_telegram_page()
    veb_lh_page.verify_url_telegram_care_page()

#6 - проверка перехода на страницу с документом "Условиями пользования"
def test_terms_of_usage_document_veb_lh(setup_veb_lh, veb_lh_page):
    veb_lh_page.scroll_till_bottom_veb_lh_page()
    veb_lh_page.click_to_terms_of_usage_button_veb_lh()
    veb_lh_page.move_to_new_document_page()
    veb_lh_page.get_url('https://life-help.ru/agreement/')

#7 - проверка перехода на страницу с документом "Политика конфиденциальности"
def test_privacy_policy_document_veb_lh(setup_veb_lh, veb_lh_page):
    veb_lh_page.scroll_till_bottom_veb_lh_page()
    veb_lh_page.click_to_privacy_policy_button_veb_lh()
    veb_lh_page.move_to_new_document_page()
    veb_lh_page.get_url('https://life-help.ru/privacy-policy/')

#8 - проверка перехода на страницу с документом "Согласие на получение информационных рассылок"
def test_consent_mailing_document_veb_lh(setup_veb_lh, veb_lh_page):
    veb_lh_page.scroll_till_bottom_veb_lh_page()
    veb_lh_page.click_to_consent_mailing_button_veb_lh()
    veb_lh_page.move_to_new_document_page()
    veb_lh_page.get_url('https://life-help.ru/consent-mailing/')

#9 - проверка отправки заявки на 20-минутку
def test_query_20_min_session_veb_lh(setup_veb_lh, veb_lh_page):
    veb_lh_page.click_order_20min_session_button_veb_lh()
    veb_lh_page.set_name_20min_order_veb_lh()
    veb_lh_page.set_phone_20min_order_veb_lh()
    veb_lh_page.click_send_order_20min_session_button_veb_lh()
    veb_lh_page.verify_successful_send_request_20min_session_veb_lh()

#10 - проверка перехода на страницу группы life-help.pro ВКонтакте по клику на виджет VK
def test_vk_button_footer_veb_lh(veb_lh_page):
    veb_lh_page.scroll_till_bottom_veb_lh_page()
    veb_lh_page.click_to_vk_button_veb_lh()
    veb_lh_page.move_to_new_document_page()
    veb_lh_page.get_url('https://vk.com/life_help')

#11 - проверка перехода на страницу группы life-help.pro Telegram по клику на виджет TG
def test_telegram_group_button_footer_veb_lh(veb_lh_page):
    veb_lh_page.scroll_till_bottom_veb_lh_page()
    veb_lh_page.click_to_telegram_group_button_veb_lh()
    veb_lh_page.move_to_new_document_page()
    veb_lh_page.get_url('https://t.me/life_help_pro')

#12 - проверка перехода на страницу регистрации life-help.pro по клику на кнопку "Зарегистрироваться" в футере страницы
def test_register_button_footer_veb_lh(veb_lh_page):
    veb_lh_page.scroll_till_bottom_veb_lh_page()
    veb_lh_page.click_to_register_button_footer_veb_lh()
    veb_lh_page.get_url('https://life-help.ru/auth/?utm_source=veb.life-help.pro&utm_medium=&utm_campaign=&utm_content'
                        '=&utm_term=%C2%A0')

#13 - проверка перехода на страницу с документом "Договор оферты"
def test_oferta_document_veb_lh(setup_veb_lh, veb_lh_page):
    veb_lh_page.scroll_till_bottom_veb_lh_page()
    veb_lh_page.click_to_oferta_button_veb_lh()
    veb_lh_page.move_to_new_document_page()
    veb_lh_page.get_url('https://life-help.ru/contract-offer/')



