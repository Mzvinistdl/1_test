"""Module providing Step Methods for Navigation"""
from behave import given, then, when # pylint: disable=no-name-in-module


@given('user is on the home screen')
def step_impl_home(context):
    """Step for validation Home Screen"""
    context.home_page.verify_home_page()
    # inherited method in login_page:
    context.login_page.verify_home_page()


@when('user tap on option {number:d}')
def step_impl_tap_op(context, number):
    """Step for tapping on specific Option"""
    context.home_page.verify_home_page().tap_on_option_by_index(number)


@then('user is on the login screen')
def step_impl_login(context):
    """Step for validation Login Screen"""
    context.login_page.verify_login_page()


@then('user is on list screen')
def step_impl_list(context):
    context.list_page.verify_list_page()


@then('user is on shop screen')
def step_impl_shop(context):
    context.shop_page.verify_shop_page()

