from selenium.webdriver.common.by import By

class TaplinkLocators:
    CREATE_ORDER_SESSION_BTN = (By.CSS_SELECTOR, "div[class='block-item block-link b-870df62d43d011ed94baac1f6bd74bd8']"
                                                 " div[class='is-ltr'] div div:nth-child(1)")
    PARENTAL_BURNOUT_BTN_TEST = (By.CSS_SELECTOR, "div[class='block-item block-link b-616976421b2011ee80bcac1f6bd8b194']"
                                                  " div[class='is-ltr'] div div:nth-child(1)")
    TAKE_TEST_PARENTAL_BURNOUT_BTN_MRQZ = (By.XPATH, "//button[contains(text(),'Пройти тест на выгорание')]")
    CODEPENDENCY_BTN_TEST_TAPLINK = (By.CSS_SELECTOR, "div[class='block-item block-link b-50836816fe1f11ed80bcac1f6bd8b"
                                                      "194'] div[class='is-ltr'] div div:nth-child(1)")
    TAKE_CODEPENDENCY_TEST_BTN_MRQZ = (By.XPATH, "//h1[contains(text(),'Тест на созависимость «Я не могу без тебя»')]")
    SELFESTIMATION_TEST_BTN = (By.CSS_SELECTOR, "div[class='block-item block-link b-2416bcbb054111ee80bcac1f6bd8b194']"
                                                " div[class='is-ltr'] div div:nth-child(1)")
    FEEL_DIFFIDENCE_MRQZ = (By.XPATH, "//h1[contains(text(),'Чувствуешь неуверенность в себе?')]")
    ASK_QUESTION_TELEGRAM = (By.CSS_SELECTOR, "div[class='block-item block-link b-6da06bc6e3a9410793a36def5a743124']"
                                              " div[class='is-ltr'] div div:nth-child(1)")
    ASK_QUESTION_WHATSAPP = (By.CSS_SELECTOR, "div[class='block-item block-link b-2795c456d2e311edb36cac1f6bd74bd8']"
                                              " div[class='is-ltr'] div div:nth-child(1)")
    TO_BECOME_PSYCHOLOGISTS_TEAM_MEMBER = (By.CSS_SELECTOR, "div[class='block-item block-link b-83afb8b9e34811ed85b1"
                                                            "ac1f6bd74bd8'] div[class='is-ltr'] div div:nth-child(1)")
    FOR_NEW_USERS_990_BTN = (By.CSS_SELECTOR, "div[class='block-item block-link b-5a273d3783e211ee80bcac1f6bd8b194'] "
                                              "div[class='is-ltr'] div div:nth-child(1)")
    FREE_DIAGNOSTIK_BTN = (By.CSS_SELECTOR, "div[class='block-item block-link b-ada8d277a57611eeb622ac1f6bd74bd8'] "
                                            "div[class='is-ltr'] div div:nth-child(1)")

