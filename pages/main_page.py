from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class MainPage(BasePage):
    SEARCH_BOX = (By.ID, "search")

    def open_main(self):
        self.open_url('https://www.target.com/')

    def search_product(self, product):
        search = self.find_element(*self.SEARCH_BOX)
        search.clear()
        search.send_keys(product)
        search.send_keys(Keys.ENTER)
