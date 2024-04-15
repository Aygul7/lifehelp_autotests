from selenium.webdriver.common.by import By

class LifehelpProLocators:
    FIND_PSYCHOLOGIST_UPPER_1ST_BUTTON = (By.XPATH, "//a[@class='btn btn-legacy font-text css17']//span[@class='text']"
                                                    "[contains(text(),'Подобрать психолога')]")
    GENERAL_QUESTIONS_TITLE_QUESTIONNAIRE = (By.CSS_SELECTOR, "a[class='progress_page active'] p:nth-child(1)")
    TEXT_INDIVIDUAL_50_GENERAL_QUESIONNAIRE = (By.CSS_SELECTOR, "label[for='1']")
    WANT_TO_TRY_BTN = (By.XPATH, "//span[contains(text(),'Хочу попробовать')]")
    TO_LOGIN_BTN = (By.CSS_SELECTOR, "a[class='btn btn-legacy font-text css16'] span[class='text']")
    MENU_BTN = (By.CSS_SELECTOR, ".fas.fa-align-justify")
    GET_PSYCHOLOGIST_MENU_BTN = (By.CSS_SELECTOR, "span[class='text icon'] span")
    TO_BUY_CERTIFICATE_MENU_BTN =  (By.XPATH, "(//span[contains(text(),'Купить сертификат')])[1]")
    THERAPY_QUERIES_TITLE = (By.CSS_SELECTOR, "p[class='textable css43'] strong")
    GET_PSYCHOLOGIST_BTN_UNDER_THERAPY_QUERIES_UNIT = (By.XPATH, "(//span[@class='text'][contains(text(),"
                                                                 "'Подобрать психолога')])[2]")
    HOW_IT_WORKS_TITLE = (By.XPATH, "(//p[@class='textable css72'])[2]")
    # application for 20min diagnostic form
    GET_DIAGNOSTIC_BTN_UNDER_HOW_IT_WORKS_UNIT = (By.XPATH, "(//span[contains(text(),'Получить диагностику')])[1]")
    LEAVE_YOUR_CREDENTIALS_BTN_DIAGNOSTIC_APPLICATION_FORM = (By.CSS_SELECTOR, "button[class='btn btn-legacy "
                                                                               "font-text css63'] span[class='text']")
    INPUT_NAME_FIELD_APPLICATION_FORM_FOR_DIAGNOSTIC = (By.CSS_SELECTOR, "input[autocomplete='name']")
    INPUT_PHONE_FIELD_APPLICATION_FORM_FOR_DIAGNOSTIC = (By.CSS_SELECTOR, "input[autocomplete='tel']")
    APPLY_PSYCHOLOGIST_REQUEST_BTN = (By.XPATH, "//span[contains(text(),'ЗАПИСАТЬСЯ НА ПОДБОР')]")
    SUCCESSFUL_APPLICATION_NOTIFICATION_TEXT = (By.CSS_SELECTOR, ".swal-title")
    APPLY_VIA_WHATSAPP_BTN_FORM_FOR_DIAGNOSTIC = (By.XPATH, "(//div[@class='node widget-button widget css8'])[2]")
    APPLY_VIA_TELEGRAM_BTN_FORM_FOR_DIAGNOSTIC = (By.XPATH, "//span[contains(text(),'Записаться в Telegram')]")

    TITLE_BLOCK_STABILITY_WARRANTY = (By.XPATH, "//strong[contains(text(),'Гарантируем стабильность')]")
    GET_PSYCHOLOGIST_BTN_UNDER_WHY_USERS_PREFER_LH = (By.XPATH, "(//span[contains(text(),'Подобрать психолога')])[3]")

    TITLE_ORDER_TIME_USERS_STEPS_DESCRIPTION = (By.XPATH, "//strong[contains(text(),'Забронируйте время')]")
    FILL_QUESTIONNAIRE_BTN = (By.XPATH, "(//span[contains(text(),'Заполнить анкету')])[1]")
    ALLPY_FOR_DIAGNOSTIC_BTN_UNDER_USER_STEPS_DESCRIPTION_UNIT = (By.XPATH, "//span[contains(text(),"
                                                                            "'Записаться на диагностику')]")

    TEXT_TIME_LIMIT_UNDER_PRICES = (By.XPATH, "//p[contains(text(),'Сроки указаны при условии, что вы будете встречать')]")
    GET_PSYCHOLOGIST_THEMSELVES_BTN_UNDER_PRICES = (By.XPATH, "(//span[@class='text'][contains(text(),"
                                                              "'Подобрать психолога самостоятельно')])[1]")
    GET_FREE_PSYCHOLOGIST_SET = (By.XPATH, "//div[@id='price']//div[@class='node widget-button widget rubikr css123']"
                                           "//div[@class='btn-content']")

    USERS_REVIEW_TITLE_UNIT = (By.XPATH, "(//strong[contains(text(),'Отзывы наших клиентов')])[1]")
    GET_PSYCHOLOGIST_BTN_UNDER_USERS_REVIEW_UNIT = (By.XPATH, "(//span[@class='text'][contains(text(),"
                                                              "'Подобрать психолога')])[5]")

    TEXT_UNDER_LAST_QUESTION_FAQ_UNIT = (By.XPATH, "//p[contains(text(),'Нажмите на одну из кнопок ниже, "
                                             "выберите специалис')]")
    GET_PSYCHOLOGIST_THEMSELVES_BTN_UNDER_FAQ = (By.XPATH, "(//span[@class='text'][contains(text(),"
                                                           "'Подобрать психолога самостоятельно')])[2]")
    GET_FREE_PSYCHOLOGIST_SET_UNDER_FAQ = (By.XPATH, "(//span[@class='text'][contains(text(),"
                                                     "'Получить бесплатный подбор психолога')])[2]")

    SEVERAL_CLICKS_TO_PSYCHOLOGIST_TITLE = (By.XPATH, "//p[contains(text(),'До психолога вас отделяет несколько"
                                                      " кликов')]")
    WHATSAPP_CARE_ICON = (By.XPATH, "//div[@class='xs-force-center soc-icon paddings-30px color css186']/"
                                    "/a[@class='link wa']//div[contains(@class,'bg')]")
    TELEGRAM_CARE_ICON = (By.XPATH, "//div[@class='xs-force-center soc-icon paddings-30px color css186']"
                                    "//a[@class='link tg']//div[contains(@class,'bg')]")

    # page bottom
    LIFEHELP_SERVICE_TEXT_PAGE_BOTTOM = (By.CSS_SELECTOR, "p[class='textable css191'] strong")
    CONTRACT_OFFER_TITLE_PAGE_BOTTOM = (By.XPATH, "(//span[@class='text'][contains(text(),'Договор оферты')])[1]")
    AGREEMENT_TITLE_PAGE_BOTTOM = (By.XPATH, "(//span[@class='text'][contains(text(),'Условия использования')])[1]")
    PRIVACY_POLICY_PAGE_BOTTOM = (By.XPATH, "(//span[@class='text'][contains(text(),'Политика конфиденциальности')])[1]")
    CONSENT_MAILING_PAGE_BOTTOM = (By.XPATH, "(//span[@class='text'][contains(text(),'Согласие на получение "
                                             "информационных рассылок')])[1]")
    VK_ICON_PAGE_BOTTOM = (By.XPATH, "//div[@class='xs-force-center soc-icon paddings-10px white css196']//"
                                     "a[@class='link vk']//div[contains(@class,'bg')]")
    TELEGRAM_ICON_PAGE_BOTTOM = (By.XPATH, "//div[@class='xs-force-center soc-icon paddings-10px white css196']"
                                           "//a[@class='link tg']//div[contains(@class,'bg')]")
    TO_REGISTER_PAGE_BOTTOM = (By.CSS_SELECTOR, ".btn.btn-legacy.hvr-shutter-out-horizontal.font-header.css198")
