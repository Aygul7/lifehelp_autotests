import allure
import pytest
from pages.user_account_page import UserAccountPage
from pages.authorization_page import AuthorizationPage
from locators.authorization_locators import AuthorizationLocators




# 1 - Проверка сообщения "Ваши данные сохранены" при клике "Сохранить изменения" в лк клиента-Личные данные
def test_successful_msg_data_saved_client_personal_account(authorization_page, user_account_page):
    authorization_page.login_user_email_password()
    user_account_page.click_to_personal_information_menu()
    user_account_page.scroll_to_button_save_changes()
    user_account_page.click_to_button_save_changes()
    user_account_page.verify_message_your_data_is_saved()

# 2 - Проверяем, что клиент в лк-Личные данные может указать имя
def test_set_client_name(authorization_page, user_account_page):
    authorization_page.login_user_email_password()
    user_account_page.click_to_personal_information_menu()
    user_account_page.delete_client_name()
    user_account_page.set_client_name()
    user_account_page.scroll_to_button_save_changes()
    user_account_page.click_to_button_save_changes()
    user_account_page.refresh_page()
    user_account_page.verify_client_name()

# 3 - Проверяем, что клиент в лк-Личные данные может указать возраст
def test_set_client_age(authorization_page, user_account_page):
    authorization_page.login_user_email_password()
    user_account_page.click_to_personal_information_menu()
    user_account_page.delete_client_age()
    user_account_page.set_client_age()
    user_account_page.scroll_to_button_save_changes()
    user_account_page.click_to_button_save_changes()
    user_account_page.refresh_page()
    user_account_page.verify_client_age()

# 4 - Проверка - клиенту без email в лк-Личные данные отображается сообщение "Заполните электронную почту и сохраните
# изменения"
def test_message_client_without_email(authorization_page, user_account_page):
    authorization_page.login_user_phone_password()
    user_account_page.click_to_personal_information_menu()
    user_account_page.delete_client_email()
    user_account_page.scroll_to_button_save_changes()
    user_account_page.click_to_button_save_changes()
    user_account_page.refresh_page()
    user_account_page.verify_message_set_email()

# 5 - Проверка - клиент может поменять флаг в поле телефон в лк - Личные данные
def test_change_phone_code_client_account(authorization_page, user_account_page):
    authorization_page.login_user_phone_password()
    user_account_page.click_to_personal_information_menu()
    user_account_page.click_to_flag_phone_field()
    user_account_page.click_to_belarus_flag_phone_field()
    user_account_page.scroll_to_button_save_changes()
    user_account_page.click_to_button_save_changes()
    user_account_page.refresh_page()
    user_account_page.verify_belarus_code_phone_field()

# 6 - Проверка - появляется сообщение об ошибке "Неправильный номер" при подставлении белорусского флага в поле телефон
# с рос.номером в лк - Личные данные
def test_error_message_rus_phone_belarus_code_client_account(authorization_page, user_account_page):
    authorization_page.login_user_phone_password()
    user_account_page.click_to_personal_information_menu()
    user_account_page.click_to_flag_phone_field()
    user_account_page.click_to_belarus_flag_phone_field()
    user_account_page.click_outside_fields_user_personal_data()
    user_account_page.verify_error_message_rus_phone_bel_code()

# 7 - Проверка "глазика" в поле "Пароль" - скрытые значения открываются (лк клиента - Личные данные)
def test_view_password_client_personal_data(authorization_page, user_account_page):
    authorization_page.login_user_phone_password()
    user_account_page.click_to_personal_information_menu()
    user_account_page.set_password_client_personal_data()
    user_account_page.verify_hidden_type_password_field()
    user_account_page.click_to_view_password_button_client_account()
    user_account_page.verify_viewed_type_password_field()

# 8 - Проверка повторного клика на "глазик" в поле "Пароль" - скрываются введенные значения (лк клиента - Личные данные)
def test_hide_password_client_personal_data(authorization_page, user_account_page):
    authorization_page.login_user_phone_password()
    user_account_page.click_to_personal_information_menu()
    user_account_page.set_password_client_personal_data()
    user_account_page.click_to_view_password_button_client_account()
    user_account_page.click_to_hide_password_button_client_account()
    user_account_page.verify_hidden_type_password_field()

# 9 - Проверка при клике на знак вопроса в поле "Новый пароль" открываются требования к паролю
# (лк клиента - Личные данные)
def test_open_password_requirements_information_client_personal_data(authorization_page, user_account_page):
    authorization_page.login_user_phone_password()
    user_account_page.click_to_personal_information_menu()
    user_account_page.click_to_information_btn_password_client_account()
    user_account_page.verify_demands_to_password()

# 10 - Проверка "глазика" в поле "Повторите пароль" - скрытые значения открываются (лк клиента - Личные данные)
def test_view_repeat_password_client_personal_data(authorization_page, user_account_page):
    authorization_page.login_user_phone_password()
    user_account_page.click_to_personal_information_menu()
    user_account_page.set_repeat_password_client_personal_data()
    user_account_page.verify_hidden_type_repeat_password_field()
    user_account_page.click_to_view_repeat_password_button_client_account()
    user_account_page.verify_viewed_type_repeat_password_field()

# 11 - Проверка повторного клика на "глазик" в поле "Повторите пароль" - скрываются введенные значения (лк клиента - Личные данные)
def test_hide_repeat_password_client_personal_data(authorization_page, user_account_page):
    authorization_page.login_user_phone_password()
    user_account_page.click_to_personal_information_menu()
    user_account_page.set_repeat_password_client_personal_data()
    user_account_page.click_to_view_repeat_password_button_client_account()
    user_account_page.click_to_hide_repeat_password_button_client_account()
    user_account_page.verify_hidden_type_repeat_password_field()

# 12 - Проверка при клике на знак вопроса в поле "Повторите пароль" открываются требования к паролю
# (лк клиента - Личные данные)
def test_repeat_password_information_client_personal_data(authorization_page, user_account_page):
    authorization_page.login_user_phone_password()
    user_account_page.click_to_personal_information_menu()
    user_account_page.click_to_information_btn_repeat_password_client_account()
    user_account_page.verify_demands_to_repeat_password()

# 13 - Проверяем, что клиент в лк-Личные данные может указать почту
def test_set_client_email(authorization_page, user_account_page):
    authorization_page.login_user_phone_password()
    user_account_page.click_to_personal_information_menu()
    user_account_page.delete_client_email()
    user_account_page.set_client_email()
    user_account_page.scroll_to_button_save_changes()
    user_account_page.click_to_button_save_changes()
    user_account_page.refresh_page()
    user_account_page.verify_client_email()

# 14 - Проверяем, что клиент без email при вводе нового пароля в лк-Личные данные появляется сообщение
# "Введите правильный адрес электронной почты"
def test_set_new_password_user_wo_email(authorization_page, user_account_page):
    authorization_page.login_user_phone_password()
    user_account_page.click_to_personal_information_menu()
    user_account_page.delete_client_email()
    user_account_page.set_password_client_personal_data()
    user_account_page.set_repeat_password_client_personal_data()
    user_account_page.scroll_to_button_save_changes()
    user_account_page.click_to_button_save_changes()
    user_account_page.verify_error_set_your_email_message()


# 15,16,17 - Проверяем валидацию длины и совпадение введенных значений нового пароля в лк клиента - Личные данные
# 15 - короткий пароль (4 символа - 'pass')
# 16- длинный пароль (20 символов - 'password1@password1@')
# 17 - пароли не совпадают
case_1 = ['pass', 'pass', 'Это значение должно содержать от 8 до 16 символов.']
case_2 = ['password1@password1@', 'password1@password1@', 'Это значение должно содержать от 8 до 16 символов.']
case_3 = ['lifehelp1@', 'password1@', 'Это значение должно совпадать.']

@pytest.mark.parametrize('first, second, third', (case_1, case_2, case_3),
                             ids=['short_password', 'long_password', 'not_matching_passwords'])

def test_error_new_password_length_user_account(authorization_page, user_account_page, first, second, third):
    authorization_page.login_user_phone_password()
    user_account_page.click_to_personal_information_menu()
    user_account_page.set_error_length_password_client_personal_data(first)
    user_account_page.set_error_length_repeat_password_client_personal_data(second)
    user_account_page.scroll_to_button_save_changes()
    user_account_page.click_to_button_save_changes()
    user_account_page.verify_error_length_password(third)


# 18,19,20,21 - Проверяем валидацию символов нового пароля в лк клиента - Личные данные
# 18 - пароль без цифр ('Пароль должен содержать цифры')
# 19 - пароль без спец. символов (''Пароль должен содержать хотя бы один из символов: !?@#$%&*'')
# 20 - пароль с буквой кириллицы ('Пароль не должен содержать буквы кириллицы')
# 21 - пароль без лат.буквы ('Пароль должен содержать хотя бы одну букву латинского алфавита')
case_1 = ['lifehelp@', 'lifehelp@', 'Пароль должен содержать цифры']
case_2 = ['lifehelp1', 'lifehelp1', 'Пароль должен содержать хотя бы один из символов: !?@#$%&*']
case_3 = ['lifehelп1@', 'lifehelп1@', 'Пароль не должен содержать буквы кириллицы']
case_4 = ['12345671@', '12345671@', 'Пароль должен содержать хотя бы одну букву латинского алфавита']

@pytest.mark.parametrize('first, second, third', (case_1, case_2, case_3, case_4),
                             ids=['missing_number_password', "missing_symbol_password", "cyrillic_password",
                                  "missing_latin_letter_password"])

def test_validation_symbols_password_fields_user_account(authorization_page, user_account_page, first, second, third):
    authorization_page.login_user_phone_password()
    user_account_page.click_to_personal_information_menu()
    user_account_page.set_password_validation(first)
    user_account_page.repeat_password_validation(second)
    user_account_page.scroll_to_button_save_changes()
    user_account_page.click_to_button_save_changes()
    user_account_page.verify_error_password_validation(third)

# 22 - Проверяем, что в лк-Личные данные после ввода почты появляется сообщение о неподтвержденной почте
def test_message_not_verified_email_client(authorization_page, user_account_page):
    authorization_page.login_user_phone_password()
    user_account_page.click_to_personal_information_menu()
    user_account_page.delete_client_email()
    user_account_page.set_client_email()
    user_account_page.scroll_to_button_save_changes()
    user_account_page.click_to_button_save_changes()
    user_account_page.refresh_page()
    user_account_page.verify_message_your_email_not_verified()

# 23 - Проверяем, что в лк-Личные данные после ввода почты и клика "Отправить письмо" появляется сообщение об успешно
# отправленного письма для подтверждения почты - скрыла шаги по установке новой почты, при обновлении страницы и
# скролле вверх кнопка "отправить письмо" не всегда полностью на экране и выходит ошибка click intercepted
def test_message_sent_verification_email_client(authorization_page, user_account_page):
    authorization_page.login_user_phone_password()
    user_account_page.click_to_personal_information_menu()
    user_account_page.click_to_send_letter_btn_not_verified_email_client_account()
    user_account_page.verify_message_msg_successful_sent_letter_to_your_email()

# 24 - Проверка отображения Имени Отчества психолога в лк клиента "Мое расписание"
def test_doctor_name_client_my_schedule(authorization_page, user_account_page):
    authorization_page.login_user_phone_password()
    user_account_page.verify_doctor_name_user_account()


# 25 - Проверка отображения Имени Отчества психолога в лк клиента "Чат с психологом"
def test_doctor_name_client_chat_w_psychologist(authorization_page, user_account_page):
    authorization_page.login_user_phone_password()
    authorization_page.move_to_chat_w_psychologist()
    user_account_page.verify_doctor_name_user_chat_account()

# 26 - Проверка отображения Имени Отчества психолога в лк клиента "Закрытые сессии"
def test_doctor_name_client_terminated_sessions(authorization_page, user_account_page):
    authorization_page.login_user_phone_password()
    authorization_page.click_terminated_sessions_title()
    user_account_page.verify_doctor_name_user_terminated_session()

# 27 - Проверка появления модального окна для ввода кода сертификата при клике "активировать сертификат"
# в лк клиента - Мое расписание
def test_click_activate_certificate_opens_modal_page_my_schedule(authorization_page, user_account_page):
    authorization_page.login_user_phone_password()
    user_account_page.click_to_activate_certificate_btn_my_schedule()
    user_account_page.verify_modal_title_activate_certificate()

# 28 - Проверка отображения Имени Отчества психолога в лк клиента "Истории платежей"
def test_doctor_name_client_payment_history(authorization_page, user_account_page):
    authorization_page.login_user_phone_password()
    authorization_page.click_my_balance_menu_navigation()
    user_account_page.click_to_payment_history_btn_my_balance()
    user_account_page.verify_doctor_name_payment_history()

# 29 - Проверка отображения Имени Отчества психолога в лк клиента "Истории платежей"
def test_doctor_name_client_regular_sessions_page(authorization_page, user_account_page):
    authorization_page.login_user_phone_password()
    authorization_page.click_to_three_dots_button_ordered_session()
    authorization_page.click_regular_session_order_dropdown_menu_list()
    user_account_page.verify_doctor_name_regular_sessions_page()

# 30 (46) - проверка создания цели в лк клиента
def test_create_aim_client(authorization_page):
    authorization_page.login_user_email_password()
    authorization_page.click_aims_menu_client()
    authorization_page.click_personal_aims_menu_client()
    authorization_page.click_add_new_aim_button_client()
    authorization_page.type_aim_name_create_client()
    authorization_page.type_aim_description_create_client()
    authorization_page.set_start_day_aim_button_client()
    authorization_page.set_end_day_aim_button_client()
    authorization_page.click_create_new_aim_button_client()
    authorization_page.verify_created_aim_in_client_account()

