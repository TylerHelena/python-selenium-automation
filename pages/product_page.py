from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ProductPage(BasePage):
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")  # main PDP button
    SIDE_NAV_ADD_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")  # side cart button (if shown)
    VIEW_CART_CHECKOUT_BTN = (By.XPATH, "//a[.//span[contains(text(),'View cart') or contains(text(),'view cart')]]")

    def add_to_cart(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.ADD_TO_CART_BTN)
        ).click()

    def confirm_side_nav_add(self):
        # optional: some flows open side drawer where you must confirm
        try:
            WebDriverWait(self.driver, 6).until(
                EC.element_to_be_clickable(self.SIDE_NAV_ADD_BTN)
            ).click()
        except Exception:
            pass  # if no side nav, ignore

    def go_to_cart_from_drawer(self):
        try:
            WebDriverWait(self.driver, 8).until(
                EC.element_to_be_clickable(self.VIEW_CART_CHECKOUT_BTN)
            ).click()
        except Exception:
            pass
