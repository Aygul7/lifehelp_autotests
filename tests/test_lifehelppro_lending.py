import allure
import pytest




# 1 - Проверка - клик по кнопке "Подобрать психолога" в правом верхнем углу страницы ведет на начальную страницу анкеты
def test_find_psychologist_btn_leads_questionnaire(lifehelp_pro_page):
    lifehelp_pro_page.click_to_find_psychologist_upper_1st_btn()
    lifehelp_pro_page.move_to_page_bottom()
    # lifehelp_pro_page.verify_title_general_questions_questionnaire()

# 2 - Проверка - клик по кнопке "Хочу попробовать" ведет на начальную страницу анкеты
def test_want_to_try_btn_leads_questionnaire(lifehelp_pro_page):
    lifehelp_pro_page.click_to_want_to_try_btn()
    lifehelp_pro_page.move_to_page_bottom()
    # lifehelp_pro_page.verify_text_ind50_general_questions_questionnaire()

# 3 - Проверка - клик по кнопке "Войти" в правом верхнем углу страницы ведет на страницу авторизации
def test_to_login_btn_leads_auth_page(lifehelp_pro_page):
    lifehelp_pro_page.click_to_login_btn()
    lifehelp_pro_page.get_url('https://life-help.ru/auth/?utm_source=veb.life-help.pro&utm_medium=&utm_campaign=&utm_'
                              'content=&utm_term=%C2%A0')

# 4 - Проверка - клик по кнопке "Подобрать психолога" в меню страницы ведет
# на блок "Получите экспресс-диагностику бесплатно"
def test_to_get_psychologist_menu_list_opens_questionnaire_page(lifehelp_pro_page):
    lifehelp_pro_page.click_to_menu_btn()
    lifehelp_pro_page.click_to_get_psychologist_btn_menu_list()
    # lifehelp_pro_page.verify_text_ind50_general_questions_questionnaire()

# 5 - Проверка - клик по кнопке "Купить сертификат" в меню страницы ведет на страницу предложения подарочных сертификатов
def test_to_buy_certificate_menu_list_opens_certificate_offer_page(lifehelp_pro_page):
    lifehelp_pro_page.click_to_menu_btn()
    lifehelp_pro_page.click_to_buy_certificate_btn_menu_list()
    lifehelp_pro_page.get_url('https://lifehelp.pro/gifts?utm_campaign=&utm_content=&utm_source=&utm_medium=&utm_term=&roistat=')

# 6 - Проверка - клик по кнопке "Подобрать психолога" под блоком с темами запросов ведет на страницу анкеты
def test_therapy_queries_move(lifehelp_pro_page):
    lifehelp_pro_page.scroll_to_therapy_queries_unit()
    lifehelp_pro_page.click_to_get_psychologist_btn_under_therapy_queries_unit()

# 7 - Проверка - клик по кнопке "Получить диагностику" под блоком "получить диагностику бесплатно" ведет на форму
# заявки на 20минутку
def test_apply_diagnostic_request(lifehelp_pro_page):
    lifehelp_pro_page.scroll_to_how_it_works_unit()
    lifehelp_pro_page.click_to_get_diagnostic_btn_under_how_it_works_unit()
    lifehelp_pro_page.click_to_leave_credentials_btn_diagnostic_application_form()
    lifehelp_pro_page.set_name_application_form_for_diagnostic()
    lifehelp_pro_page.set_phone_application_form_for_diagnostic()
    lifehelp_pro_page.click_to_apply_psychologist_request_btn_diagnostic_application_form()
    lifehelp_pro_page.verify_successful_application_notification_text()

# 8 - Проверка - клик по кнопке "Подобрать психолога" под блоком "Почему клиенты выбирают LH" ведет на анкету
def test_get_psychologst_btn_under_unit_why_users_prefer_lh(lifehelp_pro_page):
    lifehelp_pro_page.scroll_to_block_stability_warranty_title()
    lifehelp_pro_page.click_to_get_psychologist_btn_under_unit_why_users_prefer_lh()

# 9 - Проверка - клик по кнопке "Заполнить анкету" под блоком "Как начать" ведет на анкету
def test_fill_questionnaire_btn_under_users_steps_description_unit_opens_questionnaire(lifehelp_pro_page):
    lifehelp_pro_page.scroll_to_title_order_time_in_users_steps_description()
    lifehelp_pro_page.click_to_fill_questionnaire_btn_under_users_step_description_unit()

# 10 - Проверка - клик по кнопке "Записаться на диагностику" под блоком "Как начать" и “Оставить свои контакты для
# связи” приводит к отправке заявки на 20минутку
def test_apply_diagnostic_request_btn_under_users_steps_description_unit_opens_application_form(lifehelp_pro_page):
    lifehelp_pro_page.scroll_to_title_order_time_in_users_steps_description()
    lifehelp_pro_page.click_to_apply_diagnostic_btn_under_users_step_description_unit()
    lifehelp_pro_page.click_to_leave_credentials_btn_diagnostic_application_form()
    lifehelp_pro_page.set_name_application_form_for_diagnostic()
    lifehelp_pro_page.set_phone_application_form_for_diagnostic()
    lifehelp_pro_page.click_to_apply_psychologist_request_btn_diagnostic_application_form()
    lifehelp_pro_page.verify_successful_application_notification_text()

# 11 - Проверка - клик по кнопке "Записаться в Whatsapp" в форме заявки на 20минутку ведет на страницу Whatsapp
# службы заботы
def test_apply_diagnostic_request_via_whatsapp_btn_under_users_steps_unit_opens_application_form(lifehelp_pro_page):
    lifehelp_pro_page.scroll_to_title_order_time_in_users_steps_description()
    lifehelp_pro_page.click_to_apply_diagnostic_btn_under_users_step_description_unit()
    lifehelp_pro_page.click_to_apply_via_whatsapp_btn_diagnostic_application_form()
    lifehelp_pro_page.move_to_new_page()
    lifehelp_pro_page.get_url('https://api.whatsapp.com/send/?phone=79297600963&text=%D0%97%D0%B4%D1%80%D0%B0%D0%B2%D1'
                              '%81%D1%82%D0%B2%D1%83%D0%B9%D1%82%D0%B5%21+%D0%AF+%D1%85%D0%BE%D1%87%D1%83+%D0%B7%D0%B0'
                              '%D0%BF%D0%B8%D1%81%D0%B0%D1%82%D1%8C%D1%81%D1%8F+%D0%BD%D0%B0+%D0%B8%D0%BD%D0%B4%D0%B8%'
                              'D0%B2%D0%B8%D0%B4%D1%83%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9+%D0%BF%D0%BE%D0%B4%D0%B1%D0%'
                              'BE%D1%80+%D0%BF%D1%81%D0%B8%D1%85%D0%BE%D0%BB%D0%BE%D0%B3%D0%B0&type=phone_number&app_'
                              'absent=0')

# 12 - Проверка - клик по кнопке "Записаться в Telegram" в форме заявки на 20минутку ведет на страницу Telegram
# службы заботы
def test_apply_diagnostic_request_via_telegram_btn_under_users_steps_unit_opens_application_form(lifehelp_pro_page):
    lifehelp_pro_page.scroll_to_title_order_time_in_users_steps_description()
    lifehelp_pro_page.click_to_apply_diagnostic_btn_under_users_step_description_unit()
    lifehelp_pro_page.click_to_apply_via_telegram_btn_diagnostic_application_form()
    lifehelp_pro_page.move_to_new_page()
    lifehelp_pro_page.get_url('https://t.me/+79600645557')

# 13 - Проверка - клик по кнопке "Записаться на диагностику" под блоком "Как начать" ведет на форму заявки на 20минутку
def test_get_psychologist_themselves_btn_under_prices_unit(lifehelp_pro_page):
    lifehelp_pro_page.scroll_to_text_time_limit_under_prices_unit()
    lifehelp_pro_page.click_to_get_psychologist_themselves_btn_under_prices_unit()

# 14 - Проверка - клик по кнопке "Получить бесплатный подбор психолога" под блоком "Как начать" ведет на форму
# заявки на 20минутку
def test_get_free_psychologist_set_btn_under_prices_unit(lifehelp_pro_page):
    lifehelp_pro_page.scroll_to_text_time_limit_under_prices_unit()
    lifehelp_pro_page.click_to_get_free_psychologist_set_btn_under_prices_unit()
    lifehelp_pro_page.click_to_leave_credentials_btn_diagnostic_application_form()
    lifehelp_pro_page.set_name_application_form_for_diagnostic()
    lifehelp_pro_page.set_phone_application_form_for_diagnostic()
    lifehelp_pro_page.click_to_apply_psychologist_request_btn_diagnostic_application_form()
    lifehelp_pro_page.verify_successful_application_notification_text()

# 15 - Проверка - клик по кнопке "Подобрать психолога" под блоком "Отзывы наших клиентов" ведет на анкету
def test_get_psychologist_btn_under_users_review_unit(lifehelp_pro_page):
    lifehelp_pro_page.scroll_to_users_review_unit_title()
    lifehelp_pro_page.click_to_get_psychologist_btn_under_users_review_unit()

# 16 -Проверка - клик по кнопке "Подобрать психолога самостоятельно" под блоком "FAQ" ведет на начальную страницу анкеты
def test_get_psychologist_themselves_btn_under_faq_unit(lifehelp_pro_page):
    lifehelp_pro_page.scroll_to_text_under_last_question_faq_unit()
    lifehelp_pro_page.click_to_get_psychologist_themselves_btn_under_faq_unit()

# 17 - Проверка - клик по кнопке "Получить бесплатный подбор психолога" под блоком "FAQ" ведет на форму заявки
# на 20минутку
def test_get_free_psychologist_set_btn_under_faq_unit(lifehelp_pro_page):
    lifehelp_pro_page.scroll_to_text_under_last_question_faq_unit()
    lifehelp_pro_page.click_to_get_free_psychologist_set_btn_under_faq_unit()
    lifehelp_pro_page.click_to_leave_credentials_btn_diagnostic_application_form()
    lifehelp_pro_page.set_name_application_form_for_diagnostic()
    lifehelp_pro_page.set_phone_application_form_for_diagnostic()
    lifehelp_pro_page.click_to_apply_psychologist_request_btn_diagnostic_application_form()
    lifehelp_pro_page.verify_successful_application_notification_text()

# 18 - Проверка - клик по иконке "Whatsapp" в самом низу страницы ведет на страницу Whatsapp службы заботы
# в соседней вкладке
def test_click_whatsapp_icon_opens_whatsapp_care_page(lifehelp_pro_page):
    lifehelp_pro_page.scroll_to_text_several_clicks_to_psychologist()
    lifehelp_pro_page.click_to_whatsapp_care_icon()
    lifehelp_pro_page.move_to_new_page()
    lifehelp_pro_page.get_url('https://api.whatsapp.com/send/?phone=79297600963&text&type=phone_number&app_absent=0')

# 19 - Проверка - клик по иконке "Telegram" в самом низу страницы ведет на страницу Telegram службы заботы
# в соседней вкладке
def test_click_telegram_icon_opens_telegram_care_page(lifehelp_pro_page):
    lifehelp_pro_page.scroll_to_text_several_clicks_to_psychologist()
    lifehelp_pro_page.click_to_telegram_care_icon()
    lifehelp_pro_page.move_to_new_page()
    lifehelp_pro_page.get_url('https://t.me/+79600645557')

# 20 - Проверка - клик по названию "Договор оферты" в подвале страницы ведет на страницу с документом в соседней вкладке
def test_click_offer_text_page_bottom_opens_contract_offer_document(lifehelp_pro_page):
    lifehelp_pro_page.scroll_to_page_bottom_till_lifefelp_service()
    lifehelp_pro_page.click_to_contract_offer_text_page_bottom()
    lifehelp_pro_page.move_to_new_page()
    lifehelp_pro_page.get_url('https://life-help.ru/contract-offer/')

# 21 - Проверка - клик по названию "Условия использования" в подвале страницы ведет на страницу с документом
# в соседней вкладке
def test_click_agreement_text_page_bottom_opens_agreement_document(lifehelp_pro_page):
    lifehelp_pro_page.scroll_to_page_bottom_till_lifefelp_service()
    lifehelp_pro_page.click_to_agreement_text_page_bottom()
    lifehelp_pro_page.move_to_new_page()
    lifehelp_pro_page.get_url('https://life-help.ru/agreement/')

# 22 - Проверка - клик по названию "Условия использования" в подвале страницы ведет на страницу с документом
# в соседней вкладке
def test_click_privacy_policy_text_page_bottom_opens_privacy_policy_document(lifehelp_pro_page):
    lifehelp_pro_page.scroll_to_page_bottom_till_lifefelp_service()
    lifehelp_pro_page.click_to_privacy_policy_text_page_bottom()
    lifehelp_pro_page.move_to_new_page()
    lifehelp_pro_page.get_url('https://life-help.ru/privacy-policy/')

# 23 - Проверка - клик по названию "Согласие на рассылку" в подвале страницы ведет на страницу с документом
# в соседней вкладке
def test_click_consent_mailing_text_page_bottom_opens_consent_mailing_document(lifehelp_pro_page):
    lifehelp_pro_page.scroll_to_page_bottom_till_lifefelp_service()
    lifehelp_pro_page.click_to_consent_mailing_text_page_bottom()
    lifehelp_pro_page.move_to_new_page()
    lifehelp_pro_page.get_url('https://life-help.ru/consent-mailing/')

# 24 - Проверка - клик по иконке VK в подвале страницы ведет на страницу VK Life Help в соседней вкладке
def test_click_vk_icon_page_bottom_opens_vk_lh_page(lifehelp_pro_page):
    lifehelp_pro_page.scroll_to_page_bottom_till_lifefelp_service()
    lifehelp_pro_page.click_to_vk_icon_page_bottom()
    lifehelp_pro_page.move_to_new_page()
    lifehelp_pro_page.get_url('https://vk.com/life_help')

# 25 - Проверка - клик по иконке Telegram в подвале страницы ведет на страницу Telegram Life Help в соседней вкладке
def test_click_telegram_icon_page_bottom_opens_telegram_lh_page(lifehelp_pro_page):
    lifehelp_pro_page.scroll_to_page_bottom_till_lifefelp_service()
    lifehelp_pro_page.click_to_telegram_icon_page_bottom()
    lifehelp_pro_page.move_to_new_page()
    lifehelp_pro_page.get_url('https://t.me/life_help_pro')

# 26- Проверка - клик по кнопке "Зарегистрироваться" в подвале страницы ведет на страницу авторизации Life Help
# в этой же вкладке
def test_click_to_register_btn_page_bottom_opens_auth_lh_page(lifehelp_pro_page):
    lifehelp_pro_page.scroll_to_page_bottom_till_lifefelp_service()
    lifehelp_pro_page.click_to_register_btn_page_bottom()
    lifehelp_pro_page.get_url('https://life-help.ru/auth/?utm_source=veb.life-help.pro&utm_medium=&utm_campaign='
                              '&utm_content=&utm_term=%C2%A0')
