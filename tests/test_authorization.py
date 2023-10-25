import allure
import pytest

from locators.authorization_locators import AuthorizationLocators

# @allure.description('Authorization with email and password')
# @allure.label('owner', 'Aygul')
# @allure.title('Authorization with email and password')
# @allure.suite('Authorization pack')
# @allure.severity(allure.severity_level.BLOCKER)
# тест 1 - успешная авторизация по email с паролем (клиент)
# тест 2 - успешная авторизация по телефону с паролем (психолог)

case_1 = ['sh.aygul@gmail.com', 'lifehelp1@', 'https://life-help.ru/user/notes']
case_2 = ['89520476828', 'lifehelp1@', 'https://life-help.ru/doctor/sessions']


@pytest.mark.parametrize('first, second, third', (case_1, case_2),
                             ids=['success_login_user', 'success_login_psychologist'])
def test_authorization(authorization_page, first, second, third):
    #authorization_page.click_to_accept_cookies()
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email(first)
    authorization_page.set_password(second)
    authorization_page.click_to_authorize_button()
    authorization_page.get_page_url()

# 3 - sms-code positive test
def test_authorization_code(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.set_phone_number()
    authorization_page.click_first_checkbox()
    authorization_page.click_get_code_btn()
    authorization_page.verify_appearance_set_code_field()

# 4 - sms-code negative test
def test_authorization_error(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.set_wrong_phone_number()
    authorization_page.click_first_checkbox()
    authorization_page.click_get_code_btn()
    authorization_page.verify_wrong_number_message_rapid_auth_page()

# 5 - проверка выхода из лк клиента
def test_logout_client(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_email()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.click_logout_btn()
    authorization_page.click_to_login_button()
    authorization_page.verify_url_authorization_page()


# 6 - проверка выхода из лк психолога
def test_logout_psychologist(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_psychologist()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.click_logout_btn()
    authorization_page.click_to_login_button()
    authorization_page.verify_url_authorization_page()

# 7 - проверка работы чата в лк клиента
def test_client_chat (authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_email()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.move_to_chat_w_psychologist()
    authorization_page.type_greeting_chat_field()
    authorization_page.click_btn_send_msg_chat()
    authorization_page.verify_successful_send_msg_chat()

# 8 - проверка работы чата в лк психолога
def test_psychologist_chat (authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_psychologist()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.move_to_chat_w_client()
    authorization_page.select_chat_w_client()
    authorization_page.type_greeting_chat_field_psychologist()
    authorization_page.click_btn_send_msg_chat()
    authorization_page.verify_successful_send_msg_chat_psychologist()

# 9 - по клику на кнопку "Подобрать психолога" пользователь переходит на страницу анкеты
def test_get_pshychologist_btn(authorization_page):
    authorization_page.click_get_psychologist_btn()
    authorization_page.verify_url_get_psychologist_page()

# 10 - по клику на кнопку "Войти" пользователь переходит на страницу авторизации
def test_login_button (authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.verify_url_authorization_page()

# 11 - переход из лк клиента на главную страницу по клику на логотип страницы
def test_logo_redirect(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_email()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.click_logo_btn()
    authorization_page.get_url('https://life-help.ru/')

# 12 - покупка пакета из лк клиента картой РФ (Cloudpayments)
# def test_buy_package_4_cloudpayments(authorization_page):
#     authorization_page.click_to_login_button()
#     authorization_page.click_to_login_w_password_button()
#     authorization_page.set_email_email()
#     authorization_page.set_password_pass()
#     authorization_page.click_to_authorize_button()
#     authorization_page.click_my_balance_menu_navigation()
#     authorization_page.click_buy_package()
#     authorization_page.click_buy_package_4_sessions()
#     authorization_page.click_card_rf_button_package()
#     authorization_page.click_pay_online_button_package()
#     authorization_page.verify_location_cloudpayments_page()

# 12a - покупка пакета из лк клиента картой РФ (Tinkoff касса)
def test_buy_package_4_tinkoff_kassa(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_email()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.click_my_balance_menu_navigation()
    authorization_page.click_buy_package()
    authorization_page.click_buy_package_4_sessions()
    authorization_page.click_card_rf_button_package()
    authorization_page.click_pay_online_button_package()
    authorization_page.verify_location_tinkoff_kassa_page_rapid_pay()

# 13 - покупка пакета из лк клиента иностранной картой (Prodamus)
def test_buy_package_4_prodamus(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_email()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.click_my_balance_menu_navigation()
    authorization_page.click_buy_package()
    authorization_page.click_buy_package_4_sessions()
    authorization_page.click_foreign_card_button_package()
    authorization_page.click_pay_online_button_package()
    authorization_page.verify_whatsapp_care_page()
    #если бы страница ватсапп открывалась на соседней странице
    # authorization_page.move_to_new_whatsapp_help_page()
    # новая версия для Продамуса
    # authorization_page.click_not_russian_card_prodamus_button()
    # authorization_page.verify_vs_ms_kzt_card_prodamus_page()
    # старая версия для Продамуса
    #authorization_page.click_russian_card_prodamus_button()
    # authorization_page.verify_location_prodamus_page()


# 14 - запись на повторный сеанс из завершенных сессий - Cloudpayments
# def test_client_second_session_order_cloudpayments(authorization_page):
#     authorization_page.click_to_login_button()
#     authorization_page.click_to_login_w_password_button()
#     authorization_page.set_phone_password_authorization()
#     authorization_page.set_password_pass()
#     authorization_page.click_to_authorize_button()
#     authorization_page.click_terminated_sessions_title()
#     authorization_page.click_order_session_again_button()
#     authorization_page.scroll_till_go_to_payment_button_psychologyst_schedule()
#     authorization_page.select_time_session_schedule_psychologist()
#     authorization_page.click_rapid_go_payment_btn()
#     authorization_page.click_card_rf_button_session()
#     authorization_page.click_pay_online_button_session()
#     authorization_page.click_no_continue_payment_button_order_page()
#     authorization_page.verify_location_cloudpayments_page()

# 14a - запись на повторный сеанс из завершенных сессий - Tinkoff kassa
def test_client_second_session_order_tinkoff_kassa (authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_phone_password_authorization()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.click_terminated_sessions_title()
    authorization_page.click_order_session_again_button()
    authorization_page.select_2nd_time_session_rapid_schedule_psychologist()
    authorization_page.click_rapid_go_payment_btn()
    authorization_page.click_card_rf_button_session()
    authorization_page.click_pay_online_button_session()
    authorization_page.click_no_continue_payment_button_order_page()
    authorization_page.verify_location_tinkoff_kassa_page_rapid_pay()


# # 15 - запись на повторный сеанс из завершенных сессий - Prodamus
def test_client_second_session_order_prodamus (authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_phone_password_authorization()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.click_terminated_sessions_title()
    authorization_page.click_order_session_again_button()
    authorization_page.select_2nd_time_session_rapid_schedule_psychologist()
    authorization_page.click_rapid_go_payment_btn()
    authorization_page.click_foreign_card_button_session()
    authorization_page.click_pay_online_button_session()
    authorization_page.click_no_continue_payment_button_order_page()
    authorization_page.verify_whatsapp_care_page()
    # новая версия для Продамуса
    # authorization_page.click_not_russian_card_prodamus_button()
    # authorization_page.verify_vs_ms_kzt_card_prodamus_page()
    # старая версия для Продамуса
    # authorization_page.click_russian_card_prodamus_button()
    # authorization_page.verify_location_prodamus_page()

# 16 - проверка наличия Ирины Панковой в подборе анкеты Инд50-Рус-Стресс
def test_questionnaire_stress_pankova(authorization_page):
    authorization_page.click_get_psychologist_btn()
    authorization_page.set_age_field_questionnaire()
    authorization_page.click_personal_questions_title()
    authorization_page.select_stress_questionnaire()
    authorization_page.click_psychologist_preferences_title_questionnaire()
    authorization_page.click_age_over_30_questionnaire()
    authorization_page.click_select_psychologist_title_questionnaire()
    authorization_page.verify_presence_pankova_choose_specialist()

# 17 - проверка наличия Алисы в подборе анкеты Инд90-Рус-Стресс
def test_questionnaire_ind_90_alisa(authorization_page):
    authorization_page.click_get_psychologist_btn()
    authorization_page.click_ind_90_questionnaire()
    authorization_page.set_age_field_questionnaire()
    authorization_page.click_personal_questions_title()
    authorization_page.select_stress_questionnaire()
    authorization_page.click_psychologist_preferences_title_questionnaire()
    authorization_page.click_age_over_30_questionnaire()
    authorization_page.click_select_psychologist_title_questionnaire()
    authorization_page.verify_presence_alisa_ivannikova_choose_specialist()

# 18 - проверка наличия Алии в подборе анкеты Инд50-Татар-Стресс
def test_questionnaire_tatar_aliya(authorization_page):
    authorization_page.click_get_psychologist_btn()
    authorization_page.click_tatar_button_questionnaire()
    authorization_page.set_age_field_questionnaire()
    authorization_page.click_personal_questions_title()
    authorization_page.select_stress_questionnaire()
    authorization_page.click_psychologist_preferences_title_questionnaire()
    authorization_page.click_age_over_30_questionnaire()
    authorization_page.click_select_psychologist_title_questionnaire()
    authorization_page.verify_presence_aliya_askarova_choose_specialist()

# 19 - проверка наличия Елены Калкан в подборе анкеты Парной консультации - Сложности в отношениях
def test_questionnaire_paired_elena(authorization_page):
    authorization_page.click_get_psychologist_btn()
    authorization_page.click_paired_consultation_button_questionnaire()
    authorization_page.set_age_field_questionnaire()
    authorization_page.click_personal_questions_title()
    authorization_page.click_difficulties_in_relationship_paired_consultation_button_questionnaire()
    authorization_page.click_psychologist_preferences_title_questionnaire()
    authorization_page.click_age_over_30_questionnaire()
    authorization_page.click_select_psychologist_title_questionnaire()
    authorization_page.verify_presence_elena_kalkan_choose_specialist()

# 20 - проверка наличия Алии в подборе анкеты Парной консультации - Татарский язык - Сложности в отношениях
def test_questionnaire_paired_tatar_aliya(authorization_page):
    authorization_page.click_get_psychologist_btn()
    authorization_page.click_paired_consultation_button_questionnaire()
    authorization_page.click_tatar_button_questionnaire()
    authorization_page.set_age_field_questionnaire()
    authorization_page.click_personal_questions_title()
    authorization_page.click_difficulties_in_relationship_paired_consultation_button_questionnaire()
    authorization_page.click_psychologist_preferences_title_questionnaire()
    authorization_page.click_age_over_30_questionnaire()
    authorization_page.click_select_psychologist_title_questionnaire()
    authorization_page.verify_presence_aliya_askarova_choose_specialist()

# 21 - проверка пути восстановления пароля до отправки email со ссылкой на email
def test_get_link_reset_password(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.click_forgot_password()
    authorization_page.set_email_forgot_password()
    authorization_page.click_reset_password_button()
    authorization_page.verify_message_sent_link_reset_password()

# # 22 - проверка пути регистрации пользователя до отправки email со ссылкой на email - перенесен в файл registration.py
# def test_registration_new_user(authorization_page):
#     authorization_page.click_to_login_button()
#     authorization_page.click_to_login_w_password_button()
#     authorization_page.click_register_hypertext()
#     authorization_page.set_email_registration_form()
#     authorization_page.set_password_registration_form()
#     authorization_page.repeat_password_registration_form()
#     authorization_page.click_first_checkbox_consent_registration_form()
#     authorization_page.scroll_to_register_button_registration_form()
#     authorization_page.click_to_register_button_registration_form()
#     authorization_page.verify_sent_msg_registration()

# # 23 - проверка пути регистрации пользователя до отправки email со ссылкой на существующий email - перенесен в файл registration.py
# def test_error_registration_registered_user(authorization_page):
#     authorization_page.click_to_login_button()
#     authorization_page.click_to_login_w_password_button()
#     authorization_page.click_register_hypertext()
#     authorization_page.set_email_registered_user_registration_form()
#     authorization_page.set_password_registration_form()
#     authorization_page.repeat_password_registration_form()
#     authorization_page.click_first_checkbox_consent_registration_form()
#     authorization_page.scroll_to_register_button_registration_form()
#     authorization_page.click_to_register_button_registration_form()
#     authorization_page.verify_error_msg_registration()

#24 - проверка, что клик на знак Телеграмма в службе заботы открывает в соседней вкладке переписку в Тг
def test_click_opens_telegram_care_page(authorization_page):
    authorization_page.click_to_accept_cookies()
    authorization_page.click_to_telegram_care_button()
    authorization_page.move_to_new_telegram_care_page()
    authorization_page.verify_url_telegram_care_page()

# 25 - проверка, что клик на знак Whatsapp в службе заботы открывает в соседней вкладке переписку в Whatsapp
def test_click_opens_whatsapp_care_page(authorization_page):
    authorization_page.click_to_accept_cookies()
    authorization_page.click_to_whatsapp_care_button()
    authorization_page.move_to_new_whatsapp_care_page()
    authorization_page.verify_whatsapp_care_page()

# 26 - проверка "глазика" в поле "Пароль" - скрытые значения открываются
def test_view_password_authorization_form(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_password_pass()
    authorization_page.verify_hidden_type_password_field()
    authorization_page.click_to_view_password_button_auth_page()
    authorization_page.verify_viewed_type_password_field()


# 27 - проверка повторного клика на "глазик" в поле "Пароль" - скрываются введенные значения
def test_hide_password_authorization_form(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_password_pass()
    authorization_page.click_to_view_password_button_auth_page()
    authorization_page.verify_viewed_type_password_field()
    authorization_page.click_to_hide_password_button_auth_page()

# 28 - проверка появления сообщения "Неверный логин или пароль" при вводе неверного пароля при авторизации с паролем
def test_wrong_password_authorization(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_email()
    authorization_page.set_wrong_password()
    authorization_page.click_to_authorize_button()
    authorization_page.verify_wrong_password_message_authorization()

# 29 - проверка появления сообщения "Пароль ранее не был установлен" при авторизации пользователя
# с неустановленным паролем
def test_error_authorization_without_set_password(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_phone_user_wo_password()
    authorization_page.set_wrong_password()
    authorization_page.click_to_authorize_button()
    authorization_page.verify_error_msg_authorization_user_wo_password()

# 30 - проверка появления сообщения "Введенный код неверен" при авторизации пользователя с неправильным кодом по смс
def test_error_wrong_sms_code_authorization(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.set_phone_number()
    authorization_page.click_first_checkbox()
    authorization_page.click_get_code_btn()
    authorization_page.type_wrong_sms_code_authorization()
    authorization_page.click_to_auth_code_button()
    authorization_page.verify_error_msg_authorization_user_wrong_sms_code()

# # 31 - авт. бронь при незавершенной оплате при записи на повторный сеанс из завершенных сессий - возвращение
# со страницы заказа
def test_automatic_order_after_stopped_payment(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_phone_password_authorization()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.click_terminated_sessions_title()
    authorization_page.click_order_session_again_button()
    authorization_page.select_2nd_time_session_rapid_schedule_psychologist()
    authorization_page.click_rapid_go_payment_btn()
    authorization_page.click_card_rf_button_session()
    authorization_page.click_to_back_button_order_page()
    authorization_page.click_to_user_avatar_button_psychologist_page()
    authorization_page.verify_session_status_waits_payment()
    # authorization_page.click_pay_online_button_session()
    # authorization_page.click_no_continue_payment_button_order_page()

    # authorization_page.scroll_to_come_back_to_cabinet_button_client()
    # authorization_page.click_to_come_back_cabinet_button()


# 32 - перенос авт. брони при незавершенной оплате при записи на повторный сеанс из завершенных сессий - Cloudpayments
def test_reschedule_automatic_order(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_email()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.click_to_three_dots_button_ordered_session()
    authorization_page.click_to_reschedule_ordered_session_drop_down()
    authorization_page.select_seventh_time_to_reschedule_order()
    authorization_page.click_to_change_time_button_to_reschedule_order()
    authorization_page.get_url('https://life-help.ru/user/notes')

# 33 - отмена авт. брони при незавершенной оплате при записи на повторный сеанс из завершенных сессий - Cloudpayments
def test_deny_payment_automatic_order(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_email()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.click_to_three_dots_button_ordered_session()
    authorization_page.click_to_deny_payment_ordered_session_drop_down()
    authorization_page.click_to_yes_deny_payment_button_to_deny_order()
    authorization_page.click_to_good_button_after_deny_order()
    # authorization_page.verify_absence_order()

# 34 - проверка бронирования сеанса из лк психолога - не сработал последний этап
def test_psychologist_order_session(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_psychologist()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.click_to_clients_and_aims_menu_psychologist()
    authorization_page.select_aygul_clients_and_aims_menu_psychologist()
    authorization_page.click_to_three_dots_clients_and_aims_menu_psychologist()
    authorization_page.click_to_create_new_session_for_clients_menu_psychologist()
    authorization_page.click_to_create_button_to_create_new_session_for_clients_menu_psychologist()
    authorization_page.verify_successful_creation_order_text_psychologist()
    # authorization_page.verify_successful_creation_session_text_psychologist()

# 35 - появление модального окна с просьбой указать свой возраст в анкете
def test_error_wo_age_questionnaire(authorization_page):
    authorization_page.click_get_psychologist_btn()
    authorization_page.click_personal_questions_title()
    authorization_page.verify_window_to_set_age_questionnaire()

# 36 - проверка того, что нельзя перейти к предпочтениям к психологу без выбора темы в анкете
def test_questionnaire(authorization_page):
    authorization_page.click_get_psychologist_btn()
    authorization_page.set_age_field_questionnaire()
    authorization_page.click_psychologist_preferences_title_questionnaire()
    authorization_page.get_url('https://life-help.ru/questionnaire/personal/')

# 37 - проверка применения промокода promo на полную стоимость сеанса при повторной записи
def test_promocode(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_phone_password_authorization()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.click_terminated_sessions_title()
    authorization_page.click_order_session_again_button()
    authorization_page.select_2nd_time_session_rapid_schedule_psychologist()
    authorization_page.click_rapid_go_payment_btn()
    authorization_page.click_to_ihave_promocode_order_page()
    authorization_page.verify_price_1_rubble_button_order_page_before_promo()
    authorization_page.enter_free_promocode_session_order_page()
    authorization_page.click_to_submit_promocode_button_session_order_page()
    authorization_page.verify_price_0_rubbles_button_order_page_after_promo()

# 38 - запись на сеанс в пакете
def test_order_session_in_package_4(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_email()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.click_my_balance_menu_navigation()
    authorization_page.scroll_to_empty_element_order_session_package()
    # authorization_page.click_to_order_session_package()
    # authorization_page.save_selected_time_to_order_session_package()
    authorization_page.select_time_to_order_session_package()
    authorization_page.submit_selected_time_to_order_session_package()
    # authorization_page.save_ordered_time_session_package()
    authorization_page.verify_presence_ordered_session_package()

# 39,40,41 - появление модального окна с просьбой указать свой возраст в анкете, если указать меньше 16
case_1 = ['0']
case_2 = ['15']
case_3 = ['120']
@pytest.mark.parametrize('first', (case_1, case_2, case_3),
                             ids=['0 years', '15 years', '120 years'])

def test_error_age_out_16and119_questionnaire(authorization_page, first):
    authorization_page.click_get_psychologist_btn()
    authorization_page.set_age_field_negative_validation_questionnaire(first)
    authorization_page.click_personal_questions_title()
    authorization_page.verify_window_age_above16_questionnaire()

# 42,43,44 - проверка возможности продолжить заполнение анкеты при указании возраста в диапазоне 16-119 (16,45,119)
case_1 = ['16']
case_2 = ['45']
case_3 = ['119']
@pytest.mark.parametrize('age', (case_1, case_2, case_3),
                             ids=['16 years', '45 years', '119 years'])

def test_correct_age_within_16and119_questionnaire(authorization_page, age):
    authorization_page.click_get_psychologist_btn()
    authorization_page.set_age_field_positive_validation_questionnaire(age)
    authorization_page.click_personal_questions_title()
    authorization_page.get_url("https://life-help.ru/questionnaire/personal/")

# 45 - Проверка открытия страницы службы заботы в Whatsapp при клике на «Помощь в подборе» после анкеты
def test_questionnaire_help_nastya(authorization_page):
    authorization_page.click_get_psychologist_btn()
    authorization_page.click_paired_consultation_button_questionnaire()
    authorization_page.set_age_field_questionnaire()
    authorization_page.click_personal_questions_title()
    authorization_page.click_difficulties_in_relationship_paired_consultation_button_questionnaire()
    authorization_page.click_psychologist_preferences_title_questionnaire()
    authorization_page.click_age_over_30_questionnaire()
    authorization_page.click_select_psychologist_title_questionnaire()
    authorization_page.click_help_to_select_psychologyst_questionnaire()
    authorization_page.move_to_new_whatsapp_care_page()
    authorization_page.verify_whatsapp_care_page()
    # authorization_page.get_url("https://life-help.ru/choose-manager/") - было раньше, когда клиенту открывалась
    # страница с расписанием 20-минуток
    # authorization_page.verify_for_free_button_manager_help_page() альтернатива
    # authorization_page.verify_choose_manager_help_page() альтернатива

# 46 - проверка создания цели в лк клиента
def test_create_aim_client(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_email()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.click_aims_menu_client()
    authorization_page.click_personal_aims_menu_client()
    authorization_page.click_add_new_aim_button_client()
    authorization_page.type_aim_name_create_client()
    authorization_page.type_aim_description_create_client()
    authorization_page.set_start_day_aim_button_client()
    authorization_page.set_end_day_aim_button_client()
    authorization_page.click_save_aim_changes_client_account()
    authorization_page.verify_created_aim_in_client_account()

# 47 - проверка создания цели в лк психолога
def test_create_aim_psychologist(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_psychologist()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.click_to_clients_and_aims_menu_psychologist()
    authorization_page.select_aygul_clients_and_aims_menu_psychologist()
    authorization_page.click_add_new_aim_button_psychologist()
    authorization_page.type_aim_name_create_client()
    authorization_page.type_aim_description_create_client()
    authorization_page.set_start_day_aim_button_client()
    authorization_page.set_end_day_aim_button_client()
    authorization_page.click_create_new_aim_button_client()
    authorization_page.verify_created_aim_in_client_account()

# 48 - переход на страницу пакетов при клике "Да, посмотреть пакеты" на странице заказа страницы
def test_move_to_packages_from_order_page_by_click_yes(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_phone_password_authorization()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.click_terminated_sessions_title()
    authorization_page.click_order_session_again_button()
    authorization_page.select_2nd_time_session_rapid_schedule_psychologist()
    authorization_page.click_rapid_go_payment_btn()
    authorization_page.click_card_rf_button_session()
    authorization_page.click_pay_online_button_session()
    authorization_page.click_yes_see_packages_offer_button_order_page()
    authorization_page.move_to_new_packages_offer_page()
    authorization_page.get_url("https://life-help.ru/packages/")

# 49 - переход к оформлению рассрочки Тинькофф при покупке пакета 54 из лк клиента
def test_buy_package_54_w_tinkoff(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_email()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.click_my_balance_menu_navigation()
    authorization_page.click_buy_package()
    authorization_page.click_buy_package_54_by_tinkoff_installments()
    authorization_page.click_continue_button_by_tinkoff_installments()
    authorization_page.move_to_new_tinkoff_installments_page()
    authorization_page.verify_tinkoff_installments_application_page_conditions()

# 50 - проверка покупки сеанса "Записаться повторно" с помощью пакета (путь без страницы заказа)
def test_pay_buy_session_by_package(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_email()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.click_terminated_sessions_title()
    authorization_page.click_order_session_again_button()
    authorization_page.select_2nd_time_session_rapid_schedule_psychologist()
    authorization_page.click_rapid_go_payment_btn()
    authorization_page.verify_presence_package_test_payment_page()

# 51 - проверка перехода на страницу авторизации с помощью ВК
def test_authorization_via_vk(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.click_vk_auth_button()
    authorization_page.verify_vk_auth_page_title()

# 52 - проверка - поле ввода телефона подсвечивается красным при клике "Получить код" без ввода телефона
def test_no_authorization_code_without_phone_number(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_get_code_btn()
    authorization_page.verify_red_phonefield_wo_phonenumber_auth_page()

# 53 - проверка подсвечивания поля ввода кода красным при клике "Войти" без ввода кода по смс
def test_red_field_wo_code_authorization_page(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.set_phone_number()
    authorization_page.click_first_checkbox()
    authorization_page.click_get_code_btn()
    authorization_page.click_auth_code_btn()
    authorization_page.verify_red_codefield_wo_codenumber_auth_page()

# 54 - проверка подсвечивания поля ввода email/телефона красным при клике "Войти" без ввода email/телефона
def test_red_email_phone_field_wo_phone_auth_page(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.click_to_authorize_button()
    authorization_page.verify_red_email_phone_field_wo_email_auth_page()

# 55 - проверка подсвечивания поля ввода пароля красным при клике "Войти" с вводом email, но без пароля
def test_red_password_field_wo_password_auth_page(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_email()
    authorization_page.click_to_authorize_button()
    authorization_page.verify_red_password_field_wo_password_auth_page()

# 56 - проверка появления сообщения об ошибке "Неправильный номер" при вводе немецкого номера без +
def test_german_phone_error_rapid_auth_page(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.set_german_phone_number()
    authorization_page.click_first_checkbox()
    authorization_page.click_get_code_btn()
    authorization_page.verify_wrong_number_message_rapid_auth_page()

# 57 - проверка появления сообщения об ошибке "Телефон слишком короткий" при вводе номера из 9 цифр
def test_short_phone_error_rapid_auth_page(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.set_short_phone_number()
    authorization_page.click_first_checkbox()
    authorization_page.click_get_code_btn()
    authorization_page.verify_short_number_message_rapid_auth_page()

# 58 - проверка появления сообщения об ошибке "Телефон слишком длинный" при вводе номера из 15 цифр
def test_long_phone_error_rapid_auth_page(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.set_long_phone_number()
    authorization_page.click_first_checkbox()
    authorization_page.click_get_code_btn()
    authorization_page.verify_long_number_message_rapid_auth_page()


# 59 - проверка нельзя войти без выбора первого чек-бокса - подсвечивается красным (быстрый вход)
def test_red_unselected_first_checkbox_rapid_auth_page(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.set_phone_number()
    authorization_page.click_second_checkbox()
    authorization_page.click_get_code_btn()
    authorization_page.verify_red_unselected_first_checkbox_auth_page()

# 60 - проверка - определяется флаг страны Германия при вводе номера с +
def test_german_flag_number_w_plus_rapid_auth_page(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.set_german_phone_number_with_plus()
    authorization_page.verify_german_flag_auth_page()

# 61 - проверка - не определяется флаг страны Германия при вводе номера без +
def test_russian_flag_with_german_number_wo_plus_rapid_auth_page(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.set_german_phone_number()
    authorization_page.verify_russian_flag_auth_page()


# 62 - проверка - в поле ввода телефона можно поменять флаг на Грузинский из списка стран при авторизации по коду смс
def test_change_flag_rapid_auth_page(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_flag_btn_rapid_auth()
    authorization_page.select_georgian_flag_rapid_auth()

# 63 - проверка появления сообщения "Неверные данные авторизации" при вводе почты несуществующего пользователя
# при авторизации с паролем
def test_wrong_auth_data_w_password(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_not_existing_user()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.verify_wrong_wrong_auth_data_message_unexisting_user_authorization()

# 64 - проверка перехода на страницу авторизации с помощью ВК - дубль 51
# def test_vk_authorization(authorization_page):
#     authorization_page.click_to_login_button()
#     authorization_page.click_to_login_w_password_button()
#     authorization_page.click_vk_auth_button()
#     authorization_page.verify_vk_auth_page_title()

# # 64, 65, 66, 67, 68, 69 - проверка валидации полей ввода email и пароля в форме регистрации - перенесла в отдельный файл registration.py
# case_1 = ['71234567890', 'lifehelp1@', 'lifehelp1@', 'Пожалуйста, введите правильный адрес электронной почты']
# case_2 = ['aigul.shafigullina@yandex.ru', 'lifehelp1@', 'password1@', 'Введенные пароли не совпадают']
# case_3 = ['aigul.shafigullina@yandex.ru', 'lifehelp@', 'lifehelp@', 'Пароль должен содержать хотя бы одну цифру']
# case_4 = ['aigul.shafigullina@yandex.ru', 'lifehelp1', 'lifehelp1', 'Пароль должен содержать хотя бы один из символов: '
#                                                                     '!?@#$%&*']
# case_5 = ['aigul.shafigullina@yandex.ru', 'lifehelп1@', 'lifehelп1@', 'Пароль не должен содержать буквы кириллицы']
# case_6 = ['aigul.shafigullina@yandex.ru', '12345671@', '12345671@', 'Пароль должен содержать хотя бы одну букву '
#                                                                     'латинского алфавита']
#
# @pytest.mark.parametrize('first, second, third, fourth', (case_1, case_2, case_3, case_4, case_5, case_6),
#                              ids=['phone_instead_email', 'not_matching_passwords', 'missing_number_password',
#                                   "missing_symbol_password", "cyrillic_password", "missing_latin_letter_password" ])
# def test_registrations_error_messages(authorization_page, first, second, third, fourth):
#     authorization_page.click_to_login_button()
#     authorization_page.click_to_login_w_password_button()
#     authorization_page.click_register_hypertext()
#     authorization_page.set_your_email_registration_fixture(first)
#     authorization_page.set_password_registration_form_fixture(second)
#     authorization_page.repeat_password_registration_form_fixture(third)
#     authorization_page.click_first_checkbox_consent_registration_form()
#     authorization_page.scroll_to_register_button_registration_form()
#     authorization_page.click_to_register_button_registration_form()
#     authorization_page.verify_error_message_registration_fixture(fourth)

# #70 - проверка перехода на быстрый вход по клику на кнопку "Быстрый вход" со страницы регистрации - перенесла в registration.py
# def test_move_to_rapid_auth_from_registration_page(authorization_page):
#     authorization_page.click_to_login_button()
#     authorization_page.click_to_login_w_password_button()
#     authorization_page.click_register_hypertext()
#     authorization_page.scroll_to_rapid_auth_button_registration_form()
#     authorization_page.click_rapid_auth_btn_registration_page()
#     authorization_page.get_url('https://life-help.ru/auth/')

#71 -  проверка перехода в лк по клику на аватарку на странице заказа пакета
def test_back_account_package_order_page(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_email()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.click_my_balance_menu_navigation()
    authorization_page.click_buy_package()
    authorization_page.click_buy_package_4_sessions()
    authorization_page.click_avatar_package_order_page()
    authorization_page.get_url('https://life-help.ru/user/notes')

# # 72 - проверка названия платежа на странице оплаты пакета из лк клиента картой РФ (Cloudpayments)
# def test_package_4_name_cloudpayments_page(authorization_page):
#     authorization_page.click_to_login_button()
#     authorization_page.click_to_login_w_password_button()
#     authorization_page.set_email_email()
#     authorization_page.set_password_pass()
#     authorization_page.click_to_authorize_button()
#     authorization_page.click_my_balance_menu_navigation()
#     authorization_page.click_buy_package()
#     authorization_page.click_buy_package_4_sessions()
#     authorization_page.click_card_rf_button_package()
#     authorization_page.click_pay_online_button_package()
#     authorization_page.verify_name_package_payment_cloudpayments_page()

# 72а - проверка названия платежа на странице оплаты пакета из лк клиента картой РФ (Tinkoff kassa)
def test_package_4_name_tinkoff_page(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_email()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.click_my_balance_menu_navigation()
    authorization_page.click_buy_package()
    authorization_page.click_buy_package_4_sessions()
    authorization_page.click_card_rf_button_package()
    authorization_page.click_pay_online_button_package()
    authorization_page.verify_location_tinkoff_kassa_page_rapid_pay()



# # 73 - проверка названия платежа на странице оплаты сеанса из лк клиента картой РФ (Cloudpayments)
# def test_session_name_cloudpayments_page(authorization_page):
#     authorization_page.click_to_login_button()
#     authorization_page.click_to_login_w_password_button()
#     authorization_page.set_phone_password_authorization()
#     authorization_page.set_password_pass()
#     authorization_page.click_to_authorize_button()
#     authorization_page.click_terminated_sessions_title()
#     authorization_page.click_order_session_again_button()
#     authorization_page.select_time_session_schedule_psychologist()
    # authorization_page.click_card_rf_button_session()
    # authorization_page.click_pay_online_button_session()
    # authorization_page.click_no_continue_payment_button_order_page()
    # authorization_page.verify_name_session_payment_cloudpayments_page()

# 73a - проверка названия платежа на странице оплаты сеанса из лк клиента картой РФ (Tinkoff)
# def test_session_name_tinkoff_payment_page(authorization_page):
#     authorization_page.click_to_login_button()
#     authorization_page.click_to_login_w_password_button()
#     authorization_page.set_phone_password_authorization()
#     authorization_page.set_password_pass()
#     authorization_page.click_to_authorize_button()
#     authorization_page.click_terminated_sessions_title()
#     authorization_page.click_order_session_again_button()
#     authorization_page.select_2nd_time_session_rapid_schedule_psychologist()
#     authorization_page.click_rapid_go_payment_btn()
#     authorization_page.click_card_rf_button_session()
#     authorization_page.click_pay_online_button_session()
#     authorization_page.click_no_continue_payment_button_order_page()
#     time.sleep(5)
#     authorization_page.click_price_payment_info_tinkoff_page()
    # authorization_page.verify_name_session_payment_cloudpayments_page()

# 74 - перенос оплаченной сессии по клику на кнопку "Перейти к сеансу" - "Перенести сеанс"
def test_reschedule_payed_session(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_email()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.click_go_to_payed_session_btn()
    authorization_page.click_to_reschedule_session_time_btn()
    authorization_page.select_seventh_time_to_reschedule_order()
    authorization_page.click_to_change_time_button_to_reschedule_order()
    authorization_page.get_url('https://life-help.ru/user/notes')

# 75 - отмена оплаченной сессии по клику на кнопку "Перейти к сеансу" - "Отменить сеанс"
def test_deny_paied_session(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_email()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.click_go_to_payed_session_btn()
    authorization_page.click_to_deny_payed_session_btn()
    authorization_page.click_to_yes_deny_payed_session_btn()
    authorization_page.verify_modal_confirmation_message_session_denied()

# 76 - При отмене "отменить сеанс" (через "Перенести сеанс")пользователь возвращается на страницу ожидания видеосеанса
def test_not_terminated_deny_paied_session(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_email()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.click_go_to_payed_session_btn()
    authorization_page.click_to_deny_payed_session_btn()
    authorization_page.click_do_not_deny_btn_package_session()
    authorization_page.verify_name_video_sesion_page_heading()

# 77 - поменять психолога при записи на сеанс в пакете
def test_change_psychologist_during_order_session_in_package_4(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_email()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.click_my_balance_menu_navigation()
    authorization_page.scroll_to_empty_element_order_session_package()
    authorization_page.click_to_select_new_doctor_btn_package_session()
    authorization_page.verify_url_questionnaire_page()

# 78 - оплата брони пакетом (короткий путь без страницы заказа)
def test_buy_order_by_package_short_pathway(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_email()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.click_to_pay_btn_order_my_schedule_page()
    authorization_page.verify_presence_package_test_order_payment_page()

#79 - проверка перехода на страницу Регулярное расписание по клику на 3 точки - регулярное расписание
def test_regular_session_order_schedule(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_bitrix_email()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.click_to_three_dots_button_ordered_session()
    # authorization_page.click_regular_session_order_icon()
    authorization_page.click_regular_session_order_dropdown_menu_list()

# 80 - переход авторизованного клиента с главной страницы в лк по клику на аватар
def test_avatar_redirect_from_main_page_to_account(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_email()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.click_my_balance_menu_navigation()
    authorization_page.click_logo_btn()
    authorization_page.click_to_user_avatar_button_psychologist_page()
    authorization_page.verify_my_schedule_user_page_url()

# 81 - проверка наличия видео в карточке психолога в подборе анкеты Инд50-Рус-Стресс
def test_video_psychologist(authorization_page):
    authorization_page.click_get_psychologist_btn()
    authorization_page.set_age_field_questionnaire()
    authorization_page.click_personal_questions_title()
    authorization_page.select_stress_questionnaire()
    authorization_page.click_psychologist_preferences_title_questionnaire()
    authorization_page.click_age_over_30_questionnaire()
    authorization_page.click_select_psychologist_title_questionnaire()
    authorization_page.click_pankova_video()
    authorization_page.verify_video_frame_psychologist_page()

# 82 - проверка - нельзя повторно забронировать сеанса из лк психолога на занятое бронью время
def test_error_psychologist_order_occupied_time_session(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_psychologist()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.click_to_clients_and_aims_menu_psychologist()
    authorization_page.select_aygul_clients_and_aims_menu_psychologist()
    authorization_page.click_to_three_dots_clients_and_aims_menu_psychologist()
    authorization_page.click_to_create_new_session_for_clients_menu_psychologist()
    authorization_page.click_to_create_button_to_create_new_session_for_clients_menu_psychologist()
    # authorization_page.click_ok_button_successful_order_by_psychologist()
    # authorization_page.click_to_create_new_session_for_clients_menu_psychologist()
    # authorization_page.click_to_create_button_to_create_new_session_for_clients_menu_psychologist()
    authorization_page.verify_error_unsuccessful_creation_order_text_psychologist()

# 83 - проверка перехода в чат с психологом по клику на 3 точки напротив имени психолога в лк клиента - Мое расписание
def test_client_three_dots_go_to_chat (authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_email()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.click_to_three_dots_psychologists_name()
    authorization_page.click_go_to_chat_three_dots_menu_client()
    authorization_page.move_to_chat_w_psychologist_page()
    authorization_page.verify_chats_w_psychologist_page_title()

# 84 - проверка перехода на расписание психолога по клику на 3 точки-Записаться повторно в лк клиента - Мое расписание
def test_client_three_dots_go_to_psychologist_schedule (authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_phone_password_authorization()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.click_to_three_dots_psychologists_name()
    authorization_page.click_order_session_again_three_dots_menu_btn_client()
    authorization_page.verify_url_psychologist_page_order_session_again()

# 85 - проверка - кнопка "Восстановить пароль" неактивная без ввода email
def test_inactive_button_get_link_reset_password(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.click_forgot_password()
    authorization_page.verify_disabled_type_button_reset_password_page()

# # 86 - проверка кнопка "Зарегистрироваться" неактивная без ввода данных - перенесла в registration.py
# def test_disabled_button_registration_page(authorization_page):
#     authorization_page.click_to_login_button()
#     authorization_page.click_to_login_w_password_button()
#     authorization_page.click_register_hypertext()
#     authorization_page.verify_disabled_type_button_registration_page()
    # authorization_page.set_email_registration_form()
    # authorization_page.set_password_registration_form()
    # authorization_page.repeat_password_registration_form()
    # authorization_page.click_first_checkbox_consent_registration_form()
    # authorization_page.scroll_to_register_button_registration_form()
    # authorization_page.click_to_register_button_registration_form()
    # authorization_page.verify_sent_msg_registration()

#87 - наличие модального окна с предупреждением о невозврате оплаты при отмене сеанса, если осталось менее 12ч
def test_deny_paied_session_modal_window(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_email()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.click_go_to_payed_session_btn()
    authorization_page.click_to_deny_payed_session_btn()
    authorization_page.verify_modal_window_caution_refund_session_denied()

#88 - проверка - закрыть модальное окно с предупреждением о невозврате оплаты при отмене сеанса кликом
# за пределами модального окна
def test_deny_paied_session_outside_modal_window(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_email()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.click_go_to_payed_session_btn()
    authorization_page.click_to_deny_payed_session_btn()
    authorization_page.click_click_outside_deny_payed_session_modal_window()
    authorization_page.verify_title_page_timer_before_session()

#89 - проверка - закрыть модальное окно с предупреждением о невозврате оплаты при отмене сеанса кликом
# на крестик в верхнем правом углу модального окна
def test_deny_paied_session_cross_btn_modal_window(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_email()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.click_go_to_payed_session_btn()
    authorization_page.click_to_deny_payed_session_btn()
    authorization_page.click_cross_to_close_modal_window_deny_payed_session()
    authorization_page.verify_title_page_timer_before_session()

# 90 - перенос оплаченной сессии по клику 3 точки - "Перенести сеанс" - пользователь без рег.расписания
def test_reschedule_payed_session_three_dots(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_email()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.click_to_three_dots_button_ordered_session()
    authorization_page.click_to_reschedule_payed_session_drop_down()
    # authorization_page.click_to_reschedule_only_this_session_button()
    authorization_page.select_seventh_time_to_reschedule_order()
    authorization_page.click_to_change_time_button_to_reschedule_order()
    authorization_page.get_url('https://life-help.ru/user/notes')

# 91 - проверка перехода в лк Мое расписание по клику на стрелку над окном ожидания видеосеанса
def test_back_to_my_schedule_page_from_video_by_arrow_btn_click(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_email()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.click_go_to_payed_session_btn()
    authorization_page.click_to_arrow_button_to_back_from_videosession_page_to_my_schedule_page()
    authorization_page.get_url('https://life-help.ru/user/notes')

# 92 - перенос оплаченной сессии по клику 3 точки - "Перенести сеанс" пользователь с рег.расписанием
def test_reschedule_payed_session_three_dots_reg_schedule(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_bitrix_email()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.click_to_three_dots_button_ordered_session()
    authorization_page.click_to_reschedule_payed_session_drop_down()
    authorization_page.click_to_reschedule_only_this_session_button()
    authorization_page.select_seventh_time_to_reschedule_order()
    authorization_page.click_to_change_time_button_to_reschedule_order()
    authorization_page.get_url('https://life-help.ru/user/notes')

# 93 - проверка перехода на карточку психолога при клике на его имя из лк клиента-мое расписание-мой психолог
def test_click_psychologist_name_opens_psychologist_schedule_from_client_account(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_email()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.click_my_psychologist_name()
    authorization_page.move_to_new_page_psychologist_schedule()
    authorization_page.verify_url_psychologist_schedule_page()

# 94 - проверка перехода на карточку психолога при клике на его имя из чата клиента
def test_click_psychologist_name_opens_psychologist_schedule_from_client_chat(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_email()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.move_to_chat_w_psychologist()
    authorization_page.click_my_psychologist_name_chat()
    authorization_page.move_to_new_page_psychologist_schedule()
    authorization_page.verify_url_psychologist_schedule_page()

# 95 - проверка смена статуса цели на "В работе" из лк клиента
def test_change_aim_status_in_progeress_client(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_email()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.click_aims_menu_client()
    authorization_page.click_aim_2_client_account()
    authorization_page.click_aim_2_status_client_account()
    authorization_page.select_aim_status_in_progress_client_account()
    authorization_page.click_save_aim_changes_client_account()
    authorization_page.verify_aim_status_in_progress_client()

# 96 - проверка смена статуса цели на "Завершена" из лк клиента
def test_change_aim_status_completed_client(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_email()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.click_aims_menu_client()
    authorization_page.click_aim_2_client_account()
    authorization_page.click_aim_2_status_client_account()
    authorization_page.select_aim_status_completed_client_account()
    authorization_page.click_save_aim_changes_client_account()
    authorization_page.verify_aim_status_completed_client()

# 97 - проверка смена статуса цели на "Создана" из лк клиента
def test_change_aim_status_created_client(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_email()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.click_aims_menu_client()
    authorization_page.click_aim_2_client_account()
    authorization_page.click_aim_2_status_client_account()
    authorization_page.select_aim_status_created_client_account()
    authorization_page.click_save_aim_changes_client_account()
    authorization_page.verify_aim_status_created_client()

# 98 - проверка удаления цели из лк клиента
def test_remove_aim_client(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_email()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.click_aims_menu_client()
    authorization_page.click_aim_2_client_account()
    authorization_page.click_remove_aim_button_client_account()
    authorization_page.verify_url_client_aims_list_page()

# 99 - проверка смена статуса цели на "В работе" из лк психолога
def test_change_aim_status_in_progress_psychologist(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_psychologist()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.click_to_clients_and_aims_menu_psychologist()
    authorization_page.select_aygul_clients_and_aims_menu_psychologist()
    authorization_page.click_aim_2_client_account()
    authorization_page.click_aim_2_status_client_account()
    authorization_page.select_aim_status_in_progress_client_account()
    authorization_page.click_save_aim_changes_client_account()
    authorization_page.verify_aim_status_in_progress_client()

# 100 - проверка смена статуса цели на "Завершена" из лк психолога
def test_change_aim_status_completed_psychologist(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_psychologist()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.click_to_clients_and_aims_menu_psychologist()
    authorization_page.select_aygul_clients_and_aims_menu_psychologist()
    authorization_page.click_aim_2_client_account()
    authorization_page.click_aim_2_status_client_account()
    authorization_page.select_aim_status_completed_client_account()
    authorization_page.click_save_aim_changes_client_account()
    authorization_page.verify_aim_status_completed_client()

# 101 - проверка смена статуса цели на "Создана" из лк психолога
def test_change_aim_status_created_psychologist(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_psychologist()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.click_to_clients_and_aims_menu_psychologist()
    authorization_page.select_aygul_clients_and_aims_menu_psychologist()
    authorization_page.click_aim_2_client_account()
    authorization_page.click_aim_2_status_client_account()
    authorization_page.select_aim_status_created_client_account()
    authorization_page.click_save_aim_changes_client_account()
    authorization_page.verify_aim_status_created_client()

# 102 - проверка удаления цели из лк психолога
def test_remove_aim_psychologist(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_psychologist()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.click_to_clients_and_aims_menu_psychologist()
    authorization_page.select_aygul_clients_and_aims_menu_psychologist()
    authorization_page.click_aim_2_client_account()
    authorization_page.click_remove_aim_button_client_account()
    authorization_page.verify_url_psychologist_aims_list_page()

# 103 - Проверка сообщения "Такого сертификата не существует" при вводе неправильного номера сертификата
def test_activate_certificate_client(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_email()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.click_my_balance_menu_navigation()
    authorization_page.click_activate_certificate_button_client_my_balance()
    authorization_page.set_false_certificate_code()
    authorization_page.click_activate_certificate_button_client_after_code_input()
    authorization_page.verify_error_certificate_doesnot_exist_text()

# 104 - Проверяем соответствие первого слота для быстрой записи и первого слота в расписании психолога
# (при переходе на карточку психолога через три точки - записаться повторно)
def test_equal_rapid_first_order_time(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_email()
    authorization_page.set_password_pass()
    authorization_page.click_to_authorize_button()
    authorization_page.click_to_three_dots_psychologists_name()
    authorization_page.click_order_session_again_three_dots_menu_btn_client()
    authorization_page.verify_rapid_first_order_time()

# 105 - проверка появления сообщения об ошибке "Неправильный номер" при вводе номера из 10 цифр, но не сообщения "Телефон слишком короткий"
def test_10_numbers_phone_rapid_auth_page(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.set_10_numbers_phone_number()
    authorization_page.click_first_checkbox()
    authorization_page.click_get_code_btn()
    authorization_page.verify_10number_phone_not_short_rapid_auth_page()

# 105 - проверка появления сообщения об ошибке "Неправильный номер" при вводе номера из 14 цифр, но не сообщения "Телефон слишком длинный"
def test_14_numbers_phone_rapid_auth_page(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.set_14_numbers_phone_number()
    authorization_page.click_first_checkbox()
    authorization_page.click_get_code_btn()
    authorization_page.verify_14number_phone_not_long_rapid_auth_page()

# 81 - переход авторизованного клиента с главной страницы в лк по клику на аватар
# def test_psychologist_video_page(authorization_page):
#     authorization_page.click_to_login_button()
#     authorization_page.click_to_login_w_password_button()
#     authorization_page.set_email_email()
#     authorization_page.set_password_pass()
#     authorization_page.click_to_authorize_button()
#     authorization_page.click_to_get_psychologists_btn_client_menu()

# 82 - проверка наличия Елены Калкан в подборе анкеты Парной консультации - Сложности в отношениях
# def test_video_questionnaire_paired_elena(authorization_page):
#     authorization_page.click_get_psychologist_btn()
#     authorization_page.click_paired_consultation_button_questionnaire()
#     authorization_page.set_age_field_questionnaire()
#     authorization_page.click_personal_questions_title()
#     authorization_page.click_difficulties_in_relationship_paired_consultation_button_questionnaire()
#     authorization_page.click_psychologist_preferences_title_questionnaire()
#     authorization_page.click_age_over_30_questionnaire()
#     authorization_page.click_select_psychologist_title_questionnaire()
#     authorization_page.click_elena_kalkan_name()


# 79 - проверка записи по акции (не работает выбор времени и скролл до кнопки Перейти к оплате - element click intercepted)
# def test_action_session_pathway(authorization_page):
#     authorization_page.click_to_login_button()
#     authorization_page.click_to_login_w_password_button()
#     authorization_page.set_phone_password_authorization()
#     authorization_page.set_password_pass()
#     authorization_page.click_to_authorize_button()
#     authorization_page. click_select_psychologist_button_action()
#     authorization_page.scroll_till_bottom_schedule_page()
    # authorization_page.click_select_psychologist_time_action_schedule()

#78 - не работает переход с личных вопросов на предпочтения к психологу
# def test_personal_questions_questionnaire(authorization_page):
#     authorization_page.click_get_psychologist_btn()
#     authorization_page.set_age_field_questionnaire()
#     authorization_page.click_personal_questions_title()
#     authorization_page.click_psychologist_preferences_title_questionnaire()
#     authorization_page.select_stress_questionnaire()
#     authorization_page.scroll_to_next_button_questionnaire()
#     authorization_page.click_next_button_questionnaire()
#     authorization_page.verify_error_text_no_personal_questions_questionnaire()






# 37 -
# def test_action_order(authorization_page):
#     authorization_page.click_to_login_button()
#     authorization_page.click_to_login_w_password_button()
#     authorization_page.set_email_email()
#     authorization_page.set_password_pass()
#     authorization_page.click_to_authorize_button()
#     authorization_page.scroll_to_select_psychologist_action()
#     # authorization_page.click_to_select_psychologyst_button_action()
#     authorization_page.scroll_to_payment_button_psychologist_action_page()
#     authorization_page.select_time_action_schedule_psychologist()
# authorization_page.scroll_till_go_to_payment_button_psychologyst_schedule()





    

# # 16 - проверка наличия Анны Капу в подборе анкеты Инд50-Рус-Стресс
# def test_questionnaire_stress_registered_user(authorization_page):
#     authorization_page.click_get_psychologist_btn()
#     authorization_page.set_age_field_questionnaire()
#     authorization_page.click_personal_questions_title()
#     authorization_page.select_stress_questionnaire()
#     authorization_page.click_psychologist_preferences_title_questionnaire()
#     authorization_page.click_age_over_30_questionnaire()
#     authorization_page.click_select_psychologist_title_questionnaire()
#     authorization_page.select_time_session_main_schedule_psychologist()
#     authorization_page.click_3rd_time_pankova_schedule_page()


# - наличие рекапчи на странице авторизации
# def test_presence_recaptcha_rapid_auth(authorization_page):
#     authorization_page.click_to_login_button()
#     authorization_page.verify_confidentiality_recaptcha_auth_page_title()

# 52 - проверка перехода на страницу Skype для звонка в службу поддержку - не получается закрыть alert-окно
# def test_call_skype_help(authorization_page):
#     authorization_page.click_phone_number_skype_button()

# 48 - (дубль покупки повторной сессии) переход на страницу оплаты при клике "Нет, продолжить покупку" на странице заказа страницы
# def test_move_to_payment_from_order_page_by_click_no(authorization_page):
#     authorization_page.click_to_login_button()
#     authorization_page.click_to_login_w_password_button()
#     authorization_page.set_email_email()
#     authorization_page.set_password_pass()
#     authorization_page.click_to_authorize_button()
#     authorization_page.click_terminated_sessions_title()
#     authorization_page.click_order_session_again_button()
#     authorization_page.select_time_session_schedule_psychologist()
#     authorization_page.click_rapid_go_payment_btn()
#     authorization_page.click_card_rf_button_session()
#     authorization_page.click_pay_online_button_session()
#     authorization_page.click_no_continue_payment_button_order_page()
#     authorization_page.verify_location_cloudpayments_page()



# 49 - проверка записи к Елене Калкан (Парной консультации - Сложности в отношениях) нового
# def test_new_user_ordered_session_Kapu(authorization_page):
#     authorization_page.click_get_psychologist_btn()
#     authorization_page.set_age_field_questionnaire()
#     authorization_page.click_personal_questions_title()
#     authorization_page.select_stress_questionnaire()
#     authorization_page.click_psychologist_preferences_title_questionnaire()
#     authorization_page.click_age_over_30_questionnaire()
#     authorization_page.click_select_psychologist_title_questionnaire()
#     authorization_page.scroll_to_3rd_rapid_time_button_pankova_schedule()
#     authorization_page.click_3rd_time_pankova_schedule_page()







# #26 - проверка, что клик на знак Телеграмма в соц.сетях открывает в соседней
# # вкладке группу Life Helpв Тг
# # не проходит скролл до футера и не находит элементы в футере страницы
# def test_click_opens_telegram_group(authorization_page):
#     authorization_page.click_to_accept_cookies()
#     authorization_page.scroll_to_footer()
#     authorization_page.click_to_telegram_group_network_footer()
#     authorization_page.move_to_new_telegram_care_page()
#     authorization_page.verify_url_telegram_care_page()
#
#
# # 27 - проверка, что клик на знак документ согласия открывает в соседней вкладке переписку в Whatsapp
# def test_click_opens_document_consent_mailing(authorization_page):
#     authorization_page.click_to_accept_cookies()
#     authorization_page.scroll_to_footer()
#     authorization_page.click_to_consent_mailing_name_footer_bottom()
#     authorization_page.move_to_new_page_w_consent_mailing_document()
#     authorization_page.get_url("https://life-help.ru/consent-mailing/")

    # authorization_page.scroll_to_main_page_footer()



#  проверка некликабельности кнопки на странице регистрации
# def test_register_button_is_not_clickable_wo_filling_form(authorization_page):
#      authorization_page.click_to_login_button()
#      authorization_page.click_to_login_w_password_button()
#      authorization_page.click_register_hypertext()
#      authorization_page.verify_button_is_not_clickable()












