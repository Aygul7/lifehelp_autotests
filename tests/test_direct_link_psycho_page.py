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

#4- проверяем запись на консультацию существующего клиента
# def test_order_session_3rd_rapid_time(setup_direct_link, direct_psychologist_page):
#     direct_psychologist_page.select_3rd_time_session_rapid_schedule_psychologist()
#     direct_psychologist_page.scroll_to_rapid_payment_button()
#     direct_psychologist_page.click_rapid_go_payment_btn()
#     direct_psychologist_page.set_client_name()
#     direct_psychologist_page.set_client_phone()
#     direct_psychologist_page.set_client_email()
#     direct_psychologist_page.click_green_payment_btn()





# проверяем наличие слота времени в расписании (первый слот)
# def test_presence_order_time(setup_direct_link, direct_psychologist_page):
#     direct_psychologist_page.check_presence_first_order_time()
#
# # проверяем возможность выбрать время и кликнуть на "Перейти к оплате" с переходом на страницу заказа
# def test_order_session(setup_direct_link, direct_psychologist_page):
#     direct_psychologist_page.scroll_to_schedule()
#     direct_psychologist_page.select_rapid_order_time()

    #print(PsychologistPageLocators.RAPID_ORDER_TIME)
    # direct_psychologist_page.scroll_to_element()
    # direct_psychologist_page.click_to_move_to_payment_button()