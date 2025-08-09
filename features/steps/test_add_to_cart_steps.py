from behave import given, when, then

@given("Open Target main page")
def step_open_main(context):
    context.app.main_page.open_main()

@when('Search for "{product}" from header')
def step_search(context, product):
    context.app.header.search_product(product)

@when("Open first product from results")
def step_open_first_pdp(context):
    context.app.search_results.open_first_product()

@when("Add product to cart")
def step_add_to_cart(context):
    context.app.product_page.add_to_cart()
    context.app.product_page.confirm_side_nav_add()
    context.app.product_page.go_to_cart_from_drawer()

@then("Verify cart has at least one item")
def step_verify_cart_item(context):
    # If the side drawer didn't navigate, open cart via header icon:
    if not context.app.cart_page.has_items():
        context.app.cart_page.open_cart()
    assert context.app.cart_page.has_items(), "Cart has no items (still empty)."
