from behave import given, when, then
from pages.sign_in_page import SignInPage

@given("Open Target sign in page")
def open_sign_in(context):
    # Direct link per homework
    context.app.sign_in_page.open_direct("https://www.target.com/orders?lnk=acct_nav_my_account")

@when("Store original window")
def store_original_window(context):
    context.original_window = context.driver.current_window_handle

@when("Click on Terms & Conditions link")
def click_terms(context):
    context.app.sign_in_page.click_terms_link()

@when("Switch to the newly opened window")
def switch_to_new_window(context):
    context.app.sign_in_page.switch_to_new_window(context.original_window)

@then("Verify Terms & Conditions page is opened")
def verify_terms_open(context):
    assert context.app.sign_in_page.terms_page_is_open(), "Terms & Conditions page not opened"

@then("Close new window and switch back to original")
def close_and_back(context):
    context.driver.close()
    context.driver.switch_to.window(context.original_window)
