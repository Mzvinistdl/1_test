"""Module providing Page Methods and Elements for Home Page"""
from testui.elements.testui_element import e
from features.pages.base_page import BasePage


class HomePage(BasePage):
    """Home page class and methods"""
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver = driver
        self.__page_title = e(driver, "id", "headerTitle")
        self.__options = e(driver, "className", "android.widget.Button")

    def verify_home_page(self):
        """Verifies home page elements"""
        self.__page_title.wait_until_attribute(attr='text', text='HomeScreen', seconds=10)
        return self

    def tap_on_option_by_index(self, num):
        """Taps on the specific option to test"""
        self.__options.get(num - 1).click()
