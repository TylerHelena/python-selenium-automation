from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchResultsPage(BasePage):
    SEARCH_RESULTS = (By.XPATH, "//div[@data-test='resultsHeading']")  # Fix syntax if needed

    def verify_search_results(self):
        actual_result = self.find_element(*self.SEARCH_RESULTS).text
        assert 'tea' in actual_result, f'Expected text tea not in actual {actual_result}'

    PRODUCT_TITLES = (By.XPATH, "//a[@data-test='product-title']")
    PRODUCT_IMAGES = (By.XPATH, "//img[contains(@src, 'target')]")

    def verify_all_products_have_name_and_image(self):
        titles = self.driver.find_elements(*self.PRODUCT_TITLES)
        images = self.driver.find_elements(*self.PRODUCT_IMAGES)

        assert len(titles) > 0, "No product titles found"
        assert len(images) > 0, "No product images found"

        for i, title in enumerate(titles):
            assert title.text.strip() != "", f"Product {i + 1} has no name"

        for i, img in enumerate(images):
            src = img.get_attribute("src")
            assert src and "http" in src, f"Product {i + 1} has no valid image"



