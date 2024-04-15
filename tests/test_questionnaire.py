import allure
import time
from pages.questionnaire_page import QuestionnairePage
import pytest
from pages.authorization_page import AuthorizationPage
from locators.authorization_locators import AuthorizationLocators

# @allure.description('Questionnaire - general questions')
# @allure.label('owner', 'Aygul')
# @allure.title('Questionnaire')
# @allure.suite('Questionnaire pack')
# @allure.severity(allure.severity_level.BLOCKER)
# 16 - проверка наличия Ирины Панковой в подборе анкеты Инд50-Рус-Стресс
def test_questionnaire_stress_pankova(questionnaire_page):
    questionnaire_page.set_age_questionnaire()
    questionnaire_page.click_personal_questions_title()
    questionnaire_page.select_stress_questionnaire()
    questionnaire_page.click_psychologist_preferences_title_questionnaire()
    questionnaire_page.click_age_over_30_questionnaire()
    questionnaire_page.click_select_psychologist_title_questionnaire()
    questionnaire_page.verify_presence_pankova_choose_specialist()

# 17 - проверка наличия Алисы в подборе анкеты Инд90-Рус-Стресс
def test_questionnaire_ind_90_alisa(questionnaire_page):
    questionnaire_page.click_ind_90_questionnaire()
    questionnaire_page.set_age_questionnaire()
    questionnaire_page.click_personal_questions_title()
    questionnaire_page.select_stress_questionnaire()
    questionnaire_page.click_psychologist_preferences_title_questionnaire()
    questionnaire_page.click_age_over_30_questionnaire()
    questionnaire_page.click_select_psychologist_title_questionnaire()
    questionnaire_page.verify_presence_alisa_ivannikova_choose_specialist()

# 18 - проверка наличия Алии в подборе анкеты Инд50-Татар-Стресс
def test_questionnaire_tatar_aliya(questionnaire_page):
    questionnaire_page.click_tatar_button_questionnaire()
    questionnaire_page.set_age_questionnaire()
    questionnaire_page.click_personal_questions_title()
    questionnaire_page.select_stress_questionnaire()
    questionnaire_page.click_psychologist_preferences_title_questionnaire()
    questionnaire_page.click_age_over_30_questionnaire()
    questionnaire_page.click_select_psychologist_title_questionnaire()
    questionnaire_page.verify_presence_aliya_askarova_choose_specialist()

# 19 - проверка наличия Елены Калкан в подборе анкеты Парной консультации - Сложности в отношениях
def test_questionnaire_paired_elena(questionnaire_page):
    questionnaire_page.click_paired_consultation_button_questionnaire()
    questionnaire_page.set_age_questionnaire()
    questionnaire_page.click_personal_questions_title()
    questionnaire_page.click_difficulties_in_relationship_paired_consultation_button_questionnaire()
    questionnaire_page.click_psychologist_preferences_title_questionnaire()
    questionnaire_page.click_age_over_30_questionnaire()
    questionnaire_page.click_select_psychologist_title_questionnaire()
    questionnaire_page.verify_presence_elena_kalkan_choose_specialist()

# 20 - проверка наличия Алии в подборе анкеты Парной консультации - Татарский язык - Сложности в отношениях
def test_questionnaire_paired_tatar_aliya(questionnaire_page):
    questionnaire_page.click_tatar_button_questionnaire()
    questionnaire_page.click_paired_consultation_button_questionnaire()
    questionnaire_page.set_age_questionnaire()
    questionnaire_page.click_personal_questions_title()
    questionnaire_page.click_difficulties_in_relationship_paired_consultation_button_questionnaire()
    questionnaire_page.click_psychologist_preferences_title_questionnaire()
    questionnaire_page.click_age_over_30_questionnaire()
    questionnaire_page.click_select_psychologist_title_questionnaire()
    questionnaire_page.verify_presence_aliya_askarova_choose_specialist()

# 35 - появление модального окна с просьбой указать свой возраст в анкете
def test_error_wo_age_questionnaire(questionnaire_page):
    questionnaire_page.click_personal_questions_title()
    questionnaire_page.verify_window_to_set_age_questionnaire()

# 36 - проверка того, что нельзя перейти к предпочтениям к психологу без выбора темы в анкете
def test_questionnaire(questionnaire_page):
    questionnaire_page.set_age_questionnaire()
    questionnaire_page.click_psychologist_preferences_title_questionnaire()
    questionnaire_page.get_url('https://life-help.ru/questionnaire/personal/')


# 39,40,41 - появление модального окна с просьбой указать свой возраст в анкете, если указать меньше 16
case_1 = ['0']
case_2 = ['15']
case_3 = ['120']

@pytest.mark.parametrize('first', (case_1, case_2, case_3),
                             ids=['0 years', '15 years', '120 years'])

def test_error_age_out_16and119_questionnaire(questionnaire_page, first):
    questionnaire_page.set_age_field_negative_validation_questionnaire(first)
    questionnaire_page.click_personal_questions_title()
    questionnaire_page.verify_window_age_above16_questionnaire()

# 42,43,44 - проверка возможности продолжить заполнение анкеты при указании возраста в диапазоне 16-119 (16,45,119)
case_1 = ['16']
case_2 = ['45']
case_3 = ['119']
@pytest.mark.parametrize('age', (case_1, case_2, case_3),
                             ids=['16 years', '45 years', '119 years'])

def test_correct_age_within_16and119_questionnaire(questionnaire_page, age):
    questionnaire_page.set_age_field_positive_validation_questionnaire(age)
    questionnaire_page.click_personal_questions_title()
    questionnaire_page.get_url("https://life-help.ru/questionnaire/personal/")

# 14 - клик enter для перехода между страницами анкеты
def test_enter_instead_click_between_questionnaire_pages(questionnaire_page):
    questionnaire_page.set_age_questionnaire()
    questionnaire_page.enter_instead_click_to_next_button_questionnaire()
    questionnaire_page.select_stress_questionnaire()
    questionnaire_page.enter_instead_click_to_next_button_questionnaire()
    questionnaire_page.click_age_over_30_questionnaire()
    questionnaire_page.enter_instead_click_to_next_button_questionnaire()
    questionnaire_page.verify_presence_pankova_choose_specialist()

# 15 - психолог-мужчина моложе 30 лет в подборе (стресс) - на примере Южаков Никита
def test_male_doctors_till_30_age_questionnaire(questionnaire_page):
    questionnaire_page.set_age_questionnaire()
    questionnaire_page.enter_instead_click_to_next_button_questionnaire()
    questionnaire_page.select_stress_questionnaire()
    questionnaire_page.enter_instead_click_to_next_button_questionnaire()
    questionnaire_page.click_age_till_30_questionnaire_preferences()
    questionnaire_page.click_male_button_questionnaire_preferences()
    questionnaire_page.enter_instead_click_to_next_button_questionnaire()
    questionnaire_page.verify_presence_nikita_choose_specialist()

# 16 - психолог-мужчина старше 30 лет в подборе (стресс) - на примере Прокопова Дмитрия
def test_male_doctors_over_30_age_questionnaire(questionnaire_page):
    questionnaire_page.set_age_questionnaire()
    questionnaire_page.enter_instead_click_to_next_button_questionnaire()
    questionnaire_page.select_stress_questionnaire()
    questionnaire_page.enter_instead_click_to_next_button_questionnaire()
    questionnaire_page.click_age_over_30_questionnaire()
    questionnaire_page.click_male_button_questionnaire_preferences()
    questionnaire_page.enter_instead_click_to_next_button_questionnaire()
    questionnaire_page.verify_presence_dmitrii_choose_specialist()


# 17 - психологи без детей в подборе (стресс) - на примере Лилии Серёгиной
def test_doctors_wo_children_questionnaire(questionnaire_page):
    questionnaire_page.set_age_questionnaire()
    questionnaire_page.enter_instead_click_to_next_button_questionnaire()
    questionnaire_page.select_stress_questionnaire()
    questionnaire_page.enter_instead_click_to_next_button_questionnaire()
    questionnaire_page.click_wo_children_questionnaire_preferences()
    questionnaire_page.enter_instead_click_to_next_button_questionnaire()
    questionnaire_page.verify_presence_lilia_choose_specialist()

# 18 - Имя Отчество психолога в карточке в подборе - на примере Лилии Серёгиной
def test_doctor_full_name_wo_surname_questionnaire(questionnaire_page):
    questionnaire_page.set_age_questionnaire()
    questionnaire_page.enter_instead_click_to_next_button_questionnaire()
    questionnaire_page.select_stress_questionnaire()
    questionnaire_page.enter_instead_click_to_next_button_questionnaire()
    questionnaire_page.click_wo_children_questionnaire_preferences()
    questionnaire_page.enter_instead_click_to_next_button_questionnaire()
    questionnaire_page.verify_lilia_sergeevna_name_choose_specialist()

# 19 - Стоимость услуги психолога в карточке в подборе 2950 (для инд50) - на примере Лилии Серёгиной
def test_doctor_price_2950_questionnaire_page(questionnaire_page):
    questionnaire_page.set_age_questionnaire()
    questionnaire_page.enter_instead_click_to_next_button_questionnaire()
    questionnaire_page.select_stress_questionnaire()
    questionnaire_page.enter_instead_click_to_next_button_questionnaire()
    questionnaire_page.click_wo_children_questionnaire_preferences()
    questionnaire_page.enter_instead_click_to_next_button_questionnaire()
    questionnaire_page.verify_lilia_price_2950_choose_specialist()


# 20 - проверка стоимости услуги инд90 (стресс) - 4200 в карточке психолога в подборе анкеты - пример Иванниковой Алисы
def test_doctor_price_4200_ind90_questionnaire(questionnaire_page):
    questionnaire_page.click_ind_90_questionnaire()
    questionnaire_page.set_age_questionnaire()
    questionnaire_page.click_personal_questions_title()
    questionnaire_page.select_stress_questionnaire()
    questionnaire_page.click_psychologist_preferences_title_questionnaire()
    questionnaire_page.click_age_over_30_questionnaire()
    questionnaire_page.click_select_psychologist_title_questionnaire()
    questionnaire_page.verify_ind90_price_4200_choose_specialist()


# 21 - проверка стоимости услуги парная консультация (сложности в отношениях) - 4850 в карточке психолога
# в подборе анкеты - пример Шевяковой Натальи
def test_doctor_price_4850_paired_questionnaire(questionnaire_page):
    questionnaire_page.click_paired_consultation_button_questionnaire()
    questionnaire_page.set_age_questionnaire()
    questionnaire_page.click_personal_questions_title()
    questionnaire_page.click_difficulties_in_relationship_paired_consultation_button_questionnaire()
    questionnaire_page.click_psychologist_preferences_title_questionnaire()
    questionnaire_page.click_age_over_30_questionnaire()
    questionnaire_page.click_select_psychologist_title_questionnaire()
    questionnaire_page.verify_paired_price_4850_choose_specialist()

# 22 - Проверка перехода на страницу авторизации после анкеты (для инд50, стресс) для неавторизованного клиента
def test_move_to_auth_form_before_order_after_questionnaire_page(questionnaire_page):
    questionnaire_page.set_age_questionnaire()
    questionnaire_page.enter_instead_click_to_next_button_questionnaire()
    questionnaire_page.select_stress_questionnaire()
    questionnaire_page.enter_instead_click_to_next_button_questionnaire()
    questionnaire_page.click_wo_children_questionnaire_preferences()
    questionnaire_page.enter_instead_click_to_next_button_questionnaire()
    questionnaire_page.click_first_rapid_time_choose_doctor_page()
    questionnaire_page.scroll_till_btn_order_rapid_time_psychologist_schedule()
    questionnaire_page.click_to_btn_order_rapid_time_choose_doctor_page()
    questionnaire_page.verify_auth_form_after_choose_specialist()

# 23 - Проверка перехода на модальное окно для ввода кода из смс без выбора чекбокса "рассылка"
# на странице авторизации после анкеты (для инд50, стресс) для неавторизованного клиента
def test_error_class_unselected_agreement_checkbox_order_auth_page(questionnaire_page):
    questionnaire_page.set_age_questionnaire()
    questionnaire_page.enter_instead_click_to_next_button_questionnaire()
    questionnaire_page.select_stress_questionnaire()
    questionnaire_page.enter_instead_click_to_next_button_questionnaire()
    questionnaire_page.click_wo_children_questionnaire_preferences()
    questionnaire_page.enter_instead_click_to_next_button_questionnaire()
    questionnaire_page.click_first_rapid_time_choose_doctor_page()
    questionnaire_page.scroll_till_btn_order_rapid_time_psychologist_schedule()
    questionnaire_page.click_to_btn_order_rapid_time_choose_doctor_page()
    questionnaire_page.set_user_name_order_auth_page()
    questionnaire_page.set_user_phone_order_auth_page()
    questionnaire_page.select_agreement_checkbox_auth_order_page()
    questionnaire_page.unselect_mailing_checkbox_auth_order_page()
    questionnaire_page.click_to_move_to_order_button_auth_order_page()
    questionnaire_page.verify_title_modal_window_enter_sms_code()

# 24 - Проверка подсвечивания красным ошибки незаполненного поля "Телефон"
# на странице авторизации после анкеты (для инд50, стресс) для неавторизованного клиента
def test_error_empty_user_phone_field_order_auth_page(questionnaire_page):
    questionnaire_page.set_age_questionnaire()
    questionnaire_page.enter_instead_click_to_next_button_questionnaire()
    questionnaire_page.select_stress_questionnaire()
    questionnaire_page.enter_instead_click_to_next_button_questionnaire()
    questionnaire_page.click_wo_children_questionnaire_preferences()
    questionnaire_page.enter_instead_click_to_next_button_questionnaire()
    questionnaire_page.click_first_rapid_time_choose_doctor_page()
    questionnaire_page.scroll_till_btn_order_rapid_time_psychologist_schedule()
    questionnaire_page.click_to_btn_order_rapid_time_choose_doctor_page()
    questionnaire_page.set_user_name_order_auth_page()
    questionnaire_page.select_agreement_checkbox_auth_order_page()
    questionnaire_page.click_to_move_to_order_button_auth_order_page()
    questionnaire_page.verify_error_empty_user_phone_field_order_auth_page()

# 25 - Проверка перехода на страницу подбора психолога при клике на Профиль психолога
# на странице авторизации с подбора психолога
def test_click_doctor_profile_order_auth_page_opens_doctor_page(questionnaire_page):
    questionnaire_page.set_age_questionnaire()
    questionnaire_page.enter_instead_click_to_next_button_questionnaire()
    questionnaire_page.select_stress_questionnaire()
    questionnaire_page.enter_instead_click_to_next_button_questionnaire()
    questionnaire_page.click_wo_children_questionnaire_preferences()
    questionnaire_page.enter_instead_click_to_next_button_questionnaire()
    questionnaire_page.click_first_rapid_time_choose_doctor_page()
    questionnaire_page.scroll_till_btn_order_rapid_time_psychologist_schedule()
    questionnaire_page.click_to_btn_order_rapid_time_choose_doctor_page()
    questionnaire_page.click_doctor_profile_auth_order_page()
    questionnaire_page.move_to_new_page()
    questionnaire_page.get_url('https://life-help.ru/questionnaire/choose-doctor/')


