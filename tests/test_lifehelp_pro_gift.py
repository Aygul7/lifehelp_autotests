import allure
import pytest
from selenium.webdriver.common.by import By
from pages.authorization_page import AuthorizationPage
from locators.authorization_locators import AuthorizationLocators




# 1- Проверка - при клике на верхнюю первую кнопку "Купить сертификат" пользователь перемещается
# к блоку "Вы можете выбрать подарок:"
def test_buy_certificate_upper_1st_btn(lifehelp_pro_gift_page):
    lifehelp_pro_gift_page.click_to_buy_certificate_upper_1st_btn()
    lifehelp_pro_gift_page.verify_title_block_you_can_select_gift()

# 2- Проверка - при клике на вторую кнопку "Купить сертификат" пользователь перемещается
# к блоку "Вы можете выбрать подарок:"
def test_buy_certificate_2nd_btn(lifehelp_pro_gift_page):
    lifehelp_pro_gift_page.click_to_buy_certificate_2nd_btn()
    lifehelp_pro_gift_page.verify_title_block_you_can_select_gift()

# 3- Проверка - при клике на кнопку "Узнать подробности" пользователь перемещается
# к блоку "Как это работает?"
def test_to_know_details_btn(lifehelp_pro_gift_page):
    lifehelp_pro_gift_page.click_to_know_details_btn()
    lifehelp_pro_gift_page.verify_title_block_how_it_works()


