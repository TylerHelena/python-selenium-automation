from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage

class Header(BasePage):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/search/SearchButton']")

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(10)



class Header(BasePage):
    # existing search stuff can stay...

    ACCOUNT_BTN = (By.XPATH, "//button[@data-test='accountNav-button']")
    SIGN_IN_MENU_LINK = (By.XPATH, "//a[.//span[text()='Sign in']]")

    def open_account_menu(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.ACCOUNT_BTN)
        ).click()

    def click_sign_in_from_menu(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.SIGN_IN_MENU_LINK)
        ).click()