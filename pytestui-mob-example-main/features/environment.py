"""Module providing Environment Setup/TearDown"""
from datetime import datetime
import glob
import os
import allure


from testui.support.appium_driver import NewDriver
from allure_commons.types import AttachmentType
from allure_behave.hooks import allure_report

from features.pages.base_page import BasePage
from features.pages.home_page import HomePage
from features.pages.list_page import ListPage
from features.pages.login_page import LoginPage


def before_all(_context):
    """Before all - Cleaning artifacts folder"""
    reports = glob.glob('features/artifacts/reports/*')
    screenshots = glob.glob('features/artifacts/screenshots/*')
    folders = [reports, screenshots]

    try:
        for folder in folders:
            for file in folder:
                os.remove(file)
    except OSError:
        print('-- Reports folder empty --')

    # Creating folder for screenshots
    try:
        os.mkdir('features/artifacts/screenshots')
    except OSError as error:
        print(error)


def before_scenario(context, scenario):
    """SetUP Fixtures for Test Scenarios Execution"""
    print(f'-- Start Scenario: {scenario} --')
    context.driver = (
        NewDriver().set_full_reset(True)
            .set_platform("android")
            .set_udid("RFCWB13GMAA")  # Change UDID for iOS device
            .set_app_package_activity(
        'com.example.appfortestautomation', 
        'com.example.appfortestautomation.MainActivity'
        )
            .set_logger("behave")
            .set_appium_driver()
    )
    context.driver.configuration.save_full_stacktrace = False
    context.base_page = BasePage(context.driver)
    context.home_page = HomePage(context.driver)
    context.login_page = LoginPage(context.driver)
    context.list_page = ListPage(context.driver)


def after_scenario(context, scenario):
    """TearDown Fixtures for Test Execution"""
    print(f'-- End Scenario: {scenario} --')
    test_datetime = datetime.now().strftime("%d%m%Y%H%M%S")
    screenshot_name = f"{scenario.name}_{scenario.status}_{test_datetime}.png"
    if scenario.status == 'failed':
        allure.attach(
            context.driver.get_driver().get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )
    context.driver.quit()


def after_feature(_context, _feature):
    """TearDown Fixtures for Test Execution Feature"""
    allure_report("features/artifacts/reports")
