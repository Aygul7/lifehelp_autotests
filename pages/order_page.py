from base.base_object import BaseObject
from locators.authorization_locators import AuthorizationLocators
from locators.order_page_locators import OrderPageLocators
import allure
from support.assertions import Assertions
from selenium.webdriver.common.keys import Keys




class OrderPage(BaseObject, Assertions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('click to btn "4" on order page')
    def click_to_btn_package_4_order_page(self):
        self.to_click(OrderPageLocators.PACKAGE_4_BUTTON_NEW_ORDER_PAGE)

    @allure.step('verify price on the button is 10 800 ₽')
    def verify_price_10800_rubbles_package_4_order_page(self):
        price_orange_button = self.get_text_title_of_element(
            OrderPageLocators.TO_PAY_ORANGE_BUTTON_ORDER_PAGE)
        assert price_orange_button == '10 800'

    @allure.step('click to btn "8" on order page')
    def click_to_btn_package_8_order_page(self):
        self.to_click(OrderPageLocators.PACKAGE_8_BUTTON_NEW_ORDER_PAGE)

    @allure.step('click to btn w number of session on order page - fixture')
    def click_to_number_sessions_btn_order_page_fixture(self, first):
        self.to_click(first)

    @allure.step('verify price on the button in ₽ on order page - fixture')
    def verify_price_pay_btn_order_page_fixture(self, second):
        price_orange_button = self.get_text_title_of_element(
            OrderPageLocators.TO_PAY_ORANGE_BUTTON_ORDER_PAGE)
        assert price_orange_button == second

    @allure.step('verify package description on order page - fixture')
    def verify_package_description_text_order_page_fixture(self, second):
        price_orange_button = self.get_text_title_of_element(
            OrderPageLocators.PACKAGE_DESCRIPTION_TEXT_NEW_ORDER_PAGE)
        assert price_orange_button == second

    @allure.step('verify price on the button is 20 800 ₽')
    def verify_price_20800_rubbles_package_8_order_page(self):
        price_orange_button = self.get_text_title_of_element(
            OrderPageLocators.TO_PAY_ORANGE_BUTTON_ORDER_PAGE)
        assert price_orange_button == '20 800'

    @allure.step('click to btn "12" on order page')
    def click_to_btn_package_12_order_page(self):
        self.to_click(OrderPageLocators.PACKAGE_12_BUTTON_NEW_ORDER_PAGE)

    @allure.step('verify price on the button is 28 800 ₽')
    def verify_price_28800_rubbles_package_12_order_page(self):
        price_orange_button = self.get_text_title_of_element(
            OrderPageLocators.TO_PAY_ORANGE_BUTTON_ORDER_PAGE)
        assert price_orange_button == '28 800'

    @allure.step('click to btn "54" on order page')
    def click_to_btn_package_54_order_page(self):
        self.to_click(OrderPageLocators.PACKAGE_54_BUTTON_NEW_ORDER_PAGE)

    @allure.step('click to btn "54" on order page')
    def click_to_btn_one_time_payment_package_54_order_page(self):
        self.to_click(OrderPageLocators.ONETIME_PAYMENT_PACKAGE_54_BUTTON_NEW_ORDER_PAGE)

    @allure.step('verify price on the button is 125 500 ₽')
    def verify_price_125000_rubbles_package_54_order_page(self):
        price_orange_button = self.get_text_title_of_element(
            OrderPageLocators.TO_PAY_ORANGE_BUTTON_ORDER_PAGE)
        assert price_orange_button == '125 000'

    @allure.step('verify currency ₽ on the button')
    def verify_currency_rubbles_order_page(self):
        currency_orange_button = self.get_text_title_of_element(
            OrderPageLocators.CURRENCY_ORANGE_BTN_TO_PAY_ORDER_PAGE)
        assert currency_orange_button == '₽'

    @allure.step('click to btn "usd" on order page')
    def click_to_btn_usd_payment_order_page(self):
        self.to_click(OrderPageLocators.USD_PAYMENT_BUTTON_NEW_ORDER_PAGE)

    @allure.step('verify currency $ on the button')
    def verify_currency_usd_order_page(self):
        currency_orange_button = self.get_text_title_of_element(
            OrderPageLocators.CURRENCY_ORANGE_BTN_TO_PAY_ORDER_PAGE)
        assert currency_orange_button == '$'

    @allure.step('click to btn "euro" on order page')
    def click_to_btn_euro_payment_order_page(self):
        self.to_click(OrderPageLocators.EURO_PAYMENT_BUTTON_NEW_ORDER_PAGE)

    @allure.step('verify currency Euro on the button')
    def verify_currency_euro_order_page(self):
        currency_orange_button = self.get_text_title_of_element(
            OrderPageLocators.CURRENCY_ORANGE_BTN_TO_PAY_ORDER_PAGE)
        assert currency_orange_button == '€'

    @allure.step('click to "psychologist profile" on order page')
    def click_to_psychologist_profile_order_page(self):
        self.to_click(OrderPageLocators.PSYCHOLOGIST_PROFILE)

    @allure.step('verify separate session rub price in package - fixture')
    def verify_separate_session_price_package_order_page_fixture(self, second):
        price_orange_button = self.get_text_title_of_element(
            OrderPageLocators.SEPARATE_SESSION_PRICE_PACKAGE)
        assert price_orange_button == second

    @allure.step('verify separate session usd price in package - fixture')
    def verify_separate_session_usd_price_package_order_page_fixture(self, second):
        price_orange_button = self.get_text_title_of_element(
            OrderPageLocators.SEPARATE_SESSION_USD_PRICE_PACKAGE)
        assert price_orange_button == second

    @allure.step('verify separate session euro price in package - fixture')
    def verify_separate_session_euro_price_package_order_page_fixture(self, second):
        price_orange_button = self.get_text_title_of_element(
            OrderPageLocators.SEPARATE_SESSION_EURO_PRICE_PACKAGE)
        assert price_orange_button == second

    @allure.step('click to "support" button on order page')
    def click_to_support_btn_order_page(self):
        self.to_click(OrderPageLocators.SUPPORT_BUTTON_ORDER_PAGE)

    @allure.step('move to new telegram care page')
    def move_to_new_page(self):
        new_page = self.driver.window_handles[1]
        self.driver.switch_to.window(new_page)

    @allure.step('verify url of telegram care page')
    def verify_url_telegram_care_page(self):
        self.get_url('https://t.me/+79600645557')