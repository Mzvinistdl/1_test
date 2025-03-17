"""Module providing Step Methods for Login"""
from behave import when, then # pylint: disable=no-name-in-module


@when('user enters username as "{username}"')
def step_impl_login_username(context, username):
    """Step for setting username for login"""
    context.login_page.enter_name(username)


@when('user enters email as "{email}"')
def step_impl_login_email(context, email):
    """Step for setting email for login"""
    context.login_page.enter_email(email)


@when('user enters password as "{password}"')
def step_impl_login_pwd(context, password):
    """Step for setting password for login"""
    context.login_page.enter_password(password)


@when('user taps submit button')
def step_impl_login_submit(context):
    """Step for submitting login info"""
    context.login_page.tap_submit()


@then('popup_message is "{popup_message}"')
def step_impl_login_msg(context, popup_message):
    """Step for checking login popup info"""
    context.login_page.verify_popup_message(popup_message)
