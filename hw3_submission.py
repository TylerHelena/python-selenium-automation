#Homework 3 –

#1. Amazon.com CSS Selectors:

input#ap_customer_name           # Full Name
input#ap_email                   # Email
input#ap_password                # Password
input#continue                   # Continue Button


#2. BDD Feature: Empty Cart Message

Feature: Verify empty cart on Target

  Scenario: User opens Target and checks empty cart
    Given the user opens "https://www.target.com"
    When the user clicks on the cart icon
    Then the message "Your cart is empty" should be displayed

----

#3. BDD Feature: Sign In Navigation

Feature: Verify Sign In navigation

  Scenario: Logged out user navigates to Sign In
    Given the user opens "https://www.target.com"
    When the user clicks on the account icon
    And the user clicks on the "Sign in" link
    Then the Sign In form should be displayed
"""

# Python Code: Empty Cart Test
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_cart_is_empty():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.target.com")
    time.sleep(5)

    cart = driver.find_element(By.CSS_SELECTOR, 'a[data-test="cart-button"]')
    cart.click()
    time.sleep(3)

    message = driver.find_element(By.XPATH, '//span[contains(text(),"Your cart is empty")]')
    assert message.is_displayed()
    print("Cart is empty message verified.")
    driver.quit()

# Python Code: Sign In Navigation Test
def test_sign_in_navigation():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.target.com")
    time.sleep(5)

    account = driver.find_element(By.CSS_SELECTOR, 'button[data-test="accountNav-button"]')
    account.click()
    time.sleep(2)

    signin = driver.find_element(By.XPATH, '//a[.//span[text()="Sign in"]]')
    signin.click()
    time.sleep(3)

    username = driver.find_element(By.ID, "username")
    assert username.is_displayed()
    print("Sign In form is displayed.")
    driver.quit()