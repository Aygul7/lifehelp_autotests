import allure
import pytest

from locators.index_page_locators import IndexLocators

#1 - проверка закрытия сообщения о сборе Куки (не закрывается)
def test_authorization(index_page):
    index_page.click_to_accept_cookies()

# 2 (9) - по клику на кнопку "Подобрать психолога" пользователь переходит на страницу анкеты
def test_get_pshychologist_btn(index_page):
    index_page.click_get_psychologist_btn()
    index_page.verify_url_get_psychologist_page()

# 3 (10) - по клику на кнопку "Войти" пользователь переходит на страницу авторизации
def test_login_button (index_page):
    index_page.click_to_login_button()
    index_page.verify_url_authorization_page()

#4(24) - проверка, что клик на знак Телеграмма в службе заботы открывает в соседней вкладке переписку в Тг
def test_click_opens_telegram_care_page(index_page):
    # index_page.click_to_accept_cookies()
    index_page.click_to_telegram_care_button()
    index_page.move_to_new_telegram_care_page()
    index_page.verify_url_telegram_care_page()

# 5 (25) - проверка, что клик на знак Whatsapp в службе заботы открывает в соседней вкладке переписку в Whatsapp
def test_click_opens_whatsapp_care_page(index_page):
    # index_page.click_to_accept_cookies()
    index_page.click_to_whatsapp_care_button()
    index_page.move_to_new_whatsapp_care_page()
    index_page.verify_whatsapp_care_page()

# 6 - проверка надписи с новой стоимостью на главной странице "Платите фиксированную стоимость 2950 ₽"
def test_price_2990_index_page(index_page):
    index_page.verify_price_2950()

