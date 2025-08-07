from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ICON = (By.XPATH, "//a[@data-test='@web/CartLink']")
    EMPTY_CART_TEXT = (By.XPATH, "//h1[contains(text(), 'empty')]")

    def open_cart(self):
        self.click(*self.CART_ICON)

    def verify_cart_empty_msg(self):
        actual_text = self.find_element(*self.EMPTY_CART_TEXT).text
        assert "empty" in actual_text.lower(), f'Expected "empty" in message, but got: {actual_text}'
