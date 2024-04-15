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

case_1 = ['test_user@gmail.com', 'lifehelp1@', 'https://life-help.ru/user/notes']
case_2 = ['79520445533', 'lifehelp1@', 'https://life-help.ru/doctor/sessions']


@pytest.mark.parametrize('first, second, third', (case_1, case_2),
                             ids=['success_login_user', 'success_login_psychologist'])
def test_authorization(authorization_page, first, second, third):
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
    authorization_page.login_user_email_password()
    authorization_page.click_logout_btn()
    authorization_page.click_to_login_button()
    authorization_page.verify_url_authorization_page()

# 6 - проверка выхода из лк психолога
def test_logout_psychologist(authorization_page):
    authorization_page.login_as_psychologist()
    authorization_page.click_logout_btn()
    authorization_page.click_to_login_button()
    authorization_page.verify_url_authorization_page()

# 7 - проверка работы чата в лк клиента
def test_client_chat (authorization_page):
    authorization_page.login_user_email_password()
    authorization_page.move_to_chat_w_psychologist()
    authorization_page.type_greeting_chat_field()
    authorization_page.click_btn_send_msg_chat()
    authorization_page.verify_successful_send_msg_chat()

# 8 - проверка работы чата в лк психолога
def test_psychologist_chat (authorization_page):
    authorization_page.login_as_psychologist()
    authorization_page.move_to_chat_w_client()
    authorization_page.select_chat_w_client()
    authorization_page.type_greeting_chat_field_psychologist()
    authorization_page.click_btn_send_msg_chat()
    authorization_page.verify_successful_send_msg_chat_psychologist()

# 11 - переход из лк клиента на главную страницу по клику на логотип страницы
def test_logo_redirect(authorization_page):
    authorization_page.login_user_email_password()
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

# 12a - покупка пакета из лк клиента картой РФ (Tinkoff касса) из Мой баланс - путь закрыт
# def test_buy_package_4_tinkoff_kassa(authorization_page):
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
#     authorization_page.verify_location_tinkoff_kassa_page_rapid_pay()

# 13 - покупка пакета из лк клиента иностранной картой (Prodamus) из Мой баланс - путь закрыт
# def test_buy_package_4_prodamus(authorization_page):
#     authorization_page.click_to_login_button()
#     authorization_page.click_to_login_w_password_button()
#     authorization_page.set_email_email()
#     authorization_page.set_password_pass()
#     authorization_page.click_to_authorize_button()
#     authorization_page.click_my_balance_menu_navigation()
#     authorization_page.click_buy_package()
#     authorization_page.click_buy_package_4_sessions()
#     authorization_page.click_foreign_card_button_package()
#     authorization_page.click_pay_online_button_package()
#     authorization_page.verify_whatsapp_care_page()
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
    authorization_page.login_user_phone_password()
    authorization_page.click_terminated_sessions_title()
    authorization_page.click_order_session_again_button()
    authorization_page.select_2nd_time_session_rapid_schedule_psychologist()
    authorization_page.click_rapid_go_payment_btn()
    authorization_page.click_orange_pay_button()
    authorization_page.verify_location_tinkoff_kassa_page_rapid_pay()

# # 15 - запись на повторный сеанс из завершенных сессий - иностр.карта
def test_client_second_session_order_foreign_card (authorization_page):
    authorization_page.login_user_phone_password()
    authorization_page.click_terminated_sessions_title()
    authorization_page.click_order_session_again_button()
    authorization_page.select_2nd_time_session_rapid_schedule_psychologist()
    authorization_page.click_rapid_go_payment_btn()
    authorization_page.click_foreign_card_button()
    authorization_page.click_orange_pay_button()
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

#27a - проверка - изначально введенные значения в поле "Пароль" скрытые
def test_hidden_state_password_authorization_form(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_password_pass()
    authorization_page.verify_hidden_type_password_field()


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
    authorization_page.login_user_phone_password()
    authorization_page.click_terminated_sessions_title()
    authorization_page.click_order_session_again_button()
    authorization_page.select_2nd_time_session_rapid_schedule_psychologist()
    authorization_page.click_rapid_go_payment_btn()
    authorization_page.click_to_user_avatar_button_psychologist_page()
    authorization_page.verify_session_status_waits_payment()

# 32 - перенос авт. брони при незавершенной оплате при записи на повторный сеанс из завершенных сессий - Cloudpayments
def test_reschedule_automatic_order(authorization_page):
    authorization_page.login_user_phone_password()
    authorization_page.click_to_three_dots_button_ordered_session()
    authorization_page.click_to_reschedule_ordered_session_drop_down()
    authorization_page.select_seventh_time_to_reschedule_order()
    authorization_page.click_to_change_time_button_to_reschedule_order()
    authorization_page.get_url('https://life-help.ru/user/notes')

# 33 - отмена авт. брони при незавершенной оплате при записи на повторный сеанс из завершенных сессий - Cloudpayments
def test_deny_payment_automatic_order(authorization_page):
    authorization_page.login_user_phone_password()
    authorization_page.click_to_three_dots_button_ordered_session()
    authorization_page.click_to_deny_payment_ordered_session_drop_down()
    authorization_page.click_to_yes_deny_payment_button_to_deny_order()
    authorization_page.click_to_good_button_after_deny_order()
    # authorization_page.verify_absence_order()

# 37 - проверка применения промокода uno на полную стоимость сеанса при повторной записи
def test_full_price_promocode(authorization_page):
    authorization_page.login_user_bitrix_password()
    authorization_page.click_terminated_sessions_title()
    authorization_page.click_order_session_again_button()
    authorization_page.select_2nd_time_session_rapid_schedule_psychologist()
    authorization_page.click_rapid_go_payment_btn()
    authorization_page.enter_free_promo_session_order_page()
    authorization_page.click_to_apply_promocode_btn_order_page()
    authorization_page.verify_price_0_rubbles_btn_order_page_after_promo()

# 37 - проверка применения промокода priprava на частичную стоимость сеанса при повторной записи
def test_partial_price_promocode(authorization_page):
    authorization_page.login_user_bitrix_password()
    authorization_page.click_terminated_sessions_title()
    authorization_page.click_order_session_again_button()
    authorization_page.select_2nd_time_session_rapid_schedule_psychologist()
    authorization_page.click_rapid_go_payment_btn()
    authorization_page.enter_partial_promo_session_order_page()
    authorization_page.click_to_apply_promocode_btn_order_page()
    authorization_page.verify_price_10_rubbles_btn_order_page_after_priprava_promocode()

# 38 - запись на сеанс в пакете
def test_order_session_in_package_4(authorization_page):
    authorization_page.login_user_email_password()
    authorization_page.click_my_balance_menu_navigation()
    authorization_page.scroll_to_empty_element_order_session_package()
    authorization_page.click_to_order_session_package()
    authorization_page.select_time_to_order_session_package()
    authorization_page.submit_selected_time_to_order_session_package()
    authorization_page.verify_presence_ordered_session_package()

# 45 - Проверка открытия страницы службы заботы в Whatsapp при клике на «Помощь в подборе» после анкеты
def test_questionnaire_help_care_page(authorization_page):
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


# 46 - проверка создания цели в лк клиента - перенести
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

# 49 - переход к оформлению рассрочки Тинькофф при покупке пакета 54 из лк клиента
def test_buy_package_54_w_tinkoff(authorization_page):
    authorization_page.login_user_bitrix_password()
    authorization_page.click_terminated_sessions_title()
    authorization_page.click_order_session_again_button()
    authorization_page.select_2nd_time_session_rapid_schedule_psychologist()
    authorization_page.click_rapid_go_payment_btn()
    authorization_page.click_package_54_order_page()
    authorization_page.click_package_54_12_month_installment_order_page()
    authorization_page.move_to_new_tinkoff_installments_page()
    authorization_page.verify_tinkoff_installments_application_page_conditions()

# 50 - проверка покупки сеанса "Записаться повторно" с помощью пакета (путь без страницы заказа)
def test_pay_buy_session_by_package(authorization_page):
    authorization_page.login_user_email_password()
    authorization_page.click_terminated_sessions_title()
    authorization_page.click_order_session_again_button()
    authorization_page.select_2nd_time_session_rapid_schedule_psychologist()
    authorization_page.click_rapid_go_payment_btn()
    authorization_page.verify_successful_session_payment_by_package()

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

# 72а - проверка названия платежа на странице оплаты пакета из лк клиента картой РФ (Tinkoff kassa)
def test_package_4_name_tinkoff_page(authorization_page):
    authorization_page.login_user_phone_password()
    authorization_page.click_terminated_sessions_title()
    authorization_page.click_order_session_again_button()
    authorization_page.select_2nd_time_session_rapid_schedule_psychologist()
    authorization_page.click_rapid_go_payment_btn()
    authorization_page.click_package_4_order_page()
    authorization_page.click_orange_pay_button()
    authorization_page.verify_location_tinkoff_kassa_page_rapid_pay()

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
    authorization_page.login_user_email_password()
    authorization_page.click_go_to_payed_session_btn()
    authorization_page.click_to_reschedule_session_time_btn()
    authorization_page.select_seventh_time_to_reschedule_order()
    authorization_page.click_to_change_time_button_to_reschedule_order()
    authorization_page.get_url('https://life-help.ru/user/notes')

# 75 - отмена оплаченной сессии по клику на кнопку "Перейти к сеансу" - "Отменить сеанс"
def test_deny_paied_session(authorization_page):
    authorization_page.login_user_email_password()
    authorization_page.click_go_to_payed_session_btn()
    authorization_page.click_to_deny_payed_session_btn()
    authorization_page.click_to_yes_deny_payed_session_btn()
    authorization_page.verify_modal_confirmation_message_session_denied()

# 76 - При отмене "отменить сеанс" (через "Перенести сеанс")пользователь возвращается на страницу ожидания видеосеанса
def test_not_terminated_deny_paied_session(authorization_page):
    authorization_page.login_user_email_password()
    authorization_page.click_go_to_payed_session_btn()
    authorization_page.click_to_deny_payed_session_btn()
    authorization_page.click_do_not_deny_btn_package_session()
    authorization_page.verify_name_video_sesion_page_heading()

# 77 - поменять психолога при записи на сеанс в пакете
def test_change_psychologist_during_order_session_in_package_4(authorization_page):
    authorization_page.login_user_email_password()
    authorization_page.click_my_balance_menu_navigation()
    authorization_page.scroll_to_empty_element_order_session_package()
    authorization_page.click_to_order_session_package()
    authorization_page.click_to_select_new_doctor_btn_package_session()
    authorization_page.verify_url_questionnaire_page()

# 78 - оплата брони пакетом (короткий путь без страницы заказа)
def test_buy_order_by_package_short_pathway(authorization_page):
    authorization_page.login_user_email_password()
    authorization_page.click_to_pay_btn_order_my_schedule_page()
    authorization_page.verify_successful_session_payment_by_package()

#79 - проверка перехода на страницу Регулярное расписание по клику на 3 точки - регулярное расписание
def test_regular_session_order_schedule(authorization_page):
    authorization_page.login_user_bitrix_password()
    authorization_page.click_to_three_dots_button_ordered_session()
    authorization_page.click_regular_session_order_dropdown_menu_list()

# 80 - переход авторизованного клиента с главной страницы в лк по клику на аватар
def test_avatar_redirect_from_main_page_to_account(authorization_page):
    authorization_page.login_user_email_password()
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

# 83 - проверка перехода в чат с психологом по клику на 3 точки напротив имени психолога в лк клиента - Мое расписание
def test_client_three_dots_go_to_chat (authorization_page):
    authorization_page.login_user_email_password()
    authorization_page.click_to_three_dots_psychologists_name()
    authorization_page.click_go_to_chat_three_dots_menu_client()
    authorization_page.move_to_chat_w_psychologist_page()
    authorization_page.verify_chats_w_psychologist_page_title()

# 84 - проверка перехода на расписание психолога по клику на 3 точки-Записаться повторно в лк клиента - Мое расписание
def test_client_three_dots_go_to_psychologist_schedule (authorization_page):
    authorization_page.login_user_phone_password()
    authorization_page.click_to_three_dots_psychologists_name()
    authorization_page.click_order_session_again_three_dots_menu_btn_client()
    authorization_page.verify_url_psychologist_page_order_session_again()

#87 - наличие модального окна с предупреждением о невозврате оплаты при отмене сеанса, если осталось менее 12ч
def test_deny_paied_session_modal_window(authorization_page):
    authorization_page.login_user_email_password()
    authorization_page.click_go_to_payed_session_btn()
    authorization_page.click_to_deny_payed_session_btn()
    authorization_page.verify_modal_window_caution_refund_session_denied()

#88 - проверка - закрыть модальное окно с предупреждением о невозврате оплаты при отмене сеанса кликом
# за пределами модального окна
def test_deny_paied_session_outside_modal_window(authorization_page):
    authorization_page.login_user_email_password()
    authorization_page.click_go_to_payed_session_btn()
    authorization_page.click_to_deny_payed_session_btn()
    authorization_page.click_click_outside_deny_payed_session_modal_window()
    authorization_page.verify_title_page_timer_before_session()

#89 - проверка - закрыть модальное окно с предупреждением о невозврате оплаты при отмене сеанса кликом
# на крестик в верхнем правом углу модального окна
def test_deny_paied_session_cross_btn_modal_window(authorization_page):
    authorization_page.login_user_email_password()
    authorization_page.click_go_to_payed_session_btn()
    authorization_page.click_to_deny_payed_session_btn()
    authorization_page.click_cross_to_close_modal_window_deny_payed_session()
    authorization_page.verify_title_page_timer_before_session()

# 90 - перенос оплаченной сессии по клику 3 точки - "Перенести сеанс" - пользователь без рег.расписания
def test_reschedule_payed_session_three_dots(authorization_page):
    authorization_page.login_user_email_password()
    authorization_page.click_to_three_dots_button_ordered_session()
    authorization_page.click_to_reschedule_payed_session_drop_down()
    authorization_page.select_seventh_time_to_reschedule_order()
    authorization_page.click_to_change_time_button_to_reschedule_order()
    authorization_page.get_url('https://life-help.ru/user/notes')

# 91 - проверка перехода в лк Мое расписание по клику на стрелку над окном ожидания видеосеанса
def test_back_to_my_schedule_page_from_video_by_arrow_btn_click(authorization_page):
    authorization_page.login_user_email_password()
    authorization_page.click_go_to_payed_session_btn()
    authorization_page.click_to_arrow_button_to_back_from_videosession_page_to_my_schedule_page()
    authorization_page.get_url('https://life-help.ru/user/notes')

# 92 - перенос оплаченной сессии по клику 3 точки - "Перенести сеанс" пользователь с рег.расписанием
def test_reschedule_payed_session_three_dots_reg_schedule(authorization_page):
    authorization_page.login_user_bitrix_password()
    authorization_page.click_to_three_dots_button_ordered_session()
    authorization_page.click_to_reschedule_payed_session_drop_down()
    authorization_page.click_to_reschedule_only_this_session_button()
    authorization_page.select_seventh_time_to_reschedule_order()
    authorization_page.click_to_change_time_button_to_reschedule_order()
    authorization_page.get_url('https://life-help.ru/user/notes')

# 93 - проверка перехода на карточку психолога при клике на его имя из лк клиента-мое расписание-мой психолог
def test_click_psychologist_name_opens_psychologist_schedule_from_client_account(authorization_page):
    authorization_page.login_user_email_password()
    authorization_page.click_my_psychologist_name()
    authorization_page.move_to_new_page_psychologist_schedule()
    authorization_page.verify_url_psychologist_schedule_page()

# 94 - проверка перехода на карточку психолога при клике на его имя из чата клиента
def test_click_psychologist_name_opens_psychologist_schedule_from_client_chat(authorization_page):
    authorization_page.login_user_email_password()
    authorization_page.move_to_chat_w_psychologist()
    authorization_page.click_my_psychologist_name_chat()
    authorization_page.move_to_new_page_psychologist_schedule()
    authorization_page.verify_url_psychologist_schedule_page()

# 95 - проверка смена статуса цели на "В работе" из лк клиента
def test_change_aim_status_in_progeress_client(authorization_page):
    authorization_page.login_user_email_password()
    authorization_page.click_aims_menu_client()
    authorization_page.click_aim_2_client_account()
    authorization_page.click_aim_2_status_client_account()
    authorization_page.select_aim_status_in_progress_client_account()
    authorization_page.click_save_aim_changes_client_account()
    authorization_page.verify_aim_status_in_progress_client()

# 96 - проверка смена статуса цели на "Завершена" из лк клиента
def test_change_aim_status_completed_client(authorization_page):
    authorization_page.login_user_email_password()
    authorization_page.click_aims_menu_client()
    authorization_page.click_aim_2_client_account()
    authorization_page.click_aim_2_status_client_account()
    authorization_page.select_aim_status_completed_client_account()
    authorization_page.click_save_aim_changes_client_account()
    authorization_page.verify_aim_status_completed_client()

# 97 - проверка смена статуса цели на "Создана" из лк клиента
def test_change_aim_status_created_client(authorization_page):
    authorization_page.login_user_email_password()
    authorization_page.click_aims_menu_client()
    authorization_page.click_aim_2_client_account()
    authorization_page.click_aim_2_status_client_account()
    authorization_page.select_aim_status_created_client_account()
    authorization_page.click_save_aim_changes_client_account()
    authorization_page.verify_aim_status_created_client()

# 98 - проверка удаления цели из лк клиента
def test_remove_aim_client(authorization_page):
    authorization_page.login_user_email_password()
    authorization_page.click_aims_menu_client()
    authorization_page.click_aim_2_client_account()
    authorization_page.click_remove_aim_button_client_account()
    authorization_page.verify_url_client_aims_list_page()

# 103 - Проверка сообщения "Такого сертификата не существует" при вводе неправильного номера сертификата
def test_set_wrong_certificate_number_error_msg_by_activation_client(authorization_page):
    authorization_page.login_user_email_password()
    authorization_page.click_my_balance_menu_navigation()
    authorization_page.click_activate_certificate_button_client_my_balance()
    authorization_page.set_false_certificate_code()
    authorization_page.click_activate_certificate_button_client_after_code_input()
    authorization_page.verify_error_certificate_doesnot_exist_text()

# 104 - Проверяем соответствие первого слота для быстрой записи и первого слота в расписании психолога
# (при переходе на карточку психолога через три точки - записаться повторно)
def test_equal_rapid_first_order_time(authorization_page):
    authorization_page.login_user_phone_password()
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

# 106 - проверка стоимости консультации 2950 на странице заказа (новая цена)
def test_price_session_2950_order_page(authorization_page):
    authorization_page.login_user_bitrix_password()
    authorization_page.click_terminated_sessions_title()
    authorization_page.click_order_session_again_button()
    authorization_page.select_2nd_time_session_rapid_schedule_psychologist()
    authorization_page.click_rapid_go_payment_btn()
    authorization_page.verify_session_price_2950_rubbles_order_page()

#107 - проверка наличия и открывания пользовательского соглашения на странице авторизации, 1-ый чекбокс
def test_contract_offer_auth_page(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_contract_offer_auth_page()
    authorization_page.move_to_new_page()
    authorization_page.verify_url_contract_offer_page()

#108 - проверка наличия и открывания согласия на обработку персональных данных на странице авторизации, 1-ый чекбокс
def test_agreement_auth_page(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_agreement_auth_page()
    authorization_page.move_to_new_page()
    authorization_page.verify_url_agreement_page()

#109 - проверка наличия и открывания согласие на информационную рассылку на странице авторизации, 2-ой чекбокс
def test_consent_mailing_auth_page(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_consent_mailing_auth_page()
    authorization_page.move_to_new_page()
    authorization_page.verify_url_consent_mailing_page()

#110 - проверка стоимости консультации инд50 "2 950 ₽" на странице анкеты Общие вопросы
def test_price_2950_questionnaire_general(authorization_page):
    authorization_page.click_get_psychologist_btn()
    authorization_page.verify_session_price_2950_rubbles_questionnaire_general_page()

# 111 - Enter вместо кнопки "Получить код" на странице авторизации с кодом смс
def test_enter_to_get_code_authorization_page(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.set_phone_number()
    authorization_page.click_first_checkbox()
    authorization_page.enter_instead_click_get_code_btn()
    authorization_page.verify_appearance_set_code_field()


# 112 - Enter вместо кнопки "Получить код" на странице авторизации с паролем
def test_enter_instead_login_btn_w_pass_auth_page(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_bitrix_email()
    authorization_page.set_password_pass()
    authorization_page.enter_instead_click_to_authorize_button()
    authorization_page.verify_url_user_account()

# 113 - Проверка перехода на страницу заказа после анкеты (для инд50, стресс) для авторизованного клиента
def test_move_to_order_page_authorized_user_after_questionnaire(authorization_page):
    authorization_page.login_user_email_password()
    authorization_page.click_to_btn_find_psychologist_account_page()
    authorization_page.click_personal_questions_title()
    authorization_page.click_select_psychologist_title_questionnaire()
    authorization_page.click_first_rapid_time_choose_doctor_page()
    authorization_page.scroll_till_btn_order_rapid_time_psychologist_schedule()
    authorization_page.click_to_btn_order_rapid_time_choose_doctor_page()
    authorization_page.verify_order_page_title()

# 116 - проверка после обновления страницы после ввода номера телефона и выбора чекбокса все сбрасывается
def test_refresh_auth_page_w_phone_checkbox(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.set_phone_number()
    authorization_page.click_first_checkbox()
    authorization_page.refresh_page()
    authorization_page.click_get_code_btn()
    authorization_page.verify_red_phonefield_wo_phonenumber_auth_page()

# 117 - проверка - при обновлении страницы с введенными логин и паролем пользователь остается на странице авторизации
def test_refresh_page_w_login_password(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.set_email_psychologist()
    authorization_page.set_password_pass()
    authorization_page.refresh_page()
    authorization_page.get_page_url()

# 118 - проверка - клик на гипертекст "зарегистрироваться" на странице авторизации с паролем
# ведет на страницу регеистрации
def test_register_btn_leads_registration_page(authorization_page):
    authorization_page.click_to_login_button()
    authorization_page.click_to_login_w_password_button()
    authorization_page.click_to_btn_register_auth_page()
    authorization_page.get_url('https://life-help.ru/registration/')









