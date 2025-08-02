from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_target_signin():  # <--- Add this function!
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://www.target.com")
    time.sleep(8)

    try:
        account_btn = driver.find_element(By.XPATH, '//button[@data-test="accountNav-button"]')
        account_btn.click()
        print("Clicked account button.")

        time.sleep(2)

        signin_link = driver.find_element(By.LINK_TEXT, "Sign in")
        signin_link.click()
        print("Clicked sign in.")

    except Exception as e:
        print("Something went wrong:", e)

    time.sleep(5)
    driver.quit()