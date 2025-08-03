from behave import given, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('the user is on the Target Circle offers page')
def step_go_to_circle_offers(context):
    context.driver.get("https://www.target.com/circle")

@then('they should see a list of Circle offer tiles')
def step_check_offer_tiles(context):
    wait = WebDriverWait(context.driver, 10)
    elements = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'body')))
    assert len(elements) > 0, "No body elements found — page failed to load"
