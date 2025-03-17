"""Module providing Page Methods and Elements for Login Page"""
from testui.elements.testui_element import e
from testui.elements.testui_collection import ee

from features.pages.home_page import HomePage


class LoginPage(HomePage):
    """Login page class and methods"""
    def __init__(self, driver):
        HomePage.__init__(self, driver)
        self.driver = driver
        self.__page_identifier = e(driver, "xpath", "//*[contains(@text, 'Part ')]")
        self.__username_field = e(driver, "id", "editTextTextPersonName")
        self.__email_field = e(driver, "id", "editTextTextEmailAddress")
        self.__password_field = e(driver, "id", "editTextTextPassword")
        self.__submit_button = e(driver, "id", "submit")
        self.__popup = e(driver, "id", "popupRecyclerView")

    def verify_login_page(self):
        """Verify login page method"""
        collection = ee(
            self.__page_identifier, self.__username_field, self.__email_field,
            self.__password_field, self.__submit_button
            )
        collection.wait_until_all_visible(10)

    def enter_name(self, name):
        """Type name in login name field, 
        input: name (string)"""
        self.__username_field.send_keys(name)

    def enter_email(self, email):
        """Type email in login email field, 
        input: email (string)"""
        self.__email_field.send_keys(email)

    def enter_password(self, pwd):
        """Type pasword in login password field, 
        input: pwd (string)"""
        self.__password_field.send_keys(pwd)

    def tap_submit(self):
        """Taps on submit button in login form"""
        self.__submit_button.click()

    def verify_popup_message(self, reason=None):
        """Verifies message in login form"""
        msg = None
        self.__popup.wait_until_visible()

        # match feature (switch case) might be used only in python 3.10+
        match reason:
            case "username_err":
                msg = "Incorrect username! Expected to match: ^[a-zA-Z0-9]{4,}$"
            case "email_err":
                msg = r"Incorrect email! Expected to match: ^[a-zA-Z0-9].+@[a-z0-9].+\.[a-z].+$"
            case "password_err":
                msg = "Incorrect password! Expected to match: "\
                "^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[@$!%*#?&])[A-Za-z0-9@$!%*#?&]{8,}$"
            case "success":
                msg = "Success"

        e(self.driver, "xpath", f"//*[contains(@text, '{msg}')]").wait_until_visible()
