from selenium.webdriver.common.by import By

class VebLifeHelpLocators:
    LOGIN_BUTTON_VEB_LH = (By.CSS_SELECTOR, "div[class='grid valign-middle paddings-10px xs-wrap'] div[class='grid v"
                                     "align-middle paddings-0px'] span[class='text']")
    REGISTRATION_BUTTON_VEB_LH = (By.CSS_SELECTOR, "div[class='node widget-button widget css12'] span[class='text']")
    PRESENT_CERTIFICATE_BUTTON = (By.CSS_SELECTOR, "div[class='node widget-menu widget xs-hidden sm-hidden lg-hidden "
                                                   "css13'] span[class='text']")
    WIDGET_HELP_ELEMENTS = (By.CSS_SELECTOR, "div[class='node widget-menu widget xs-hidden sm-hidden lg-hidden css13'] "
                                             "span[class='text']")
    WHATSAPP_WIDGET_VEB_LH = (By.CSS_SELECTOR, "div[class='node widget-element widget css222'] a[class='sprite "
                                               "sprite-92whatsapp']")
    TELEGRAM_WIDGET_VEB_LH = (By.CSS_SELECTOR, "div[class='node widget-element widget css222'] a[class='sprite "
                                               "sprite-93telegram']")
    TERMS_OF_USAGE_VEB_LH = (By.XPATH, "//a[@class='btn btn-legacy hvr-fade font-text css298']//span[@class='text']"
                                       "[contains(text(),'Условия использования')]")
    PRIVACY_POLICY_VEB_LH = (By.XPATH, "//a[@class='btn btn-legacy hvr-fade font-text css298']//span[@class='text']"
                                       "[contains(text(),'Политика конфиденциальности')]")
    CONSENT_MAILING_VEB_LH = (By.XPATH, "//a[@class='btn btn-legacy hvr-fade font-text css298']//span[@class='text']"
                                        "[contains(text(),'Согласие на получение информационных рассылок')]")
    OFERTA_DOCUMENT_VEB_LH = (By.XPATH, "//a[@class='btn btn-legacy hvr-fade font-text css298']//span[@class='text']"
                                        "[contains(text(),'Договор оферты')]")
    ORDER_20_MIN_SESSION_VEB_LH = (By.XPATH, "//button[@class='btn btn-legacy font-text css60']//span[@class='text']"
                                             "[contains(text(),'Записаться на бесплатную 20-минутную консультацию')]")
    NAME_20MIN_ORDER_VEB_LH = (By.CSS_SELECTOR, "input[autocomplete='name']")
    PHONE_20MIN_ORDER_VEB_LH = (By.CSS_SELECTOR, "input[autocomplete='tel']")
    SEND_20MIN_ORDER_VEB_LH = (By.XPATH, "//span[contains(text(),'ЗАПИСАТЬСЯ НА ПОДБОР')]")
    SUCCESSFUL_ANSWER_SEND_ORDER_20MIN_VEB_LH = (By.XPATH, "(//div[@class='swal-title'])[1]")
    VK_WIDGET_VEB_LH = (By.XPATH, "//div[@class='xs-force-center soc-icon paddings-10px white css280']//"
                                  "a[@class='link vk']")
    TELEGRAM_GROUP_WIDGET_VEB_LH = (By.XPATH, "//div[@class='xs-force-center soc-icon paddings-10px white css280']//"
                                              "a[@class='link tg']")
    TO_REGISTER_BUTTON_FOOTER = (By.XPATH, "//a[@class='btn btn-legacy hvr-shutter-out-horizontal font-header css296']")

