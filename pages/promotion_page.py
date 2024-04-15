from base.base_object import BaseObject
from locators.promotion_locators import PromotionLocators
import allure
from support.assertions import Assertions




class PromotionPage(BaseObject, Assertions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('clicking to "Login with password" button')
    def click_to_login_w_password_button(self):
        self.to_click(PromotionLocators.LOGIN_WITH_PASSWORD_BUTTON)

    @allure.step('verify title of successful registration to promotion')
    def verify_title_successful_registration_promotion(self):
        actual_result = self.get_text_title_of_element(PromotionLocators.SUCCESSFUL_REGISTRATION_PROMOTION_TITLE)
        expected_result = 'Вы успешно зарегистрировались в акции "Тестовая акция"!'
        self.verify(expected_result, actual_result)

    def set_email_email(self):
        self.set_value(PromotionLocators.EMAIL_PHONE_FIELD, 'sh.aygul@gmail.com')

    @allure.step('set up password')
    def set_password_pass(self):
        self.set_value(PromotionLocators.PASSWORD_FIELD, 'lifehelp1@')

    @allure.step('clicking to "Authorize" button')
    def click_to_authorize_button(self):
        self.to_click(PromotionLocators.AUTH_BUTTON)

    @allure.step('clicking to "get doctor" button by promotion')
    def click_to_get_doctor_promotion_button(self):
        self.to_click(PromotionLocators.GET_DOCTOR_PROMOTION_BTN)

    @allure.step('clicking to "move to account" button by promotion')
    def click_to_move_user_account_promotion_button(self):
        self.to_click(PromotionLocators.MOVE_TO_USER_ACCOUNT_BTN)

    @allure.step('verify price of the separate session in certificate "4"')
    def verify_title_promotion_user_account(self):
        actual_result = self.get_text_title_of_element(PromotionLocators.PROMOTION_TITLE_USER_ACCOUNT)
        expected_result = 'Тестовая акция'
        self.verify(expected_result, actual_result)

    @allure.step('clicking to "select psychologist" button by promotion')
    def click_to_select_psychologist_btn_promotion(self):
        self.to_click(PromotionLocators.SELECT_DOCTOR_PROMOTION_BUTTON)

    @allure.step('select the nearest time for second session')
    def select_2nd_time_session_rapid_schedule_psychologist(self):
        self.to_click(PromotionLocators.RAPID_SCHEDULE_2ND_TIME_DOCTOR)

    @allure.step('click to "go to payment" button')
    def click_rapid_go_payment_btn(self):
        self.to_click(PromotionLocators.RAPID_GO_TO_PAYMENT_BTN)

    @allure.step('click to orange "pay" button on order page')
    def click_orange_pay_button(self):
        self.to_click(PromotionLocators.ORANGE_PAY_BUTTON_ORDER_PAGE)

    @allure.step('scroll to "select rapid time" block on psychologist schedule')
    def scroll_till_block_select_rapid_time_doctor_schedule(self):
        self.move_to_element(PromotionLocators.SELECT_RAPID_TIME_BLOCK)

    @allure.step('verify price of the separate session in promotion')
    def verify_session_price_promotion_user_account(self):
        actual_result = self.get_text_title_of_element(PromotionLocators.PROMOTION_SESSION_PRICE)
        expected_result = 'Стоимость 1 сессии 0.00 ₽'
        self.verify(expected_result, actual_result)

    @allure.step('verify count of the sessions in promotion')
    def verify_session_count_promotion_user_account(self):
        actual_result = self.get_text_title_of_element(PromotionLocators.PROMOTION_SESSION_COUNT)
        expected_result = 'Доступно сессий - 2'
        self.verify(expected_result, actual_result)

    @allure.step('verify end date of the promotion')
    def verify_end_date_promotion_user_account(self):
        actual_result = self.get_text_title_of_element(PromotionLocators.PROMOTION_END_DATE)
        expected_result = 'Действует до 15.11.2025'
        self.verify(expected_result, actual_result)