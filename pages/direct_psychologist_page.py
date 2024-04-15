from base.base_object import BaseObject
from locators.psychologist_page_locators import PsychologistPageLocators
import allure
from support.assertions import Assertions

class PsychologistPage(BaseObject, Assertions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('verify psychologist title - Elena Kalkan page')
    def verify_psy_page_title(self):
        actual_result = self.get_text_title_of_element(PsychologistPageLocators.PSYCHOLOGIST_ELENA_KALKAN_TITLE)
        expected_result = 'Елена Геннадьевна'
        self.verify(expected_result, actual_result)

    @allure.step('check presence of the first order time')
    def check_presence_first_order_time(self):
        self.is_clickable(PsychologistPageLocators.FIRST_ORDER_TIME)

    @allure.step('verify first order time is equal to first order time of the rapid schedule')
    def verify_rapid_first_order_time(self):
        actual_result = self.is_clickable(PsychologistPageLocators.FIRST_ORDER_TIME)
        actual_result_value = actual_result.get_attribute("value")
        expected_result = self.is_clickable(PsychologistPageLocators.RAPID_ORDER_TIME)
        expected_result_value = expected_result.get_attribute("value")
        self.verify_value(actual_result_value, expected_result_value)

    @allure.step('select first order time')
    def choose_first_order_time_kalkan(self):
        self.to_click(PsychologistPageLocators.FIRST_ORDER_KALKAN)

    @allure.step('select the 3rd rapid time')
    def select_rapid_order_time(self):
        self.to_click(PsychologistPageLocators.ELENA_KALKAN_RAPID_TIME_3)

    @allure.step('click to payment button')
    def click_to_move_to_payment_button(self):
        self.to_click(PsychologistPageLocators.MOVE_TO_PAYMENT_BUTTON)

    @allure.step('scroll till the payment button')
    def scroll_to_element(self):
        self.move_to_element(PsychologistPageLocators.MOVE_TO_PAYMENT_BUTTON)

    @allure.step('scroll till the main schedule')
    def scroll_to_schedule(self):
        self.move_to_element(PsychologistPageLocators.ORDER_TIME_TEST)

    @allure.step('click to the psychologist video')
    def click_to_psychologist_video(self):
        self.to_click(PsychologistPageLocators.ELENA_KALKAN_VIDEO)

    @allure.step('verify video frame of the psychologist')
    def verify_video_frame_psychologist_page(self):
        actual_result = self.is_visible(PsychologistPageLocators.VIDEO_FRAME).get_attribute('allow')
        assert actual_result == 'autoplay'

    @allure.step('select the nearest 3rd time for session')
    def select_3rd_time_session_rapid_schedule_psychologist(self):
        self.to_click(PsychologistPageLocators.RAPID_SCHEDULE_3RD_TIME_DOCTOR)

    @allure.step('click to "go to payment" button')
    def click_rapid_go_payment_btn(self):
        self.to_click(PsychologistPageLocators.RAPID_GO_TO_PAYMENT_BTN)

    @allure.step('set client name')
    def set_client_name(self):
        self.set_value(PsychologistPageLocators.NAME_FIELD_ORDER_PAGE, 'Test_wo_package')

    @allure.step('set client phone')
    def set_client_phone(self):
        self.set_value(PsychologistPageLocators.PHONE_FIELD_ORDER_PAGE, '+3759274197879')

    @allure.step('set client email')
    def set_client_email(self):
        self.set_value(PsychologistPageLocators.EMAIL_FIELD_ORDER_PAGE, 'abrakadaba@mail.ru')

    @allure.step('click to "go to payment" button')
    def click_green_payment_btn(self):
        self.to_click(PsychologistPageLocators.PAYMENT_GREEN_BTN_ORDER_PAGE)

    @allure.step('scroll to button "rapid payment"')
    def scroll_to_rapid_payment_button(self):
        self.move_to_element(PsychologistPageLocators.RAPID_GO_TO_PAYMENT_BTN)

    @allure.step('verify price on the button is 2 950 ₽')
    def verify_session_price_2950_rubbles_psychologist_page(self):
        ind_50_session_result = self.get_text_title_of_element(
            PsychologistPageLocators.PRICE_2950_DOCTOR_PAGE)
        assert ind_50_session_result == '2950.00 ₽'

    @allure.step('verify doctor name in user account, terminated session - Имя Отчество ')
    def verify_doctor_name_user_terminated_session(self):
        actual_result = self.get_text_title_of_element(PsychologistPageLocators.DOCTOR_NAME_DOCTOR_PAGE)
        expected_result = 'Елена Геннадьевна'
        self.verify(expected_result, actual_result)

    @allure.step('verify price on the button is 4 200 ₽')
    def verify_session_price_4200_rubbles_psychologist_page(self):
        ind_90_session_result = self.get_text_title_of_element(
            PsychologistPageLocators.PRICE_4200_DOCTOR_PAGE)
        assert ind_90_session_result == '4200.00 ₽'

    @allure.step('verify price on the button is 4 850 ₽')
    def verify_session_price_4850_rubbles_psychologist_page(self):
        paired_session_result = self.get_text_title_of_element(
            PsychologistPageLocators.PRICE_4850_DOCTOR_PAGE)
        assert paired_session_result == '4850.00 ₽'