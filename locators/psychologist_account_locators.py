from selenium.webdriver.common.by import By

class PsychologistAccountLocators:
    SEE_FIRST_SESSION_INSTRUCTION_BTN = (By.CSS_SELECTOR, ".animate__button-filled.button__medium-blue-filled")
    WEEK_SCHEDULE_BTN = (By.XPATH, "//a[contains(text(),'Неделя')]")
    MONTH_SCHEDULE_BTN = (By.XPATH, "//a[contains(text(),'Месяц')]")
    PERSONAL_DATA_MENU_NAVIGATION = (By.XPATH, "//span[contains(text(),'Личные данные')]")
    WORKING_HOURS_TITLE_PERSONAL_DATA = (By.XPATH, "//a[contains(text(),'График работы')]")
    HOUR_00_SUNDAY = (By.XPATH, "(//div[@class='select-time__card-checkbox-content'][normalize-space()='0:00'])[7]")
    SAVE_CHANGES_BTN = (By.CSS_SELECTOR, "button[data-name='weekschedule']")
    WORKING_HOUR_172_SUNDAY_00 = (By.XPATH, "(//label)[172]")
    BOOKING_TIME_PSYCHOLOGIST_ACCOUNT = (By.XPATH, "//input[@id='booking-time__input']")
    SET_EXACT_DAY_SCHEDULE = (By.XPATH, "//a[contains(text(),'Настройте каждый день')]")
    FIRST_TIME_LAST_EXACT_DAY_SCHEDULE = (By.XPATH, "(//label)[508]")
    SAVE_CHANGES_EXACT_DAY_SCHEDULE = (By.CSS_SELECTOR, "button[data-name='dateschedule']")

    CLIENTS_AND_AIMS_MENU_PSYCHOLOGIST = (By.XPATH, "//span[contains(text(),'Клиенты и цели')]")
    SELECT_AYGUL_TEST_CLIENTS_AIMS = (By.CSS_SELECTOR, "div[class='account__my-notes-tab-item active'] a:nth-child(1)")
    THREE_DOTS_PSYCHOLOGIST_CLIENTS_AIM = (By.XPATH, "//a[@class='client__context-menu-button']//*[name()='svg']")
    CREATE_NEW_SESSION_PSYCHOLOGIST = (By.CSS_SELECTOR, ".context__menu-link.create__new-session")
    TO_CREATE_BUTTON_CREATE_SESSION_PSYCHOLOGIST = (By.CSS_SELECTOR, "div[class='form__buttons'] button"
                                                                     "[class='animate__button-filled button__"
                                                                     "medium-blue-filled']")
    SUCCESSFUL_CREATION_SESSION_PSYCHOLOGIST_TEXT = (By.CSS_SELECTOR, "div[id='recreate-session-success'] h1")
    FINE_BUTTON_CREATE_SESSION_PSYCHOLOGIST = (By.XPATH, "//button[contains(text(),'Отлично!')]")
    YOU_HAVE_SUCCESSFULLY_ORDERED_CLIENT_SESSION_MSG = (By.XPATH, "//div[@id='recreate-session-success']//h1")
    ERROR_MSG_SELECTED_ORDER_TIME_IS_OCCUPIED = (By.XPATH, "//p[@class='recreate__session-notification-error-text']")

    # aims
    ADD_NEW_AIM_BUTTON_PSYCHOLOGIST = (By.CSS_SELECTOR, ".animate__button-outline.button__medium-blue-outline")
    AIM_NAME_FIELD_CREATE_CLIENT = (By.CSS_SELECTOR, "#target-title")
    AIM_DESCRIPTION_FIELD_CREATE_CLIENT = (By.CSS_SELECTOR, "#target-description")
    AIM_START_DAY_CREATE_CLIENT = (By.CSS_SELECTOR, "input[name='start-date']")
    AIM_END_DAY_CREATE_CLIENT = (By.CSS_SELECTOR, "input[name='end-date']")
    CREATE_NEW_AIM_BUTTON_CLIENT = (By.CSS_SELECTOR, "#target__form-create-button")
    NAME_OF_THE_CREATED_AIM_CLIENT = (By.XPATH, "//h3[normalize-space()='My aim']")
    AIM_2_CLIENT_ACCOUNT = (By.XPATH, "(//a[contains(@class,'client__target-object')])[2]")
    AIM_STATUS_CLIENT_ACCOUNT = (By.XPATH, "//div[contains(@class,'update__target-subform')]//select[contains"
                                           "(@name,'target-status')]")
    AIM_STATUS_IN_PROGRESS = (By.XPATH, "(//option[@value='1'][contains(text(),'В работе')])[2]")
    SAVE_AIM_CHANGES_BUTTON_CLIENT = (By.CSS_SELECTOR, "#target__form-update-button")
    AIM_STATUS_COMPLETED = (By.XPATH, "//option[@value='2']")
    AIM_STATUS_CREATED = (By.XPATH, "//div[@class='update__target-subform']//option[@value='0'][contains(text(),"
                                    "'Создана')]")
    REMOVE_AIM_BUTTON_CLIENT = (By.CSS_SELECTOR, "#target__form-remove-button")