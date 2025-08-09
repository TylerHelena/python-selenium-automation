from pages.base_page import BasePage
from pages.header import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.cart_page import CartPage
from pages.sign_in_page import SignInPage

class Application:

    def __init__(self, driver):
        self.driver = driver
        self.base_page = BasePage(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_results = SearchResultsPage(driver)
        self.cart_page = CartPage(driver)  # ← Add this


class Application:
    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_results = SearchResultsPage(driver)
        self.sign_in_page = SignInPage(driver)


class Application:
    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_results = SearchResultsPage(driver)
        self.product_page = ProductPage(driver)
        self.cart_page = CartPage(driver)



