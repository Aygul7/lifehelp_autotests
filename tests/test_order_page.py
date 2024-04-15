import allure
import pytest
from selenium.webdriver.common.by import By

from pages.authorization_page import AuthorizationPage
from pages.order_page import OrderPage
from locators.authorization_locators import AuthorizationLocators
from locators.order_page_locators import OrderPageLocators



one_session_btn = (By.CSS_SELECTOR, "label[for='quantity-1'] span")
four_sessions_btn = (By.CSS_SELECTOR, "label[for='quantity-4'] span")
eight_sessions_btn = (By.CSS_SELECTOR, "label[for='quantity-8'] span")
twelve_sessions_btn = (By.CSS_SELECTOR, "label[for='quantity-12'] span")
fifty_four_sessions_btn = (By.CSS_SELECTOR, "label[for='quantity-54']")

case_1 = [one_session_btn, '2 950']
case_2 = [four_sessions_btn, '10 800']
case_3 = [eight_sessions_btn, '20 800']
case_4 = [twelve_sessions_btn, '28 800']


@pytest.mark.parametrize('first, second', (case_1, case_2, case_3, case_4),
                             ids=['price of single session', 'price of 4 sessions',
                                  'price of 8 sessions', 'price of 12 sessions'])

# 1-4 - Проверка стоимости 1,4,8,12 сеансов в рублях на кнопке "Оплатить" на странице заказа
def test_price_in_rubbles_on_orange_order_page(authorization_page, order_page, first, second):
    authorization_page.login_user_phone_password()
    authorization_page.click_to_pay_btn_order_my_schedule_page()
    order_page.click_to_number_sessions_btn_order_page_fixture(first)
    order_page.verify_price_pay_btn_order_page_fixture(second)

# 5 - Проверка валюты "Рубли" на кнопке "Оплатить" на странице заказа (оплата картой РФ)
def test_rubbles_currency_on_order_page(authorization_page, order_page):
    authorization_page.login_user_phone_password()
    authorization_page.click_terminated_sessions_title()
    authorization_page.click_order_session_again_button()
    authorization_page.select_2nd_time_session_rapid_schedule_psychologist()
    authorization_page.click_rapid_go_payment_btn()
    order_page.verify_currency_rubbles_order_page()


# 6-9 - Проверка стоимости 1,4,8,12 сеансов в долларах на кнопке "Оплатить" на странице заказа
case_1 = [one_session_btn, '40']
case_2 = [four_sessions_btn, '145']
case_3 = [eight_sessions_btn, '279']
case_4 = [twelve_sessions_btn, '386']

@pytest.mark.parametrize('first, second', (case_1, case_2, case_3, case_4),
                             ids=['price of single session', 'price of 4 sessions',
                                  'price of 8 sessions', 'price of 12 sessions'])

def test_price_in_dollars_on_orange_order_page(authorization_page, order_page, first, second):
    authorization_page.login_user_phone_password()
    authorization_page.click_to_pay_btn_order_my_schedule_page()
    authorization_page.click_foreign_card_button()
    order_page.click_to_btn_usd_payment_order_page()
    order_page.click_to_number_sessions_btn_order_page_fixture(first)
    order_page.verify_price_pay_btn_order_page_fixture(second)


# 10-13 - Проверка стоимости 1,4,8,12 сеансов в евро на кнопке "Оплатить" на странице заказа
case_1 = [one_session_btn, '36']
case_2 = [four_sessions_btn, '131']
case_3 = [eight_sessions_btn, '252']
case_4 = [twelve_sessions_btn, '349']

@pytest.mark.parametrize('first, second', (case_1, case_2, case_3, case_4),
                             ids=['price of single session', 'price of 4 sessions',
                                  'price of 8 sessions', 'price of 12 sessions'])

def test_price_in_euro_on_orange_order_page(authorization_page, order_page, first, second):
    authorization_page.login_user_phone_password()
    authorization_page.click_to_pay_btn_order_my_schedule_page()
    authorization_page.click_foreign_card_button()
    order_page.click_to_btn_euro_payment_order_page()
    order_page.click_to_number_sessions_btn_order_page_fixture(first)
    order_page.verify_price_pay_btn_order_page_fixture(second)

# 14-17 - Проверка описания пакетов на странице заказа
case_1 = [four_sessions_btn, 'Пакет на 4 консультации – самый популярный у клиентов Life Help. Регулярность повышает '
                             'эффективность психотерапии. Если вы ходите к психологу каждую неделю, пакета хватит '
                             'на месяц.']
case_2 = [eight_sessions_btn, '53% клиентов чувствуют существенные изменения после 8 встреч с психологом. Приобретайте '
                              'пакет консультаций: его хватит на 2 месяца еженедельной психотерапии.']
case_3 = [twelve_sessions_btn, 'Эффект от 12-15 консультаций с психологом сравним с 2 годами самостоятельной работы '
                               'над собой. Приобретайте пакет консультаций: его хватит на 3 месяца '
                               'еженедельной психотерапии.']
case_4 = [fifty_four_sessions_btn, 'Если вам нужны глубокие устойчивые изменения или постоянная поддержка психолога, '
                                   'приобретайте пакет на 54 консультации в рассрочку. Ежемесячный платеж составит '
                                   'от 10 416₽, а экономия – 34 300₽. Консультации из пакета можно распределить между '
                                   'ближайшими родственниками.']

@pytest.mark.parametrize('first, second', (case_1, case_2, case_3, case_4),
                             ids=['description of package 4', 'description of package 8',
                                  'description of package 12', 'description of package 54'])

def test_package_description_text_on_orange_order_page(authorization_page, order_page, first, second):
    authorization_page.login_user_phone_password()
    authorization_page.click_to_pay_btn_order_my_schedule_page()
    order_page.click_to_number_sessions_btn_order_page_fixture(first)
    order_page.verify_package_description_text_order_page_fixture(second)


# 18-21 - Проверка стоимости единичной консультации в руб в пакетах 4,8,12,54
case_1 = [four_sessions_btn, '2 700']
case_2 = [eight_sessions_btn, '2 600']
case_3 = [twelve_sessions_btn, '2 400']
case_4 = [fifty_four_sessions_btn, '2 315']

@pytest.mark.parametrize('first, second', (case_1, case_2, case_3, case_4),
                             ids=['session price in package 4', 'session price in package 8',
                                  'session price in package 12', 'session price in package 54'])

def test_separate_session_rub_price_package_order_page(authorization_page, order_page, first, second):
    authorization_page.login_user_phone_password()
    authorization_page.click_to_pay_btn_order_my_schedule_page()
    order_page.click_to_number_sessions_btn_order_page_fixture(first)
    order_page.verify_separate_session_price_package_order_page_fixture(second)

# 22-24 - Проверка стоимости единичной консультации в $ в пакетах 4,8,12
case_1 = [four_sessions_btn, '36']
case_2 = [eight_sessions_btn, '35']
case_3 = [twelve_sessions_btn, '32']

@pytest.mark.parametrize('first, second', (case_1, case_2, case_3),
                             ids=['session price in package 4', 'session price in package 8',
                                  'session price in package 12'])

def test_separate_session_usd_price_package_order_page(authorization_page, order_page, first, second):
    authorization_page.login_user_phone_password()
    authorization_page.click_to_pay_btn_order_my_schedule_page()
    authorization_page.click_foreign_card_button()
    order_page.click_to_btn_usd_payment_order_page()
    order_page.click_to_number_sessions_btn_order_page_fixture(first)
    order_page.verify_separate_session_usd_price_package_order_page_fixture(second)

# 25-27 - Проверка стоимости единичной консультации в евро в пакетах 4,8,12
case_1 = [four_sessions_btn, '33']
case_2 = [eight_sessions_btn, '31']
case_3 = [twelve_sessions_btn, '29']

@pytest.mark.parametrize('first, second', (case_1, case_2, case_3),
                             ids=['session price in package 4', 'session price in package 8',
                                  'session price in package 12'])

def test_separate_session_euro_price_package_order_page(authorization_page, order_page, first, second):
    authorization_page.login_user_phone_password()
    authorization_page.click_to_pay_btn_order_my_schedule_page()
    authorization_page.click_foreign_card_button()
    order_page.click_to_btn_euro_payment_order_page()
    order_page.click_to_number_sessions_btn_order_page_fixture(first)
    order_page.verify_separate_session_euro_price_package_order_page_fixture(second)


# 28 (119) - Проверка стоимости пакета 54 на кнопке "Оплатить" на странице заказа
def test_price_package_54_on_orange_order_page(authorization_page, order_page):
    authorization_page.login_user_phone_password()
    authorization_page.click_to_pay_btn_order_my_schedule_page()
    order_page.click_to_btn_package_54_order_page()
    order_page.click_to_btn_one_time_payment_package_54_order_page()
    order_page.verify_price_125000_rubbles_package_54_order_page()

# 29 (120) - Проверка валюты "$" на кнопке "Оплатить" на странице заказа (оплата иностранной картой)
def test_usd_currency_single_session_on_order_page(authorization_page, order_page):
    authorization_page.login_user_phone_password()
    authorization_page.click_to_pay_btn_order_my_schedule_page()
    authorization_page.click_foreign_card_button()
    order_page.click_to_btn_usd_payment_order_page()
    order_page.verify_currency_usd_order_page()

# 30 (121) - Проверка валюты "Euro" на кнопке "Оплатить" на странице заказа (оплата иностранной картой)
def test_euro_currency_single_session_on_order_page(authorization_page, order_page):
    authorization_page.login_user_phone_password()
    authorization_page.click_to_pay_btn_order_my_schedule_page()
    authorization_page.click_foreign_card_button()
    order_page.click_to_btn_euro_payment_order_page()
    order_page.verify_currency_euro_order_page()

# 31 (121) - Проверка перехода в профиль психолога по клику на его имя на странице заказа
def test_move_to_psychologist_profile_from_order_page(authorization_page, order_page):
    authorization_page.login_user_phone_password()
    authorization_page.click_to_pay_btn_order_my_schedule_page()
    order_page.click_to_psychologist_profile_order_page()
    order_page.get_url('https://life-help.ru/link-to-psychologist/136')

# 32 - Проверка - клик по кнопке "Написать в поддержку" ведет на чат Tg в соседней вкладке
def test_support_btn_tlg_new_page_on_order_page(authorization_page, order_page):
    authorization_page.login_user_phone_password()
    authorization_page.click_to_pay_btn_order_my_schedule_page()
    order_page.click_to_support_btn_order_page()
    order_page.move_to_new_page()
    order_page.verify_url_telegram_care_page()

