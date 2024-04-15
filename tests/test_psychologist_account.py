import allure
import pytest
from pages.psychologist_account_page import PsychologistAccountLocators
from pages.authorization_page import AuthorizationPage
from locators.authorization_locators import AuthorizationLocators




# 1 - Проверка перехода на Инструкцию по подготовке к первой консультации из лк психолога
def test_click_btn_opens_insctruction_for_first_session_psychologist(authorization_page, psychologist_account_page):
    authorization_page.login_as_psychologist()
    psychologist_account_page.click_to_see_first_session_btn()
    psychologist_account_page.get_url('https://life-help.ru/doctor/instruction/doctor')

# 2 - Проверка перехода на расписание на неделю в лк психолога
def test_click_btn_opens_week_schedule_psychologist(authorization_page, psychologist_account_page):
    authorization_page.login_as_psychologist()
    psychologist_account_page.click_week_schedule_btn()
    psychologist_account_page.get_url('https://life-help.ru/doctor/sessions/week')

# 3 - Проверка перехода на расписание на месяц в лк психолога
def test_click_btn_opens_month_schedule_psychologist(authorization_page, psychologist_account_page):
    authorization_page.login_as_psychologist()
    psychologist_account_page.click_month_schedule_btn()
    psychologist_account_page.get_url('https://life-help.ru/doctor/sessions/month')

# 4 - Проверка добавления слота в общем расписании в лк психолога
def test_add_time_general_schedule_psychologist(authorization_page, psychologist_account_page):
    authorization_page.login_as_psychologist()
    psychologist_account_page.click_title_personal_data()
    psychologist_account_page.click_title_working_hours()
    psychologist_account_page.click_sunday_00_working_hour()
    psychologist_account_page.scroll_till_page_bottom()
    psychologist_account_page.click_save_changes()
    psychologist_account_page.scroll_till_page_top()
    psychologist_account_page.verify_checked_hour_sunday_00()

# 5 - Проверка удаления слота в общем расписании в лк психолога
def test_remove_time_general_schedule_psychologist(authorization_page, psychologist_account_page):
    authorization_page.login_as_psychologist()
    psychologist_account_page.click_title_personal_data()
    psychologist_account_page.click_title_working_hours()
    psychologist_account_page.click_sunday_00_working_hour()
    psychologist_account_page.scroll_till_page_bottom()
    psychologist_account_page.click_save_changes()
    psychologist_account_page.scroll_till_page_top()
    psychologist_account_page.verify_unselected_hour_sunday_00()

# 6,7 - Проверка указать время (пограничные сеансы), за которое клиенты могут записаться на приём - 2 и 48ч,
# в лк психолога

case_1 = ['2', '2']
case_2 = ['48', '48']


@pytest.mark.parametrize('first, second', (case_1, case_2),
                             ids=['success_2_hours', 'success_48_hours'])

def test_set_booking_time_3_hours_psychologist_schedule(authorization_page, psychologist_account_page, first, second):
    authorization_page.login_as_psychologist()
    psychologist_account_page.click_title_personal_data()
    psychologist_account_page.click_title_working_hours()
    psychologist_account_page.clear_booking_time()
    psychologist_account_page.set_valid_booking_time_psychologist_account(first)
    psychologist_account_page.click_set_exact_day_schedule()
    psychologist_account_page.verify_valid_booking_time(second)

# 8,9,10 - Проверка - нельзя указать время 1ч, за которое клиенты могут записаться на приём - в лк психолога,
# автоматически меняется на 2ч
case_1 = ['0', '2']
case_2 = ['1', '2']
case_3 = ['49', '48']


@pytest.mark.parametrize('first, second', (case_1, case_2, case_3),
                             ids=['impossible_0_hour', 'impossible_1_hour', 'impossible_49_hour'])
def test_set_invalid_booking_time_psychologist_schedule(authorization_page, psychologist_account_page, first, second):
    authorization_page.login_as_psychologist()
    psychologist_account_page.click_title_personal_data()
    psychologist_account_page.click_title_working_hours()
    psychologist_account_page.clear_booking_time()
    psychologist_account_page.set_invalid_booking_time_psychologist_account(first)
    psychologist_account_page.click_set_exact_day_schedule()
    psychologist_account_page.verify_invalid_booking_time(second)

# 11 - Проверка выбора первого слота в расписании "Настройте каждый день" в лк психолога
def test_set_first_time_exact_time_schedule_psychologist(authorization_page, psychologist_account_page):
    authorization_page.login_as_psychologist()
    psychologist_account_page.click_title_personal_data()
    psychologist_account_page.click_title_working_hours()
    psychologist_account_page.click_set_exact_day_schedule()
    psychologist_account_page.click_first_time_exact_day_schedule()
    psychologist_account_page.scroll_till_page_bottom()
    psychologist_account_page.click_save_changes_exact_day_schedule()
    psychologist_account_page.scroll_till_page_top()
    psychologist_account_page.verify_selected_first_hour_exact_day_schedule()

# 12 - Проверка удаления первого слота в расписании "Настройте каждый день" в лк психолога
def test_remove_first_time_exact_time_schedule_psychologist(authorization_page, psychologist_account_page):
    authorization_page.login_as_psychologist()
    psychologist_account_page.click_title_personal_data()
    psychologist_account_page.click_title_working_hours()
    psychologist_account_page.click_set_exact_day_schedule()
    psychologist_account_page.click_first_time_exact_day_schedule()
    psychologist_account_page.scroll_till_page_bottom()
    psychologist_account_page.click_save_changes_exact_day_schedule()
    psychologist_account_page.scroll_till_page_top()
    psychologist_account_page.verify_unselected_first_hour_exact_day_schedule()

# 13 - проверка бронирования сеанса из лк психолога
def test_psychologist_order_session(authorization_page, psychologist_account_page):
    authorization_page.login_as_psychologist()
    psychologist_account_page.click_to_clients_and_aims_menu_psychologist()
    psychologist_account_page.select_aygul_clients_and_aims_menu_psychologist()
    psychologist_account_page.click_to_three_dots_clients_and_aims_menu_psychologist()
    psychologist_account_page.click_to_create_new_session_for_clients_menu_psychologist()
    psychologist_account_page.click_to_create_button_to_create_new_session_for_clients_menu_psychologist()
    psychologist_account_page.verify_successful_creation_order_text_psychologist()

# 14 - проверка - нельзя повторно забронировать сеанса из лк психолога на занятое бронью время
def test_error_psychologist_order_occupied_time_session(authorization_page, psychologist_account_page):
    authorization_page.login_as_psychologist()
    psychologist_account_page.click_to_clients_and_aims_menu_psychologist()
    psychologist_account_page.select_aygul_clients_and_aims_menu_psychologist()
    psychologist_account_page.click_to_three_dots_clients_and_aims_menu_psychologist()
    psychologist_account_page.click_to_create_new_session_for_clients_menu_psychologist()
    psychologist_account_page.click_to_create_button_to_create_new_session_for_clients_menu_psychologist()
    psychologist_account_page.verify_error_unsuccessful_creation_order_text_psychologist()

# 15 - проверка создания цели в лк психолога
def test_create_aim_psychologist(authorization_page, psychologist_account_page):
    authorization_page.login_as_psychologist()
    psychologist_account_page.click_to_clients_and_aims_menu_psychologist()
    psychologist_account_page.select_aygul_clients_and_aims_menu_psychologist()
    psychologist_account_page.click_add_new_aim_button_psychologist()
    psychologist_account_page.type_aim_name_create_client()
    psychologist_account_page.type_aim_description_create_client()
    psychologist_account_page.set_start_day_aim_button_client()
    psychologist_account_page.set_end_day_aim_button_client()
    psychologist_account_page.click_create_new_aim_button_client()
    psychologist_account_page.verify_created_aim_in_client_account()

# 16 - проверка смена статуса цели на "В работе" из лк психолога
def test_change_aim_status_in_progress_psychologist(authorization_page, psychologist_account_page):
    authorization_page.login_as_psychologist()
    psychologist_account_page.click_to_clients_and_aims_menu_psychologist()
    psychologist_account_page.select_aygul_clients_and_aims_menu_psychologist()
    psychologist_account_page.click_aim_2_client_account()
    psychologist_account_page.click_aim_2_status_client_account()
    psychologist_account_page.select_aim_status_in_progress_client_account()
    psychologist_account_page.click_save_aim_changes_client_account()
    psychologist_account_page.verify_aim_status_in_progress_client()

# 17 - проверка смена статуса цели на "Завершена" из лк психолога
def test_change_aim_status_completed_psychologist(authorization_page, psychologist_account_page):
    authorization_page.login_as_psychologist()
    psychologist_account_page.click_to_clients_and_aims_menu_psychologist()
    psychologist_account_page.select_aygul_clients_and_aims_menu_psychologist()
    psychologist_account_page.click_aim_2_client_account()
    psychologist_account_page.click_aim_2_status_client_account()
    psychologist_account_page.select_aim_status_completed_client_account()
    psychologist_account_page.click_save_aim_changes_client_account()
    psychologist_account_page.verify_aim_status_completed_client()

# 18 - проверка смена статуса цели на "Создана" из лк психолога
def test_change_aim_status_created_psychologist(authorization_page, psychologist_account_page):
    authorization_page.login_as_psychologist()
    psychologist_account_page.click_to_clients_and_aims_menu_psychologist()
    psychologist_account_page.select_aygul_clients_and_aims_menu_psychologist()
    psychologist_account_page.click_aim_2_client_account()
    psychologist_account_page.click_aim_2_status_client_account()
    psychologist_account_page.select_aim_status_created_client_account()
    psychologist_account_page.click_save_aim_changes_client_account()
    psychologist_account_page.verify_aim_status_created_client()

# 19 - проверка удаления цели из лк психолога
def test_remove_aim_psychologist(authorization_page, psychologist_account_page):
    authorization_page.login_as_psychologist()
    psychologist_account_page.click_to_clients_and_aims_menu_psychologist()
    psychologist_account_page.select_aygul_clients_and_aims_menu_psychologist()
    psychologist_account_page.click_aim_2_client_account()
    psychologist_account_page.click_remove_aim_button_client_account()
    psychologist_account_page.verify_url_psychologist_aims_list_page()

