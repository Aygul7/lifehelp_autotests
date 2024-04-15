from selenium.webdriver.common.by import By

class IndexLocators:
    COOKIE_BUTTON = (By.CSS_SELECTOR, '.animate__button-filled.button__medium-red-filled')
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".animate__button-outline.button__small-small-width-blue-outline")
    GET_PSYCHOLOGIST_BUTTON = (By.XPATH, "//button[@class='animate__button-filled button__small-red-filled']")
    TELEGRAM_CARE_LOGO = (By.CSS_SELECTOR, "div[class='care-service-social'] img[alt='telegram-logo']")
    WHATSAPP_CARE_LOGO = (By.CSS_SELECTOR, "div[class='care-service-social'] img[alt='whatsapp-logo']")
    WHATSAPP_PAGE_HEADER = (By.XPATH, "//span[@class='_afw1']//img[@alt='Главная страница WhatsApp']")
    SKYPE_PHONE_NUMBER_HELP_MAIN_PAGE = (By.CSS_SELECTOR, ".phone__call")
    VK_GROUP_FOOTER_WIDGET = (By.XPATH, "//a[@href='https://vk.com/life_help']//*[name()='svg']")
    PAY_2990_PRICE = (By.XPATH, "//strong[contains(text(),'2950 ₽')]")