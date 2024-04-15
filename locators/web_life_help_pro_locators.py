from selenium.webdriver.common.by import By

class WebLifeHelpLocators:
    SELECT_DOCTOR_BUTTON_WEB_LH = (By.CSS_SELECTOR, "div[class='node widget-grid widget css10'] span[class='text']")
    TELEGRAM_HELP_WEB_LH_PRO = (By.CSS_SELECTOR, "div[class='xs-force-center soc-icon paddings-10px white css40'] "
                                                 "a[class='link tg']")
    WHATSAPP_WIDGET_WEB_LH = (By.CSS_SELECTOR, "div[class='xs-force-center soc-icon paddings-10px white css40'] "
                                               "a[class='link wa']")
    WHATSAPP_PAGE_HEADER = (By.XPATH, "//span[@class='_afw1']//img[@alt='Главная страница WhatsApp']")

    TERMS_OF_USAGE_WEB_LH = (By.XPATH, "//a[@class='btn btn-legacy hvr-fade font-text css222']//span[@class='text']"
                                       "[contains(text(),'Условия использования')]")
    PRIVACY_POLICY_WEB_LH = (By.XPATH, "//a[@class='btn btn-legacy hvr-fade font-text css222']//span[@class='text']"
                                       "[contains(text(),'Политика конфиденциальности')]")
    CONSENT_MAILING_WEB_LH = (By.XPATH, "//a[@class='btn btn-legacy hvr-fade font-text css222']//span[@class='text']"
                                        "[contains(text(),'Согласие на получение информационных рассылок')]")
    VK_WIDGET_WEB_LH = (By.XPATH, "//div[@class='xs-force-center soc-icon paddings-10px white css210']//"
                                  "a[@class='link vk']")
    TELEGRAM_GROUP_WIDGET_WEB_LH = (By.XPATH, "//div[@class='xs-force-center soc-icon paddings-10px white css210']//"
                                              "a[@class='link tg']")
