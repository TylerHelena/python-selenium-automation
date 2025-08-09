from behave import given, when, then
from pages.search_results_page import SearchResultsPage
from pages.main_page import MainPage
from pages.header import Header

@given("the user is on the Target homepage")
def step_go_home(context):
    MainPage(context.driver).open_main()

@when('the user searches for "{product}"')
def step_search(context, product):
    Header(context.driver).search_product(product)

@then('Verify search results contain the word "{product}"')
def step_verify_heading(context, product):
    # If your SearchResultsPage has verify_search_results(expected_text)
    SearchResultsPage(context.driver).verify_search_results(product)

@then("Verify that every product has a name and an image")
def step_verify_cards(context):
    SearchResultsPage(context.driver).verify_all_products_have_name_and_image()
