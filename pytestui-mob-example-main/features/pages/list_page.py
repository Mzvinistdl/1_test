import re
import time

from appium.webdriver.common.touch_action import TouchAction
from testui.elements.testui_element import e
from features.pages.home_page import HomePage


def clean_car_brands(car_brands):
    """Cleans the car brands list by removing special characters"""
    cleaned_brands = []

    for brand in car_brands:
        cleaned_text = re.sub(r"[^a-zA-Z0-9\s-]", "", brand)
        if cleaned_text:  # Only add non-empty cleaned text
            cleaned_brands.append(cleaned_text)

    return cleaned_brands


class ListPage(HomePage):
    """List page class and methods"""
    def __init__(self, driver):
        HomePage.__init__(self, driver)
        self.driver = driver
        self.__page_identifier = e(driver, "xpath", "//*[contains(@text, 'Part 2')]")
        self.__car_brands = e(driver, "xpath", "//android.widget.TextView")
        self.__end_element = e(driver, "xpath", "//android.widget.TextView")

    def verify_list_page(self):
        """Verify list page method"""
        self.__page_identifier.wait_until_visible(10)

    def swipe_up(self):
        """Swipe up to reveal more elements."""
        start_x = 500
        start_y = 2150
        end_y = 400

        TouchAction(self.driver).press(x=start_x, y=start_y).move_to(x=start_x, y=end_y).release().perform()
        time.sleep(2)

    def get_car_brands(self):
        """Extracts the car brand names from the list while preserving order, removing duplicates"""
        car_brands = []
        seen = set()
        index = 1
        last_element_text = "Zcc"

        while True:
            try:
                car_brand_element = e(self.driver, "xpath",
                                      f"//android.widget.TextView[@resource-id='com.example.appfortestautomation"
                                      f":id/textView'][{index}]")

                # If element is not found, perform a swipe
                if not car_brand_element.is_visible():
                    print(f"Element at index {index} not found, performing swipe to load more.")
                    self.swipe_up()
                    index = 1
                    continue

                text = car_brand_element.get_text()
                print(f"Element {index} text: {text}")

                if text and "---" not in text and text not in seen:
                    seen.add(text)  # Mark as seen
                    car_brands.append(text)

                if text == last_element_text:
                    print(f"Reached last element: {last_element_text}")
                    break

                index += 1

            except Exception as ex:
                print(f"Failed to retrieve car brand at index {index}: {ex}")
                break

        return clean_car_brands(car_brands)

    def verify_list(self):
        """Checks if the car brand list is displayed in correct alphabetical order"""
        car_brands = self.get_car_brands()

        sorted_brands = sorted(car_brands, key=lambda x: x.lower())  # Case-insensitive sorting

        assert car_brands == sorted_brands, (f"Car brands list is NOT displayed in correct alphabetical order! "
                                             f"\nOriginal: {car_brands}"
                                             f"\nSorted: {sorted_brands}")

