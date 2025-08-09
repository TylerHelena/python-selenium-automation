from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class SignInPage(BasePage):
    EMAIL_INPUT = (By.ID, "username")   # Target's email/username field
    # You can add PASSWORD = (By.ID, "password") later if needed

    def is_open(self):
        # returns True if the username field is present/visible
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.EMAIL_INPUT)
        )
        return True

