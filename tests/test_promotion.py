import allure
import pytest


from locators.promotion_locators import PromotionLocators
from locators.authorization_locators import AuthorizationLocators
from pages.authorization_page import AuthorizationLocators

# 1 - Проверка - неавторизованный пользователь при переходе по ссылке на акцию переходит на страницу авторизации
def test_unauthorized_user_authorization_page(promotion_page):
    promotion_page.get_url('https://life-help.ru/auth/?next=/promotion/registration/Mg/1eab51ec072a4c9c86a5c784102b1b55/endless/')


# 2 - Проверка - при переходе по ссылке на акцию и авторизацию пользователю появляется сообщение об успешной регистрации
# на акцию
def test_authorized_user_successful_promotion_page(promotion_page):
    promotion_page.click_to_login_w_password_button()
    promotion_page.set_email_email()
    promotion_page.set_password_pass()
    promotion_page.click_to_authorize_button()
    promotion_page.verify_title_successful_registration_promotion()

# 3 - Проверка - при переходе по ссылке на акцию и авторизацию пользователю появляется сообщение об успешной регистрации
# на акцию
def test_get_psychologist_btn_promotion_page(promotion_page):
    promotion_page.click_to_login_w_password_button()
    promotion_page.set_email_email()
    promotion_page.set_password_pass()
    promotion_page.click_to_authorize_button()
    promotion_page.click_to_get_doctor_promotion_button()
    promotion_page.get_url('https://life-help.ru/user/promotion/testovaya-akciya/')

# 4 - Проверка - при переходе по ссылке на акцию и клике "Перейти в личный кабинет" пользователю переходит
# в личный кабинет, где отображается акция
def test_move_user_account_btn_promotion_page(promotion_page):
    promotion_page.click_to_login_w_password_button()
    promotion_page.set_email_email()
    promotion_page.set_password_pass()
    promotion_page.click_to_authorize_button()
    promotion_page.click_to_move_user_account_promotion_button()
    promotion_page.verify_title_promotion_user_account()

# 5 - Проверка - при переходе по ссылке на акцию и клике "Перейти в личный кабинет" пользователю переходит
# в личный кабинет, где отображается акция
def test_select_psychologist_btn_promotion(promotion_page):
    promotion_page.click_to_login_w_password_button()
    promotion_page.set_email_email()
    promotion_page.set_password_pass()
    promotion_page.click_to_authorize_button()
    promotion_page.click_to_move_user_account_promotion_button()
    promotion_page.click_to_select_psychologist_btn_promotion()
    promotion_page.get_url('https://life-help.ru/user/promotion/testovaya-akciya/')

# 6 - Проверка стоимости отдельного сеанса по акции в блоке Акция в лк клиента
def test_price_session_promotion_user_account_page(promotion_page):
    promotion_page.click_to_login_w_password_button()
    promotion_page.set_email_email()
    promotion_page.set_password_pass()
    promotion_page.click_to_authorize_button()
    promotion_page.click_to_move_user_account_promotion_button()
    promotion_page.verify_session_price_promotion_user_account()

# 7 - Проверка количества доступных сеансов по акции в блоке Акция в лк клиента (без записи на сеанс по акции)
def test_count_sessions_promotion_user_account_page(promotion_page):
    promotion_page.click_to_login_w_password_button()
    promotion_page.set_email_email()
    promotion_page.set_password_pass()
    promotion_page.click_to_authorize_button()
    promotion_page.click_to_move_user_account_promotion_button()
    promotion_page.verify_session_count_promotion_user_account()

# 8 - Проверка срок действия акции в блоке Акция в лк клиента
def test_end_date_promotion_user_account_page(promotion_page):
    promotion_page.click_to_login_w_password_button()
    promotion_page.set_email_email()
    promotion_page.set_password_pass()
    promotion_page.click_to_authorize_button()
    promotion_page.click_to_move_user_account_promotion_button()
    promotion_page.verify_end_date_promotion_user_account()


