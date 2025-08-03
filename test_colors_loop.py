from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_color_selection_loop():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.target.com/p/A-91511634")

    try:
        # Wait for color swatches to be visible
        color_swatches = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-test="colorSwatch"]')))

        for swatch in color_swatches:
            swatch.click()
            time.sleep(1)  # okay to keep if needed for UI animation
            selected = swatch.get_attribute("aria-checked")
            print("Swatch selected:", selected)
            assert selected == "true"

    except Exception as e:
        print("Error selecting colors:", e)

    driver.quit()
