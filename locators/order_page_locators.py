from selenium.webdriver.common.by import By

class OrderPageLocators:
    TITLE_ORDER_PAGE = (By.CSS_SELECTOR, ".order-header__text")

    ONE_SESSION_BTN = (By.CSS_SELECTOR, "label[for='quantity-1'] span")
    PACKAGE_4_BUTTON_NEW_ORDER_PAGE = (By.CSS_SELECTOR, "label[for='quantity-4'] span")
    TO_PAY_ORANGE_BUTTON_ORDER_PAGE = (By.CSS_SELECTOR, ".price-price.payment-button__price")

    CURRENCY_ORANGE_BTN_TO_PAY_ORDER_PAGE = (By.CSS_SELECTOR, ".payment-button.price-currency")

    PACKAGE_8_BUTTON_NEW_ORDER_PAGE = (By.CSS_SELECTOR, "label[for='quantity-8'] span")
    PACKAGE_12_BUTTON_NEW_ORDER_PAGE = (By.CSS_SELECTOR, "label[for='quantity-12'] span")
    PACKAGE_54_BUTTON_NEW_ORDER_PAGE = (By.CSS_SELECTOR, "label[for='quantity-54']")
    ONETIME_PAYMENT_PACKAGE_54_BUTTON_NEW_ORDER_PAGE = (By.XPATH, "//span[contains(text(),'Единоразовый платеж')]")
    USD_PAYMENT_BUTTON_NEW_ORDER_PAGE = (By.CSS_SELECTOR, "label[for='usd']")
    EURO_PAYMENT_BUTTON_NEW_ORDER_PAGE = (By.CSS_SELECTOR, "label[for='eur']")
    PACKAGE_DESCRIPTION_TEXT_NEW_ORDER_PAGE = (By.CSS_SELECTOR, "div[class='content-left__line package-info RUB active']"
                                                                " div[class='quantity-description'] div")
    PSYCHOLOGIST_PROFILE = (By.CSS_SELECTOR, "a[class='order-nav__link']")

    SEPARATE_SESSION_PRICE_PACKAGE = (By.CSS_SELECTOR, "div[class='content-left__line package-info RUB active'] "
                                                       "div[class='quantity-price'] span[class='total-price']")
    SEPARATE_SESSION_USD_PRICE_PACKAGE = (By.CSS_SELECTOR, "div[class='content-left__line package-info USD active'] "
                                                           "div[class='quantity-price'] span[class='total-price']")
    SEPARATE_SESSION_EURO_PRICE_PACKAGE = (By.CSS_SELECTOR, "div[class='content-left__line package-info EUR active'] "
                                                            "div[class='quantity-price'] span[class='total-price']")
    SUPPORT_BUTTON_ORDER_PAGE = (By.CSS_SELECTOR, ".support-button")