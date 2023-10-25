import allure
import pytest


# 1 - Проверка, что успешного восстановления пароля - сообщение"Вы успешно установили новый пароль!"
def test_successful_restore_password_page(restore_password_link_page):
    restore_password_link_page.set_new_password()
    restore_password_link_page.repeat_new_password()
    restore_password_link_page.click_to_save_btn_restore_password()
    restore_password_link_page.verify_message_successful_password_restore()

# 2 - Проверка, что ссылка для восстановления пароля ведет на страницу обновления пароля
def test_correct_restore_password_page(restore_password_link_page):
    restore_password_link_page.verify_page_restore_password()

#3 - Проверка, что при попытке обновить пароль по ссылке с недействительным токеном появляется сообщение об ошибке
# "Токен для обновления пароля недействителен"
def test_set_new_password(restore_password_link_page):
    restore_password_link_page.set_new_password()
    restore_password_link_page.repeat_new_password()
    restore_password_link_page.click_to_save_btn_restore_password()
    restore_password_link_page.verify_invalid_token_error_message()

#4 - Проверка, что при переходе по ссылке в сообщении об ошибке "Токен для обновления пароля недействителен"
# пользователь переходит на страницу https://life-help.ru/forgot/
def test_link_leads_to_forgot_password_page(restore_password_link_page):
    restore_password_link_page.set_new_password()
    restore_password_link_page.repeat_new_password()
    restore_password_link_page.click_to_save_btn_restore_password()
    restore_password_link_page.click_to_link_btn_password_error_message()
    restore_password_link_page.verify_url_forgot_password_page()

# 5, 6, 7, 8,9 - проверка валидации полей ввода нового пароля и повтора пароля в форме восстановления пароля
case_1 = ['lifehelp1@', 'password1@', 'Введенные пароли не совпадают']
case_2 = ['lifehelp@', 'lifehelp@', 'Пароль должен содержать цифры']
case_3 = ['lifehelp1', 'lifehelp1', 'Пароль должен содержать хотя бы один из символов: !?@#$%&*']
case_4 = ['lifehelп1@', 'lifehelп1@', 'Пароль не должен содержать буквы кириллицы']
case_5 = ['12345671@', '12345671@', 'Пароль должен содержать хотя бы одну букву латинского алфавита']


@pytest.mark.parametrize('first, second, third', (case_1, case_2, case_3, case_4, case_5),
                             ids=['not_matching_passwords', 'missing_number_password', "missing_symbol_password",
                                  "cyrillic_password", "missing_latin_letter_password"])
def test_set_new_password_error_messages(restore_password_link_page, first, second, third):
    restore_password_link_page.set_new_password_fixture(first)
    restore_password_link_page.repeat_new_password_fixture(second)
    restore_password_link_page.click_to_save_btn_restore_password()
    restore_password_link_page.verify_error_message_restore_password_fixture(third)

# 10 - проверка "глазика" в поле "Пароль" - скрытые значения открываются в форме восстановления пароля
def test_view_password_restore_form(restore_password_link_page):
    restore_password_link_page.set_new_password()
    restore_password_link_page.repeat_new_password()
    restore_password_link_page.verify_hidden_type_password_field()

# 11 - проверка "глазика" в поле "Пароль" - скрытые значения в форме восстановления пароля
def test_hidden_password_fields_restore_form(restore_password_link_page):
    restore_password_link_page.set_new_password()
    restore_password_link_page.repeat_new_password()
    restore_password_link_page.verify_hidden_type_password_field()

# 12 - проверка "глазика" в поле "Пароль" - открываются скрытые значения в форме восстановления пароля
def test_view_password_fields_restore_form(restore_password_link_page):
    restore_password_link_page.set_new_password()
    restore_password_link_page.repeat_new_password()
    restore_password_link_page.click_to_view_password_button_restore_password_page()
    restore_password_link_page.verify_viewed_type_password_field_restore_password_page()

#13-Проверка повторного клика на "глазик" в поле "Пароль" - скрываются открытые значения в форме восстановления пароля
def test_hide_password_fields_restore_form(restore_password_link_page):
    restore_password_link_page.set_new_password()
    restore_password_link_page.repeat_new_password()
    restore_password_link_page.click_to_view_password_button_restore_password_page()
    restore_password_link_page.verify_viewed_type_password_field_restore_password_page()
    restore_password_link_page.click_to_hide_password_button_restore_password_page()
    restore_password_link_page.verify_hidden_type_password_field()

# 14 - проверка кнопка "Сохранить" неактивная без ввода данных
def test_disabled_button_save_reset_password_page_wo_both_fields(restore_password_link_page):
    restore_password_link_page.verify_disabled_type_button_save_reset_password_page()

# 15 - проверка кнопка "Сохранить" неактивная при вводе пароля в поле "Новый пароль", но без ввода данных в поле "Повторите пароль"
def test_disabled_button_save_reset_password_page_wo_repeat_field(restore_password_link_page):
    restore_password_link_page.set_new_password()
    restore_password_link_page.verify_disabled_type_button_save_reset_password_page()

# 16 - проверка кнопка "Сохранить" неактивная при вводе пароля в поле "Повторите пароль", но без ввода данных в поле "Новый пароль"
def test_disabled_button_save_reset_password_page_wo_new_pass_field(restore_password_link_page):
    restore_password_link_page.repeat_new_password()
    restore_password_link_page.verify_disabled_type_button_save_reset_password_page()

