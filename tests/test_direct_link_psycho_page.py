import allure
import time
from locators.psychologist_page_locators import PsychologistPageLocators
from pages.direct_psychologist_page import PsychologistPage

#1 - проверяем, что страница психолога Елены Калкан открывается (не 404 ошибка)
def test_direct_link_to_psychologist(setup_direct_link, direct_psychologist_page):
    direct_psychologist_page.verify_psy_page_title()

#2- проверяем соответствие первого слота для быстрой записи и первого слота в расписании
def test_equal_rapid_first_order_time(setup_direct_link, direct_psychologist_page):
    direct_psychologist_page.verify_rapid_first_order_time()

# 3 - Проверка, что по клику на изображение психолога открывается его видео:
def test_video_psychologist(setup_direct_link, direct_psychologist_page):
    direct_psychologist_page.click_to_psychologist_video()
    direct_psychologist_page.verify_video_frame_psychologist_page()

#4 - проверка стоимости инд50 консультаци "2950.00 ₽" на карточке психолога по прямой ссылке
def test_price_2950_psychologist_page(setup_direct_link, direct_psychologist_page):
    direct_psychologist_page.verify_session_price_2950_rubbles_psychologist_page()

#5 - проверка стоимости инд90 консультаци "4200.00 ₽" на карточке психолога по прямой ссылке
def test_price_4200_psychologist_page(setup_direct_link, direct_psychologist_page):
    direct_psychologist_page.verify_session_price_4200_rubbles_psychologist_page()

#6 - проверка стоимости парной консультаци "4850.00 ₽" на карточке психолога по прямой ссылке
def test_price_4850_psychologist_page(setup_direct_link, direct_psychologist_page):
    direct_psychologist_page.verify_session_price_4850_rubbles_psychologist_page()

#7 - проверка Имени Отчества психолога на карточке психолога по прямой ссылке
def test_name_psychologist_page(setup_direct_link, direct_psychologist_page):
    direct_psychologist_page.verify_doctor_name_user_terminated_session()

