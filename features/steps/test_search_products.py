from behave import given, when, then
from time import sleep
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage

@given('the user is on the Target homepage')
def step_go_to_homepage(context):
    context.driver.get("https://www.target.com")
    sleep(2)

@when('the user searches for "{product}"')
def step_search_product(context, product):
    main_page = MainPage(context.driver)
    main_page.search_product(product)

@then('Verify that every product has a name and an image')
def verify_products_have_name_and_image(context):
    results_page = SearchResultsPage(context.driver)
    results_page.verify_all_products_have_name_and_image()
