"""Module providing Page Methods and Elements for Base Page"""
from testui.elements.testui_element import e

class BasePage:
    """Class Base Page"""
    def __init__(self, driver):
        self.driver = driver
        self.__example_element = e(driver, "xpath", "//random")

    def example_inherit(self, test):
        """Example of inheritance"""
        print(f'Inherit test: {test}')
        print(self.__example_element.is_visible())

    def example_inherit_2(self, test):
        """Example of inheritance"""
        print(f'Inherit test2: {test}')
        print(self.__example_element.is_visible())
