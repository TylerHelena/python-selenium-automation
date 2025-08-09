from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ICON = (By.XPATH, "//a[@data-test='@web/CartLink']")
    CART_ITEM = (By.CSS_SELECTOR, "[data-test='cartItem']")  # generic cart line item
    EMPTY_TITLE = (By.XPATH, "//h1[contains(translate(., 'EMPTY', 'empty'),'empty')]")

    def open_cart(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.CART_ICON)
        ).click()

    def has_items(self):
        # returns True if at least one item present and not the empty message
        try:
            WebDriverWait(self.driver, 8).until(
                EC.presence_of_element_located(self.CART_ITEM)
            )
            return True
        except Exception:
            return False

    def is_empty(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.EMPTY_TITLE)
            )
            return True
        except Exception:
            return False