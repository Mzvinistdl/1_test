"""Module providing Environment Setup/TearDown"""
import json
from datetime import datetime
import glob
import os
import allure


from testui.support.appium_driver import NewDriver
from allure_commons.types import AttachmentType
from allure_behave.hooks import allure_report
from testui.support.logger import log_info

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

    env = os.getenv("ENV")
    if not env:
        raise ValueError(log_info("TEST environment variable is not set!"))

    with open('resources/env.json', 'r') as file:
        data = json.load(file)

    if env not in data:
        raise ValueError(log_info(f"Environment '{env}' is not defined in {file.name} file!"))

    env_data = data[env]

    driver_builder = NewDriver().set_full_reset(True).set_platform(env_data["platform"]).set_udid(env_data["udid"])

    if env_data["platform"].lower() == "android":
        driver_builder.set_app_package_activity(env_data["pckg"], env_data["activity"])
    elif env_data["platform"].lower() == "ios":
        driver_builder.set_bundle_id(env_data["bundleId"])
    else:
        raise ValueError(log_info(f"Unsupported platform: {env_data['platform']}"))

    context.driver = driver_builder.set_logger("behave").set_appium_driver()
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
