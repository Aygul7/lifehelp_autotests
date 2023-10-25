from selenium.webdriver.common.by import By

class QuestionnaireLocators:
    CLOSE_WIDGET_BUTTON = (By.XPATH, '//jdiv[@id="jivo_close_button"]')
    INDIVIDUAL_CONSULTATION_BUTTON = (By.XPATH, '//label[contains(text(),"Индивидуальная")]')
    PAIRED_CONSULTATION_BUTTON = (By.XPATH, '//label[contains(text(),"Индивидуальная")]')
    RUSSIAN_LANGUAGE_BUTTON = (By.XPATH, '//label[contains(text(),"Русский")]')
    TATAR_LANGUAGE_BUTTON = (By.XPATH, '//label[contains(text(),"Татарский")]')
    VIDEO_BUTTON = (By.XPATH, '//label[contains(text(),"Видео")]')
    AUDIO_BUTTON = (By.XPATH, '//label[contains(text(),"Аудио")]')
    CHAT_BUTTON = (By.XPATH, '//label[contains(text(),"Чат")]')
    AGE_FIELD = (By.XPATH, '//input[@id="age"]')
    NEXT_BUTTON = (By.XPATH, '//button[contains(text(),"Далее")]')
    PERSONAL_QUESTIONS_TITLE = (By.XPATH, '//p[contains(text(),"Личные вопросы")]')

