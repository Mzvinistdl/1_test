from behave import then  # pylint: disable=no-name-in-module


@then('verify list is displayed in alphabetical order')
def step_impl_verify_list(context):
    context.list_page.verify_list()
