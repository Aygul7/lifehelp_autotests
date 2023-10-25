import allure
import pytest

# 22 - проверка пути регистрации пользователя до отправки email со ссылкой на email
def test_registration_new_user_1(registration_page):
    # authorization_page.click_to_login_button()
    # authorization_page.click_to_login_w_password_button()
    # authorization_page.click_register_hypertext()
    registration_page.set_email_registration_form()
    registration_page.set_password_registration_form()
    registration_page.repeat_password_registration_form()
    registration_page.click_first_checkbox_consent_registration_form()
    registration_page.scroll_to_register_button_registration_form()
    registration_page.click_to_register_button_registration_form()
    registration_page.verify_sent_msg_registration()

# 23 - проверка пути регистрации пользователя до отправки email со ссылкой на существующий email
def test_error_registration_registered_user_2(registration_page):
    # authorization_page.click_to_login_button()
    # authorization_page.click_to_login_w_password_button()
    # authorization_page.click_register_hypertext()
    registration_page.set_email_registered_user_registration_form()
    registration_page.set_password_registration_form()
    registration_page.repeat_password_registration_form()
    registration_page.click_first_checkbox_consent_registration_form()
    registration_page.scroll_to_register_button_registration_form()
    registration_page.click_to_register_button_registration_form()
    registration_page.verify_error_msg_registration()


# 64, 65, 66, 67, 68, 69 - проверка валидации полей ввода email и пароля в форме регистрации
case_1 = ['71234567890', 'lifehelp1@', 'lifehelp1@', 'Пожалуйста, введите правильный адрес электронной почты']
case_2 = ['aigul.shafigullina@yandex.ru', 'lifehelp1@', 'password1@', 'Введенные пароли не совпадают']
case_3 = ['aigul.shafigullina@yandex.ru', 'lifehelp@', 'lifehelp@', 'Пароль должен содержать хотя бы одну цифру']
case_4 = ['aigul.shafigullina@yandex.ru', 'lifehelp1', 'lifehelp1', 'Пароль должен содержать хотя бы один из символов: '
                                                                    '!?@#$%&*']
case_5 = ['aigul.shafigullina@yandex.ru', 'lifehelп1@', 'lifehelп1@', 'Пароль не должен содержать буквы кириллицы']
case_6 = ['aigul.shafigullina@yandex.ru', '12345671@', '12345671@', 'Пароль должен содержать хотя бы одну букву '
                                                                    'латинского алфавита']

@pytest.mark.parametrize('first, second, third, fourth', (case_1, case_2, case_3, case_4, case_5, case_6),
                             ids=['phone_instead_email', 'not_matching_passwords', 'missing_number_password',
                                  "missing_symbol_password", "cyrillic_password", "missing_latin_letter_password" ])
def test_registrations_error_messages_345678(registration_page, first, second, third, fourth):
    registration_page.set_your_email_registration_fixture(first)
    registration_page.set_password_registration_form_fixture(second)
    registration_page.repeat_password_registration_form_fixture(third)
    registration_page.click_first_checkbox_consent_registration_form()
    registration_page.scroll_to_register_button_registration_form()
    registration_page.click_to_register_button_registration_form()
    registration_page.verify_error_message_registration_fixture(fourth)


#70 - проверка перехода на быстрый вход по клику на кнопку "Быстрый вход" со страницы регистрации
def test_move_to_rapid_auth_from_registration_page_7(authorization_page, registration_page):
    registration_page.scroll_to_rapid_auth_button_registration_form()
    registration_page.click_rapid_auth_btn_registration_page()
    authorization_page.get_url('https://life-help.ru/auth/')

# 86 - проверка кнопка "Зарегистрироваться" неактивная без ввода данных
def test_disabled_button_registration_page_8(authorization_page, registration_page):
    registration_page.verify_disabled_type_button_registration_page()
    authorization_page.verify_disabled_type_button_registration_page()

