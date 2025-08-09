from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class SignInPage(BasePage):
    EMAIL_INPUT = (By.ID, "username")  # presence = page loaded
    # A robust locator for the link (text can vary slightly). We try a few fallbacks.
    TERMS_LINK_XPATHS = [
        "//a[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'terms')]",
        "//a[contains(@href, 'terms')]",
        "//a[contains(@href, 'terms-conditions')]"
    ]

    def open_direct(self, url):
        self.open_url(url)
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(self.EMAIL_INPUT))

    def click_terms_link(self):
        wait = WebDriverWait(self.driver, 15)
        last_err = None
        for xp in self.TERMS_LINK_XPATHS:
            try:
                wait.until(EC.element_to_be_clickable((By.XPATH, xp))).click()
                return
            except Exception as e:
                last_err = e
        raise last_err or AssertionError("Terms link not found/clickable")

    def switch_to_new_window(self, original_handle):
        wait = WebDriverWait(self.driver, 15)
        wait.until(lambda d: len(d.window_handles) > 1)
        for handle in self.driver.window_handles:
            if handle != original_handle:
                self.driver.switch_to.window(handle)
                return
        raise AssertionError("New window not found")

    def terms_page_is_open(self):
        # Basic verification: title or URL contains "term"
        try:
            WebDriverWait(self.driver, 15).until(
                lambda d: ("term" in d.title.lower()) or ("term" in d.current_url.lower())
            )
            return True
        except Exception:
            return False


