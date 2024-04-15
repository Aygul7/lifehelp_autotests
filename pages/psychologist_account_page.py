from base.base_object import BaseObject
from locators.psychologist_account_locators import PsychologistAccountLocators
import allure
from support.assertions import Assertions




class PsychologistAccountPage(BaseObject, Assertions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('click btn "see instruction for the first session" - psychologist account')
    def click_to_see_first_session_btn(self):
        self.to_click(PsychologistAccountLocators.SEE_FIRST_SESSION_INSTRUCTION_BTN)

    @allure.step('click btn "week schedule" - psychologist account')
    def click_week_schedule_btn(self):
        self.to_click(PsychologistAccountLocators.WEEK_SCHEDULE_BTN)

    @allure.step('click btn "month schedule" - psychologist account')
    def click_month_schedule_btn(self):
        self.to_click(PsychologistAccountLocators.MONTH_SCHEDULE_BTN)

    @allure.step('click title "personal data" - psychologist account')
    def click_title_personal_data(self):
        self.to_click(PsychologistAccountLocators.PERSONAL_DATA_MENU_NAVIGATION)

    @allure.step('click title "personal data" - psychologist account')
    def click_title_working_hours(self):
        self.to_click(PsychologistAccountLocators.WORKING_HOURS_TITLE_PERSONAL_DATA)

    @allure.step('click title "personal data" - psychologist account')
    def click_sunday_00_working_hour(self):
        self.to_click(PsychologistAccountLocators.HOUR_00_SUNDAY)

    @allure.step('scroll to bottom of the page')
    def scroll_till_page_bottom(self):
        self.move_to_page_bottom()

    @allure.step('click "save changes" - psychologist account, schedule')
    def click_save_changes(self):
        self.to_click(PsychologistAccountLocators.SAVE_CHANGES_BTN)

    @allure.step('verify selected status of the time - 00 Sunday, class')
    def verify_checked_hour_sunday_00(self):
        actual_result = self.is_visible(PsychologistAccountLocators.WORKING_HOUR_172_SUNDAY_00).get_attribute('class')
        assert actual_result == 'select-time__card-checkbox checked'

    @allure.step('scroll to top of the page')
    def scroll_till_page_top(self):
        self.move_to_page_top()

    @allure.step('verify unselected status of the time - 00 Sunday, class')
    def verify_unselected_hour_sunday_00(self):
        actual_result = self.is_visible(PsychologistAccountLocators.WORKING_HOUR_172_SUNDAY_00).get_attribute('class')
        assert actual_result == 'select-time__card-checkbox'

    @allure.step('clear value in booking time field- psychologist account')
    def clear_booking_time(self):
        self.is_visible(PsychologistAccountLocators.BOOKING_TIME_PSYCHOLOGIST_ACCOUNT).clear()

    @allure.step('input valid booking time in psychologist account - fixture')
    def set_valid_booking_time_psychologist_account(self, first):
        self.set_value(PsychologistAccountLocators.BOOKING_TIME_PSYCHOLOGIST_ACCOUNT, first)

    @allure.step('verify valid booking time - psychologist schedule, fixture')
    def verify_valid_booking_time(self, second):
        actual_result = self.is_visible(PsychologistAccountLocators.BOOKING_TIME_PSYCHOLOGIST_ACCOUNT).get_attribute('value')
        assert actual_result == second

    @allure.step('input valid booking time in psychologist account - fixture')
    def set_invalid_booking_time_psychologist_account(self, first):
        self.set_value(PsychologistAccountLocators.BOOKING_TIME_PSYCHOLOGIST_ACCOUNT, first)

    @allure.step('verify valid booking time - psychologist schedule, fixture')
    def verify_invalid_booking_time(self, second):
        actual_result = self.is_visible(PsychologistAccountLocators.BOOKING_TIME_PSYCHOLOGIST_ACCOUNT).get_attribute(
            'value')
        assert actual_result == second

    @allure.step('click "set exact day schedule" - psychologist account')
    def click_set_exact_day_schedule(self):
        self.to_click(PsychologistAccountLocators.SET_EXACT_DAY_SCHEDULE)

    @allure.step('click "first time" - psychologist account, exact day schedule')
    def click_first_time_exact_day_schedule(self):
        self.to_click(PsychologistAccountLocators.FIRST_TIME_LAST_EXACT_DAY_SCHEDULE)

    @allure.step('click "save changes" - psychologist account, exact day schedule')
    def click_save_changes_exact_day_schedule(self):
        self.to_click(PsychologistAccountLocators.SAVE_CHANGES_EXACT_DAY_SCHEDULE)

    @allure.step('verify selected status of the first time - first day, class')
    def verify_selected_first_hour_exact_day_schedule(self):
        actual_result = self.is_visible(PsychologistAccountLocators.FIRST_TIME_LAST_EXACT_DAY_SCHEDULE).get_attribute('class')
        assert actual_result == 'select-time__card-checkbox checked'

    @allure.step('verify unselected status of the first time - first day, class')
    def verify_unselected_first_hour_exact_day_schedule(self):
        actual_result = self.is_visible(PsychologistAccountLocators.FIRST_TIME_LAST_EXACT_DAY_SCHEDULE).get_attribute(
            'class')
        assert actual_result == 'select-time__card-checkbox'

    # clients and aims
    @allure.step('click to "clients and aims" button in menu navigation of psychologist account')
    def click_to_clients_and_aims_menu_psychologist(self):
        self.to_click(PsychologistAccountLocators.CLIENTS_AND_AIMS_MENU_PSYCHOLOGIST)

    @allure.step('select Aygul-test in "clients and aims" of menu navigation of psychologist account')
    def select_aygul_clients_and_aims_menu_psychologist(self):
        self.to_click(PsychologistAccountLocators.SELECT_AYGUL_TEST_CLIENTS_AIMS)

    @allure.step('click to three dots in client in "clients and aims" of menu navigation of psychologist account')
    def click_to_three_dots_clients_and_aims_menu_psychologist(self):
        self.to_click(PsychologistAccountLocators.THREE_DOTS_PSYCHOLOGIST_CLIENTS_AIM)

    @allure.step(
        'click "to create new session" button for client in "clients and aims" of menu navigation of psychologist account')
    def click_to_create_new_session_for_clients_menu_psychologist(self):
        self.to_click(PsychologistAccountLocators.CREATE_NEW_SESSION_PSYCHOLOGIST)

    @allure.step(
        'click to "to create" button for creating new session for client in "clients and aims" of menu navigation of psychologist account')
    def click_to_create_button_to_create_new_session_for_clients_menu_psychologist(self):
        self.to_click(PsychologistAccountLocators.TO_CREATE_BUTTON_CREATE_SESSION_PSYCHOLOGIST)

    @allure.step('verify successful creation of session from psychologist account')
    def verify_successful_creation_session_text_psychologist(self):
        actual_result = self.get_text_title_of_element(PsychologistAccountLocators.FINE_BUTTON_CREATE_SESSION_PSYCHOLOGIST)
        assert actual_result == 'Отлично!'

    @allure.step('verify successful creation of session from psychologist account')
    def verify_successful_creation_order_text_psychologist(self):
        actual_result = self.get_text_title_of_element(
            PsychologistAccountLocators.YOU_HAVE_SUCCESSFULLY_ORDERED_CLIENT_SESSION_MSG)
        assert 'Вы успешно забронировали' in actual_result

    # aims

    @allure.step('click "Add new aim" button psychologist account')
    def click_add_new_aim_button_psychologist(self):
        self.to_click(PsychologistAccountLocators.ADD_NEW_AIM_BUTTON_PSYCHOLOGIST)

    @allure.step('type "my aim" in the aim name field while creating aim in clients account')
    def type_aim_name_create_client(self):
        self.set_value(PsychologistAccountLocators.AIM_NAME_FIELD_CREATE_CLIENT, 'My aim')

    @allure.step('type "my aim description" in the aim description field while creating aim in clients account')
    def type_aim_description_create_client(self):
        self.set_value(PsychologistAccountLocators.AIM_DESCRIPTION_FIELD_CREATE_CLIENT, 'My aim description')

    @allure.step('set "start day" of the new aim in clients account')
    def set_start_day_aim_button_client(self):
        self.set_value(PsychologistAccountLocators.AIM_START_DAY_CREATE_CLIENT, '01.08.2023')

    @allure.step('set "end day" of the new aim in clients account')
    def set_end_day_aim_button_client(self):
        self.set_value(PsychologistAccountLocators.AIM_END_DAY_CREATE_CLIENT, '10.08.2023')

    @allure.step('click "Add new aim" button clients account')
    def click_create_new_aim_button_client(self):
        self.to_click(PsychologistAccountLocators.CREATE_NEW_AIM_BUTTON_CLIENT)

    @allure.step('verify appearance of new created aim in the clients account')
    def verify_created_aim_in_client_account(self):
        actual_result = self.get_text_title_of_element(PsychologistAccountLocators.NAME_OF_THE_CREATED_AIM_CLIENT)
        assert actual_result == 'My aim'

    @allure.step('verify unsuccessful creation of session from psychologist account')
    def verify_error_unsuccessful_creation_order_text_psychologist(self):
        actual_result = self.get_text_title_of_element(
            PsychologistAccountLocators.ERROR_MSG_SELECTED_ORDER_TIME_IS_OCCUPIED)
        assert actual_result == 'Это время уже занято. Пожалуйста, выберите другое время.'

    @allure.step('click to "aim 2" in client aim list')
    def click_aim_2_client_account(self):
        self.to_click(PsychologistAccountLocators.AIM_2_CLIENT_ACCOUNT)

    @allure.step('click to "aim status" in client aim 2 modal window')
    def click_aim_2_status_client_account(self):
        self.to_click(PsychologistAccountLocators.AIM_STATUS_CLIENT_ACCOUNT)

    @allure.step('click to "in progress " aim status in client aim 2 modal window')
    def select_aim_status_in_progress_client_account(self):
        self.to_click(PsychologistAccountLocators.AIM_STATUS_IN_PROGRESS)

    @allure.step('click to "save " button to save aim changes client')
    def click_save_aim_changes_client_account(self):
        self.to_click(PsychologistAccountLocators.SAVE_AIM_CHANGES_BUTTON_CLIENT)

    @allure.step('verify aim status is "in progress" client')
    def verify_aim_status_in_progress_client(self):
        actual_result = self.is_visible(PsychologistAccountLocators.AIM_2_CLIENT_ACCOUNT).get_attribute('class')
        assert actual_result == 'client__target-object in-progress'

    @allure.step('click to "terminated" aim status in client aim 2 modal window')
    def select_aim_status_completed_client_account(self):
        self.to_click(PsychologistAccountLocators.AIM_STATUS_COMPLETED)

    @allure.step('verify aim status is "in progress" client')
    def verify_aim_status_completed_client(self):
        actual_result = self.is_visible(PsychologistAccountLocators.AIM_2_CLIENT_ACCOUNT).get_attribute('class')
        assert actual_result == 'client__target-object completed'

    @allure.step('click to "created" aim status in client aim 2 modal window')
    def select_aim_status_created_client_account(self):
        self.to_click(PsychologistAccountLocators.AIM_STATUS_CREATED)

    @allure.step('verify aim status is "created" client')
    def verify_aim_status_created_client(self):
        actual_result = self.is_visible(PsychologistAccountLocators.AIM_2_CLIENT_ACCOUNT).get_attribute('class')
        assert actual_result == 'client__target-object created'

    @allure.step('click to "remove aim" button in client aim 2 modal window')
    def click_remove_aim_button_client_account(self):
        self.to_click(PsychologistAccountLocators.REMOVE_AIM_BUTTON_CLIENT)

    @allure.step('verify url of psychologist aim page')
    def verify_url_psychologist_aims_list_page(self):
        self.get_url('https://life-help.ru/doctor/contract/')

