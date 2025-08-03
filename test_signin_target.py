from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_target_signin():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://www.target.com")

    wait = WebDriverWait(driver, 15)

    try:
        account_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-test="accountNav-button"]')))
        account_btn.click()

        signin_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign in")))
        signin_link.click()

        wait.until(EC.presence_of_element_located((By.ID, "username")))

    except Exception as e:
        print("Something went wrong:", e)

    driver.quit()
