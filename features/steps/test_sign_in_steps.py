from behave import given, when, then

@given("Open Target main page")
def step_open_main(context):
    context.app.main_page.open_main()

@when("Click Sign In from header menu")
def step_click_sign_in(context):
    context.app.header.open_account_menu()
    context.app.header.click_sign_in_from_menu()

@then("Verify Sign In form opened")
def step_verify_sign_in_form(context):
    assert context.app.sign_in_page.is_open()
