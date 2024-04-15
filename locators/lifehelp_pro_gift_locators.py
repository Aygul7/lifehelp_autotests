from selenium.webdriver.common.by import By

class LhproGiftLocators:
    BUY_CERTIFICATE_UPPER_1ST_BTN = (By.XPATH, "(//span[@class='text'][contains(text(),'Купить сертификат')])[1]")
    YOU_CAN_SELECT_GIFT_BLOCK_TITLE = (By.XPATH, "//body/div[@class='area-wrapper']/div[7]/div[2]/div[1]/div[1]/h2[1]")
    BUY_CERTIFICATE_2ND_BTN = (By.CSS_SELECTOR, "a[class='btn btn-legacy font-text css26'] span[class='text']")
    TO_KNOW_DETAILS_BTN = (By.CSS_SELECTOR, "a[class='btn btn-legacy font-text css27'] span[class='text']")
    HOW_IT_WORKS_DETAILS_BLOCK_TITLE = (By.CSS_SELECTOR, "div[id='how'] h2[class='textable css56']")
    SELECT_CERTIFICATE_STEP_ONE = (By.XPATH, "//h2[contains(text(),'Выбирайте номинал сертификата и нажимайте кнопку «')]")
    CERTIFICATES_SLIDER_RIGHT_BTN = (By.CSS_SELECTOR, ".slider1-next")
    CERTIFICATE_4_SESSIONS_TITLE = (By.XPATH, "//div[@class='node widget-max-width widget css66 css67']"
                                        "//strong[contains(text(),'4 сессии')]")
    CERTIFICATES_SLIDER_LEFT_BTN = (By.CSS_SELECTOR, ".fa.fa-chevron-left")
    CERTIFICATE_54_SESSIONS_TITLE = (By.XPATH, "//strong[contains(text(),'54 сессии')]")
    PRICE_125000_CERTIFICATE_54 = (By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(15) > div:nth-child(2) > "
                                                    "div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-"
                                                    "child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) "
                                                    "> div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth"
                                                    "-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3)"
                                                    " > p:nth-child(1) > span:nth-child(1) > strong:nth-child(1)")
    PRICE_28800_CERTIFICATE_12 = (By.XPATH, "//strong[contains(text(),'28 800 ₽')]")
    PRICE_20800_CERTIFICATE_8 = (By.XPATH, "//strong[contains(text(),'20 800 ₽')]")
    PRICE_10800_CERTIFICATE_4 = (By.XPATH, "//strong[contains(text(),'10 800 ₽')]")
    PRICE_2950_CERTIFICATE_1 = (By.XPATH, "//strong[contains(text(),'2 950 ₽')]")

    CERTIFICATE_54_IMAGE = (By.CSS_SELECTOR, "img[src='https://img2.creatium.app/disk2/9d/3d/4a/2a1a47ef3d396d5aa6ff"
                                             "ccb4bc1dcadd50/card_11_1.png']")

    TO_PRESENT_CERTIFICATE_54_SESSIONS_BTN = (By.XPATH, "(//span[contains(text(),'Подарить')])[1]")
    TO_PRESENT_CERTIFICATE_12_SESSIONS_BTN = (By.XPATH, "(//span[@class='text'][contains(text(),'Подарить')])[2]")
    TO_PRESENT_CERTIFICATE_8_SESSIONS_BTN = (By.XPATH, "(//span[@class='text'][contains(text(),'Подарить')])[3]")
    TO_PRESENT_CERTIFICATE_4_SESSIONS_BTN = (By.XPATH, "(//span[@class='text'][contains(text(),'Подарить')])[4]")
    TO_PRESENT_CERTIFICATE_1_SESSIONS_BTN = (By.XPATH, "(//span[@class='text'][contains(text(),'Подарить')])[5]")

    PRIVACY_POLICY_TITLE = (By.XPATH, "//a[@class='btn btn-legacy hvr-fade font-text css109']//span[@class='text']"
                                      "[contains(text(),'Политика обработки персональных данных')]")
    SEPARATE_SESSION_PRICE_CERTIFICATE_54 = (By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(15) > div:nth-"
                                                              "child(2) > div:nth-child(1) > div:nth-child(3) > div:nth"
                                                              "-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth"
                                                              "-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth"
                                                              "-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth"
                                                              "-child(2) > div:nth-child(2) > div:nth-child(1) > p:nth-"
                                                              "child(1) > span:nth-child(1) > strong:nth-child(1)")
    SEPARATE_SESSION_PRICE_CERTIFICATE_12 = (By.XPATH, "//strong[contains(text(),'2 400 ₽/встреча')]")
    SEPARATE_SESSION_PRICE_CERTIFICATE_8 = (By.XPATH, "//strong[contains(text(),'2 600 ₽/встреча')]")
    SEPARATE_SESSION_PRICE_CERTIFICATE_4 = (By.XPATH, "//strong[contains(text(),'2 700 ₽/встреча')]")


