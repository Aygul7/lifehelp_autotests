import json
import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.authorization_page import AuthorizationPage
from pages.questionnaire_page import QuestionnairePage
from pages.direct_psychologist_page import PsychologistPage
from pages.user_account_page import UserAccountPage
from pages.veb_life_help_page import VebLhPage
from pages.taplink_pages import TaplinkPage
from pages.restore_password_link_page import RestorePasswordLinkPage
from pages.registration_page import RegistrationPage
from pages.web_life_help_page import WebLhPage
from pages.index_page import IndexPage
from pages.order_page import OrderPage
from pages.lifehelp_pro_gift_page import LhproGiftPage
from pages.promotion_page import PromotionPage
from pages.psychologist_account_page import PsychologistAccountPage
from pages.lifehelppro_page import LifehelpProPage

# FULL_PATH = os.path.dirname(os.path.realpath(__file__))
# COOKIE_PATH = str(FULL_PATH) + '/cookies.json'
# filePath = "\C:\Users\Owner\PycharmProjects\LifeHelp\support\happy_client.png"


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    # options.add_argument('--headless')
    return options

@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    # s = Service('C:/Users/WebDriver/bin/chromedriver.exe')
    # driver = webdriver.Chrome(service=s)
    # # driver = webdriver.Chrome(executable_path=r"C:/WebDriver/bin/ChromeStandaloneSetup64")
    # driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    driver.set_window_size(1920,1080)
    return driver

@pytest.fixture
def setup(get_webdriver):
    URL = 'https://life-help.ru/'
    get_webdriver.get(URL)
    #execute_cookies()
    yield get_webdriver
    get_webdriver.quit()

@pytest.fixture
def setup_direct_link(get_webdriver):
    URL = 'https://life-help.ru/link-to-psychologist/128'
    get_webdriver.get(URL)
    yield get_webdriver
    get_webdriver.quit()

@pytest.fixture
def setup_veb_lh(get_webdriver):
    URL = 'https://veb.life-help.pro/'
    get_webdriver.get(URL)
    yield get_webdriver
    get_webdriver.quit()

@pytest.fixture
def setup_taplink(get_webdriver):
    URL = 'https://taplink.cc/life.help.pro'
    get_webdriver.get(URL)
    yield get_webdriver
    get_webdriver.quit()

@pytest.fixture
def setup_restore_password_link(get_webdriver):
    URL = 'https://life-help.ru/set-new-password/MTMzOA/c3gssu-0908daeb9688d6822ead89b7250e83db/'
    get_webdriver.get(URL)
    yield get_webdriver
    get_webdriver.quit()

@pytest.fixture
def setup_questionnaire(get_webdriver):
    URL = 'https://life-help.ru/questionnaire/general/'
    get_webdriver.get(URL)
    yield get_webdriver
    get_webdriver.quit()

@pytest.fixture
def setup_user_account(get_webdriver):
    URL = 'https://life-help.ru/'
    get_webdriver.get(URL)
    yield get_webdriver
    get_webdriver.quit()

@pytest.fixture
def setup_psychologist_account(get_webdriver):
    URL = 'https://life-help.ru/'
    get_webdriver.get(URL)
    yield get_webdriver
    get_webdriver.quit()

@pytest.fixture
def setup_registration(get_webdriver):
    URL = 'https://life-help.ru/registration/'
    get_webdriver.get(URL)
    yield get_webdriver
    get_webdriver.quit()

@pytest.fixture
def setup_web_lh(get_webdriver):
    URL = 'https://web.life-help.pro/'
    get_webdriver.get(URL)
    yield get_webdriver
    get_webdriver.quit()

@pytest.fixture
def setup_lh_pro_gift(get_webdriver):
    URL = 'https://lifehelp.pro/gifts'
    get_webdriver.get(URL)
    yield get_webdriver
    get_webdriver.quit()

@pytest.fixture
def setup_lh_pro(get_webdriver):
    URL = 'https://lifehelp.pro/'
    get_webdriver.get(URL)
    yield get_webdriver
    get_webdriver.quit()

@pytest.fixture
def setup_promotion(get_webdriver):
    URL = 'https://life-help.ru/promotion/registration/Mg/1eab51ec072a4c9c86a5c784102b1b55/endless/'
    get_webdriver.get(URL)
    yield get_webdriver
    get_webdriver.quit()

@pytest.fixture
def authorization_page(setup):
    yield AuthorizationPage(setup)

@pytest.fixture
def order_page(setup):
    yield OrderPage(setup)

@pytest.fixture
def index_page(setup):
    yield IndexPage(setup)

@pytest.fixture
def lifehelp_pro_gift_page(setup_lh_pro_gift):
    yield LhproGiftPage(setup_lh_pro_gift)

@pytest.fixture
def lifehelp_pro_page(setup_lh_pro):
    yield LifehelpProPage(setup_lh_pro)

@pytest.fixture
def questionnaire_page(setup_questionnaire):
    yield QuestionnairePage(setup_questionnaire)

@pytest.fixture
def direct_psychologist_page(setup_direct_link):
    yield PsychologistPage(setup_direct_link)

@pytest.fixture
def veb_lh_page(setup_veb_lh):
    yield VebLhPage(setup_veb_lh)

@pytest.fixture
def taplink_page(setup_taplink):
    yield TaplinkPage(setup_taplink)

@pytest.fixture
def restore_password_link_page(setup_restore_password_link):
    yield RestorePasswordLinkPage(setup_restore_password_link)

@pytest.fixture
def user_account_page(setup_user_account):
    yield UserAccountPage(setup_user_account)

@pytest.fixture
def psychologist_account_page(setup_psychologist_account):
    yield PsychologistAccountPage(setup_psychologist_account)

@pytest.fixture
def registration_page(setup_registration):
    yield RegistrationPage(setup_registration)

@pytest.fixture
def web_lh_page(setup_web_lh):
    yield WebLhPage(setup_web_lh)

@pytest.fixture
def promotion_page(setup_promotion):
    yield PromotionPage(setup_promotion)

# @pytest.fixture
# def main_page_question_page(setup):
#     yield QuestionMainPage(setup)

# @pytest.fixture
# def user_account_page(get_app_cookies_user):
#     yield UserAccountPage(get_app_cookies_user)
#
# @pytest.fixture
# def get_app_cookies_user(driver, url):
#     driver.get(url)
#     authorization_page.login_user()
#     new_cookies = driver.get_cookie("cookie_name") # replace cookie_name with your cookie name - CookieConsent
#     new_value = new_cookies["value"]
#     expiry_date = new_cookies["expiry"]
#
#     with open(COOKIE_PATH, "r") as f:
#         data1 = json.load(f)
#     for d in data1:
#         d.update((k, new_value) for k, v in d.items() if k == "value")
#     for d in data1:
#         d.update((k, expiry_date) for k, v in d.items() if k == "expiry")
#
#     with open(COOKIE_PATH, "w") as f:
#         json.dump(data1, f)


def load_app_cookies(driver, url):
    cookies = json.load(open(COOKIE_PATH, "rb"))
    driver.execute_cdp_cmd('Network.enable', {})
    for cookie in cookies:
        if "expiry" in cookie:
            cookie["expires"] = cookie["expiry"]
            del cookie["expiry"]
        cookie["domain"] = cookie["domain"]
        driver.execute_cdp_cmd('Network.setCookie', cookie)
    driver.execute_cdp_cmd('Network.disable', {})
    driver.get(url)


def execute_cookies(driver, url):
    with open(COOKIE_PATH, "r") as f:
        data1 = json.load(f)
    data2 = dict(ChainMap(*data1))
    print(data2)
    today_date = datetime.date.today()
    print(data2["expiry"])
    epoch_time = data2["expiry"]
    new_date = datetime.datetime.fromtimestamp(epoch_time).date()
    if today_date < new_date:
        load_app_cookies(driver, url)
    elif today_date >= new_date:
        get_app_cookies(driver, url)


