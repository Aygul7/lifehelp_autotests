from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

class BaseObject:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def is_visible(self, locator):
        """
        method to find element, that presented on the page
        :param locator: locator of web element
        :return: visible element
        """
        return self.wait.until(ec.visibility_of_element_located(locator))

    def is_clickable(self, locator):
        """
        method to find element, that is clickable on the page
        :param locator: locator of web element
        :return: clickable element
        """
        return self.wait.until(ec.element_to_be_clickable(locator))

    def to_click(self, locator):
        """
        method to click on the element, that is clickable on the page
        :param locator: locator of web element
        :return: click on the element
        """
        self.is_clickable(locator).click()

    def set_value(self,locator, value):
        """
        method to get value of the element, that is visible on the page
        :param locator: locator of web element
        :return: value of the element
        """
        self.is_clickable(locator).send_keys(value)

    def get_text_of_element(self, locator):
        """
        method to get text of the element, that is visible on the page
        :param locator: locator of web element
        :return: text of the element
        """
        return self.is_clickable(locator).text

    def get_text_title_of_element(self, locator):
        """
        method to get title of the element, that is visible on the page
        :param locator: locator of web element
        :return: title of the element
        """
        return self.is_clickable(locator).text

    def get_url(self, url):
        """
        method to url of the current page
        :param: url
        :return: url
        """
        return self.wait.until(ec.url_to_be(url))

    def move_to_element(self, locator):
        """
        method to scroll till the element, that is clickable on the page
        :param: locator of web element
        :return: scroll till the element
        """
        window_height = self.driver.execute_script("return window.innerHeight")
        self.driver.execute_script(f"window.scrollTo(0, 1080);")
        elements_btn = self.is_clickable(locator)
        # elements_btn.click()

    def move_to_page_bottom(self):
        """
        method to scroll till the bottom of the page
        :param: size of the window (0, 1080)
        :return: scroll to the page bottom
        """
        window_height = self.driver.execute_script("return window.innerHeight")
        self.driver.execute_script(f"window.scrollTo(0, 1080);")
