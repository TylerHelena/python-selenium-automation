from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@given('the user is on the Target homepage')
def step_go_to_homepage(context):
    context.driver.get("https://www.target.com")
    time.sleep(2)

@when('the user searches for "{product}"')
def step_search_product(context, product):
    search_box = context.driver.find_element(By.ID, "search")
    search_box.clear()
    search_box.send_keys(product)
    search_box.send_keys(Keys.ENTER)
    time.sleep(3)

@then('they should see results for "{product}"')
def step_see_results(context, product):
    assert product.lower() in context.driver.page_source.lower()
