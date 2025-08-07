from behave import given, when, then
from pages.cart_page import CartPage


@given("Open Target main page")
def step_open_main(context):
    context.app.main_page.open_main()


@when("Click on Cart icon")
def step_click_cart(context):
    context.app.cart_page.open_cart()


@then('Verify "Your cart is empty" message is shown')
def step_verify_empty_cart_msg(context):
    context.app.cart_page.verify_cart_empty_msg()
